const express = require("express");

const app = express ();
app.use(express.json());

const PORT = process.env.PORT || 8000;

app.post("/generate", (req, res) => {
    const { name, age } = req.body;
    res.json({
      name,
      age,
      message: `Hello ${name}, you are ${age} years old!`,
    });  
});

app.listen(PORT, () => {
    console.log("Server Listening on PORT:", port);
  });
  