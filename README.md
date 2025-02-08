# Manify: AI Visual Mathematics Tutor

### Revolutionizing Math Tutoring with AI-Powered Visualizations

---

## Overview

**Manify** transforms how students learn mathematics by combining cutting-edge AI agents with advanced visual animations. Our platform converts complex mathematical concepts into engaging, interactive video explanations, making math more accessible and fun for learners of all levels.

---

## What Did We Build?

Manify is an innovative web application that:
- **Generates Custom Animations:** Uses OpenAI's code-generation capabilities to produce Python Manim code tailored to the user's math query.
- **Renders Visual Explanations:** Executes the generated Manim code to create dynamic, high-quality animation videos.
- **Provides Transcripts:** Offers an accompanying transcript for each video, enhancing learning through textual reinforcement.
- **Stores History:** Saves past prompts locally for quick access and review.

---

## How Does It Work?

1. **User Input:**  
   A student submits a math-related prompt via our sleek, responsive React interface.

2. **AI Code Generation:**  
   The prompt is sent to OpenAI's API, which generates a custom Python code snippet using the Manim library to create an animation.

3. **Video Rendering:**  
   The generated code is saved and executed using Manim (invoked via `python -m manim`), producing an explanatory video.

4. **Transcript Creation:**  
   Execution logs or AI-generated explanations are provided as a transcript alongside the video.

5. **Interactive History:**  
   Previous prompts and generated content are stored locally, allowing users to revisit or delete past entries.

---

## Technologies Used

- **Frontend:**  
  - React  
  - Tailwind CSS

- **Backend:**  
  - Express.js  
  - Node.js

- **AI Services:**  
  - OpenAI API (ChatGPT for code generation)

- **Visualization:**  
  - Manim (Python library for mathematical animations)

- **Storage:**  
  - LocalStorage for prompt history

---

## Demo

Watch our demo video: [Insert Demo Video Link or GIF]

Try the live demo here: [manify.us](www.manify.us)

---

## Team

- **Akif Dirican** – Frontend & UX Design  
- **Alp Niksarli** – Backend Development & AI Integration  
- **Utkan Uygur** – Data Science & Visualization

---

## Challenges & Learnings

Building Manify came with unique challenges:
- **AI Integration:** Seamlessly connecting AI-generated code with dynamic video rendering.
- **Execution Safety:** Running dynamically generated Python code securely and reliably.
- **User Experience:** Crafting a responsive, intuitive interface that works across devices.
- **Data Persistence:** Efficiently managing prompt history with local storage.

These challenges pushed us to explore innovative solutions and helped us deepen our expertise in AI, asynchronous processing, and modern web development.

---

## Future Enhancements

- **Real-Time Interactivity:** Enable users to tweak animations live for a more personalized learning experience.
- **Wider Topic Support:** Expand our subject matter to cover more areas of mathematics.
- **Collaboration Features:** Allow users to share, comment on, and collaborate over generated content.
- **Enhanced Analytics:** Provide detailed insights into user engagement and learning outcomes.

---

## Acknowledgements

We extend our gratitude to:
- **OpenAI** for their state-of-the-art AI models.
- **Manim Community** for the powerful visualization tools.
- Our mentors and beta testers, whose feedback was invaluable.

---

## License

This project is licensed under the [MIT License](LICENSE).

