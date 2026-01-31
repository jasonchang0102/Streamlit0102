import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Jason Chang | Portfolio", page_icon="◆")

# AWARD-WINNING LEVEL CSS
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700;800&display=swap' rel='stylesheet'>
<style>
    /* === ROOT VARIABLES === */
    :root {
        --black: #0a0a0a;
        --white: #ffffff;
        --grey: #888888;
        --grey-light: #f5f5f5;
        --grey-dark: #1a1a1a;
        --accent: #ff4d4d;
    }
    
    /* === BASE === */
    .stApp {
        background: var(--white) !important;
        overflow-x: hidden !important;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .block-container {
        padding: 2rem 4rem 6rem 4rem !important;
        max-width: 1300px !important;
    }
    
    /* === NOISE TEXTURE OVERLAY === */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
        opacity: 0.015;
        pointer-events: none;
        z-index: 1000;
    }
    
    /* === SCROLL PROGRESS BAR === */
    .scroll-progress {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: rgba(0,0,0,0.05);
        z-index: 9999;
    }
    
    .scroll-progress-bar {
        height: 100%;
        background: var(--black);
        width: 0%;
        transition: width 0.1s ease;
    }
    
    /* === ANIMATIONS === */
    @keyframes revealUp {
        0% {
            opacity: 0;
            transform: translateY(100px) rotateX(-15deg);
        }
        100% {
            opacity: 1;
            transform: translateY(0) rotateX(0);
        }
    }
    
    @keyframes revealLeft {
        0% {
            opacity: 0;
            transform: translateX(-80px);
        }
        100% {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes fadeInScale {
        0% {
            opacity: 0;
            transform: scale(0.9);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes lineExpand {
        0% { transform: scaleX(0); }
        100% { transform: scaleX(1); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    
    @keyframes countUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* === HERO NAME - MASSIVE 120px === */
    .hero-name {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 140px !important;
        font-weight: 400 !important;
        color: var(--black) !important;
        letter-spacing: -2px !important;
        text-transform: uppercase !important;
        line-height: 0.85 !important;
        margin-bottom: 0 !important;
        animation: revealUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
        transform-origin: bottom !important;
    }
    
    /* === OUTLINE TEXT EFFECT === */
    .hero-name-outline {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 140px !important;
        font-weight: 400 !important;
        color: transparent !important;
        -webkit-text-stroke: 2px var(--black) !important;
        letter-spacing: -2px !important;
        text-transform: uppercase !important;
        line-height: 0.85 !important;
        margin-bottom: 0 !important;
        animation: revealUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.1s forwards !important;
        opacity: 0;
    }
    
    /* === SUBTITLE WITH LINE === */
    .hero-sub {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-top: 40px;
        margin-bottom: 80px;
        animation: revealLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.4s forwards;
        opacity: 0;
    }
    
    .hero-sub-line {
        width: 60px;
        height: 1px;
        background: var(--black);
    }
    
    .hero-sub-text {
        font-family: 'Inter', sans-serif !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        color: var(--grey) !important;
        letter-spacing: 4px !important;
        text-transform: uppercase !important;
    }
    
    /* === TAGLINE === */
    .tagline {
        font-family: 'Inter', sans-serif !important;
        font-size: 28px !important;
        font-weight: 300 !important;
        color: var(--black) !important;
        line-height: 1.5 !important;
        margin-bottom: 40px !important;
        max-width: 700px !important;
        animation: revealUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.5s forwards !important;
        opacity: 0 !important;
    }
    
    .tagline strong {
        font-weight: 700 !important;
        background: linear-gradient(90deg, var(--black) 0%, var(--grey) 50%, var(--black) 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s linear infinite;
    }
    
    /* === BODY TEXT === */
    .body-text {
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        font-weight: 400 !important;
        color: var(--grey) !important;
        line-height: 1.9 !important;
        margin-bottom: 20px !important;
        max-width: 600px !important;
    }
    
    .body-text strong {
        color: var(--black) !important;
        font-weight: 600 !important;
    }
    
    /* === SECTION HEADER - 120px === */
    .section-header {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 120px !important;
        color: var(--black) !important;
        letter-spacing: -2px !important;
        text-transform: uppercase !important;
        margin-bottom: 60px !important;
        line-height: 0.85 !important;
        animation: revealUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
    }
    
    /* === SUBSECTION WITH COUNTER === */
    .subsection {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-top: 70px;
        margin-bottom: 25px;
    }
    
    .subsection-num {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 14px;
        color: var(--grey);
        letter-spacing: 1px;
    }
    
    .subsection-text {
        font-family: 'Inter', sans-serif !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        color: var(--black) !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
    }
    
    .subsection-line {
        flex: 1;
        height: 1px;
        background: #e0e0e0;
        max-width: 200px;
    }
    
    /* === METRIC CARDS - GLASSMORPHISM === */
    .metric-card {
        background: rgba(245, 245, 245, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(0,0,0,0.05);
        padding: 60px 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, transparent 0%, rgba(0,0,0,0.02) 100%);
        transition: opacity 0.5s ease;
    }
    
    .metric-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 3px;
        background: var(--black);
        transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .metric-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 30px 60px rgba(0,0,0,0.1);
    }
    
    .metric-card:hover::after {
        width: 60px;
    }
    
    .metric-number {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 100px !important;
        color: var(--black) !important;
        line-height: 1 !important;
        position: relative;
        z-index: 1;
        animation: countUp 0.8s ease forwards;
    }
    
    .metric-label {
        font-family: 'Inter', sans-serif !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        color: var(--grey) !important;
        margin-top: 20px !important;
        text-transform: uppercase !important;
        letter-spacing: 3px !important;
        position: relative;
        z-index: 1;
    }
    
    /* === RESULT CARDS === */
    .result-card {
        background: var(--grey-light);
        padding: 50px;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .result-card::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 4px;
        background: var(--black);
        transform: scaleY(0);
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        transform-origin: bottom;
    }
    
    .result-card:hover {
        transform: translateX(15px);
        background: #ebebeb;
    }
    
    .result-card:hover::before {
        transform: scaleY(1);
    }
    
    .result-number {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 80px !important;
        color: var(--black) !important;
        line-height: 1 !important;
    }
    
    .result-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        color: var(--black) !important;
        margin: 20px 0 10px 0 !important;
        text-transform: uppercase !important;
        letter-spacing: 3px !important;
    }
    
    .result-desc {
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        color: var(--grey) !important;
        line-height: 1.6 !important;
    }
    
    /* === BULLET POINTS === */
    .bullet {
        font-family: 'Inter', sans-serif !important;
        font-size: 15px !important;
        color: var(--grey) !important;
        line-height: 2 !important;
        margin-bottom: 10px !important;
        padding-left: 25px !important;
        position: relative !important;
        transition: all 0.3s ease !important;
    }
    
    .bullet::before {
        content: '';
        position: absolute;
        left: 0;
        top: 12px;
        width: 8px;
        height: 1px;
        background: var(--black);
        transition: width 0.3s ease;
    }
    
    .bullet:hover {
        transform: translateX(10px);
        color: var(--black) !important;
    }
    
    .bullet:hover::before {
        width: 15px;
    }
    
    .bullet strong {
        color: var(--black) !important;
        font-weight: 600 !important;
    }
    
    /* === INFO CARDS === */
    .info-card {
        background: var(--grey-light);
        padding: 40px;
        margin: 15px 0;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
    }
    
    .info-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: var(--black);
        transform: scaleX(0);
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        transform-origin: left;
    }
    
    .info-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    }
    
    .info-card:hover::after {
        transform: scaleX(1);
    }
    
    /* === SIDEBAR === */
    section[data-testid="stSidebar"] {
        background: var(--white) !important;
        border-right: 1px solid #f0f0f0 !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label {
        background: transparent !important;
        color: var(--grey) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        padding: 18px 25px !important;
        letter-spacing: 0.5px !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
        border-left: 3px solid transparent !important;
        position: relative !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label:hover {
        color: var(--black) !important;
        padding-left: 35px !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] {
        color: var(--black) !important;
        font-weight: 700 !important;
        border-left-color: var(--black) !important;
        background: rgba(0,0,0,0.02) !important;
    }
    
    .nav-title {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 32px !important;
        color: var(--black) !important;
        letter-spacing: 2px !important;
        margin-bottom: 40px !important;
        padding-bottom: 20px !important;
        border-bottom: 2px solid var(--black) !important;
    }
    
    /* === SKILLS === */
    .skill-category {
        font-family: 'Inter', sans-serif !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        color: var(--black) !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        margin-bottom: 12px !important;
    }
    
    .skill-list {
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        color: var(--grey) !important;
        line-height: 1.8 !important;
    }
    
    /* === CERTIFICATIONS === */
    .cert-card {
        background: var(--grey-light);
        padding: 30px 40px;
        margin: 20px 0;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
    }
    
    .cert-card::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 0;
        background: var(--black);
        transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .cert-card:hover {
        padding-left: 60px;
    }
    
    .cert-card:hover::before {
        width: 4px;
    }
    
    .cert-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        color: var(--black) !important;
        margin-bottom: 5px !important;
        position: relative;
        z-index: 1;
    }
    
    .cert-org {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        color: var(--grey) !important;
        position: relative;
        z-index: 1;
    }
    
    /* === CONTACT CARDS === */
    .contact-card {
        background: var(--grey-light);
        padding: 35px 40px;
        margin: 15px 0;
        transition: all 0.4s ease;
        border-bottom: 3px solid transparent;
    }
    
    .contact-card:hover {
        background: #ebebeb;
        border-bottom-color: var(--black);
    }
    
    .contact-label {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 700 !important;
        color: var(--grey) !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        margin-bottom: 10px !important;
    }
    
    .contact-value {
        font-family: 'Inter', sans-serif !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        color: var(--black) !important;
    }
    
    /* === QUOTE === */
    .quote {
        font-family: 'Inter', sans-serif !important;
        font-size: 26px !important;
        font-weight: 300 !important;
        color: var(--black) !important;
        font-style: italic !important;
        line-height: 1.7 !important;
        padding-left: 40px !important;
        margin: 80px 0 !important;
        max-width: 600px !important;
        position: relative !important;
        animation: revealUp 0.8s ease forwards !important;
    }
    
    .quote::before {
        content: '"';
        position: absolute;
        left: 0;
        top: -20px;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 120px;
        color: #f0f0f0;
        line-height: 1;
    }
    
    /* === CODE LABEL === */
    .code-label {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 700 !important;
        color: var(--black) !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        margin-bottom: 15px !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
    }
    
    .code-label::after {
        content: '';
        flex: 1;
        height: 1px;
        background: #e0e0e0;
        max-width: 100px;
    }
    
    /* === DIVIDER === */
    .divider {
        width: 100%;
        height: 1px;
        background: linear-gradient(to right, var(--black) 0%, transparent 100%);
        margin: 80px 0;
        opacity: 0.1;
    }
    
    /* === LINKS === */
    a {
        color: var(--black) !important;
        text-decoration: none !important;
        position: relative !important;
        font-weight: 500 !important;
    }
    
    a::after {
        content: ' →';
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    a:hover::after {
        opacity: 1;
    }
    
    /* === IMAGE HOVER === */
    .stImage img {
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
        filter: grayscale(0%);
    }
    
    .stImage img:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 30px 60px rgba(0,0,0,0.15) !important;
    }
    
    /* === OVERRIDES === */
    h1, h2, h3 {
        font-family: 'Bebas Neue', sans-serif !important;
        color: var(--black) !important;
    }
    
    p, li {
        font-family: 'Inter', sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

# Scroll to top function
def scroll_to_top():
    scroll_js = """
    <script>
        const containers = [
            window.parent.document.querySelector('.main'),
            window.parent.document.querySelector('[data-testid="stAppViewContainer"]'),
            window.parent.document.querySelector('section.main'),
            window.parent.document.body,
            window.parent.document.documentElement
        ];
        
        containers.forEach(container => {
            if (container) {
                container.scrollTop = 0;
                container.scrollTo({ top: 0, behavior: 'instant' });
            }
        });
        
        const topEl = window.parent.document.querySelector('.block-container');
        if (topEl) {
            topEl.scrollIntoView({ behavior: 'instant', block: 'start' });
        }
    </script>
    """
    components.html(scroll_js, height=0, width=0)

# Sidebar
with st.sidebar:
    st.markdown('<p class="nav-title">MENU</p>', unsafe_allow_html=True)
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

scroll_to_top()

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
    st.markdown('<p class="hero-name">JASON</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-name-outline">CHANG</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-sub">
        <div class="hero-sub-line"></div>
        <span class="hero-sub-text">Data Analytics Portfolio</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="tagline"><strong>Revenue Growth Leader</strong> with 10+ years scaling national programs through analytics, strategy, and data-driven decision making.</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="body-text">
    I translate complex data into actionable insights that accelerate decisions and drive measurable growth. Proficient in <strong>Snowflake, SQL, Power BI, and Python</strong>.
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
    st.markdown('<p class="section-header">PLAYER<br>ENGAGEMENT<br>& MONETIZATION</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><span class="subsection-num">01</span><span class="subsection-text">Situation</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Tasked with maximizing revenue and player engagement for Warcraft during two key in-game events. Challenge: understanding player segment behavior and identifying monetization opportunities.</p>', unsafe_allow_html=True)

    st.markdown('<div class="subsection"><span class="subsection-num">02</span><span class="subsection-text">Task</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet">Identify high-spending player segments for targeted promotions</p>
    <p class="bullet">Analyze low spending trends by region and platform</p>
    <p class="bullet">Conduct exploratory analysis on spending behaviors</p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection"><span class="subsection-num">03</span><span class="subsection-text">Action</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>EDA & Clustering</strong> — Python-based analysis with K-Means segmentation</p>
    <p class="bullet"><strong>Heatmap Analysis</strong> — Identified spending patterns across segments</p>
    <p class="bullet"><strong>Strategic Output</strong> — Prioritized Platform 3, Region 1 for promotions</p>
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
    fig1.patch.set_facecolor('#ffffff')
    ax1.set_facecolor('#ffffff')
    sns.heatmap(heatmap_data, annot=True, cmap="Greys", fmt=".2f", linewidths=1, ax=ax1,
                annot_kws={"color": "#0a0a0a", "fontsize": 10, "fontweight": "bold"})
    ax1.set_title("Avg Spend by Region & Platform", color='#0a0a0a', fontsize=14, fontweight='700', pad=20)
    ax1.tick_params(colors='#0a0a0a')
    ax1.set_xlabel('Platform', color='#888888', fontsize=11)
    ax1.set_ylabel('Region', color='#888888', fontsize=11)
    for spine in ax1.spines.values():
        spine.set_visible(False)
    st.pyplot(fig1)
    plt.close(fig1)

    # KDE
    e1 = data[(data['Date'] >= '2017-01-24') & (data['Date'] <= '2017-02-14')]
    e2 = data[(data['Date'] >= '2017-02-28') & (data['Date'] <= '2017-03-21')]
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    fig.patch.set_facecolor('#ffffff')
    for ax in axes.flat:
        ax.set_facecolor('#ffffff')
        ax.tick_params(colors='#0a0a0a', labelsize=9)
        ax.xaxis.label.set_color('#888888')
        ax.yaxis.label.set_color('#888888')
        ax.title.set_color('#0a0a0a')
        for spine in ax.spines.values():
            spine.set_visible(False)
    
    for idx, (col, title) in enumerate([('games_played', 'Games Played'), ('skill_last', 'Skill Level'), ('items_crafted', 'Items Crafted'), ('dollars_spent', 'Dollars Spent')]):
        ax = axes[idx // 2, idx % 2]
        sns.kdeplot(e1[col], fill=True, color="#0a0a0a", label="Event 1", ax=ax, alpha=0.2)
        sns.kdeplot(e2[col], fill=True, color="#888888", label="Event 2", ax=ax, alpha=0.3)
        ax.set_title(title, fontsize=12, fontweight='700')
        ax.legend(fontsize=9, frameon=False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', use_container_width=True)

    st.markdown('<div class="subsection"><span class="subsection-num">04</span><span class="subsection-text">Results</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
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
    
    st.markdown('<div class="subsection"><span class="subsection-num">01</span><span class="subsection-text">Situation</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Post-merger environment with fragmented data across systems. Finance lacked unified performance measurement.</p>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', use_container_width=True)
    
    st.markdown('<div class="subsection"><span class="subsection-num">02</span><span class="subsection-text">Task</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Design dynamic reporting solution with accurate KPIs for executive decision-making.</p>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', use_container_width=True)

    st.markdown('<div class="subsection"><span class="subsection-num">03</span><span class="subsection-text">Action</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>Data Engineering</strong> — SQL extraction, deduplication, normalization</p>
    <p class="bullet"><strong>Schema Design</strong> — Flexible architecture for evolving needs</p>
    <p class="bullet"><strong>Dashboard</strong> — Stakeholder collaboration on key metrics</p>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><span class="subsection-num">04</span><span class="subsection-text">Results</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
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
    
    st.markdown('<div class="subsection"><span class="subsection-num">01</span><span class="subsection-text">Situation</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Escalating logistics costs impacting bottom line. SKYLAB and 3PL Logistics identified as key areas for potential inefficiency.</p>', unsafe_allow_html=True)

    st.markdown('<div class="subsection"><span class="subsection-num">02</span><span class="subsection-text">Task</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Conduct detailed cost analysis to identify waste and optimization opportunities.</p>', unsafe_allow_html=True)

    st.markdown('<div class="subsection"><span class="subsection-num">03</span><span class="subsection-text">Action</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>Financial Analysis</strong> — Python deep dive into expenditure patterns</p>
    <p class="bullet"><strong>Inefficiency Mapping</strong> — Pinpointed cost drivers in both divisions</p>
    <p class="bullet"><strong>Strategy</strong> — Recommendations for operations and vendor contracts</p>
    """, unsafe_allow_html=True)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', use_container_width=True)

    st.markdown('<div class="subsection"><span class="subsection-num">04</span><span class="subsection-text">Results</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
        <p class="bullet"><strong>Cost Reduction</strong> — Identified inefficiencies leading to significant savings</p>
        <p class="bullet"><strong>Streamlined Ops</strong> — Process improvements with positive P&L impact</p>
        <p class="bullet"><strong>Framework</strong> — Established ongoing optimization process</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== AUTOMATION =====================
elif page == "Automation":
    st.markdown('<p class="section-header">QUARTERLY<br>ROYALTY<br>AUTOMATION</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><span class="subsection-num">01</span><span class="subsection-text">Situation</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Month-long manual Excel lookups across years of unorganized data. High error risk, significant analyst burden.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="code-label">Python Automation</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', use_container_width=True)
    with col2:
        st.markdown('<p class="code-label">VBA Integration</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', use_container_width=True)

    st.markdown('<div class="subsection"><span class="subsection-num">02</span><span class="subsection-text">Task</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Transform month-long manual process into automated workflow while maintaining accuracy.</p>', unsafe_allow_html=True)

    st.markdown('<div class="subsection"><span class="subsection-num">03</span><span class="subsection-text">Action</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="bullet"><strong>Data Audit</strong> — Mapped historical structures and requirements</p>
    <p class="bullet"><strong>Python Pipeline</strong> — Automated consolidation and validation</p>
    <p class="bullet"><strong>VBA</strong> — Automated Excel report generation</p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection"><span class="subsection-num">04</span><span class="subsection-text">Results</span><span class="subsection-line"></span></div>', unsafe_allow_html=True)
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
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=260)
    
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
        st.image(img, width=460)
        if link:
            st.markdown(f"<a href='{link}' target='_blank'>Verify Certificate</a>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ===================== CONTACT =====================
elif page == "Contact":
    st.markdown('<p class="section-header">LET\'S<br>CONNECT</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="quote">In God we trust; for all else, we turn to the validation of data.</p>', unsafe_allow_html=True)
    
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
