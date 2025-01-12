import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="AI Explanation Panel",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .explanation-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        margin: 1rem 0;
    }
    .highlight {
        background-color: #e9ecef;
        padding: 0.5rem;
        border-radius: 0.25rem;
    }
    </style>
""", unsafe_allow_html=True)

# Mock AI explanation data
@st.cache_data
def get_ai_explanation_data():
    return {
        'decision_factors': {
            'Technical Skills': {
                'weight': 0.35,
                'score': 92,
                'explanation': 'Strong proficiency in required technical skills',
                'confidence': 0.95,
                'key_points': [
                    'Advanced Python programming skills',
                    'Extensive ML/AI experience',
                    'Strong cloud platform knowledge'
                ]
            },
            'Experience': {
                'weight': 0.30,
                'score': 88,
                'explanation': 'Relevant experience in similar roles',
                'confidence': 0.90,
                'key_points': [
                    'Leadership experience',
                    'Project management skills',
                    'Industry expertise'
                ]
            },
            'Education': {
                'weight': 0.20,
                'score': 95,
                'explanation': 'Advanced degree in relevant field',
                'confidence': 0.98,
                'key_points': [
                    'PhD in Computer Science',
                    'Research background',
                    'Academic achievements'
                ]
            },
            'Cultural Fit': {
                'weight': 0.15,
                'score': 90,
                'explanation': 'Strong alignment with company values',
                'confidence': 0.85,
                'key_points': [
                    'Communication skills',
                    'Team collaboration',
                    'Leadership potential'
                ]
            }
        },
        'bias_analysis': {
            'gender_bias': {'risk': 'Low', 'confidence': 0.95},
            'age_bias': {'risk': 'Low', 'confidence': 0.92},
            'education_bias': {'risk': 'Medium', 'confidence': 0.85},
            'cultural_bias': {'risk': 'Low', 'confidence': 0.90}
        },
        'evaluation_process': [
            {
                'step': 1,
                'name': 'Resume Analysis',
                'description': 'Parsed and analyzed resume content',
                'duration': '2.3s',
                'confidence': 0.95
            },
            {
                'step': 2,
                'name': 'Skills Validation',
                'description': 'Verified technical skills and experience',
                'duration': '3.1s',
                'confidence': 0.92
            },
            {
                'step': 3,
                'name': 'Background Check',
                'description': 'Validated education and work history',
                'duration': '4.2s',
                'confidence': 0.88
            },
            {
                'step': 4,
                'name': 'Bias Detection',
                'description': 'Analyzed for potential biases',
                'duration': '1.8s',
                'confidence': 0.94
            }
        ],
        'model_interpretation': {
            'feature_importance': {
                'Technical Skills Score': 0.35,
                'Years of Experience': 0.25,
                'Education Level': 0.20,
                'Leadership Experience': 0.15,
                'Project Complexity': 0.05
            }
        }
    }

# Load explanation data
explanation_data = get_ai_explanation_data()

# Header
st.title("🤖 AI Decision Explanation Panel")
st.markdown("Understanding how the AI evaluates candidates")

# Decision Factors Analysis
st.header("Decision Factors Analysis")

# Create weighted score visualization
factors_df = pd.DataFrame({
    'Factor': list(explanation_data['decision_factors'].keys()),
    'Weight': [f['weight'] for f in explanation_data['decision_factors'].values()],
    'Score': [f['score'] for f in explanation_data['decision_factors'].values()],
    'Weighted Score': [f['weight'] * f['score'] for f in explanation_data['decision_factors'].values()]
})

# Display factors breakdown
col1, col2 = st.columns([2, 1])

with col1:
    fig = px.bar(
        factors_df,
        x='Factor',
        y=['Weight', 'Score'],
        barmode='group',
        title='Decision Factors: Weights vs Scores'
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.pie(
        factors_df,
        values='Weight',
        names='Factor',
        title='Factor Weights Distribution'
    )
    st.plotly_chart(fig, use_container_width=True)

# Detailed factor analysis
st.subheader("Detailed Factor Analysis")
for factor, details in explanation_data['decision_factors'].items():
    with st.expander(f"{factor} (Score: {details['score']}, Confidence: {details['confidence']*100:.1f}%)", expanded=True):
        st.write(f"**Weight:** {details['weight']}")
        st.write(f"**Explanation:** {details['explanation']}")
        st.write("**Key Points:**")
        for point in details['key_points']:
            st.write(f"- {point}")

# Bias Analysis
st.header("Bias Analysis")

# Create bias risk visualization
bias_df = pd.DataFrame({
    'Type': list(explanation_data['bias_analysis'].keys()),
    'Risk': [b['risk'] for b in explanation_data['bias_analysis'].values()],
    'Confidence': [b['confidence'] for b in explanation_data['bias_analysis'].values()]
})

fig = go.Figure(data=[
    go.Bar(name='Confidence', x=bias_df['Type'], y=bias_df['Confidence']),
])
fig.update_layout(title='Bias Analysis Confidence Levels')
st.plotly_chart(fig, use_container_width=True)

# Evaluation Process Visualization
st.header("Evaluation Process")

# Create timeline of evaluation steps
for step in explanation_data['evaluation_process']:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.metric(f"Step {step['step']}", step['name'])
    
    with col2:
        st.write(f"**Description:** {step['description']}")
        st.progress(step['confidence'])
    
    with col3:
        st.write(f"**Duration:** {step['duration']}")
        st.write(f"**Confidence:** {step['confidence']*100:.1f}%")

# Model Interpretation
st.header("Model Interpretation")

# Feature importance visualization
feature_importance = explanation_data['model_interpretation']['feature_importance']
fig = px.bar(
    x=list(feature_importance.keys()),
    y=list(feature_importance.values()),
    title="Feature Importance in AI Decision Making"
)
st.plotly_chart(fig, use_container_width=True)

# Export section
st.divider()
col1, col2 = st.columns(2)

with col1:
    if st.button("📥 Download Full Analysis", use_container_width=True):
        st.download_button(
            label="Download PDF Report",
            data="AI Analysis Report...",  # In real app, generate PDF here
            file_name=f"ai_analysis_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf",
            key="download_report"
        )

with col2:
    if st.button("📊 Export Raw Data", use_container_width=True):
        st.download_button(
            label="Download JSON Data",
            data=str(explanation_data),  # In real app, proper JSON formatting
            file_name=f"ai_data_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json",
            key="download_json"
        )

# Footer
st.markdown("---")
st.caption("AI Explanation System v2.0 - Powered by Advanced Machine Learning")
