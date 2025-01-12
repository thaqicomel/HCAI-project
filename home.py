import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Hiring Platform",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
    }
    .big-font {
        font-size: 24px !important;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.8rem;
        background-color: #f8f9fa;
        margin: 0.5rem 0;
        border: 1px solid #e9ecef;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-card {
        text-align: center;
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .welcome-header {
        padding: 2rem;
        background: linear-gradient(135deg, #0066cc, #0044aa);
        color: white;
        border-radius: 0.8rem;
        margin-bottom: 2rem;
    }
    .stat-box {
        padding: 1rem;
        background-color: white;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Welcome Header
st.markdown("""
    <div class="welcome-header">
        <h1>🏢 Hiring Platform</h1>
        <p style='font-size: 1.2rem;'>Welcome to the next generation of AI-powered recruitment and candidate evaluation</p>
    </div>
""", unsafe_allow_html=True)

# Quick Stats Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="stat-box">
            <h3 style='color: #0066cc;'>243</h3>
            <p>Active Candidates</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-box">
            <h3 style='color: #0066cc;'>28</h3>
            <p>Today's Evaluations</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-box">
            <h3 style='color: #0066cc;'>2.3s</h3>
            <p>Avg. Response Time</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stat-box">
            <h3 style='color: #0066cc;'>99.7%</h3>
            <p>Bias Detection Rate</p>
        </div>
    """, unsafe_allow_html=True)

# Main Features Section
st.markdown("### 🎯 Platform Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="card">
            <h4>📊 Dashboard</h4>
            <p>Comprehensive overview of all candidates and evaluations</p>
            <ul>
                <li>Real-time analytics</li>
                <li>Performance metrics</li>
                <li>Trend analysis</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Dashboard", key="dash_btn"):
        st.switch_page("pages/1_📊_dashboard.py")

    st.markdown("""
        <div class="card">
            <h4>🤖 Bias Report and AI Explanation</h4>
            <p>Bias Report Analysis and Transparent insights into AI decision-making</p>
            <ul>
                <li>Decision factors</li>
                <li>Bias detection</li>
                <li>Confidence scores</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("View Insights", key="ai_btn"):
        st.switch_page("pages/3_🤖_bias_report_and_ai_explanation.py")

with col2:
    st.markdown("""
        <div class="card">
            <h4>👤 Candidate Profiles</h4>
            <p>In-depth candidate information and assessments</p>
            <ul>
                <li>Skill evaluations</li>
                <li>Experience analysis</li>
                <li>Cultural fit assessment</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Browse Candidates", key="cand_btn"):
        st.switch_page("pages/2_👤_candidate_profile.py")

    st.markdown("""
        <div class="card">
            <h4>👥 Human Oversight</h4>
            <p>Review and adjust AI decisions</p>
            <ul>
                <li>Manual overrides</li>
                <li>Decision tracking</li>
                <li>Audit trail</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Access Oversight Panel", key="oversight_btn"):
        st.switch_page("pages/4_👥_human_oversight.py")

# Recent Activity Section
st.markdown("### 📝 Recent Activity")

# Create tabs for different activity types
tab1, tab2, tab3 = st.tabs(["Latest Evaluations", "System Updates", "Notifications"])

with tab1:
    activities = [
        {"time": "2 minutes ago", "action": "New candidate evaluation completed", "details": "Senior Data Scientist position"},
        {"time": "15 minutes ago", "action": "Bias check performed", "details": "All candidates reviewed"},
        {"time": "1 hour ago", "action": "Manual override by HR", "details": "Candidate ID #1234"}
    ]
    
    for activity in activities:
        st.markdown(f"""
            <div style='padding: 0.5rem; border-left: 3px solid #0066cc; margin: 0.5rem 0; background-color: white;'>
                <p style='margin: 0; color: #666;'>{activity['time']}</p>
                <p style='margin: 0; font-weight: bold;'>{activity['action']}</p>
                <p style='margin: 0;'>{activity['details']}</p>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    updates = [
        {"date": "Today", "update": "AI Model Refresh", "status": "Completed"},
        {"date": "Yesterday", "update": "New Bias Detection Rules", "status": "Active"},
        {"date": "2 days ago", "update": "Performance Optimization", "status": "Completed"}
    ]
    
    for update in updates:
        st.markdown(f"""
            <div style='padding: 0.5rem; border-left: 3px solid #28a745; margin: 0.5rem 0; background-color: white;'>
                <p style='margin: 0; color: #666;'>{update['date']}</p>
                <p style='margin: 0; font-weight: bold;'>{update['update']}</p>
                <p style='margin: 0;'>Status: {update['status']}</p>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    notifications = [
        {"type": "⚠️ Warning", "message": "High bias risk detected in recent evaluations", "time": "1 hour ago"},
        {"type": "ℹ️ Info", "message": "System maintenance scheduled for tonight", "time": "2 hours ago"},
        {"type": "✅ Success", "message": "Weekly report generated successfully", "time": "3 hours ago"}
    ]
    
    for notif in notifications:
        st.markdown(f"""
            <div style='padding: 0.5rem; border-left: 3px solid #ffc107; margin: 0.5rem 0; background-color: white;'>
                <p style='margin: 0; color: #666;'>{notif['time']}</p>
                <p style='margin: 0; font-weight: bold;'>{notif['type']}</p>
                <p style='margin: 0;'>{notif['message']}</p>
            </div>
        """, unsafe_allow_html=True)

# Help & Support Section in Sidebar
with st.sidebar:
    st.header("Need Help?")
    st.markdown("""
    - 📚 [Documentation](https://docs.example.com)
    - 💡 [Quick Start Guide](https://guide.example.com)
    - 🎯 [Best Practices](https://best-practices.example.com)
    - 📧 [Contact Support](mailto:support@example.com)
    """)

# Footer
st.markdown("---")
st.caption("Hiring Platform v2.0 - Powered by Tharazeenuddin")
st.caption("© 2025 Hiring Platform. All rights reserved.")
