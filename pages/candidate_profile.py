import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Candidate Profile",
    page_icon="👤",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .profile-header {
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .skill-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f1f3f5;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Mock candidate data
@st.cache_data
def get_candidate_data(candidate_id):
    return {
        'personal': {
            'name': 'John Smith',
            'email': 'john.smith@email.com',
            'phone': '+1 (555) 123-4567',
            'location': 'San Francisco, CA',
            'position': 'Senior Data Scientist',
            'department': 'Data Science',
            'status': 'In Review',
            'application_date': '2024-01-01'
        },
        'education': [
            {
                'degree': 'Ph.D. in Computer Science',
                'institution': 'Stanford University',
                'year': '2018-2022',
                'gpa': '3.9'
            },
            {
                'degree': 'M.S. in Data Science',
                'institution': 'MIT',
                'year': '2016-2018',
                'gpa': '3.8'
            }
        ],
        'experience': [
            {
                'title': 'Lead Data Scientist',
                'company': 'Tech Corp',
                'duration': '2022-Present',
                'description': 'Led a team of 5 data scientists in developing ML models'
            },
            {
                'title': 'Data Scientist',
                'company': 'AI Startup',
                'duration': '2018-2022',
                'description': 'Developed and deployed ML models for client projects'
            }
        ],
        'skills': {
            'technical': {
                'Python': 95,
                'Machine Learning': 90,
                'Deep Learning': 85,
                'SQL': 88,
                'Cloud Platforms': 82
            },
            'soft': {
                'Leadership': 90,
                'Communication': 88,
                'Problem Solving': 92,
                'Teamwork': 95,
                'Project Management': 85
            }
        },
        'ai_evaluation': {
            'overall_score': 92,
            'technical_score': 90,
            'experience_score': 88,
            'education_score': 95,
            'cultural_fit': 92,
            'bias_risk': 'Low',
            'flags': [],
            'recommendations': [
                'Strong technical background',
                'Excellent leadership experience',
                'Cultural fit alignment'
            ]
        }
    }

# Load candidate data
candidate = get_candidate_data(1)  # In real app, get ID from URL or selection

# Header section
st.title("👤 Candidate Profile")

# Personal information card
with st.container():
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.subheader(candidate['personal']['name'])
        st.write(f"📧 {candidate['personal']['email']}")
        st.write(f"📱 {candidate['personal']['phone']}")
        st.write(f"📍 {candidate['personal']['location']}")
    
    with col2:
        st.metric(
            "AI Score",
            f"{candidate['ai_evaluation']['overall_score']}/100",
            delta="Top 10%"
        )
    
    with col3:
        st.metric(
            "Bias Risk",
            candidate['ai_evaluation']['bias_risk'],
            delta="Low Risk"
        )

# Main content tabs
tab1, tab2, tab3 = st.tabs(["Profile", "Skills & Experience", "AI Evaluation"])

# Profile tab
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        # Education section
        st.subheader("🎓 Education")
        for edu in candidate['education']:
            with st.expander(f"{edu['degree']} - {edu['institution']}", expanded=True):
                st.write(f"**Year:** {edu['year']}")
                st.write(f"**GPA:** {edu['gpa']}")
    
    with col2:
        # Experience section
        st.subheader("💼 Experience")
        for exp in candidate['experience']:
            with st.expander(f"{exp['title']} at {exp['company']}", expanded=True):
                st.write(f"**Duration:** {exp['duration']}")
                st.write(exp['description'])

# Skills & Experience tab
with tab2:
    # Technical skills
    st.subheader("Technical Skills")
    
    # Create radar chart for technical skills
    technical_skills = candidate['skills']['technical']
    fig = go.Figure(data=go.Scatterpolar(
        r=list(technical_skills.values()),
        theta=list(technical_skills.keys()),
        fill='toself'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Soft skills
    st.subheader("Soft Skills")
    soft_skills = candidate['skills']['soft']
    for skill, score in soft_skills.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.progress(score/100)
        with col2:
            st.write(f"{skill}: {score}%")

# AI Evaluation tab
with tab3:
    # AI scores breakdown
    st.subheader("AI Evaluation Scores")
    scores = {
        'Technical Assessment': candidate['ai_evaluation']['technical_score'],
        'Experience Evaluation': candidate['ai_evaluation']['experience_score'],
        'Education Assessment': candidate['ai_evaluation']['education_score'],
        'Cultural Fit': candidate['ai_evaluation']['cultural_fit']
    }
    
    fig = px.bar(
        x=list(scores.keys()),
        y=list(scores.values()),
        title="AI Evaluation Breakdown"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # AI recommendations
    st.subheader("AI Recommendations")
    for rec in candidate['ai_evaluation']['recommendations']:
        st.info(rec)
    
    # Flags (if any)
    if candidate['ai_evaluation']['flags']:
        st.subheader("⚠️ Flags")
        for flag in candidate['ai_evaluation']['flags']:
            st.warning(flag)

# Action buttons
st.divider()
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("👍 Approve", type="primary", use_container_width=True):
        st.success("Candidate approved!")

with col2:
    if st.button("👎 Reject", type="secondary", use_container_width=True):
        st.error("Candidate rejected.")

with col3:
    if st.button("📝 Request More Info", use_container_width=True):
        st.info("Information request sent.")

with col4:
    if st.button("📊 Download Profile", use_container_width=True):
        st.download_button(
            label="Download PDF",
            data="Profile data...",  # In real app, generate PDF here
            file_name=f"candidate_profile_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf"
        )