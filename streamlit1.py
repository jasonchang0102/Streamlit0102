import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page configuration and title
st.set_page_config(layout="wide", page_title="Jason Chang | Portfolio", page_icon="📊")

# Professional CSS styling
st.markdown("""
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap' rel='stylesheet'>
    <style>
        /* Main background and container */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Main content area */
        .block-container {
            padding: 2rem 4rem !important;
            max-width: 1200px;
        }
        
        /* Hero section - Name */
        .hero-name {
            font-family: 'Poppins', sans-serif;
            font-size: 72px;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 3px;
            margin-bottom: 0;
            line-height: 1.1;
        }
        
        /* Hero section - Portfolio */
        .hero-title {
            font-family: 'Poppins', sans-serif;
            font-size: 48px;
            font-weight: 300;
            color: #94a3b8;
            letter-spacing: 8px;
            margin-top: 5px;
            margin-bottom: 20px;
        }
        
        /* Accent divider */
        .accent-line {
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, #f59e0b, #d97706);
            margin: 20px 0 25px 0;
            border-radius: 2px;
        }
        
        /* Tagline */
        .hero-tagline {
            font-family: 'Poppins', sans-serif;
            font-size: 20px;
            font-weight: 500;
            color: #f59e0b;
            letter-spacing: 1px;
            margin-bottom: 30px;
        }
        
        /* Body text */
        .body-text {
            font-family: 'Inter', sans-serif;
            font-size: 17px;
            font-weight: 400;
            color: #cbd5e1;
            line-height: 1.8;
            margin-bottom: 20px;
        }
        
        /* Section headers */
        .section-header {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            font-weight: 600;
            color: #ffffff;
            margin-top: 40px;
            margin-bottom: 25px;
            padding-bottom: 10px;
            border-bottom: 2px solid #334155;
        }
        
        /* Subsection headers */
        .subsection-header {
            font-family: 'Poppins', sans-serif;
            font-size: 22px;
            font-weight: 600;
            color: #f59e0b;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        
        /* Card styling */
        .info-card {
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 25px;
            margin: 15px 0;
            backdrop-filter: blur(10px);
        }
        
        /* Metric highlight */
        .metric-highlight {
            font-family: 'Poppins', sans-serif;
            font-size: 36px;
            font-weight: 700;
            color: #22c55e;
        }
        
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
            border-right: 1px solid #334155;
        }
        
        section[data-testid="stSidebar"] .stRadio > div > label {
            background: transparent !important;
            color: #94a3b8 !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            padding: 12px 15px !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
            border-left: 3px solid transparent !important;
        }
        
        section[data-testid="stSidebar"] .stRadio > div > label:hover {
            background: rgba(59, 130, 246, 0.1) !important;
            color: #ffffff !important;
            border-left: 3px solid #3b82f6 !important;
        }
        
        /* Navigation title */
        .nav-title {
            font-family: 'Poppins', sans-serif;
            font-size: 14px;
            font-weight: 600;
            color: #f59e0b;
            letter-spacing: 2px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #334155;
        }
        
        /* Quote styling */
        .quote-text {
            font-family: 'Poppins', sans-serif;
            font-size: 24px;
            font-weight: 500;
            color: #cbd5e1;
            font-style: italic;
            line-height: 1.6;
            border-left: 4px solid #f59e0b;
            padding-left: 25px;
            margin: 40px 0;
        }
        
        /* Certification card */
        .cert-card {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .cert-title {
            font-family: 'Poppins', sans-serif;
            font-size: 18px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 5px;
        }
        
        .cert-org {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: #94a3b8;
        }
        
        /* Link styling */
        a {
            color: #3b82f6 !important;
            text-decoration: none !important;
        }
        
        a:hover {
            color: #f59e0b !important;
        }
        
        /* Streamlit elements override */
        h1, h2, h3 {
            font-family: 'Poppins', sans-serif !important;
            color: #ffffff !important;
        }
        
        h1 { font-size: 32px !important; font-weight: 600 !important; }
        h2 { font-size: 26px !important; font-weight: 600 !important; color: #f59e0b !important; }
        h3 { font-size: 20px !important; font-weight: 500 !important; }
        
        p, li {
            font-family: 'Inter', sans-serif !important;
            color: #cbd5e1 !important;
            font-size: 16px !important;
            line-height: 1.7 !important;
        }
        
        strong {
            color: #ffffff !important;
        }
        
        /* Skills section */
        .skills-category {
            font-family: 'Poppins', sans-serif;
            font-size: 18px;
            font-weight: 600;
            color: #f59e0b;
            margin-top: 25px;
            margin-bottom: 10px;
        }
        
        .skills-list {
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            color: #94a3b8;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown('<p class="nav-title">NAVIGATION</p>', unsafe_allow_html=True)
    page = st.radio(
        "",
        [
            "Welcome",
            "Engagement & Monetization",
            "Executive Business Insights",
            "Warehouse Optimization",
            "Process Automation",
            "Skills",
            "Certifications",
            "Contact"
        ],
        label_visibility="collapsed"
    )

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    
    def assign_correct_bucket(games_played):
        if games_played >= 1 and games_played <= 3:
            return 'Very Low'
        elif games_played >= 4 and games_played <= 5:
            return 'Low'
        elif games_played >= 6 and games_played <= 9:
            return 'Medium'
        elif games_played >= 10 and games_played <= 68:
            return 'High'
        else:
            return 'Unknown'
    
    data['games_played_bucket'] = data['games_played'].apply(assign_correct_bucket)
    return data

data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)

# ==================== WELCOME PAGE ====================
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
    Skilled in <strong>Snowflake, SQL, Power BI, and Python</strong> to enable scalable, data-backed market impact. Experienced leading cross-functional programs, unifying fragmented data systems, and automating reporting pipelines to improve operational efficiency and revenue outcomes.
    </p>
    """, unsafe_allow_html=True)
    
    # Key highlights
    st.markdown('<div class="accent-line" style="margin-top: 40px;"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">10+</p>
            <p style="color: #94a3b8; font-size: 14px; margin: 0;">Years Experience</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">85%</p>
            <p style="color: #94a3b8; font-size: 14px; margin: 0;">Process Efficiency Gains</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">21%</p>
            <p style="color: #94a3b8; font-size: 14px; margin: 0;">Revenue Growth</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== ENGAGEMENT & MONETIZATION ====================
elif page == "Engagement & Monetization":
    st.markdown('<p class="section-header">Data Analytics: Engagement & Monetization</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    In an effort to maximize revenue and enhance player engagement in Warcraft, we identified the need to analyze player behavior and spending patterns during two key in-game events. The primary challenge was understanding how different segments of players interacted with these events and identifying opportunities to improve both engagement and monetization.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Lead the data analytics process, focusing on:<br>
    • Identifying high-spending player segments for targeted promotions<br>
    • Understanding low spending trends in specific regions and platforms<br>
    • Conducting exploratory data analysis on spending behaviors related to games played, skill levels, and items crafted
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    <strong>Data Exploration and Analysis:</strong><br>
    • Conducted comprehensive exploratory data analysis using Python<br>
    • Utilized K-Means Clustering to segment players based on engagement metrics<br>
    • Performed heatmap analysis to identify patterns of player engagement and spending
    </p>
    <p class="body-text">
    <strong>Strategic Implementation:</strong><br>
    • Identified high-spending segments in Platform 3, Region 1 as priority for future promotions<br>
    • Highlighted low spending in Platform 1, Region 5 for strategic adjustment
    </p>
    """, unsafe_allow_html=True)

    # Visualizations
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/333', use_container_width=True)
    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/222', use_container_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/777', caption='Distribution of Spending Across Skill Brackets', use_container_width=True)
    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/111', caption='Day-by-Day Churn Rate: Event 1 vs Event 2', use_container_width=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/444', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/555', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/666', use_container_width=True)

    # Heatmap
    heatmap_data = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    fig1.patch.set_facecolor('#1e293b')
    ax1.set_facecolor('#1e293b')
    sns.heatmap(heatmap_data, annot=True, cmap="YlOrBr", fmt=".2f", linewidths=.5, ax=ax1,
                cbar_kws={'label': 'Avg Dollars Spent'})
    ax1.set_title("Average Dollars Spent by Region and Platform", color='white', fontsize=14, fontweight='bold')
    ax1.tick_params(colors='white')
    ax1.set_xlabel('Platform', color='white')
    ax1.set_ylabel('Region', color='white')
    st.pyplot(fig1)
    plt.close(fig1)

    # KDE plots
    event_1_start, event_1_end = pd.Timestamp('2017-01-24'), pd.Timestamp('2017-02-14')
    event_2_start, event_2_end = pd.Timestamp('2017-02-28'), pd.Timestamp('2017-03-21')
    event_1_data = data[(data['Date'] >= event_1_start) & (data['Date'] <= event_1_end)]
    event_2_data = data[(data['Date'] >= event_2_start) & (data['Date'] <= event_2_end)]

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.patch.set_facecolor('#1e293b')
    
    for ax in axes.flat:
        ax.set_facecolor('#1e293b')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')

    sns.kdeplot(event_1_data['games_played'], fill=True, color="#3b82f6", label="Event 1", ax=axes[0, 0], alpha=0.7)
    sns.kdeplot(event_2_data['games_played'], fill=True, color="#f59e0b", label="Event 2", ax=axes[0, 0], alpha=0.7)
    axes[0, 0].set_title('Distribution of Games Played', fontweight='bold')
    axes[0, 0].legend()

    sns.kdeplot(event_1_data['skill_last'], fill=True, color="#3b82f6", label="Event 1", ax=axes[0, 1], alpha=0.7)
    sns.kdeplot(event_2_data['skill_last'], fill=True, color="#f59e0b", label="Event 2", ax=axes[0, 1], alpha=0.7)
    axes[0, 1].set_title('Distribution of Skill Last', fontweight='bold')
    axes[0, 1].legend()

    sns.kdeplot(event_1_data['items_crafted'], fill=True, color="#3b82f6", label="Event 1", ax=axes[1, 0], alpha=0.7)
    sns.kdeplot(event_2_data['items_crafted'], fill=True, color="#f59e0b", label="Event 2", ax=axes[1, 0], alpha=0.7)
    axes[1, 0].set_title('Distribution of Items Crafted', fontweight='bold')
    axes[1, 0].legend()

    sns.kdeplot(event_1_data['dollars_spent'], fill=True, color="#3b82f6", label="Event 1", ax=axes[1, 1], alpha=0.7)
    sns.kdeplot(event_2_data['dollars_spent'], fill=True, color="#f59e0b", label="Event 2", ax=axes[1, 1], alpha=0.7)
    axes[1, 1].set_title('Distribution of Dollars Spent', fontweight='bold')
    axes[1, 1].legend()

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', use_container_width=True)

    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <p class="metric-highlight" style="margin-bottom: 5px;">+21%</p>
            <p style="color: #ffffff; font-weight: 600; margin-bottom: 10px;">Player Engagement Increase</p>
            <p style="color: #94a3b8; font-size: 14px; margin: 0;">Through targeted promotions and tailored in-game events in high-value segments</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
            <p class="metric-highlight" style="margin-bottom: 5px;">-15%</p>
            <p style="color: #ffffff; font-weight: 600; margin-bottom: 10px;">Churn Rate Reduction</p>
            <p style="color: #94a3b8; font-size: 14px; margin: 0;">Strategic review and adjustment for underperforming segments improved player satisfaction</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== EXECUTIVE BUSINESS INSIGHTS ====================
elif page == "Executive Business Insights":
    st.markdown('<p class="section-header">Dashboard: Executive Business Insights</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Post-merger, the business faced challenges with unstructured data across systems, affecting the Finance department's performance measurement and IGM.
    </p>
    """, unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', use_container_width=True)
    
    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Gather business requirements for accurate performance measurement and develop dynamic reporting capabilities.
    </p>
    """, unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', use_container_width=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    <strong>Data Gathering and Cleaning:</strong> Used SQL queries and existing reports to extract data. Cleaned data with deduplication, normalization, and error correction.
    </p>
    <p class="body-text">
    <strong>Schema Development:</strong> Developed a dynamic schema for flexible reporting. Collaborated with management to identify key metrics and designed a user-friendly dashboard.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <p style="color: #f59e0b; font-weight: 600; font-size: 16px;">Informed Decision-Making</p>
            <p style="color: #94a3b8; font-size: 14px; margin: 0;">Enhanced management's strategic planning and operational efficiency</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
            <p style="color: #f59e0b; font-weight: 600; font-size: 16px;">Enhanced Reporting</p>
            <p style="color: #94a3b8; font-size: 14px; margin: 0;">Improved Finance's performance measurement and adaptability to business changes</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== WAREHOUSE OPTIMIZATION ====================
elif page == "Warehouse Optimization":
    st.markdown('<p class="section-header">Data Analysis: Warehouse & GL Account Optimization</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Our company faced challenges with escalating costs in logistics and warehouse operations, directly impacting the bottom line. A comprehensive analysis was initiated focusing on the 'SKYLAB' and '3PL Logistics' divisions, known for significant contribution to operations but also potential inefficiencies.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Conduct a detailed examination of logistics and warehouse operations to uncover cost-saving opportunities. Identify areas of waste, inefficiencies, and potential for process optimizations.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    • <strong>Financial Data Analysis:</strong> Leveraged Python for in-depth analysis of financial records, focusing on expenditure patterns<br>
    • <strong>Identification of Inefficiencies:</strong> Pinpointed specific areas within 'SKYLAB' and '3PL Logistics' where inefficiencies were prevalent<br>
    • <strong>Optimization Opportunities:</strong> Developed strategies for cost optimization including adjustments in operations, resource allocation, and contract renegotiations
    </p>
    """, unsafe_allow_html=True)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', use_container_width=True)

    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
        <p class="body-text" style="margin-bottom: 15px;">
        <strong>Cost-saving Opportunities Uncovered:</strong> Deep dive into financial data revealed multiple inefficiencies that, when addressed, significantly reduced costs.
        </p>
        <p class="body-text" style="margin-bottom: 15px;">
        <strong>Strategic Improvements Implemented:</strong> Recommendations led to streamlined operations with positive bottom-line impact.
        </p>
        <p class="body-text" style="margin: 0;">
        <strong>Foundation for Continuous Improvement:</strong> Established framework for ongoing analysis and optimization serving as cornerstone for future enhancements.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== PROCESS AUTOMATION ====================
elif page == "Process Automation":
    st.markdown('<p class="section-header">Process Automation: Quarterly Royalty Management</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Years of data were unorganized, with the quarterly royalty management process involving extensive manual lookup in Excel. This was a month-long task for financial analysts, significantly affecting operational efficiency and increasing risk of errors.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p style="color: #f59e0b; font-weight: 600; font-size: 16px; margin-bottom: 10px;">PYTHON</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', use_container_width=True)
    with col2:
        st.markdown('<p style="color: #f59e0b; font-weight: 600; font-size: 16px; margin-bottom: 10px;">VBA</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', use_container_width=True)

    st.markdown('<p class="subsection-header">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Streamline the quarterly royalty management process, reducing time from a month-long task to an automated process. Support operations with an efficient dashboard and improved operational efficiency.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    • <strong>Understanding Historical Data:</strong> Gained hands-on understanding of historical data and royalty reporting<br>
    • <strong>Strategic Planning:</strong> Provided plan and roadmap for resource approval, collaborated with field managers<br>
    • <strong>Process Automation:</strong> Developed custom Python script for data consolidation and Excel VBA for automating data extraction and report generation
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection-header">Results</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight">85%</p>
            <p style="color: #ffffff; font-weight: 600; margin: 5px 0;">Time Reduction</p>
            <p style="color: #94a3b8; font-size: 13px; margin: 0;">From 1 month to 8 hours</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight" style="color: #3b82f6;">2</p>
            <p style="color: #ffffff; font-weight: 600; margin: 5px 0;">Analysts Freed</p>
            <p style="color: #94a3b8; font-size: 13px; margin: 0;">Senior financial analysts</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <p class="metric-highlight" style="color: #f59e0b;">↑</p>
            <p style="color: #ffffff; font-weight: 600; margin: 5px 0;">Accuracy</p>
            <p style="color: #94a3b8; font-size: 13px; margin: 0;">Improved reliability</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== SKILLS ====================
elif page == "Skills":
    st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=500)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Programming Languages</p>
            <p class="skills-list">Python, VBA, SQL</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Data Engineering</p>
            <p class="skills-list">ETL, SSMS, AS400, Snowflake, Power Query, System Integration Analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Data Analysis Libraries</p>
            <p class="skills-list">Pandas, NumPy, Seaborn, Matplotlib, Openpyxl, SciPy, TensorFlow</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Data Modeling</p>
            <p class="skills-list">STAR/ER/DAG diagrams, Normalization</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Statistical Analysis</p>
            <p class="skills-list">Descriptive/Inferential Statistics, A/B Testing, Predictive Modeling, Forecasting, Regression Analysis, Hypothesis Testing, Time Series Analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">BI Tools</p>
            <p class="skills-list">Power BI, Google Analytics, Looker Studio</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p class="skills-category">Digital Marketing</p>
            <p class="skills-list">Facebook Ads, Google Ads, Shopify, Campaign Management, Performance Optimization</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== CERTIFICATIONS ====================
elif page == "Certifications":
    st.markdown('<p class="section-header">Certifications</p>', unsafe_allow_html=True)
    
    certs = [
        {
            "title": "Supervised Machine Learning: Regression and Classification",
            "org": "Stanford University / Coursera • 2024",
            "image": "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/STANDFORD.PNG",
            "link": "https://www.coursera.org/account/accomplishments/verify/YHLXRW3TL569"
        },
        {
            "title": "Neural Networks and Deep Learning",
            "org": "DeepLearning.AI / Coursera • 2024",
            "image": "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/DeepAI",
            "link": "https://www.coursera.org/account/accomplishments/verify/P3MNNDS44DLL"
        },
        {
            "title": "Analyzing and Visualizing Data with Power BI",
            "org": "EdX • 2019",
            "image": "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/edx",
            "link": "https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79"
        },
        {
            "title": "AWS Cloud Practitioner Essentials",
            "org": "Amazon Web Services • 2019",
            "image": "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/AWS1",
            "link": None
        },
        {
            "title": "SQL Certification",
            "org": "Sololearn • 2017",
            "image": "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/SQLsololearn",
            "link": "https://www.sololearn.com/en/certificates/CT-YUFRJBUH"
        }
    ]
    
    for cert in certs:
        st.markdown(f"""
        <div class="cert-card">
            <p class="cert-title">{cert['title']}</p>
            <p class="cert-org">{cert['org']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.image(cert['image'], width=700)
        if cert['link']:
            st.markdown(f"<a href='{cert['link']}' target='_blank'>View Certificate →</a>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ==================== CONTACT ====================
elif page == "Contact":
    st.markdown('<p class="section-header">Let\'s Connect</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="quote-text">
    "In God we trust; for all else, we turn to the validation of data. With data science as our compass, we're set to reveal hidden insights that our data is just dying to tell."
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <p style="color: #64748b; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Phone</p>
            <p style="color: #ffffff; font-size: 18px; margin: 0;">(626) 203 – 3319</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p style="color: #64748b; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Email</p>
            <p style="color: #ffffff; font-size: 18px; margin: 0;">jason.chang01022021@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <p style="color: #64748b; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">LinkedIn</p>
            <p style="color: #ffffff; font-size: 18px; margin: 0;"><a href="https://linkedin.com/in/jchang0102" target="_blank">linkedin.com/in/jchang0102</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <p style="color: #64748b; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">Location</p>
            <p style="color: #ffffff; font-size: 18px; margin: 0;">Irvine, CA</p>
        </div>
        """, unsafe_allow_html=True)
