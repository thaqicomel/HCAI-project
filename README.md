# Human-Centered AI Hiring Platform

## Overview
This project focuses on designing and prototyping a **Human-Centered AI Hiring Platform** that minimizes bias, ensures transparency, and promotes fairness in the hiring process. The platform incorporates **Human-Centered AI (HCAI)** principles, such as stakeholder control, explainability, and ethical guidelines, to address the challenges of bias and discrimination in AI-driven hiring systems.

The project includes:
1. **AI Explanation Panel:** Provides transparent explanations of AI decisions.
2. **Bias Report:** Detects and mitigates biases in candidate evaluations.
3. **High-Fidelity Prototype:** A non-functional design of the hiring platform, created using tools like **Streamlit**.

---

## Project Deliverables

### 1. **Report**
A comprehensive document that outlines the entire project, including:
- **Introduction:** Importance of addressing bias and ethical concerns in AI hiring platforms.
- **Research:** Ethical challenges, AI principles, and existing frameworks for bias and fairness.
- **Framework Design:** A human-centered framework for AI hiring platforms.
- **Prototype Development:** High-fidelity design of the hiring platform.
- **Testing and Evaluation:** Results of testing the prototype with synthetic data.
- **Conclusion:** Summary of findings, implications, and recommendations.

### 2. **High-Fidelity Prototype**
A **non-functional prototype** of the hiring platform, designed using **Streamlit**. The prototype includes:
- **Bias Detection and Mitigation:** Features to detect and reduce bias in candidate evaluations.
- **Explainable AI (XAI):** Techniques to make AI decisions transparent and understandable.
- **User Interface (UI):** A user-friendly interface for hiring managers to interact with the system.

### 3. **Presentation**
A summary of the project, including:
- **Introduction:** Goals and importance of the project.
- **Research Findings:** Ethical challenges and AI principles.
- **Framework Design:** Human-centered framework for hiring platforms.
- **Prototype Demonstration:** Walkthrough of the high-fidelity prototype.
- **Testing and Evaluation:** Results of testing and evaluation.
- **Conclusion and Recommendations:** Key outcomes and future development.

---

## Features

### 1. **AI Explanation Panel**
- **Decision Factors Analysis:** Breaks down the AI’s decision into key factors (e.g., Technical Skills, Experience, Education, Cultural Fit) with weights, scores, and confidence intervals.
- **Visualizations:** Includes bar charts, pie charts, and feature importance graphs to make the AI’s decision-making process transparent.
- **Detailed Explanations:** Provides step-by-step explanations for each decision factor, including key points and confidence levels.

### 2. **Bias Report**
- **Bias Detection:** Identifies potential biases in candidate evaluations (e.g., gender, age, education, cultural fit).
- **Risk Levels:** Uses color-coded alerts (red, yellow, green) to highlight high, medium, and low-risk biases.
- **Mitigation Recommendations:** Provides actionable recommendations for reducing biases (e.g., anonymizing candidate data).

### 3. **User-Friendly Interface**
- **Interactive Visualizations:** Allows users to explore decision factors and bias risks through interactive charts.
- **Feedback Mechanism:** Lets users provide feedback on the AI’s explanations and bias analysis.
- **Export Options:** Enables users to download the full analysis as a PDF or export raw data as JSON.

---

## Improvements
- **Simplified Summaries:** Added a summary section to provide a quick overview of the AI’s decision.
- **Confidence Intervals:** Included confidence intervals for decision factors to show the range of confidence in the AI’s scores.
- **Color-Coded Bias Alerts:** Used color-coded alerts to highlight high, medium, and low-risk biases.
- **Mitigation Recommendations:** Provided specific recommendations for mitigating biases.
- **Feedback Mechanism:** Added a feedback section for users to rate the explanation and provide comments.

---

## How to Run the Code

### Prerequisites
- Python 3.7 or higher
- Streamlit (`pip install streamlit`)
- Plotly (`pip install plotly`)
- Pandas (`pip install pandas`)

### Steps to Run the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hcai-hiring-platform.git
   cd hcai-hiring-platform
