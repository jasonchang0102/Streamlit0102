import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Jason Chang | Portfolio", page_icon="◆")

# TRUE Nike-Inspired CSS - WHITE background, BLACK type, GIANT hero
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&display=swap' rel='stylesheet'>
<style>
    /* === NIKE BASE - WHITE BG === */
    html, body, [data-testid="stAppViewContainer"], section.main {
        scroll-behavior: auto !important;
    }
    
    .stApp {
        background: #ffffff;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .block-container {
        padding: 3rem 6rem !important;
        max-width: 1200px;
    }
    
    /* === HERO NAME - NIKE GIANT BOLD === */
    .hero-name {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 140px;
        font-weight: 400;
        color: #111111;
        letter-spacing: 4px;
        text-transform: uppercase;
        line-height: 0.9;
        margin-bottom: 0;
    }
    
    /* === PORTFOLIO SUBTITLE === */
    .hero-sub {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 500;
        color: #757575;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: 20px;
        margin-bottom: 60px;
    }
    
    /* === TAGLINE - NIKE STYLE === */
    .tagline {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 32px;
        color: #111111;
        letter-spacing: 1px;
        margin-bottom: 30px;
    }
    
    /* === BODY TEXT === */
    .body-text {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        font-weight: 400;
        color: #111111;
        line-height: 1.8;
        margin-bottom: 20px;
        max-width: 650px;
    }
    
    .body-text strong {
        font-weight: 700;
    }
    
    /* === SECTION HEADER - GIANT === */
    .section-header {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 72px;
        color: #111111;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 50px;
        line-height: 0.95;
    }
    
    /* === SUBSECTION === */
    .subsection {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 600;
        color: #757575;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 60px;
        margin-bottom: 20px;
    }
    
    /* === METRIC CARDS - NIKE MINIMAL === */
    .metric-card {
        background: #f5f5f5;
        border: none;
        padding: 50px 30px;
        text-align: center;
        border-radius: 0;
    }
    
    .metric-number {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 72px;
        color: #111111;
        line-height: 1;
    }
    
    .metric-label {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 500;
        color: #757575;
        margin-top: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* === RESULT CARDS === */
    .result-card {
        background: #f5f5f5;
        padding: 40px;
        margin: 15px 0;
    }
    
    .result-number {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 56px;
        color: #111111;
    }
    
    .result-title {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 600;
        color: #111111;
        margin: 15px 0 10px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .result-desc {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #757575;
        line-height: 1.5;
    }
    
    /* === BULLET POINTS === */
    .bullet {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #111111;
        line-height: 1.8;
        margin-bottom: 14px;
        padding-left: 0;
    }
    
    .bullet strong {
        font-weight: 600;
    }
    
    /* === INFO CARDS === */
    .info-card {
        background: #f5f5f5;
        padding: 30px;
        margin: 15px 0;
    }
    
    /* === SIDEBAR - NIKE CLEAN === */
    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e5e5e5;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label {
        background: transparent !important;
        color: #757575 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        padding: 14px 20px !important;
        letter-spacing: 0.5px !important;
        transition: all 0.2s ease !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label:hover {
        color: #111111 !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] {
        color: #111111 !important;
        font-weight: 600 !important;
    }
    
    .nav-title {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 600;
        color: #111111;
        letter-spacing: 2px;
        margin-bottom: 25px;
        padding-bottom: 15px;
        border-bottom: 2px solid #111111;
        text-transform: uppercase;
    }
    
    /* === SKILLS === */
    .skill-category {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 700;
        color: #111111;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    
    .skill-list {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #757575;
        line-height: 1.6;
    }
    
    /* === CERTIFICATIONS === */
    .cert-card {
        background: #f5f5f5;
        padding: 25px 30px;
        margin: 20px 0;
    }
    
    .cert-title {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        font-weight: 700;
        color: #111111;
        margin-bottom: 5px;
    }
    
    .cert-org {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #757575;
    }
    
    /* === CONTACT === */
    .contact-card {
        background: #f5f5f5;
        padding: 25px 30px;
        margin: 12px 0;
    }
    
    .contact-label {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 600;
        color: #757575;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    
    .contact-value {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        font-weight: 500;
        color: #111111;
    }
    
    /* === QUOTE === */
    .quote {
        font-family: 'Inter', sans-serif;
        font-size: 20px;
        font-weight: 400;
        color: #111111;
        font-style: italic;
        line-height: 1.7;
        border-left: 3px solid #111111;
        padding-left: 30px;
        margin: 50px 0;
        max-width: 550px;
    }
    
    /* === CODE LABEL === */
    .code-label {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 600;
        color: #757575;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }
    
    /* === CTA BUTTON - NIKE STYLE === */
    .cta-btn {
        display: inline-block;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 600;
        color: #ffffff;
        background: #111111;
        padding: 15px 30px;
        text-decoration: none;
        letter-spacing: 1px;
        transition: background 0.2s ease;
    }
    
    .cta-btn:hover {
        background: #757575;
    }
    
    /* === LINKS === */
    a {
        color: #111111 !important;
        text-decoration: underline !important;
    }
    
    a:hover {
        color: #757575 !important;
    }
    
    /* === OVERRIDES === */
    h1, h2, h3 {
        font-family: 'Bebas Neue', sans-serif !important;
        color: #111111 !important;
    }
    
    p, li {
        font-family: 'Inter', sans-serif !important;
        color: #111111 !important;
    }
    
    /* === DIVIDER === */
    .divider {
        width: 100%;
        height: 1px;
        background: #e5e5e5;
        margin: 60px 0;
    }
</style>

<script>
    window.parent.document.querySelector('[data-testid="stAppViewContainer"]').scrollTo(0, 0);
</script>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<p class="nav-title">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", [
        "Home",
        "Engagement",
        "Executive",
        "Warehouse",
        "Automation",
        "Skills",
        "Certifications",
        "Contact"
    ], label_visibility="collapsed")

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

# ===================== HOME =====================
if page == "Home":
    st.markdown('<p class="hero-name">JASON<br>CHANG</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">Data Analytics Portfolio</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="tagline">Revenue Growth Leader Powered by Analytics</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="body-text">
    Data-driven leader with <strong>10+ years</strong> scaling national programs through market strategy, analytics, and channel expansion. I translate complex data into actionable insights that drive measurable revenue growth.
    </p>
    <p class="body-text">
    Proficient in <strong>Snowflake, SQL, Power BI, and Python</strong>. Experienced leading cross-functional programs and automating reporting pipelines.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
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
elif page == "Engagement":
    st.markdown('<p class="section-header">PLAYER<br>ENGAGEMENT &<br>MONETIZATION</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">Situation</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="body-text">
    Tasked with maximizing revenue and player engagement for Warcraft during two key in-game events. Challenge: understanding player segment behavior and identifying monetization opportunities.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection">Task</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet">• Identify high-spending player segments for targeted promotions</p>
    <p class="bullet">• Analyze low spending trends by region and platform</p>
    <p class="bullet">• Conduct exploratory analysis on spending behaviors</p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet">• <strong>EDA & Clustering</strong> — Python-based analysis with K-Means segmentation</p>
    <p class="bullet">• <strong>Heatmap Analysis</strong> — Identified spending patterns across segments</p>
    <p class="bullet">• <strong>Strategic Output</strong> — Prioritized Platform 3, Region 1 for promotions</p>
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

    # Heatmap - White theme
    heatmap_data = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    fig1.patch.set_facecolor('#ffffff')
    ax1.set_facecolor('#ffffff')
    sns.heatmap(heatmap_data, annot=True, cmap="Greys", fmt=".2f", linewidths=1, ax=ax1,
                annot_kws={"color": "#111111", "fontsize": 10})
    ax1.set_title("Avg Spend by Region & Platform", color='#111111', fontsize=14, fontweight='600', pad=20)
    ax1.tick_params(colors='#111111')
    ax1.set_xlabel('Platform', color='#757575', fontsize=11)
    ax1.set_ylabel('Region', color='#757575', fontsize=11)
    for spine in ax1.spines.values():
        spine.set_color('#e5e5e5')
    st.pyplot(fig1)
    plt.close(fig1)

    # KDE - White theme
    e1 = data[(data['Date'] >= '2017-01-24') & (data['Date'] <= '2017-02-14')]
    e2 = data[(data['Date'] >= '2017-02-28') & (data['Date'] <= '2017-03-21')]
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    fig.patch.set_facecolor('#ffffff')
    for ax in axes.flat:
        ax.set_facecolor('#ffffff')
        ax.tick_params(colors='#111111', labelsize=9)
        ax.xaxis.label.set_color('#757575')
        ax.yaxis.label.set_color('#757575')
        ax.title.set_color('#111111')
        for spine in ax.spines.values():
            spine.set_color('#e5e5e5')
    
    for idx, (col, title) in enumerate([('games_played', 'Games Played'), ('skill_last', 'Skill Level'), ('items_crafted', 'Items Crafted'), ('dollars_spent', 'Dollars Spent')]):
        ax = axes[idx // 2, idx % 2]
        sns.kdeplot(e1[col], fill=True, color="#111111", label="Event 1", ax=ax, alpha=0.3)
        sns.kdeplot(e2[col], fill=True, color="#757575", label="Event 2", ax=ax, alpha=0.4)
        ax.set_title(title, fontsize=12, fontweight='600')
        ax.legend(fontsize=9, frameon=False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', use_container_width=True)

    st.markdown('<p class="subsection">Results</p>', unsafe_allow_html=True)
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
elif page == "Executive":
    st.markdown('<p class="section-header">EXECUTIVE<br>BUSINESS<br>INTELLIGENCE</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">Situation</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Post-merger environment with fragmented data across systems. Finance lacked unified performance measurement.</p>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', use_container_width=True)
    
    st.markdown('<p class="subsection">Task</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Design dynamic reporting solution with accurate KPIs for executive decision-making.</p>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', use_container_width=True)

    st.markdown('<p class="subsection">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet">• <strong>Data Engineering</strong> — SQL extraction, deduplication, normalization</p>
    <p class="bullet">• <strong>Schema Design</strong> — Flexible architecture for evolving needs</p>
    <p class="bullet">• <strong>Dashboard</strong> — Stakeholder collaboration on key metrics</p>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">Results</p>', unsafe_allow_html=True)
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
elif page == "Warehouse":
    st.markdown('<p class="section-header">WAREHOUSE<br>& GL<br>OPTIMIZATION</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">Situation</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Escalating logistics costs impacting bottom line. SKYLAB and 3PL Logistics identified as key areas for potential inefficiency.</p>', unsafe_allow_html=True)

    st.markdown('<p class="subsection">Task</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Conduct detailed cost analysis to identify waste and optimization opportunities.</p>', unsafe_allow_html=True)

    st.markdown('<p class="subsection">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet">• <strong>Financial Analysis</strong> — Python deep dive into expenditure patterns</p>
    <p class="bullet">• <strong>Inefficiency Mapping</strong> — Pinpointed cost drivers in both divisions</p>
    <p class="bullet">• <strong>Strategy</strong> — Recommendations for operations and vendor contracts</p>
    """, unsafe_allow_html=True)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', use_container_width=True)

    st.markdown('<p class="subsection">Results</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
        <p class="bullet">• <strong>Cost Reduction</strong> — Identified inefficiencies leading to significant savings</p>
        <p class="bullet">• <strong>Streamlined Ops</strong> — Process improvements with positive P&L impact</p>
        <p class="bullet">• <strong>Framework</strong> — Established ongoing optimization process</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== AUTOMATION =====================
elif page == "Automation":
    st.markdown('<p class="section-header">QUARTERLY<br>ROYALTY<br>AUTOMATION</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection">Situation</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Month-long manual Excel lookups across years of unorganized data. High error risk, significant analyst burden.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="code-label">Python Automation</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', use_container_width=True)
    with col2:
        st.markdown('<p class="code-label">VBA Integration</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', use_container_width=True)

    st.markdown('<p class="subsection">Task</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Transform month-long manual process into automated workflow while maintaining accuracy.</p>', unsafe_allow_html=True)

    st.markdown('<p class="subsection">Action</p>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet">• <strong>Data Audit</strong> — Mapped historical structures and requirements</p>
    <p class="bullet">• <strong>Python Pipeline</strong> — Automated consolidation and validation</p>
    <p class="bullet">• <strong>VBA</strong> — Automated Excel report generation</p>
    """, unsafe_allow_html=True)

    st.markdown('<p class="subsection">Results</p>', unsafe_allow_html=True)
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
            <p class="metric-number">2</p>
            <p class="metric-label">FTEs Freed</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-number">↑</p>
            <p class="metric-label">Accuracy</p>
        </div>
        """, unsafe_allow_html=True)

# ===================== SKILLS =====================
elif page == "Skills":
    st.markdown('<p class="section-header">TECHNICAL<br>EXPERTISE</p>', unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=280)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
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
            <p class="skill-list">Pandas, NumPy, Seaborn, Matplotlib, SciPy</p>
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
    st.markdown('<p class="section-header">CERTIFICATIONS</p>', unsafe_allow_html=True)
    
    certs = [
        ("Supervised Machine Learning", "Stanford / Coursera · 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/STANDFORD.PNG", "https://www.coursera.org/account/accomplishments/verify/YHLXRW3TL569"),
        ("Neural Networks & Deep Learning", "DeepLearning.AI · 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/DeepAI", "https://www.coursera.org/account/accomplishments/verify/P3MNNDS44DLL"),
        ("Power BI Data Visualization", "EdX · 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/edx", "https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79"),
        ("AWS Cloud Practitioner", "Amazon Web Services · 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/AWS1", None),
        ("SQL Certification", "Sololearn · 2017", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/SQLsololearn", "https://www.sololearn.com/en/certificates/CT-YUFRJBUH")
    ]
    
    for title, org, img, link in certs:
        st.markdown(f'<div class="cert-card"><p class="cert-title">{title}</p><p class="cert-org">{org}</p></div>', unsafe_allow_html=True)
        st.image(img, width=480)
        if link:
            st.markdown(f"<a href='{link}' target='_blank'>Verify Certificate</a>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ===================== CONTACT =====================
elif page == "Contact":
    st.markdown('<p class="section-header">LET\'S<br>CONNECT</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="quote">"In God we trust; for all else, we turn to the validation of data."</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
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
