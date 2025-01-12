import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Human Oversight Interface",
    page_icon="👥",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { padding: 0rem 1rem; }
    .oversight-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        margin: 1rem 0;
    }
    .review-card {
        border: 1px solid #dee2e6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Mock oversight data
@st.cache_data
def get_oversight_data():
    return {
        'pending_reviews': [
            {
                'id': 1,
                'name': 'John Smith',
                'position': 'Senior Data Scientist',
                'ai_score': 92,
                'bias_risk': 'Low',
                'flags': [],
                'last_modified': '2024-01-10'
            },
            {
                'id': 2,
                'name': 'Sarah Johnson',
                'position': 'ML Engineer',
                'ai_score': 88,
                'bias_risk': 'Medium',
                'flags': ['Education bias detected'],
                'last_modified': '2024-01-09'
            }
        ],
        'recent_decisions': pd.DataFrame({
            'id': [3, 4, 5, 6],
            'name': ['Mike Chen', 'Emma Davis', 'James Wilson', 'Ana Lopez'],
            'position': ['Data Engineer', 'Data Scientist', 'ML Engineer', 'Data Analyst'],
            'ai_score': [95, 85, 89, 87],
            'human_score': [90, 82, 92, 85],
            'final_decision': ['Approved', 'Rejected', 'Approved', 'Review'],
            'reviewer': ['Alice Brown', 'Bob Wilson', 'Carol White', 'David Lee'],
            'date': ['2024-01-08', '2024-01-07', '2024-01-06', '2024-01-05']
        }),
        'override_statistics': {
            'total_reviews': 100,
            'override_rate': 0.15,
            'average_score_adjustment': -2.5,
            'common_reasons': {
                'Technical Skills Overestimated': 35,
                'Experience Undervalued': 25,
                'Cultural Fit Concerns': 20,
                'Communication Skills': 15,
                'Other': 5
            }
        }
    }

# Load oversight data
data = get_oversight_data()

# Header
st.title("👥 Human Oversight Interface")
st.markdown("Review and adjust AI decisions with human expertise")

# Overview metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Pending Reviews",
        len(data['pending_reviews']),
        delta="2 new"
    )

with col2:
    st.metric(
        "Override Rate",
        f"{data['override_statistics']['override_rate']*100:.1f}%",
        delta="-2.5%"
    )

with col3:
    st.metric(
        "Avg Score Adjustment",
        f"{data['override_statistics']['average_score_adjustment']:+.1f}",
        delta="Minimal bias"
    )

with col4:
    st.metric(
        "Total Reviews",
        data['override_statistics']['total_reviews'],
        delta="+10 this week"
    )

# Main content tabs
tab1, tab2, tab3 = st.tabs(["Pending Reviews", "Recent Decisions", "Override Analytics"])

# Pending Reviews tab
with tab1:
    st.subheader("Pending Reviews")
    
    for candidate in data['pending_reviews']:
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"### {candidate['name']}")
                st.write(f"**Position:** {candidate['position']}")
                if candidate['flags']:
                    for flag in candidate['flags']:
                        st.warning(flag)
            
            with col2:
                st.metric("AI Score", candidate['ai_score'])
                st.write(f"**Bias Risk:** {candidate['bias_risk']}")
            
            with col3:
                st.write(f"**Last Modified:** {candidate['last_modified']}")
                if st.button("Review Now", key=f"review_{candidate['id']}", type="primary"):
                    st.write("Opening review panel...")
            
            # Score adjustment slider
            adjusted_score = st.slider(
                "Adjust Score",
                min_value=0,
                max_value=100,
                value=candidate['ai_score'],
                key=f"slider_{candidate['id']}"
            )
            
            # Justification input
            st.text_area(
                "Justification for Adjustment",
                key=f"justification_{candidate['id']}"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                st.button(
                    "Confirm Adjustment",
                    key=f"confirm_{candidate['id']}",
                    use_container_width=True
                )
            with col2:
                st.button(
                    "Reset to AI Score",
                    key=f"reset_{candidate['id']}",
                    use_container_width=True
                )
            
            st.divider()

# Recent Decisions tab
with tab2:
    st.subheader("Recent Decisions")
    
    # Style the dataframe
    def style_decision(df):
        df_styled = pd.DataFrame('', index=df.index, columns=df.columns)
        
        # Style for final_decision column
        decision_styles = {
            'Approved': 'background-color: #d4edda',
            'Rejected': 'background-color: #f8d7da',
            'Review': 'background-color: #fff3cd'
        }
        for decision, style in decision_styles.items():
            mask = (df['final_decision'] == decision)
            df_styled.loc[mask, 'final_decision'] = style
            
        # Style for score difference
        df['score_diff'] = df['human_score'] - df['ai_score']
        mask_positive = df['score_diff'] > 0
        mask_negative = df['score_diff'] < 0
        df_styled.loc[mask_positive, 'human_score'] = 'color: green'
        df_styled.loc[mask_negative, 'human_score'] = 'color: red'
        
        return df_styled

    # Display styled dataframe
    recent_decisions_df = data['recent_decisions']
    st.dataframe(
        recent_decisions_df.style.apply(style_decision, axis=None),
        use_container_width=True
    )

# Override Analytics tab
with tab3:
    st.subheader("Override Analytics")
    
    # Override reasons chart
    reasons = data['override_statistics']['common_reasons']
    fig = px.pie(
        values=list(reasons.values()),
        names=list(reasons.keys()),
        title="Common Override Reasons"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Override trend
    trend_data = pd.DataFrame({
        'date': pd.date_range(start='2024-01-01', periods=10),
        'override_rate': [0.18, 0.16, 0.15, 0.14, 0.15, 0.13, 0.12, 0.15, 0.14, 0.15]
    })
    
    fig = px.line(
        trend_data,
        x='date',
        y='override_rate',
        title="Override Rate Trend"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Score adjustment distribution
    adjustments = pd.DataFrame({
        'adjustment': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        'frequency': [5, 8, 12, 15, 20, 25, 18, 10, 7, 5, 3]
    })
    
    fig = px.bar(
        adjustments,
        x='adjustment',
        y='frequency',
        title="Score Adjustment Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# Export options
st.divider()
col1, col2 = st.columns(2)

with col1:
    if st.button("📥 Export Override Report", use_container_width=True):
        st.download_button(
            label="Download Report",
            data="Override analysis report...",  # In real app, generate report
            file_name=f"override_report_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf"
        )

with col2:
    if st.button("📊 Download Analytics", use_container_width=True):
        st.download_button(
            label="Download Data",
            data="Analytics data...",  # In real app, prepare data
            file_name=f"override_analytics_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

# Footer
st.markdown("---")
st.caption("Human Oversight Interface v2.0 - Ensuring Fair and Accurate Evaluations")
