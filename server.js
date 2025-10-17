const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
require("dotenv").config();
const axios = require("axios");

const Submission = require("./schema");

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors({ origin: "http://localhost:3000", credentials: true }));
app.use(express.json());

mongoose
  .connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Connected to MongoDB"))
  .catch((error) => console.error("Database connection error:", error));

app.post("/submit", async (req, res) => {
  const { code, language } = req.body;
  if (!code || !language) {
    return res.status(400).json({ error: "Please provide code and language" });
  }

  try {
    let retries = 3;
    let response;
    while (retries > 0) {
      try {
        response = await axios.post("http://localhost:5001/analyze", {
          code,
          language,
        });
        break;
      } catch (error) {
        retries--;
        if (retries === 0) throw error;
        await new Promise((resolve) => setTimeout(resolve, 1000));
      }
    }

    const feedbackArray = response.data.feedback;
    const feedback =
      Array.isArray(feedbackArray) && feedbackArray.length > 0
        ? feedbackArray.join("\n")
        : "• No issues found. Your code looks good!";

    const newSubmission = new Submission({ code, language, feedback });
    await newSubmission.save();

    res.status(201).json({
      message: "Code submitted successfully",
      feedback,
    });
  } catch (error) {
    console.error("Error during code submission:", error);
    res.status(500).json({
      error: error.response?.data?.error || "Code analysis failed",
    });
  }
});

// Default route
app.use("/", (req, res) => {
  res.send("AI Powered Code Review Assistant");
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
