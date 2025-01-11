import streamlit as st

# Page configuration
st.set_page_config(
    page_title="HR AI Platform",
    page_icon="🏢",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
    }
    .big-font {
        font-size: 24px !important;
    }
    .nav-link {
        text-decoration: none;
        color: inherit;
        cursor: pointer;
    }
    .card {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🏢 HR AI Platform")
st.markdown("### AI-Powered Recruitment and Candidate Evaluation System")

# Introduction
st.markdown("""
Welcome to the HR AI Platform, your comprehensive solution for:
- 📊 Intelligent candidate evaluation
- 🤖 Bias-free recruitment
- 📈 Data-driven hiring decisions
- 👥 Enhanced candidate assessment
""")

# Navigation cards
st.subheader("Quick Navigation")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("""
        <div class="card">
            <h4>📊 Dashboard</h4>
            <p>View all candidates and their evaluations at a glance.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Dashboard", key="dash_btn", use_container_width=True):
            st.switch_page("pages/dashboard.py")
    
    with st.container():
        st.markdown("""
        <div class="card">
            <h4>👤 Candidate Profiles</h4>
            <p>Detailed candidate information and assessments.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Candidates", key="cand_btn", use_container_width=True):
            st.switch_page("pages/candidate_profile.py")

with col2:
    with st.container():
        st.markdown("""
        <div class="card">
            <h4>🤖 AI Explanations</h4>
            <p>Understand how the AI evaluates candidates.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("AI Insights", key="ai_btn", use_container_width=True):
            st.switch_page("pages/ai_explanation.py")
    
    with st.container():
        st.markdown("""
        <div class="card">
            <h4>👥 Human Oversight</h4>
            <p>Review and adjust AI decisions.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Oversight Panel", key="oversight_btn", use_container_width=True):
            st.switch_page("pages/human_oversight.py")

# System stats
st.divider()
st.subheader("System Statistics")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Active Candidates", value="243", delta="12")
with col2:
    st.metric(label="Evaluations Today", value="28", delta="5")
with col3:
    st.metric(label="Avg. Response Time", value="2.3s", delta="-0.2s")
with col4:
    st.metric(label="Bias Detection Rate", value="99.7%", delta="0.2%")

# Recent activity
st.divider()
st.subheader("Recent Activity")

# Mock recent activity data
recent_activities = [
    {"time": "2 minutes ago", "action": "New candidate evaluation completed", "details": "Senior Data Scientist position"},
    {"time": "15 minutes ago", "action": "Bias check performed", "details": "All candidates reviewed"},
    {"time": "1 hour ago", "action": "Manual override by HR", "details": "Candidate ID #1234"},
    {"time": "2 hours ago", "action": "System update", "details": "AI model refreshed"}
]

for activity in recent_activities:
    with st.expander(f"{activity['action']} - {activity['time']}", expanded=True):
        st.write(activity['details'])

# Footer
st.divider()
st.caption("HR AI Platform v2.0 - Powered by Tharazeenuddin")

# Optional: Add a help section in the sidebar
with st.sidebar:
    st.header("Need Help?")
    st.markdown("""
    - 📚 [View Documentation](#)
    - 💡 [Quick Start Guide](#)
    - 🎯 [Best Practices](#)
    - 📧 [Contact Support](#)
    """)