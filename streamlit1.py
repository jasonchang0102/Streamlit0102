import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Set the page configuration
st.set_page_config(layout="wide", page_title="Jason Chang | Portfolio", page_icon="📊")

# Scroll to top function
def scroll_to_top():
    components.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )

# Professional CSS styling
st.markdown("""
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap' rel='stylesheet'>
    <style>
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }
        
        /* Hide default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main content */
        .block-container {
            padding: 3rem 5rem !important;
            max-width: 1100px;
        }
        
        /* Hero - Name */
        .hero-name {
            font-family: 'Poppins', sans-serif;
            font-size: 64px;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 2px;
            margin-bottom: 0;
            line-height: 1.1;
        }
        
        /* Hero - Portfolio */
        .hero-title {
            font-family: 'Poppins', sans-serif;
            font-size: 42px;
            font-weight: 300;
            color: #64748b;
            letter-spacing: 6px;
            margin-top: 5px;
            margin-bottom: 15px;
        }
        
        /* Accent line */
        .accent-line {
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, #f59e0b, #d97706);
            margin: 15px 0 20px 0;
            border-radius: 2px;
        }
        
        /* Tagline */
        .hero-tagline {
            font-family: 'Poppins', sans-serif;
            font-size: 18px;
            font-weight: 500;
            color: #f59e0b;
            letter-spacing: 0.5px;
            margin-bottom: 25px;
        }
        
        /* Body text */
        .body-text {
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            font-weight: 400;
            color: #94a3b8;
            line-height: 1.75;
            margin-bottom: 16px;
        }
        
        /* Section headers */
        .section-header {
            font-family: 'Poppins', sans-serif;
            font-size: 28px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 1px solid #334155;
        }
        
        /* Subsection headers */
        .subsection-header {
            font-family: 'Poppins', sans-serif;
            font-size: 18px;
            font-weight: 600;
            color: #f59e0b;
            margin-top: 25px;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Card styling */
        .info-card {
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid #334155;
            border-radius: 10px;
            padding: 20px;
            margin: 12px 0;
        }
        
        /* Metric highlight */
        .metric-highlight {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            font-weight: 700;
            color: #22c55e;
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #0f172a;
            border-right: 1px solid #1e293b;
        }
        
        section[data-testid="stSidebar"] .stRadio > div > label {
            background: transparent !important;
            color: #64748b !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            padding: 10px 12px !important;
            border-radius: 6px !important;
            border-left: 2px solid transparent !important;
            margin: 2px 0 !important;
        }
        
        section[data-testid="stSidebar"] .stRadio > div > label:hover {
            background: rgba(59, 130, 246, 0.08) !important;
            color: #e2e8f0 !important;
        }
        
        /* Nav title */
        .nav-title {
            font-family: 'Poppins', sans-serif;
            font-size: 11px;
            font-weight: 600;
            color: #475569;
            letter-spacing: 2px;
            margin-bottom: 15px;
            text-transform: uppercase;
        }
        
        /* Quote */
        .quote-text {
            font-family: 'Inter', sans-serif;
            font-size: 20px;
            font-weight: 400;
            color: #94a3b8;
            font-style: italic;
            line-height: 1.6;
            border-left: 3px solid #f59e0b;
            padding-left: 20px;
            margin: 30px 0;
        }
        
        /* Cert card */
        .cert-card {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 16px 20px;
            margin: 15px 0;
        }
        
        .cert-title {
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 4px;
        }
        
        .cert-org {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: #64748b;
        }
        
        /* Links */
        a {
            color: #3b82f6 !important;
            text-decoration: none !important;
        }
        
        a:hover {
            color: #f59e0b !important;
        }
        
        /* Override defaults */
        h1, h2, h3 {
            font-family: 'Poppins', sans-serif !important;
            color: #ffffff !important;
        }
        
        p, li {
            font-family: 'Inter', sans-serif !important;
            color: #94a3b8 !important;
            font-size: 15px !important;
            line-height: 1.7 !important;
        }
        
        strong { color: #e2e8f0 !important; }
        
        /* Skills */
        .skills-category {
            font-family: 'Poppins', sans-serif;
            font-size: 15px;
            font-weight: 600;
            color: #f59e0b;
            margin-bottom: 8px;
        }
        
        .skills-list {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: #94a3b8;
            line-height: 1.5;
        }
        
        /* Bullet points */
        .bullet-item {
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            color: #94a3b8;
            line-height: 1.7;
            margin-bottom: 8px;
            padding-left: 15px;
            position: relative;
        }
        
        .bullet-item::before {
            content: "→";
            position: absolute;
            left: 0;
            color: #f59e0b;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<p class="nav-title">NAVIGATION</p>', unsafe_allow_html=True)
    page = st.radio(
        "",
        [
            "Welcome",
            "Engagement & Monetization",
            "Executive Insights",
            "Warehouse Optimization",
            "Process Automation",
            "Skills",
            "Certifications",
            "Contact"
        ],
        label_visibility="collapsed"
    )

# Scroll to top on every page load
scroll_to_top()

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    
    def assign_bucket(games):
        if 1 <= games <= 3: return 'Very Low'
        elif 4 <= games <= 5: return 'Low'
        elif 6 <= games <= 9: return 'Medium'
        elif 10 <= games <= 68: return 'High'
        return 'Unknown'
    
    data['games_played_bucket'] = data['games_played'].apply(assign_bucket)
    return data

data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)

# ==================== WELCOME ====================
if page == "Welcome":
    st.markdown('<p class="hero-name">JASON CHANG</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">PORTFOLIO</p>', unsafe_allow_html=True)
    st.markdown('<div class="accent-line"></div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-tagline">National Revenue Growth Leader Powered by Analytics</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="body-text">
    Data-driven leader with 10+ years scaling national programs through market strategy, analytics, and channel expansion. I translate complex data into actionable insights that accelerate decisions, improve conversion, and drive measurable revenue growth.
    </p>
    <p class="body-text">
    Proficient in <strong>Snowflake, SQL, Power BI, and Python</strong>. Experienced leading cross-functional programs, unifying fragmented data systems, and automating reporting pipelines.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="accent-line" style="margin-top: 35px;"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">10+</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Years Experience</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">85%</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Process Efficiency Gains</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">21%</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Revenue Growth</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== ENGAGEMENT & MONETIZATION ====================
elif page == "Engagement & Monetization":
    st.markdown('<p class="section-header">Player Engagement & Monetization Analytics</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Tasked with maximizing revenue and player engagement for Warcraft during two key in-game events. The challenge: understanding how different player segments interacted with events and identifying monetization opportunities.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet-item">Identify high-spending player segments for targeted promotions</p>
    <p class="bullet-item">Analyze low spending trends by region and platform</p>
    <p class="bullet-item">Conduct exploratory analysis on spending behaviors</p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text"><strong>Analysis Approach:</strong></p>
    <p class="bullet-item">Comprehensive EDA using Python for player spending behavior</p>
    <p class="bullet-item">K-Means Clustering to segment players by engagement metrics</p>
    <p class="bullet-item">Heatmap analysis to identify spending patterns across segments</p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p class="body-text"><strong>Strategic Output:</strong></p>
    <p class="bullet-item">Prioritized Platform 3, Region 1 as high-value segment for promotions</p>
    <p class="bullet-item">Flagged Platform 1, Region 5 for strategic intervention</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/333', use_container_width=True)
    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/222', use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/777', use_container_width=True)
    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/111', use_container_width=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/444', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/555', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/666', use_container_width=True)

    # Heatmap
    heatmap_data = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    fig1.patch.set_facecolor('#1e293b')
    ax1.set_facecolor('#1e293b')
    sns.heatmap(heatmap_data, annot=True, cmap="YlOrBr", fmt=".2f", linewidths=.5, ax=ax1)
    ax1.set_title("Avg Spend by Region & Platform", color='white', fontsize=12, fontweight='600')
    ax1.tick_params(colors='white')
    ax1.set_xlabel('Platform', color='#94a3b8', fontsize=10)
    ax1.set_ylabel('Region', color='#94a3b8', fontsize=10)
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

    # KDE plots
    event_1_data = data[(data['Date'] >= '2017-01-24') & (data['Date'] <= '2017-02-14')]
    event_2_data = data[(data['Date'] >= '2017-02-28') & (data['Date'] <= '2017-03-21')]

    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    fig.patch.set_facecolor('#1e293b')
    
    for ax in axes.flat:
        ax.set_facecolor('#1e293b')
        ax.tick_params(colors='white', labelsize=8)
        ax.xaxis.label.set_color('#94a3b8')
        ax.yaxis.label.set_color('#94a3b8')
        ax.title.set_color('white')

    plots = [
        ('games_played', 'Games Played'),
        ('skill_last', 'Skill Level'),
        ('items_crafted', 'Items Crafted'),
        ('dollars_spent', 'Dollars Spent')
    ]
    
    for idx, (col, title) in enumerate(plots):
        ax = axes[idx // 2, idx % 2]
        sns.kdeplot(event_1_data[col], fill=True, color="#3b82f6", label="Event 1", ax=ax, alpha=0.6)
        sns.kdeplot(event_2_data[col], fill=True, color="#f59e0b", label="Event 2", ax=ax, alpha=0.6)
        ax.set_title(title, fontsize=11, fontweight='600')
        ax.legend(fontsize=8)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', use_container_width=True)

    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <p class="metric-highlight">+21%</p>
            <p style="color: #e2e8f0; font-weight: 600; font-size: 14px; margin: 5px 0;">Engagement Increase</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Targeted promotions in high-value segments</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
            <p class="metric-highlight">-15%</p>
            <p style="color: #e2e8f0; font-weight: 600; font-size: 14px; margin: 5px 0;">Churn Reduction</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Strategic adjustments improved retention</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== EXECUTIVE INSIGHTS ====================
elif page == "Executive Insights":
    st.markdown('<p class="section-header">Executive Business Intelligence Dashboard</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Post-merger environment with fragmented data across multiple systems. Finance department lacked unified performance measurement and reporting capabilities.
    </p>
    """, unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', use_container_width=True)
    
    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Design and implement dynamic reporting solution with accurate KPIs for executive decision-making.
    </p>
    """, unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', use_container_width=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet-item"><strong>Data Engineering:</strong> SQL-based extraction, deduplication, normalization</p>
    <p class="bullet-item"><strong>Schema Design:</strong> Flexible architecture for evolving business needs</p>
    <p class="bullet-item"><strong>Dashboard Development:</strong> Collaborated with stakeholders on key metrics</p>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <p style="color: #f59e0b; font-weight: 600; font-size: 14px;">Strategic Planning</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Enhanced management decision-making with real-time insights</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
            <p style="color: #f59e0b; font-weight: 600; font-size: 14px;">Adaptive Reporting</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Scalable system that evolves with business changes</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== WAREHOUSE OPTIMIZATION ====================
elif page == "Warehouse Optimization":
    st.markdown('<p class="section-header">Warehouse & GL Account Optimization</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Escalating logistics and warehouse costs impacting bottom line. SKYLAB and 3PL Logistics divisions identified as key areas for potential inefficiency.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Conduct detailed cost analysis to identify waste, inefficiencies, and optimization opportunities without compromising operational quality.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet-item"><strong>Financial Analysis:</strong> Python-based deep dive into expenditure patterns</p>
    <p class="bullet-item"><strong>Inefficiency Mapping:</strong> Pinpointed specific cost drivers in both divisions</p>
    <p class="bullet-item"><strong>Optimization Strategy:</strong> Developed actionable recommendations for operations, resource allocation, and vendor contracts</p>
    """, unsafe_allow_html=True)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', use_container_width=True)

    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
        <p class="bullet-item"><strong>Cost Reduction:</strong> Identified multiple inefficiencies leading to significant savings</p>
        <p class="bullet-item"><strong>Streamlined Operations:</strong> Implemented process improvements with positive P&L impact</p>
        <p class="bullet-item"><strong>Continuous Improvement:</strong> Established ongoing optimization framework</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== PROCESS AUTOMATION ====================
