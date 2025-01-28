# 📚 Interactive Financial Statement Analysis System

A Streamlit-based application for analyzing financial documents through natural language queries and interactive chat. Leverages Gemini AI for processing and LlamaParse for document parsing.

![Demo](https://via.placeholder.com/800x400.png?text=Application+Demo+Screenshot)

## ✨ Features

- **Secure API Key Management** - Configure Gemini and LlamaParse keys through UI
- **PDF Document Processing** - Upload and analyze financial statements/PDFs
- **Dual Interaction Modes**:
  - **Q&A Mode** - Get precise answers to specific questions
  - **Chat Mode** - Conversational interface for document exploration
- **Session Management** - Maintain chat history and document context
- **Responsive UI** - Modern interface with enhanced readability

## 🚀 Installation

1. Clone the repository:
```bash
(https://github.com/quantumdeepak/inancial-Statement-Analysis-System)
cd financial-analysis-system


⚙️ Configuration
Obtain API keys:

Gemini API Key

LlamaParse API Key

Configure keys through the app sidebar:

Launch the app

Enter keys in the "🔑 API Keys" section

Keys persist in session state (not stored on disk)

🖥️ Usage

streamlit run app.py
Upload Document:

Click "📄 Upload Document" in sidebar

Select a PDF file (financial statements, reports, etc.)

Q&A Mode:

Ask specific questions in the "🔍 Q&A" tab

Get focused answers with source references

Chat Mode:

Engage in conversational analysis in "💬 Chat" tab

Maintains context through chat history

Document Management:

Clear current document with "🗑️ Clear Document"

Reset chat history with "🧹 Clear Chat"

📂 Project Structure
├── .gitignore
├── app.py                 # Main application logic
├── chat_interface.py      # Chat session management
├── config.py              # API key configuration
├── document_processor.py  # Document parsing and processing

📦 Dependencies
Core: streamlit

AI Backend: llama-index, google-generativeai

Document Parsing: llama-parse

Environment: python-dotenv

⚠️ Important Notes
API keys are not persisted between sessions

Processed documents are stored temporarily during session

Recommended for PDFs under 50 pages for optimal performance

Ensure network connectivity for API access
