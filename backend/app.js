const express = require("express");
const fs = require("fs");
const { exec } = require("child_process");
const { OpenAI } = require("openai"); // Using the new client interface

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 8000;

// Initialize the OpenAI client with your API key
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

/**
 * Extracts the Python code from a markdown-formatted string.
 * It looks for text between triple backticks and returns it.
 * If no code block is found, it returns the original text.
 */
function extractCode(markdownText) {
  // This regex matches a code block with optional "python" language hint.
  const codeRegex = /```(?:python)?\s*([\s\S]*?)\s*```/;
  const match = markdownText.match(codeRegex);
  if (match && match[1]) {
    return match[1].trim();
  }
  return markdownText.trim();
}

// '/generate' endpoint
app.post("/generate", async (req, res) => {
  const { prompt } = req.body;
  if (!prompt) {
    return res.status(400).json({ error: "Prompt is required" });
  }

  try {
    // Call OpenAI's Chat Completion API to generate Manim code based on the prompt.
    const response = await openai.chat.completions.create({
      model: "gpt-4", // Or another available model
      messages: [
        {
          role: "system",
          content:
            "You are an assistant that generates Python code using the Manim library. " +
            "Generate a complete code snippet that defines at least one scene producing a simple animation.",
        },
        {
          role: "user",
          content: `Generate Python Manim code for the following prompt: "${prompt}"`,
        },
      ],
      temperature: 0.2,
      max_tokens: 1000,
    });

    // Extract the generated code from the response and remove markdown formatting
    const generatedText = response.choices[0].message.content;
    const manimCode = extractCode(generatedText);
    console.log("Extracted Manim code:\n", manimCode);

    // Write the extracted code to a temporary Python file
    const codeFilePath = "./generated_manim.py";
    fs.writeFileSync(codeFilePath, manimCode);

    // Use an alternative command if "manim" is not found.
    // Try using "python -m manim" instead.
    const cmd = `python3 -m manim ${codeFilePath} Scene -ql --disable_caching`;
    exec(cmd, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing Manim: ${error}`);
        return res.status(500).json({ error: "Error generating video", details: stderr });
      }

      // Define the path to the generated video file.
      // Adjust this path based on your Manim version/configuration.
      const videoPath = "./media/videos/generated_manim/Scene.mp4";

      // Use stdout as a transcript (which may include execution logs).
      const transcript = stdout;

      return res.json({
        transcript,
        video: videoPath,
      });
    });
  } catch (error) {
    console.error("Error generating Manim code:", error);
    res.status(500).json({ error: "Error generating code" });
  }
});

app.listen(PORT, () => {
  console.log("Server listening on PORT:", PORT);
});