elif page == "Process Automation":
    st.markdown('<p class="section-header">Quarterly Royalty Management Automation</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Quarterly royalty management required month-long manual Excel lookups across years of unorganized data. High error risk and significant analyst time burden.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p style="color: #f59e0b; font-weight: 600; font-size: 13px; letter-spacing: 1px;">PYTHON AUTOMATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', use_container_width=True)
    with col2:
        st.markdown('<p style="color: #f59e0b; font-weight: 600; font-size: 13px; letter-spacing: 1px;">VBA INTEGRATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', use_container_width=True)

    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Transform month-long manual process into automated workflow while maintaining accuracy and audit compliance.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet-item"><strong>Data Audit:</strong> Mapped historical data structures and reporting requirements</p>
    <p class="bullet-item"><strong>Python Pipeline:</strong> Built automated data consolidation and validation</p>
    <p class="bullet-item"><strong>VBA Integration:</strong> Automated Excel report generation for stakeholder delivery</p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">85%</p>
            <p style="color: #e2e8f0; font-weight: 600; font-size: 13px; margin: 5px 0;">Time Saved</p>
            <p style="color: #64748b; font-size: 12px; margin: 0;">1 month → 8 hours</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight" style="color: #3b82f6;">2</p>
            <p style="color: #e2e8f0; font-weight: 600; font-size: 13px; margin: 5px 0;">FTEs Freed</p>
            <p style="color: #64748b; font-size: 12px; margin: 0;">Senior analysts</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight" style="color: #f59e0b;">↑</p>
            <p style="color: #e2e8f0; font-weight: 600; font-size: 13px; margin: 5px 0;">Accuracy</p>
            <p style="color: #64748b; font-size: 12px; margin: 0;">Eliminated manual errors</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== SKILLS ====================
