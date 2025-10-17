# 🚀 CodeGuardian AI

CodeGuardian AI is an AI-powered code review assistant that helps developers analyze and improve their code automatically. It identifies syntax errors, highlights code quality issues, and suggests actionable improvements, all through a simple web interface.

![Landing Page Screenshot](./screenshots/landing-page.png)
![Analyzer Screenshot](./screenshots/analyzer.png)

---

## ✨ Features

- 🧠 **AI-Powered Code Analysis**

  - Uses NLP models (e.g., CodeBERT) to understand and review code
  - Currently supports Python syntax analysis

- ⚡ **Instant Feedback**

  - Detects syntax errors and code smells
  - Provides clear, line-specific warnings and recommendations

- 🌐 **Web Interface**

  - User-friendly Next.js frontend for submitting code and viewing results

- 🛠 **Modular Architecture**

  - MERN stack backend with separate Python service for NLP processing

- 📈 **Extensible**

  - Easily adaptable to support more programming languages and rules

---

## 🏗 Tech Stack

- **Frontend:** Next.js, React, Tailwind CSS, Axios
- **Backend:** Node.js, Express
- **NLP Service:** Python (FastAPI/Flask) leveraging CodeBERT
- **Database:** MongoDB

---

## 🚀 Getting Started

### Prerequisites

- Node.js >= 16.x
- Python >= 3.8
- MongoDB (local or Atlas)

---

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Shreyash-Bhor/AI_Code_Review_Assistant.git
   cd AI_Code_Review_Assistant
   ```

2. **Install frontend dependencies**

   ```bash
   cd frontend
   npm install
   ```

3. **Install backend dependencies**

   ```bash
   cd ../backend
   npm install
   ```

---

### Configuration

Create environment files as needed (e.g., `.env`) to store:

- MongoDB connection URI
- Any API keys if applicable

Example `.env`:

```env
MONGO_URI=mongodb://localhost:27017/codeguardian
PORT=5000
```

---

### Running the Project

> **Start all services in separate terminals:**

- **Frontend (Next.js app):**

  ```bash
  npm run dev
  ```

  > Runs at `http://localhost:3000`

- **Backend (Node.js API):**

  ```bash
  node server.js
  ```

  > Default port: `5000`

- **Python NLP Service:**

  ```bash
  python app.py
  ```

  > Default port: `8000` (or as configured)

---

## 📡 API Endpoints

### `POST /analyze`

Analyzes submitted Python code for syntax errors.

- **Request Body:**

  ```json
  {
    "code": "<your_python_code_here>"
  }
  ```

- **Response:**

  ```json
  {
    "analysis": "Line 1: SyntaxError...",
    "suggestions": "Remove TODO comments before deployment."
  }
  ```

---

## 💻 Usage

1. Launch the frontend.
2. Paste your Python code into the editor.
3. Click **Analyze Code**.
4. Review the analysis results below the editor.

---

## 📷 Screenshots

|                Landing Page                |              Code Analyzer              |
| :----------------------------------------: | :-------------------------------------: |
| ![Landing](./screenshots/landing-page.png) | ![Analyzer](./screenshots/analyzer.png) |

---

## 🤝 Contributing

Pull requests are welcome!

If you’d like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 👤 Author

**Yashasvi Verma**

- [GitHub](https://github.com/Yashasvi260302)
- [LinkedIn](https://www.linkedin.com/in/yashasviverma02)

---

## ⭐ Acknowledgments

- [CodeBERT](https://huggingface.co/microsoft/codebert-base)
- \[MERN Stack Community]

---

