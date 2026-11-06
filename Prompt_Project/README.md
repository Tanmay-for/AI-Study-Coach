# AI Study Coach (Prompt-Based Project)

An interactive, AI-driven personal study assistant built for the **Prompt Engineering** course. This project operates entirely through advanced system prompt architecture, maintaining context and switching between multiple pedagogical modes without relying on external databases or document retrieval systems.

---

## 🚀 Key Features

* **Study Planner Mode:** Creates customized, milestone-based schedules tailored to the user's timeline and current skill level.
* **Topic Breakdown Mode (Feynman Technique):** Simplifies complex concepts using intuitive analogies and zero dense jargon.
* **Interactive Quizmaster Mode:** Tests student knowledge by asking conceptual or multiple-choice questions **one at a time**, waiting for feedback, and grading responses.
* **Local Execution:** Runs securely and efficiently offline using **Ollama** (`llama3.2`) so you have zero API costs and full data privacy.

---

## 🛠️ Tech Stack

* **Language:** Python
* **AI Engine:** Ollama (`llama3.2`)
* **Core Libraries:** `ollama` Python client package
* **Environment:** Visual Studio Code (VS Code)

---

## 💡 Prompt Engineering Techniques Used

The core intelligence of this project relies on deliberate prompt engineering strategies rather than traditional backend logic:

1. **Role & Persona Prompting:** Assigns a strict, encouraging persona ("expert, highly encouraging AI Study Coach") to govern tone and behavior.
2. **Conditional Mode Architecture:** Explicitly defines three distinct operating modes within the system prompt so the model accurately detects user intent and changes its output style.
3. **Constraint Enforcement:** Implements strict conversational boundaries (e.g., forcing the quizmaster to ask questions sequentially rather than dumping all questions at once).
4. **Stateful Conversation Management:** Appends user inputs and assistant replies dynamically to a message history list to maintain short-term memory across the chat session.

---

## ⚙️ Setup and Installation

1. Make sure **Ollama** is installed and running on your system.
2. Pull the required lightweight model in your terminal:
   ```bash
   ollama pull llama3.2