elif page == "Skills":
    st.markdown('<p class="section-header">Technical Expertise</p>', unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=400)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Languages</p>
            <p class="skills-list">Python, SQL, VBA</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Data Engineering</p>
            <p class="skills-list">Snowflake, ETL Pipelines, SSMS, AS400, Power Query</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Analytics Libraries</p>
            <p class="skills-list">Pandas, NumPy, Seaborn, Matplotlib, SciPy, TensorFlow</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Statistical Methods</p>
            <p class="skills-list">A/B Testing, Predictive Modeling, Regression, Time Series, Hypothesis Testing</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">BI & Visualization</p>
            <p class="skills-list">Power BI, Looker Studio, Google Analytics</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Data Modeling</p>
            <p class="skills-list">Star Schema, ER Diagrams, DAG, Normalization</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== CERTIFICATIONS ====================
elif page == "Certifications":
    st.markdown('<p class="section-header">Certifications</p>', unsafe_allow_html=True)
    
    certs = [
        ("Supervised Machine Learning", "Stanford / Coursera • 2024", 
         "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/STANDFORD.PNG",
         "https://www.coursera.org/account/accomplishments/verify/YHLXRW3TL569"),
        ("Neural Networks & Deep Learning", "DeepLearning.AI • 2024",
         "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/DeepAI",
         "https://www.coursera.org/account/accomplishments/verify/P3MNNDS44DLL"),
        ("Power BI Data Visualization", "EdX • 2019",
         "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/edx",
         "https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79"),
        ("AWS Cloud Practitioner", "Amazon Web Services • 2019",
         "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/AWS1", None),
        ("SQL Certification", "Sololearn • 2017",
         "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/SQLsololearn",
         "https://www.sololearn.com/en/certificates/CT-YUFRJBUH")
    ]
    
    for title, org, img, link in certs:
        st.markdown(f"""
        <div class="cert-card">
            <p class="cert-title">{title}</p>
            <p class="cert-org">{org}</p>
        </div>
        """, unsafe_allow_html=True)
        st.image(img, width=600)
        if link:
            st.markdown(f"<a href='{link}' target='_blank'>Verify →</a>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ==================== CONTACT ====================
elif page == "Contact":
    st.markdown('<p class="section-header">Let\'s Connect</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="quote-text">
    "In God we trust; for all else, we turn to the validation of data."
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <p style="color: #475569; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Phone</p>
            <p style="color: #e2e8f0; font-size: 16px; margin: 0;">(626) 203-3319</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p style="color: #475569; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Email</p>
            <p style="color: #e2e8f0; font-size: 16px; margin: 0;">jason.chang01022021@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <p style="color: #475569; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">LinkedIn</p>
            <p style="color: #e2e8f0; font-size: 16px; margin: 0;"><a href="https://linkedin.com/in/jchang0102" target="_blank">linkedin.com/in/jchang0102</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p style="color: #475569; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Location</p>
            <p style="color: #e2e8f0; font-size: 16px; margin: 0;">Irvine, CA</p>
        </div>
        """, unsafe_allow_html=True)
