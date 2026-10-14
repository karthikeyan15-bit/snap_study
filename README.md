# 📸 Snap & Study

### Snap it. Study it. Understand it.

Snap & Study is an AI-powered study assistant that transforms images of study materials into useful learning resources. Using **Google Gemini AI** and **Streamlit**, it helps students understand concepts, solve questions, summarize notes, and test their knowledge.

Instead of switching between multiple tools, students can capture a photo or upload an image and let AI help them learn.

## ✨ Features

- 📷 **Capture Study Material:** Take a photo directly using your device's camera.
- 📁 **Upload Images:** Upload JPG, JPEG, PNG, or WEBP images.
- 💡 **Explain Concepts:** Get AI-generated explanations of concepts shown in an image.
- 🧮 **Solve Questions:** Get solutions to questions captured from textbooks, notes, or worksheets.
- 📝 **Summarize Notes:** Turn study material into concise summaries.
- 🎯 **Quiz Mode:** Generate quiz-style learning content from uploaded material.
- 🤖 **Gemini AI Integration:** Analyze images using Google's Gemini model.
- ⚡ **Simple Interface:** Use a clean, interactive web interface built with Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Google Gemini AI | Image analysis and content generation |
| Google Gen AI SDK | Communication with the Gemini model |
| Pillow (PIL) | Image processing |
| python-dotenv | Environment variable management |

## 🏗️ Project Structure

```text
snap_study/
│
├── app.py              # Streamlit application
├── gemini_service.py   # Gemini API integration
├── prompts.py          # AI prompts for study modes
├── requirements.txt    # Python dependencies
├── .gitignore          # Git exclusion rules
├── .env                # Local API configuration
└── README.md           # Project documentation
```

> The `.env` file is for local configuration and should not be committed to GitHub.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- pip package manager
- A Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/karthikeyan15-bit/snap_study.git
```

### 2. Navigate to the project directory

```bash
cd snap_study
```

### 3. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your Gemini API key

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a `.env` file in the root directory of the project and add:

```env
GEMINI_API_KEY=your-gemini-api-key
```

Replace `your-gemini-api-key` with your actual API key.

**Important:** Never share your API key or commit it to a public repository.

### 6. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🚀 How to Use

1. Launch Snap & Study.
2. Select a study mode: **Explain, Solve, Summarize, or Quiz Me**.
3. Choose whether to take a photo or upload an image.
4. Capture or upload your study material.
5. Click **Analyze with Snap & Study**.
6. Read the AI-generated response and use it to support your learning.

## 🔑 API Configuration for Deployment

If deploying through Streamlit Community Cloud:

1. Open your deployed application's settings.
2. Navigate to **Settings → Secrets**.
3. Add the following configuration:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

4. Save the secrets and restart the application if necessary.

Keep API credentials private and monitor API usage and applicable rate limits.

## 🧠 How It Works

```text
Capture or Upload Image
          |
          v
Select Study Mode
          |
          v
Streamlit Application
          |
          v
Image Processing with Pillow
          |
          v
Mode-Specific AI Prompt
          |
          v
Google Gemini AI
          |
          v
Generated Learning Content
          |
          v
Display Results in Streamlit
```

## 🎯 Project Objective

The goal of Snap & Study is to reduce the time students spend manually converting study material into learning resources. By combining image input with generative AI, the application makes it easier to understand concepts, review notes, solve questions, and practice through quizzes.

## 🔮 Future Enhancements

- PDF and document uploads
- Automatic flashcard generation
- Interactive quizzes with scores
- Conversation-based follow-up questions
- Study history and saved results
- Text-to-speech explanations
- Personalized learning recommendations
- Progress tracking and revision reminders
- Support for multiple languages

## 🔒 Security and Limitations

- Store API keys in environment variables or deployment secrets.
- Do not commit `.env` files or expose credentials.
- AI-generated explanations and solutions may contain errors. Verify important information against reliable learning materials.
- Image quality, handwriting, and model availability can affect results.
- Gemini API usage may be subject to pricing, quotas, and rate limits.

## 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork this repository.
2. Create a feature branch.
3. Make your changes.
4. Commit and push your changes.
5. Open a pull request describing your contribution.

## 👨‍💻 Author

**Karthikeyan R**

- GitHub: [@karthikeyan15-bit](https://github.com/karthikeyan15-bit)
- Project Repository: [Snap & Study](https://github.com/karthikeyan15-bit/snap_study)

## 📄 License

No license has been specified for this repository yet. Add a `LICENSE` file if you intend to define permissions for using, modifying, and distributing the project.

---

**Snap & Study — Learn smarter, one snapshot at a time.** 📚
