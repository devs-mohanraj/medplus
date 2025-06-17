# MedPlus - AI-Powered Diabetes Care Assistant

MedPlus is an intelligent chat interface that provides accurate, reliable information about diabetes care using The Retrieval Augmented Generation . The system processes medical documentation and responds to user queries with contextually relevant information.

## Features

- Modern, user-friendly chat interface built with Streamlit
- AI-powered responses based on reliable diabetes care documentation
- Real-time question answering system
- Context-aware responses using document retrieval
- Clean and intuitive user experience

## Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Document Processing**: LangChain
- **Vector Store**: ChromaDB
- **AI Model**: Mixtral-8x7B-Instruct-v0.1 from Together AI

## Project Structure

```
medplus/
├── streamlit_app.py      # Main Streamlit application
├── interface.py          # Query processing interface
├── build_chain.py        # LangChain configuration
├── load_data.py         # Data loading utilities
├── retriever.py         # Document retrieval logic
├── text_splitter.py     # Text processing utilities
├── vector_store.py      # Vector database management
├── requirements.txt     # Project dependencies
└── data/               # Source documents
    └── diabetes.pdf    # Diabetes care documentation
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd medplus
```

2. Create and activate a virtual environment:
```bash
python -m venv env
.\env\Scripts\Activate.ps1  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with:
```
TOGETHER_API_KEY=your_api_key_here
```

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

2. Open your browser and navigate to `http://localhost:8501`

## Usage

1. The chat interface will appear in your browser
2. Type your diabetes-related question in the input box
3. Press Enter or click the send button
4. The AI assistant will provide a relevant response based on the medical documentation

## Security Note

This application is for informational purposes only. Always consult healthcare professionals for medical advice.

## License

this project is open-source under **MIT License**

