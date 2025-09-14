from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import random

# Initialize FastAPI app
app = FastAPI()

# Load Hugging Face text generation pipeline
pipe = pipeline("text-generation", model="distilgpt2")

# Sample dataset of careers (you can expand this with real data or connect to a DB/API)
career_db = {
    "Data Scientist": {
        "required_skills": ["Python", "Machine Learning", "Statistics", "SQL", "Data Visualization"],
        "roadmap": [
            "Learn Python programming basics",
            "Study statistics and probability",
            "Master SQL for data handling",
            "Learn machine learning algorithms",
            "Work on real-world data science projects",
            "Build a strong portfolio and apply for jobs"
        ]
    },
    "Web Developer": {
        "required_skills": ["HTML", "CSS", "JavaScript", "React", "Databases", "APIs"],
        "roadmap": [
            "Learn HTML, CSS, and JavaScript",
            "Build small static websites",
            "Learn React or Angular for frontend",
            "Understand backend basics with Node.js or Django",
            "Work with databases (SQL/NoSQL)",
            "Create full-stack projects"
        ]
    },
    "AI Engineer": {
        "required_skills": ["Python", "Deep Learning", "NLP", "TensorFlow", "PyTorch"],
        "roadmap": [
            "Master Python for AI",
            "Learn fundamentals of deep learning",
            "Work with TensorFlow or PyTorch",
            "Understand NLP and computer vision",
            "Contribute to open-source AI projects",
            "Apply AI to real-world business problems"
        ]
    },
    "Product Manager": {
        "required_skills": ["Communication", "Project Management", "Business Analysis", "Leadership"],
        "roadmap": [
            "Improve communication & leadership skills",
            "Learn basics of Agile & Scrum",
            "Study product lifecycle management",
            "Understand market research & user testing",
            "Work on case studies & mock product strategies",
            "Build portfolio with product pitch decks"
        ]
    }
}

class Skills(BaseModel):
    user_skills: str

def analyze_skills(user_skills):
    """Compare user skills with database careers to find matches and gaps."""
    user_skill_list = [s.strip().capitalize() for s in user_skills.split(",")]

    recommendations = []
    for career, details in career_db.items():
        required = set([s.capitalize() for s in details["required_skills"]])
        user = set(user_skill_list)

        matched = required.intersection(user)
        missing = required - user
        score = len(matched) / len(required) * 100

        recommendations.append({
            "career": career,
            "match_score": round(score, 2),
            "matched_skills": list(matched),
            "missing_skills": list(missing),
            "roadmap": details["roadmap"]
        })

    # Sort by best match
    recommendations = sorted(recommendations, key=lambda x: x["match_score"], reverse=True)
    return recommendations[:3]  # Top 3 recommendations

def generate_extra_advice(skills_input):
    """Generate extra personalized text advice using GPT pipeline."""
    prompt = f"Given these skills: {skills_input}, suggest professional growth tips in 3-4 sentences."
    generated_text = pipe(prompt, max_length=120, num_return_sequences=1)[0]['generated_text']
    return generated_text.strip()

@app.get("/")
def home():
    return {"message": "Welcome to the Enhanced AI Career Advisor API. Use /advise to get recommendations."}

@app.post("/advise")
def advise(skills: Skills):
    # Structured recommendations
    structured_advice = analyze_skills(skills.user_skills)

    # Extra GPT-based personalized advice
    ai_text_advice = generate_extra_advice(skills.user_skills)

    return {
        "top_careers": structured_advice,
        "personalized_tips": ai_text_advice,
        "note": "Career match scores are approximate. Continue learning and exploring!"
    }
