import streamlit as st
import requests

# URL of the FastAPI backend
FASTAPI_URL = "http://127.0.0.1:8000"

# Page config
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title and intro
st.title("🤖 Personalized AI Career Advisor")
st.markdown(
    """
    **Welcome!** 🚀  
    Enter your skills below and get **personalized career recommendations**,  
    including skill gap analysis, learning roadmaps, and growth tips.
    """
)
st.markdown("---")

# Input area
user_input_placeholder = st.empty()
user_skills = user_input_placeholder.text_area(
    "✍️ Enter your skills (comma separated, e.g., Python, Data Analysis, Public Speaking):",
    height=120,
)

# Button to trigger API
if st.button("🔍 Get Career Advice"):
    if user_skills.strip() == "":
        st.warning("⚠️ Please enter your skills to get advice!")
    else:
        with st.spinner("Analyzing your skills and generating recommendations..."):
            try:
                payload = {"user_skills": user_skills}
                response = requests.post(f"{FASTAPI_URL}/advise", json=payload)

                if response.status_code == 200:
                    data = response.json()
                    top_careers = data.get("top_careers", [])
                    tips = data.get("personalized_tips", "")
                    
                    st.success("✅ Recommendations Generated Successfully!")
                    
                    # Display Top Careers
                    st.subheader("🎯 Top Career Recommendations")
                    for idx, career in enumerate(top_careers, start=1):
                        with st.container():
                            st.markdown(f"### {idx}. {career['career']}")
                            st.progress(career['match_score'] / 100)

                            # Show score
                            st.write(f"**Match Score:** {career['match_score']}%")

                            # Matched skills
                            if career['matched_skills']:
                                st.markdown("✅ **Matched Skills:**")
                                st.write(", ".join(career['matched_skills']))
                            else:
                                st.markdown("✅ **Matched Skills:** None yet")

                            # Missing skills
                            if career['missing_skills']:
                                st.markdown("❌ **Missing Skills (to work on):**")
                                st.write(", ".join(career['missing_skills']))
                            else:
                                st.markdown("🎉 You already have all required skills!")

                            # Learning roadmap
                            st.markdown("📘 **Learning Roadmap:**")
                            for step in career['roadmap']:
                                st.write(f"- {step}")

                            st.markdown("---")

                    # Personalized GPT tips
                    st.subheader("💡 Personalized Growth Tips")
                    st.info(tips)

                else:
                    st.error(f"❌ API Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Could not connect to the API. Please ensure FastAPI server is running. Error: {e}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #7f7f7f; font-size: 12px;">
    Built with ❤️ using Streamlit, FastAPI & Hugging Face.
    </div>
    """,
    unsafe_allow_html=True,
)
