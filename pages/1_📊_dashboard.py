import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Hiring Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Mock data generation
@st.cache_data
def generate_mock_data():
    positions = ['Data Scientist', 'Software Engineer', 'Product Manager', 'UX Designer',
                'ML Engineer', 'DevOps Engineer', 'Frontend Developer', 'Backend Developer']
    departments = ['Engineering', 'Product', 'Design', 'Data']
    locations = ['New York', 'San Francisco', 'London', 'Singapore', 'Berlin']
    
    # Generate dates as datetime objects
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(50)]
    
    data = {
        'id': range(1, 51),
        'name': [f"Candidate {i}" for i in range(1, 51)],
        'position': [positions[i % len(positions)] for i in range(50)],
        'department': [departments[i % len(departments)] for i in range(50)],
        'location': [locations[i % len(locations)] for i in range(50)],
        'score': [round(50 + (i % 50), 1) for i in range(50)],
        'bias_risk': ['Low' if i > 30 else 'Medium' if i > 15 else 'High' for i in range(50)],
        'status': ['Review' if i < 20 else 'Approved' if i < 35 else 'Rejected' for i in range(50)],
        'application_date': dates
    }
    df = pd.DataFrame(data)
    # Convert application_date to datetime
    df['application_date'] = pd.to_datetime(df['application_date'])
    return df

# Load data
df = generate_mock_data()

# Sidebar filters
st.sidebar.title('Filters')

# Date range filter with default values
default_start_date = datetime.now() - timedelta(days=30)
default_end_date = datetime.now()

date_range = st.sidebar.date_input(
    "Date Range",
    value=(default_start_date, default_end_date),
    key='date_range'
)

# Convert date_range to datetime for comparison
if len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
else:
    start_date = pd.to_datetime(default_start_date)
    end_date = pd.to_datetime(default_end_date)

# Department filter
department_filter = st.sidebar.multiselect(
    'Department',
    options=df['department'].unique(),
    default=df['department'].unique()
)

# Position filter
position_filter = st.sidebar.multiselect(
    'Position',
    options=df['position'].unique(),
    default=df['position'].unique()
)

# Location filter
location_filter = st.sidebar.multiselect(
    'Location',
    options=df['location'].unique(),
    default=df['location'].unique()
)

# Status filter
status_filter = st.sidebar.multiselect(
    'Status',
    options=df['status'].unique(),
    default=df['status'].unique()
)

# Apply filters
mask = (
    df['department'].isin(department_filter) &
    df['position'].isin(position_filter) &
    df['location'].isin(location_filter) &
    df['status'].isin(status_filter) &
    (df['application_date'].dt.date >= start_date.date()) &
    (df['application_date'].dt.date <= end_date.date())
)
filtered_df = df[mask]

# Main content
st.title('📊 HR Analytics Dashboard')

# KPI metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Candidates",
        len(filtered_df),
        delta=f"{len(filtered_df) - len(df)}"
    )

with col2:
    approval_rate = round(len(filtered_df[filtered_df['status'] == 'Approved']) / len(filtered_df) * 100, 1) if len(filtered_df) > 0 else 0
    st.metric(
        "Approval Rate",
        f"{approval_rate}%",
        delta=f"{round(approval_rate - 50, 1)}%"
    )

with col3:
    avg_score = round(filtered_df['score'].mean(), 1) if len(filtered_df) > 0 else 0
    st.metric(
        "Average Score",
        avg_score,
        delta=f"{round(avg_score - df['score'].mean(), 1)}"
    )

with col4:
    low_bias = round(len(filtered_df[filtered_df['bias_risk'] == 'Low']) / len(filtered_df) * 100, 1) if len(filtered_df) > 0 else 0
    st.metric(
        "Low Bias Rate",
        f"{low_bias}%",
        delta=f"{round(low_bias - 70, 1)}%"
    )

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Score Distribution")
    if not filtered_df.empty:
        fig = px.histogram(
            filtered_df,
            x='score',
            nbins=20,
            title='Distribution of AI Scores'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for the selected filters")

    st.subheader("Applications by Department")
    if not filtered_df.empty:
        dept_counts = filtered_df['department'].value_counts()
        fig = px.pie(
            names=dept_counts.index,
            values=dept_counts.values,
            title='Applications by Department'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for the selected filters")

with col2:
    st.subheader("Status Distribution")
    if not filtered_df.empty:
        status_counts = filtered_df['status'].value_counts()
        fig = px.pie(
            names=status_counts.index,
            values=status_counts.values,
            title='Application Status Distribution',
            color=status_counts.index,
            color_discrete_map={
                'Approved': '#4CAF50',
                'Review': '#FFC107',
                'Rejected': '#F44336'
            }
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for the selected filters")

    st.subheader("Bias Risk Distribution")
    if not filtered_df.empty:
        risk_counts = filtered_df['bias_risk'].value_counts()
        fig = px.bar(
            x=risk_counts.index,
            y=risk_counts.values,
            title='Distribution of Bias Risk Levels',
            color=risk_counts.index,
            color_discrete_map={
                'Low': '#4CAF50',
                'Medium': '#FFC107',
                'High': '#F44336'
            }
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for the selected filters")

# Candidates table
st.subheader("Candidates Overview")

if not filtered_df.empty:
    # Color coding for different statuses and risks
    def style_dataframe(df):
        return df.style.apply(
            lambda x: ['background-color: #E8F5E9' if v == 'Approved'
                      else 'background-color: #FFEBEE' if v == 'Rejected'
                      else '' for v in x],
            subset=['status']
        ).apply(
            lambda x: ['color: #4CAF50' if v == 'Low'
                      else 'color: #FFC107' if v == 'Medium'
                      else 'color: #F44336' for v in x],
            subset=['bias_risk']
        )

    # Display styled dataframe
    display_df = filtered_df.copy()
    display_df['application_date'] = display_df['application_date'].dt.strftime('%Y-%m-%d')
    st.dataframe(
        style_dataframe(display_df),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No candidates match the selected filters")

# Export button
if not filtered_df.empty:
    export_df = filtered_df.copy()
    export_df['application_date'] = export_df['application_date'].dt.strftime('%Y-%m-%d')
    st.download_button(
        label="📥 Export Data",
        data=export_df.to_csv(index=False).encode('utf-8'),
        file_name=f"hr_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime='text/csv'
    )
