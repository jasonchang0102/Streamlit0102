import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Jason Chang | Portfolio", page_icon="◆")

# Premium Designer CSS
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap' rel='stylesheet'>
<style>
    /* === BASE === */
    html, body, [data-testid="stAppViewContainer"], section.main {
        scroll-behavior: auto !important;
    }
    
    .stApp {
        background: #0a0a0f;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .block-container {
        padding: 4rem 6rem !important;
        max-width: 1000px;
    }
    
    /* === HERO NAME - LARGE & BOLD === */
    .hero-name {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 120px !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #ffffff 0%, #a8b4c4 50%, #ffffff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -3px;
        line-height: 1;
        margin-bottom: 8px;
        margin-top: 0;
    }
    
    /* === PORTFOLIO SUBTITLE === */
    .hero-subtitle {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 16px;
        font-weight: 500;
        color: #4a5568;
        letter-spacing: 12px;
        text-transform: uppercase;
        margin-bottom: 40px;
    }
    
    /* === ACCENT LINE WITH GLOW === */
    .accent-bar {
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #f59e0b, #fbbf24, #f59e0b);
        border-radius: 2px;
        margin: 30px 0;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.4);
    }
    
    /* === TAGLINE === */
    .hero-tagline {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 24px;
        font-weight: 600;
        color: #f59e0b;
        margin-bottom: 30px;
        letter-spacing: -0.5px;
    }
    
    /* === BODY TEXT === */
    .body-text {
        font-family: 'Inter', sans-serif;
        font-size: 17px;
        font-weight: 400;
        color: #d1d5db;
        line-height: 1.8;
        margin-bottom: 20px;
    }
    
    .body-text strong {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* === SECTION HEADER === */
    .section-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 42px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 40px;
        letter-spacing: -1px;
    }
    
    /* === SUBSECTION === */
    .subsection {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 13px;
        font-weight: 600;
        color: #f59e0b;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 40px;
        margin-bottom: 16px;
    }
    
    /* === PREMIUM CARDS === */
    .metric-card {
        background: linear-gradient(145deg, #12121a 0%, #0d0d12 100%);
        border: 1px solid #1f1f2e;
        border-radius: 16px;
        padding: 32px 24px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: #f59e0b;
        transform: translateY(-4px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .metric-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 48px;
        font-weight: 700;
        background: linear-gradient(135deg, #22c55e, #4ade80);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
    }
    
    .metric-label {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #9ca3af;
        margin-top: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* === INFO CARDS === */
    .info-card {
        background: #12121a;
        border: 1px solid #1f1f2e;
        border-radius: 12px;
        padding: 24px;
        margin: 16px 0;
        transition: border-color 0.3s ease;
    }
    
    .info-card:hover {
        border-color: #374151;
    }
    
    /* === RESULT CARDS === */
    .result-card {
        background: linear-gradient(145deg, #12121a 0%, #0d0d12 100%);
        border: 1px solid #1f1f2e;
        border-radius: 16px;
        padding: 28px;
        margin: 12px 0;
    }
    
    .result-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 40px;
        font-weight: 700;
        background: linear-gradient(135deg, #22c55e, #4ade80);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .result-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 16px;
        font-weight: 600;
        color: #ffffff;
        margin: 8px 0;
    }
    
    .result-desc {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #9ca3af;
    }
    
    /* === BULLET POINTS === */
    .bullet {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        color: #d1d5db;
        line-height: 1.7;
        margin-bottom: 12px;
        padding-left: 24px;
        position: relative;
    }
    
    .bullet::before {
        content: "▸";
        position: absolute;
        left: 0;
        color: #f59e0b;
        font-size: 14px;
    }
    
    .bullet strong {
        color: #ffffff;
    }
    
    /* === SIDEBAR === */
    section[data-testid="stSidebar"] {
        background: #0a0a0f;
        border-right: 1px solid #1a1a24;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label {
        background: transparent !important;
        color: #4b5563 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        padding: 14px 16px !important;
        border-radius: 8px !important;
        border-left: 3px solid transparent !important;
        transition: all 0.2s ease !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label:hover {
        color: #e5e7eb !important;
        background: rgba(255,255,255,0.03) !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] {
        color: #f59e0b !important;
        border-left-color: #f59e0b !important;
        background: rgba(245, 158, 11, 0.08) !important;
    }
    
    .nav-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 11px;
        font-weight: 600;
        color: #374151;
        letter-spacing: 3px;
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 1px solid #1a1a24;
    }
    
    /* === SKILLS === */
    .skill-category {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 14px;
        font-weight: 600;
        color: #f59e0b;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }
    
    .skill-list {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #d1d5db;
        line-height: 1.6;
    }
    
    /* === CERTIFICATIONS === */
    .cert-card {
        background: #12121a;
        border: 1px solid #1f1f2e;
        border-radius: 12px;
        padding: 20px 24px;
        margin: 16px 0;
        transition: all 0.2s ease;
    }
    
    .cert-card:hover {
        border-color: #f59e0b;
    }
    
    .cert-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 4px;
    }
    
    .cert-org {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #9ca3af;
    }
    
    /* === CONTACT === */
    .contact-card {
        background: #12121a;
        border: 1px solid #1f1f2e;
        border-radius: 12px;
        padding: 20px 24px;
        margin: 12px 0;
    }
    
    .contact-label {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 500;
        color: #9ca3af;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    
    .contact-value {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px;
        font-weight: 500;
        color: #ffffff;
    }
    
    /* === QUOTE === */
    .quote {
        font-family: 'Inter', sans-serif;
        font-size: 22px;
        font-weight: 400;
        color: #d1d5db;
        font-style: italic;
        line-height: 1.6;
        border-left: 3px solid #f59e0b;
        padding-left: 24px;
        margin: 40px 0;
    }
    
    /* === LINKS === */
    a {
        color: #60a5fa !important;
        text-decoration: none !important;
        transition: color 0.2s ease !important;
    }
    
    a:hover {
        color: #f59e0b !important;
    }
    
    /* === STREAMLIT OVERRIDES === */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #ffffff !important;
    }
    
    p, li {
        font-family: 'Inter', sans-serif !important;
        color: #d1d5db !important;
    }
    
    /* === CODE LABELS === */
    .code-label {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 12px;
        font-weight: 600;
        color: #f59e0b;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }
</style>

<script>
    // Scroll to top on page load
    var mainSection = window.parent.document.querySelector('section.main');
    if (mainSection) {
        mainSection.scrollTop = 0;
    }
    window.parent.document.documentElement.scrollTop = 0;
    window.parent.document.body.scrollTop = 0;
</script>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<p class="nav-title">NAVIGATION</p>', unsafe_allow_html=True)
    page = st.radio("", [
        "Welcome",
        "Engagement & Monetization",
        "Executive Insights",
        "Warehouse Optimization",
        "Process Automation",
        "Skills",
        "Certifications",
        "Contact"
    ], label_visibility="collapsed")

# Scroll to top on page change
st.markdown(f'''
    <div id="top-anchor"></div>
    <script>
        window.parent.document.querySelector('[data-testid="stAppViewContainer"]').scrollTo(0, 0);
        window.scrollTo(0, 0);
    </script>
''', unsafe_allow_html=True)

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    def bucket(g):
        if 1 <= g <= 3: return 'Very Low'
        elif 4 <= g <= 5: return 'Low'
        elif 6 <= g <= 9: return 'Medium'
        elif 10 <= g <= 68: return 'High'
        return 'Unknown'
    data['games_played_bucket'] = data['games_played'].apply(bucket)
    return data

data = load_data("https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv")

# ===================== WELCOME =====================
if page == "Welcome":
    st.markdown('<p class="hero-name">JASON CHANG</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">PORTFOLIO</p>', unsafe_allow_html=True)
    st.markdown('<div class="accent-bar"></div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-tagline">National Revenue Growth Leader<br>Powered by Analytics</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="body-text">
    Data-driven leader with <strong>10+ years</strong> scaling national programs through market strategy, analytics, and channel expansion. I translate complex data into actionable insights that accelerate decisions, improve conversion, and drive measurable revenue growth.
    </p>
    <p class="body-text">
    Proficient in <strong>Snowflake, SQL, Power BI, and Python</strong>. Experienced leading cross-functional programs, unifying fragmented data systems, and automating reporting pipelines.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="accent-bar"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-number">10+</p>
            <p class="metric-label">Years Experience</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-number">85%</p>
            <p class="metric-label">Efficiency Gains</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-number">21%</p>
            <p class="metric-label">Revenue Growth</p>
        </div>
        """, unsafe_allow_html=True)

# ===================== ENGAGEMENT =====================
elif page == "Engagement & Monetization":
    st.markdown('<p class="section-header">Player Engagement &<br>Monetization Analytics</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">SITUATION</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Tasked with maximizing revenue and player engagement for Warcraft during two key in-game events. Challenge: understanding player segment behavior and identifying monetization opportunities.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection">TASK</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet">Identify high-spending player segments for targeted promotions</p>
    <p class="bullet">Analyze low spending trends by region and platform</p>
    <p class="bullet">Conduct exploratory analysis on spending behaviors</p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection">ACTION</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>EDA & Clustering:</strong> Python-based analysis with K-Means segmentation</p>
    <p class="bullet"><strong>Heatmap Analysis:</strong> Identified spending patterns across segments</p>
    <p class="bullet"><strong>Strategic Output:</strong> Prioritized Platform 3, Region 1 for promotions</p>
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
    fig1.patch.set_facecolor('#0a0a0f')
    ax1.set_facecolor('#0a0a0f')
    sns.heatmap(heatmap_data, annot=True, cmap="YlOrBr", fmt=".2f", linewidths=.5, ax=ax1)
    ax1.set_title("Avg Spend by Region & Platform", color='white', fontsize=12, fontweight='600')
    ax1.tick_params(colors='white')
    ax1.set_xlabel('Platform', color='#6b7280')
    ax1.set_ylabel('Region', color='#6b7280')
    st.pyplot(fig1)
    plt.close(fig1)

    # KDE
    e1 = data[(data['Date'] >= '2017-01-24') & (data['Date'] <= '2017-02-14')]
    e2 = data[(data['Date'] >= '2017-02-28') & (data['Date'] <= '2017-03-21')]
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    fig.patch.set_facecolor('#0a0a0f')
    for ax in axes.flat:
        ax.set_facecolor('#0a0a0f')
        ax.tick_params(colors='white', labelsize=8)
        ax.xaxis.label.set_color('#6b7280')
        ax.yaxis.label.set_color('#6b7280')
        ax.title.set_color('white')
    
    for idx, (col, title) in enumerate([('games_played', 'Games Played'), ('skill_last', 'Skill Level'), ('items_crafted', 'Items Crafted'), ('dollars_spent', 'Dollars Spent')]):
        ax = axes[idx // 2, idx % 2]
        sns.kdeplot(e1[col], fill=True, color="#3b82f6", label="Event 1", ax=ax, alpha=0.6)
        sns.kdeplot(e2[col], fill=True, color="#f59e0b", label="Event 2", ax=ax, alpha=0.6)
        ax.set_title(title, fontsize=11, fontweight='600')
        ax.legend(fontsize=8)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', use_container_width=True)

    st.markdown('<p class="subsection">RESULTS</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="result-card">
            <p class="result-number">+21%</p>
            <p class="result-title">Engagement Increase</p>
            <p class="result-desc">Targeted promotions in high-value segments</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="result-card">
            <p class="result-number">-15%</p>
            <p class="result-title">Churn Reduction</p>
            <p class="result-desc">Strategic adjustments improved retention</p>
        </div>
        """, unsafe_allow_html=True)

# ===================== EXECUTIVE =====================
elif page == "Executive Insights":
    st.markdown('<p class="section-header">Executive Business<br>Intelligence Dashboard</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">SITUATION</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Post-merger environment with fragmented data across systems. Finance lacked unified performance measurement.</p>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', use_container_width=True)
    
    st.markdown('<p class="subsection">TASK</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Design dynamic reporting solution with accurate KPIs for executive decision-making.</p>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', use_container_width=True)

    st.markdown('<p class="subsection">ACTION</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>Data Engineering:</strong> SQL extraction, deduplication, normalization</p>
    <p class="bullet"><strong>Schema Design:</strong> Flexible architecture for evolving needs</p>
    <p class="bullet"><strong>Dashboard:</strong> Stakeholder collaboration on key metrics</p>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">RESULTS</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <p class="skill-category">Strategic Planning</p>
            <p class="skill-list">Enhanced management decision-making with real-time insights</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
            <p class="skill-category">Adaptive Reporting</p>
            <p class="skill-list">Scalable system that evolves with business changes</p>
        </div>
        """, unsafe_allow_html=True)

# ===================== WAREHOUSE =====================
elif page == "Warehouse Optimization":
    st.markdown('<p class="section-header">Warehouse & GL<br>Account Optimization</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">SITUATION</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Escalating logistics costs impacting bottom line. SKYLAB and 3PL Logistics identified as key areas for potential inefficiency.</p>', unsafe_allow_html=True)

    st.markdown('<p class="subsection">TASK</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Conduct detailed cost analysis to identify waste and optimization opportunities.</p>', unsafe_allow_html=True)

    st.markdown('<p class="subsection">ACTION</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>Financial Analysis:</strong> Python deep dive into expenditure patterns</p>
    <p class="bullet"><strong>Inefficiency Mapping:</strong> Pinpointed cost drivers in both divisions</p>
    <p class="bullet"><strong>Strategy:</strong> Recommendations for operations and vendor contracts</p>
    """, unsafe_allow_html=True)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', use_container_width=True)

    st.markdown('<p class="subsection">RESULTS</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
        <p class="bullet"><strong>Cost Reduction:</strong> Identified inefficiencies leading to significant savings</p>
        <p class="bullet"><strong>Streamlined Ops:</strong> Process improvements with positive P&L impact</p>
        <p class="bullet"><strong>Framework:</strong> Established ongoing optimization process</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== AUTOMATION =====================
elif page == "Process Automation":
    st.markdown('<p class="section-header">Quarterly Royalty<br>Management Automation</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">SITUATION</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Month-long manual Excel lookups across years of unorganized data. High error risk, significant analyst burden.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="code-label">PYTHON AUTOMATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', use_container_width=True)
    with col2:
        st.markdown('<p class="code-label">VBA INTEGRATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', use_container_width=True)

    st.markdown('<p class="subsection">TASK</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Transform month-long manual process into automated workflow while maintaining accuracy.</p>', unsafe_allow_html=True)

    st.markdown('<p class="subsection">ACTION</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>Data Audit:</strong> Mapped historical structures and requirements</p>
    <p class="bullet"><strong>Python Pipeline:</strong> Automated consolidation and validation</p>
    <p class="bullet"><strong>VBA:</strong> Automated Excel report generation</p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection">RESULTS</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-number">85%</p>
            <p class="metric-label">Time Saved</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-number" style="background: linear-gradient(135deg, #3b82f6, #60a5fa); -webkit-background-clip: text;">2</p>
            <p class="metric-label">FTEs Freed</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-number" style="background: linear-gradient(135deg, #f59e0b, #fbbf24); -webkit-background-clip: text;">↑</p>
            <p class="metric-label">Accuracy</p>
        </div>
        """, unsafe_allow_html=True)

# ===================== SKILLS =====================
elif page == "Skills":
    st.markdown('<p class="section-header">Technical Expertise</p>', unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=350)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <p class="skill-category">Languages</p>
            <p class="skill-list">Python, SQL, VBA</p>
        </div>
        <div class="info-card">
            <p class="skill-category">Data Engineering</p>
            <p class="skill-list">Snowflake, ETL, SSMS, AS400, Power Query</p>
        </div>
        <div class="info-card">
            <p class="skill-category">Analytics</p>
            <p class="skill-list">Pandas, NumPy, Seaborn, Matplotlib, SciPy, TensorFlow</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
            <p class="skill-category">Statistics</p>
            <p class="skill-list">A/B Testing, Predictive Modeling, Regression, Time Series</p>
        </div>
        <div class="info-card">
            <p class="skill-category">BI & Visualization</p>
            <p class="skill-list">Power BI, Looker Studio, Google Analytics</p>
        </div>
        <div class="info-card">
            <p class="skill-category">Data Modeling</p>
            <p class="skill-list">Star Schema, ER Diagrams, DAG, Normalization</p>
        </div>
        """, unsafe_allow_html=True)

# ===================== CERTIFICATIONS =====================
elif page == "Certifications":
    st.markdown('<p class="section-header">Certifications</p>', unsafe_allow_html=True)
    
    certs = [
        ("Supervised Machine Learning", "Stanford / Coursera • 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/STANDFORD.PNG", "https://www.coursera.org/account/accomplishments/verify/YHLXRW3TL569"),
        ("Neural Networks & Deep Learning", "DeepLearning.AI • 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/DeepAI", "https://www.coursera.org/account/accomplishments/verify/P3MNNDS44DLL"),
        ("Power BI Data Visualization", "EdX • 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/edx", "https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79"),
        ("AWS Cloud Practitioner", "Amazon Web Services • 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/AWS1", None),
        ("SQL Certification", "Sololearn • 2017", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/SQLsololearn", "https://www.sololearn.com/en/certificates/CT-YUFRJBUH")
    ]
    
    for title, org, img, link in certs:
        st.markdown(f'<div class="cert-card"><p class="cert-title">{title}</p><p class="cert-org">{org}</p></div>', unsafe_allow_html=True)
        st.image(img, width=550)
        if link:
            st.markdown(f"<a href='{link}' target='_blank'>Verify →</a>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ===================== CONTACT =====================
elif page == "Contact":
    st.markdown('<p class="section-header">Let\'s Connect</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="quote">"In God we trust; for all else, we turn to the validation of data."</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="contact-card">
            <p class="contact-label">Phone</p>
            <p class="contact-value">(626) 203-3319</p>
        </div>
        <div class="contact-card">
            <p class="contact-label">Email</p>
            <p class="contact-value">jason.chang01022021@gmail.com</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="contact-card">
            <p class="contact-label">LinkedIn</p>
            <p class="contact-value"><a href="https://linkedin.com/in/jchang0102">linkedin.com/in/jchang0102</a></p>
        </div>
        <div class="contact-card">
            <p class="contact-label">Location</p>
            <p class="contact-value">Irvine, CA</p>
        </div>
        """, unsafe_allow_html=True)
