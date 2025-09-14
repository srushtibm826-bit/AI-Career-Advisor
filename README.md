# AI-Career-Advisor
🤖 AI Career Advisor:
This project is a personalized AI-powered career advisor. It consists of a backend API built with FastAPI that analyzes a user's skills and provides career recommendations, a skill gap analysis, and a learning roadmap. The user interface is a web application built with Streamlit that interacts with the backend to display the advice.

✨ Features
* Skill Match: Get top career recommendations based on your current skills.
* Skill Gap Analysis: See which skills you have and which ones you need to acquire for a specific career.
* Learning Roadmap: Receive a step-by-step roadmap for your desired career path.
* Personalized Tips: Get unique, AI-generated professional growth advice.

⚙️ Prerequisites
* Python 3.8 or higher
* pip package manager

🚀 Setup & Installation
Follow these steps to get the application running on your local machine.

1. Clone the repository
   git clone [repository-url]
   cd [repository-name]

(Note: Replace [repository-url] and [repository-name] with the actual details if this project were hosted in a Git repository.)

2. Install dependencies
   Install the required libraries for both the FastAPI backend and the Streamlit frontend.
   pip install fastapi "uvicorn[standard]" transformers pydantic streamlit requests

3. Run the Backend Server
  Open your terminal and start the FastAPI server. This must be running before you start      the frontend.
  uvicorn api:app --reload

4. Run the Frontend Application
  Open a new terminal and start the Streamlit application.
  streamlit run main.py

🧑‍💻 Usage
1. After running the commands above, a new browser tab should open automatically, showing the Streamlit app.

2. In the text area, enter your skills separated by commas (e.g., Python, SQL, Machine Learning).

3. Click the "🔍 Get Career Advice" button.

4. The application will display your personalized career recommendations, including match scores, skill gaps, and learning roadmaps.

💻 Technologies Used
* FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.

* Streamlit: An open-source app framework for Machine Learning and Data Science teams.

* Hugging Face Transformers: Used for the distilgpt2 model to generate personalized text advice.

* Pydantic: Used for data validation and settings management.

* Requests: A simple HTTP library for making API calls from the frontend.

