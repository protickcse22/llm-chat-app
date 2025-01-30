# Local Multi-LLM Chat Application

## Project Overview

This project is a Local Multi-LLM Chat Application that allows users to interact with multiple open-source Large Language Models (LLMs) locally on their machine. The application is built using modern technologies, including Ollama for running LLMs, FastAPI for the backend, and Streamlit for the frontend. It provides a user-friendly interface similar to ChatGPT, with the flexibility to switch between different LLMs and customize model parameters.

## Key Features

- **Multi-Model Support**: Use multiple open-source LLMs (e.g., DeepSeek, LLaMA 2, Mistral) locally.
- **Customizable Parameters**: Adjust model settings such as temperature, top-p, and max tokens to control response behavior.
- **Beautiful UI**: A modern and responsive user interface built with Streamlit.
- **Local Deployment**: All processing happens locally, ensuring data privacy and security.
- **Streaming-like Responses**: Simulated streaming for a ChatGPT-like user experience.
- **Easy to Use**: Simple setup and intuitive interface for seamless interaction.

## Technologies Used

### Backend

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Ollama**: A tool for running open-source LLMs locally.
- **Ollama Python Library**: Python bindings for interacting with Ollama.

### Frontend

- **Streamlit**: A powerful framework for building interactive web applications in Python.
- **Custom CSS**: Styling for a modern and visually appealing user interface.

### LLM Models

- **DeepSeek-r1:7b**: A high-performance open-source LLM.
- **LLaMA 2**: Meta's open-source LLM.
- **Mistral**: A lightweight and efficient LLM.

## Project Structure

```
llm-chat-app/
├── backend/
│   ├── main.py                # FastAPI backend server
├── frontend/
│   ├── app.py                 # Streamlit frontend application
│   └── static/
│       └── style.css          # Custom CSS for styling
├── requirements.txt           # Frontend dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

### Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.
- **Ollama**: Install and set up Ollama on your machine. Follow the Ollama installation guide.
- **LLM Models**: Pull the desired models using Ollama. For example:
  ```bash
  ollama pull deepseek-r1:7b
  ollama pull llama2
  ollama pull mistral
  ```

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd llm-chat-app
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Backend

Navigate to the backend directory:

```bash
cd backend
```

Start the FastAPI server:

```bash
python main.py
```

The backend will run at `http://localhost:8000`.

### Step 3: Set Up the Frontend

Navigate to the frontend directory:

```bash
cd ../frontend
```

Start the Streamlit application:

```bash
streamlit run app.py
```

The frontend will open in your browser at `http://localhost:8501`.

## Usage

### Access the Application

Open your browser and navigate to `http://localhost:8501`.

### Configure Settings

Use the sidebar to:

- Select a model (e.g., DeepSeek, LLaMA 2, Mistral).
- Adjust temperature, top-p, and max tokens to control response behavior.

### Start Chatting

Type your message in the chat input box and press Enter. The assistant will generate a response based on the selected model and parameters.

## Customization

### Add New Models

Pull a new model using Ollama:

```bash
ollama pull <model-name>
```

Add the model to the dropdown in `frontend/app.py`:

```python
st.session_state.model = st.selectbox(
        "Select Model",
        ["deepseek-r1:7b", "llama2", "mistral", "<new-model>"],
        index=0
)
```

### Modify Styling

Edit the `frontend/static/style.css` file to customize the appearance of the application.

### Adjust Backend Parameters

Modify the `backend/main.py` file to add or change model parameters.

## Benefits for the Client

- **Cost-Effective**: No need for expensive cloud-based LLM APIs.
- **Data Privacy**: All data remains on your local machine.
- **Flexibility**: Switch between multiple open-source LLMs based on your needs.
- **Customizability**: Fine-tune model parameters for optimal performance.
- **User-Friendly**: Intuitive interface for seamless interaction.

## Future Enhancements

- **Real Streaming**: Implement Server-Sent Events (SSE) for real-time response streaming.
- **Chat History**: Save and load chat sessions.
- **File Uploads**: Allow users to upload files for context-based queries.
- **Advanced Analytics**: Track usage and performance metrics.
- **Docker Support**: Simplify deployment with Docker containers.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
