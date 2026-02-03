"""
Jason C. Chang | BI Manager Portfolio
Fixed: HTML split into smaller chunks to prevent truncation
Darker case study titles for visibility
"""

import streamlit as st
from dataclasses import dataclass

# =============================================================================
# CONFIG
# =============================================================================

@dataclass(frozen=True)
class Config:
    PAGE_TITLE: str = "Jason C. Chang | BI Manager"
    PAGE_ICON: str = "+"
    NAME: str = "Jason C. Chang"
    INITIALS: str = "JC"
    TITLE: str = "BI Manager"
    TAGLINE: str = "I turn data chaos into executive clarity"
    VALUE_PROP: str = "I help executives stop arguing about numbers and start making decisions."
    EMAIL: str = "jason.chang01022024@gmail.com"
    PHONE: str = "(626) 203-3319"
    LINKEDIN: str = "linkedin.com/in/jchang0102"
    LINKEDIN_URL: str = "https://linkedin.com/in/jchang0102"
    LOCATION: str = "Hacienda Heights, CA"
    KEYWORDS: tuple = ("SQL", "Python", "Power BI", "Snowflake", "DAX")
    PAGES: tuple = ("Home", "Work", "About", "Connect")

CONFIG = Config()

# =============================================================================
# CSS
# =============================================================================

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --black: #000000;
    --white: #ffffff;
    --gray-50: #fafafa;
    --gray-100: #f5f5f5;
    --gray-200: #e5e5e5;
    --gray-300: #d4d4d4;
    --gray-400: #a3a3a3;
    --gray-500: #737373;
    --gray-600: #525252;
    --gray-700: #404040;
    --gray-800: #262626;
    --gray-900: #171717;
    --font-display: 'Bebas Neue', Impact, sans-serif;
    --font-body: 'Inter', -apple-system, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}

.stApp, [data-testid="stAppViewContainer"], .main { background: var(--white) !important; }
#MainMenu, footer, header, .stDeployButton, div[data-testid="stDecoration"], [data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

section[data-testid="stSidebar"] { background: var(--black) !important; min-width: 300px !important; max-width: 300px !important; }
section[data-testid="stSidebar"] > div:first-child { padding: 0 !important; padding-bottom: 100px !important; background: var(--black) !important; }
[data-testid="stSidebarNav"] { display: none !important; }

.sidebar-brand { padding: 64px 40px 40px; border-bottom: 1px solid var(--gray-800); text-align: center; }
.sidebar-photo { width: 100px; height: 100px; background: var(--gray-700); border: 3px solid var(--white); border-radius: 50%; margin: 0 auto 24px; display: flex; align-items: center; justify-content: center; font-family: var(--font-body); font-size: 11px; color: var(--gray-400); }
.sidebar-name { font-family: var(--font-display); font-size: 24px; color: var(--white); margin: 0 0 4px; letter-spacing: 3px; }
.sidebar-title { font-family: var(--font-body); font-size: 13px; color: var(--gray-400); margin: 0 0 16px; }
.sidebar-status { display: inline-flex; align-items: center; gap: 8px; background: var(--gray-800); padding: 8px 16px; font-family: var(--font-body); font-size: 11px; font-weight: 600; color: #4ade80; letter-spacing: 1px; }
.sidebar-status::before { content: ''; width: 8px; height: 8px; background: #4ade80; border-radius: 50%; }

[data-testid="stSidebar"] .stRadio > div { flex-direction: column !important; gap: 0 !important; padding: 24px 0 !important; }
[data-testid="stSidebar"] .stRadio label > div:first-child { display: none !important; }
[data-testid="stSidebar"] .stRadio label { background: transparent !important; padding: 16px 40px !important; margin: 0 !important; border-left: 3px solid transparent !important; }
[data-testid="stSidebar"] .stRadio label:hover { background: var(--gray-900) !important; }
[data-testid="stSidebar"] .stRadio label:has(input:checked) { background: var(--gray-900) !important; border-left-color: var(--white) !important; }
[data-testid="stSidebar"] .stRadio label p { font-family: var(--font-display) !important; font-size: 18px !important; color: var(--gray-500) !important; letter-spacing: 3px !important; }
[data-testid="stSidebar"] .stRadio label:hover p { color: var(--gray-300) !important; }
[data-testid="stSidebar"] .stRadio label:has(input:checked) p { color: var(--white) !important; }

.sidebar-footer { position: fixed; bottom: 0; left: 0; width: 300px; padding: 24px 40px; border-top: 1px solid var(--gray-800); background: var(--black); }
.sidebar-download { display: block; background: var(--white); color: var(--black); font-family: var(--font-display); font-size: 14px; letter-spacing: 2px; text-align: center; text-decoration: none; padding: 12px; }

.hero { display: grid; grid-template-columns: 1fr 280px; gap: 96px; padding: 96px 80px; min-height: calc(100vh - 200px); align-items: center; }
.hero-eyebrow { font-family: var(--font-body); font-size: 15px; font-weight: 600; color: var(--gray-500); letter-spacing: 3px; text-transform: uppercase; margin-bottom: 24px; }
.hero-headline { font-family: var(--font-display); font-size: 72px; color: var(--black); line-height: 0.95; margin: 0 0 24px; letter-spacing: 3px; }
.hero-value { font-family: var(--font-body); font-size: 22px; color: var(--gray-600); line-height: 1.6; max-width: 560px; margin-bottom: 40px; }
.hero-keywords { display: flex; flex-wrap: wrap; gap: 12px; }
.hero-keyword { font-family: var(--font-mono); font-size: 14px; color: var(--black); background: var(--gray-100); padding: 10px 18px; border: 2px solid var(--gray-200); }
.hero-photo { width: 260px; height: 260px; background: var(--gray-200); border: 4px solid var(--black); display: flex; align-items: center; justify-content: center; font-family: var(--font-body); font-size: 15px; color: var(--gray-500); text-align: center; }

.stats-section { padding: 0 80px 64px; }
.stats-bar { display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; padding: 40px 0; border-top: 2px solid var(--black); border-bottom: 2px solid var(--black); }
.stat-item { text-align: center; }
.stat-value { font-family: var(--font-display); font-size: 48px; color: var(--black); line-height: 1; }
.stat-label { font-family: var(--font-body); font-size: 14px; color: var(--gray-500); margin-top: 8px; text-transform: uppercase; letter-spacing: 1px; }

.flagship { background: var(--black); padding: 96px 80px; color: var(--white); }
.flagship-label { font-family: var(--font-body); font-size: 13px; font-weight: 600; color: var(--gray-400); letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid var(--white); display: inline-block; }
.flagship-title { font-family: var(--font-display); font-size: 44px; color: var(--white); line-height: 1.1; margin: 0 0 16px; letter-spacing: 2px; max-width: 700px; }
.flagship-meta { display: flex; flex-wrap: wrap; gap: 24px; margin-bottom: 40px; font-family: var(--font-mono); font-size: 14px; color: var(--gray-400); }
.flagship-mess { background: var(--gray-900); padding: 40px; margin-bottom: 40px; border-left: 4px solid var(--white); }
.flagship-mess-label { font-family: var(--font-display); font-size: 20px; color: var(--white); letter-spacing: 2px; margin-bottom: 16px; }
.flagship-mess-text { font-family: var(--font-body); font-size: 18px; color: var(--gray-300); line-height: 1.8; }
.flagship-results { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-bottom: 40px; }
.flagship-result { border-left: 3px solid var(--white); padding-left: 24px; }
.flagship-result-value { font-family: var(--font-display); font-size: 44px; color: var(--white); }
.flagship-result-label { font-family: var(--font-body); font-size: 13px; color: var(--gray-400); margin-top: 4px; text-transform: uppercase; letter-spacing: 1px; }
.flagship-tags { display: flex; gap: 12px; flex-wrap: wrap; }
.flagship-tag { font-family: var(--font-mono); font-size: 13px; color: var(--gray-400); background: var(--gray-800); padding: 10px 16px; }

.home-testimonial { background: var(--gray-100); padding: 64px 80px; }
.testimonial-quote { font-family: var(--font-body); font-size: 26px; font-style: italic; color: var(--black); line-height: 1.5; margin: 0 0 24px; }
.testimonial-author { font-family: var(--font-body); font-size: 16px; font-weight: 600; color: var(--black); text-transform: uppercase; letter-spacing: 1px; }
.testimonial-role { font-family: var(--font-body); font-size: 14px; color: var(--gray-500); margin-top: 2px; }

.projects-section { padding: 64px 80px 96px; }
.projects-title { font-family: var(--font-display); font-size: 32px; color: var(--black); letter-spacing: 3px; margin: 0 0 40px; }
.projects-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; }
.project-card { background: var(--white); border: 2px solid var(--gray-200); padding: 40px; }
.project-company { font-family: var(--font-body); font-size: 13px; font-weight: 600; color: var(--gray-500); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; }
.project-title { font-family: var(--font-display); font-size: 26px; color: var(--black); line-height: 1.2; margin: 0 0 8px; letter-spacing: 1px; }
.project-meta { font-family: var(--font-mono); font-size: 12px; color: var(--gray-500); margin-bottom: 16px; }
.project-desc { font-family: var(--font-body); font-size: 16px; color: var(--gray-600); line-height: 1.6; margin-bottom: 24px; }
.project-metrics { display: flex; gap: 40px; padding-top: 16px; border-top: 1px solid var(--gray-200); }
.pm-value { font-family: var(--font-display); font-size: 26px; color: var(--black); }
.pm-label { font-family: var(--font-body); font-size: 12px; color: var(--gray-500); text-transform: uppercase; }

.work-hero { background: var(--black); padding: 100px 80px; text-align: center; }
.work-hero-title { font-family: var(--font-display); font-size: 56px; color: var(--white); margin: 0 0 16px; letter-spacing: 5px; }
.work-hero-sub { font-family: var(--font-body); font-size: 18px; color: var(--gray-400); }

.case-study { padding: 96px 80px; border-bottom: 1px solid var(--gray-200); }
.case-study:nth-child(even) { background: var(--gray-50); }
.case-inner { max-width: 800px; margin: 0 auto; }
.case-label { display: inline-block; font-family: var(--font-mono); font-size: 13px; font-weight: 600; color: var(--white); background: var(--black); padding: 8px 16px; letter-spacing: 2px; margin-bottom: 24px; }
.case-title { font-family: var(--font-display); font-size: 44px; color: var(--black); line-height: 1.1; margin: 0 0 8px; letter-spacing: 2px; background: linear-gradient(180deg, transparent 60%, #fde047 60%); display: inline; padding: 0 4px; }
.case-subtitle { font-family: var(--font-body); font-size: 17px; color: var(--gray-500); margin-bottom: 40px; margin-top: 16px; }
.case-results { background: var(--black); padding: 40px; margin-bottom: 64px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; text-align: center; }
.cr-value { font-family: var(--font-display); font-size: 44px; color: var(--white); }
.cr-label { font-family: var(--font-body); font-size: 13px; color: var(--gray-400); margin-top: 4px; text-transform: uppercase; letter-spacing: 1px; }
.case-section { margin-bottom: 40px; }
.case-section-title { font-family: var(--font-display); font-size: 22px; color: var(--black); letter-spacing: 2px; margin-bottom: 16px; padding-left: 16px; border-left: 4px solid var(--black); }
.case-section p { font-family: var(--font-body); font-size: 17px; color: var(--gray-600); line-height: 1.8; margin: 0 0 16px; }
.case-section ul { margin: 0; padding: 0; list-style: none; }
.case-section li { font-family: var(--font-body); font-size: 17px; color: var(--gray-600); line-height: 1.8; margin-bottom: 8px; padding-left: 24px; position: relative; }
.case-section li::before { content: '-'; position: absolute; left: 0; color: var(--black); font-weight: 700; }
.case-quote { background: var(--gray-100); padding: 40px; margin: 40px 0; border-left: 4px solid var(--black); }
.case-quote p { font-family: var(--font-body); font-size: 20px; font-style: italic; color: var(--black); line-height: 1.6; margin: 0; }
.case-quote cite { font-family: var(--font-body); font-size: 14px; color: var(--gray-500); font-style: normal; display: block; margin-top: 16px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }

.about-hero { display: grid; grid-template-columns: 300px 1fr; gap: 96px; padding: 96px 80px; align-items: start; }
.about-photo { width: 280px; height: 280px; background: var(--gray-200); border: 4px solid var(--black); display: flex; align-items: center; justify-content: center; font-family: var(--font-body); font-size: 15px; color: var(--gray-500); text-align: center; }
.about-intro h1 { font-family: var(--font-display); font-size: 52px; color: var(--black); margin: 0 0 24px; letter-spacing: 2px; }
.about-intro p { font-family: var(--font-body); font-size: 19px; color: var(--gray-600); line-height: 1.8; margin: 0 0 16px; }

.about-section { padding: 64px 80px; border-top: 1px solid var(--gray-200); }
.about-section:nth-child(even) { background: var(--gray-50); }
.section-title { font-family: var(--font-display); font-size: 32px; color: var(--black); margin: 0 0 40px; letter-spacing: 3px; }

.timeline { max-width: 720px; position: relative; padding-left: 40px; }
.timeline::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: var(--black); }
.tl-item { padding: 24px 0; border-bottom: 1px solid var(--gray-200); display: grid; grid-template-columns: 160px 1fr; gap: 40px; position: relative; }
.tl-item::before { content: ''; position: absolute; left: -47px; top: 32px; width: 16px; height: 16px; background: var(--white); border: 3px solid var(--black); border-radius: 50%; }
.tl-item:last-child { border-bottom: none; }
.tl-year { font-family: var(--font-mono); font-size: 14px; color: var(--gray-500); }
.tl-role { font-family: var(--font-display); font-size: 22px; color: var(--black); margin: 0 0 4px; letter-spacing: 1px; }
.tl-company { font-family: var(--font-body); font-size: 16px; color: var(--gray-500); }
.tl-desc { font-family: var(--font-body); font-size: 16px; color: var(--gray-600); line-height: 1.6; margin-top: 8px; }

.skills-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 900px; }
.skill-card { background: var(--white); border: 2px solid var(--gray-200); padding: 40px; }
.skill-card-title { font-family: var(--font-display); font-size: 18px; color: var(--black); letter-spacing: 2px; margin-bottom: 16px; }
.skill-card-list { font-family: var(--font-body); font-size: 16px; color: var(--gray-600); line-height: 2.2; }

.cert-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; max-width: 900px; }
.cert-card { background: var(--white); border: 2px solid var(--gray-200); padding: 24px; }
.cert-name { font-family: var(--font-body); font-size: 17px; font-weight: 600; color: var(--black); margin-bottom: 4px; }
.cert-issuer { font-family: var(--font-body); font-size: 15px; color: var(--gray-500); }

.connect-hero { background: var(--black); padding: 100px 80px; text-align: center; }
.connect-hero h1 { font-family: var(--font-display); font-size: 56px; color: var(--white); margin: 0 0 24px; letter-spacing: 5px; }
.connect-hero p { font-family: var(--font-body); font-size: 19px; color: var(--gray-400); max-width: 500px; margin: 0 auto; }
.connect-cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; max-width: 960px; margin: 64px auto 0; }
.connect-card { background: var(--gray-900); border: 1px solid var(--gray-800); padding: 40px 24px; text-align: center; }
.cc-icon { font-size: 28px; margin-bottom: 8px; }
.cc-label { font-family: var(--font-body); font-size: 12px; color: var(--gray-500); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; font-weight: 600; }
.cc-value { font-family: var(--font-body); font-size: 15px; color: var(--white); word-break: break-all; }
.cc-value a { color: var(--gray-300); text-decoration: none; }

.testimonials { padding: 96px 80px; }
.testimonials-title { font-family: var(--font-display); font-size: 32px; color: var(--black); letter-spacing: 3px; text-align: center; margin: 0 0 40px; }
.testimonials-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto; }
.tc { background: var(--white); border: 2px solid var(--gray-200); padding: 40px; }
.tc-quote { font-family: var(--font-body); font-size: 17px; color: var(--gray-600); line-height: 1.7; font-style: italic; margin-bottom: 16px; }
.tc-author { font-family: var(--font-body); font-size: 15px; font-weight: 600; color: var(--black); text-transform: uppercase; letter-spacing: 1px; }
.tc-role { font-family: var(--font-body); font-size: 14px; color: var(--gray-500); margin-top: 2px; }

@media (max-width: 1024px) {
    .hero { grid-template-columns: 1fr; padding: 64px 40px; }
    .hero-photo { display: none; }
    .stats-bar, .flagship-results { grid-template-columns: repeat(2, 1fr); }
    .flagship, .projects-section, .case-study, .about-section, .testimonials { padding-left: 40px; padding-right: 40px; }
    .about-hero { grid-template-columns: 1fr; padding: 40px; }
    .projects-grid, .testimonials-grid { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
    .stats-bar, .flagship-results, .case-results { grid-template-columns: 1fr; }
    .skills-grid, .cert-grid, .connect-cards { grid-template-columns: 1fr; }
    .tl-item { grid-template-columns: 1fr; gap: 8px; }
    .connect-cards { grid-template-columns: repeat(2, 1fr); }
}
</style>
"""

# =============================================================================
# MAIN
# =============================================================================

def main():
    st.set_page_config(
        layout="wide",
        page_title=CONFIG.PAGE_TITLE,
        page_icon=CONFIG.PAGE_ICON,
        initial_sidebar_state="expanded"
    )
    
    st.markdown(CSS, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f'''<div class="sidebar-brand">
            <div class="sidebar-photo">Photo</div>
            <p class="sidebar-name">{CONFIG.NAME}</p>
            <p class="sidebar-title">{CONFIG.TITLE}</p>
            <div class="sidebar-status">Open to Opportunities</div>
        </div>''', unsafe_allow_html=True)
        
        page = st.radio("Nav", CONFIG.PAGES, label_visibility="collapsed")
        
        st.markdown('''<div class="sidebar-footer">
            <a href="#" class="sidebar-download">Download Resume</a>
        </div>''', unsafe_allow_html=True)
    
    if page == "Home":
        render_home()
    elif page == "Work":
        render_work()
    elif page == "About":
        render_about()
    elif page == "Connect":
        render_connect()


def render_home():
    # Hero
    keywords_html = ''.join(f'<span class="hero-keyword">{k}</span>' for k in CONFIG.KEYWORDS)
    st.markdown(f'''<div class="hero">
        <div>
            <p class="hero-eyebrow">{CONFIG.TITLE} - 10+ Years - Advantage Solutions</p>
            <h1 class="hero-headline">I TURN DATA CHAOS INTO EXECUTIVE CLARITY</h1>
            <p class="hero-value">{CONFIG.VALUE_PROP}</p>
            <div class="hero-keywords">{keywords_html}</div>
        </div>
        <div class="hero-photo">Your Photo<br>260x260</div>
    </div>''', unsafe_allow_html=True)
    
    # Stats
    st.markdown('''<div class="stats-section"><div class="stats-bar">
        <div class="stat-item"><div class="stat-value">10+</div><div class="stat-label">Years in BI</div></div>
        <div class="stat-item"><div class="stat-value">$15M</div><div class="stat-label">Revenue Impact</div></div>
        <div class="stat-item"><div class="stat-value">250+</div><div class="stat-label">Users Enabled</div></div>
        <div class="stat-item"><div class="stat-value">70%</div><div class="stat-label">Faster Decisions</div></div>
    </div></div>''', unsafe_allow_html=True)
    
    # Flagship - split into chunks
    st.markdown('''<div class="flagship">
        <div class="flagship-label">Flagship Project</div>
        <h2 class="flagship-title">UNIFIED 5 CONFLICTING DATA SOURCES INTO A SINGLE SOURCE OF TRUTH</h2>
        <div class="flagship-meta">
            <span>6 weeks</span><span>$12M annual impact</span><span>250 users</span><span>5 stakeholders</span>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="flagship-mess">
            <div class="flagship-mess-label">THE MESS I INHERITED</div>
            <p class="flagship-mess-text">After the merger, I found 5 sales systems that did not talk to each other. Each region defined revenue differently. The CFO was getting 5 different numbers in every board meeting. I had 6 weeks before Q3 close to build a single source of truth.</p>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="flagship-results">
            <div class="flagship-result"><div class="flagship-result-value">9%</div><div class="flagship-result-label">Revenue Lift</div></div>
            <div class="flagship-result"><div class="flagship-result-value">70%</div><div class="flagship-result-label">Fewer Conflicts</div></div>
            <div class="flagship-result"><div class="flagship-result-value">5-1</div><div class="flagship-result-label">Day Decision Cycle</div></div>
            <div class="flagship-result"><div class="flagship-result-value">$12M</div><div class="flagship-result-label">Annual Impact</div></div>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="flagship-tags">
            <span class="flagship-tag">Snowflake</span><span class="flagship-tag">Power BI</span><span class="flagship-tag">Python</span><span class="flagship-tag">DAX</span>
        </div>
    </div>''', unsafe_allow_html=True)
    
    # Testimonial
    st.markdown('''<div class="home-testimonial">
        <p class="testimonial-quote">"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
        <p class="testimonial-author">[Name]</p>
        <p class="testimonial-role">CFO, Advantage Solutions</p>
    </div>''', unsafe_allow_html=True)
    
    # Projects
    st.markdown('''<div class="projects-section">
        <h2 class="projects-title">MORE WORK</h2>
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-company">Modern Home Station</div>
                <h3 class="project-title">+33% CONVERSION VIA A/B TESTING</h3>
                <div class="project-meta">8 weeks - Cross-channel attribution</div>
                <p class="project-desc">Marketing was sending the same promotion to everyone. Built cross-channel attribution across GA4, Shopify, Meta.</p>
                <div class="project-metrics">
                    <div><div class="pm-value">+33%</div><div class="pm-label">Conversion</div></div>
                    <div><div class="pm-value">-18%</div><div class="pm-label">CPA</div></div>
                    <div><div class="pm-value">2x</div><div class="pm-label">ROAS</div></div>
                </div>
            </div>
            <div class="project-card">
                <div class="project-company">Operations Automation</div>
                <h3 class="project-title">160 HOURS SAVED QUARTERLY</h3>
                <div class="project-meta">4 weeks - 99 vendor sources</div>
                <p class="project-desc">Automation meant 47 Excel macros that one person understood. Replaced with Python pipelines.</p>
                <div class="project-metrics">
                    <div><div class="pm-value">160 hrs</div><div class="pm-label">Saved/Qtr</div></div>
                    <div><div class="pm-value">0%</div><div class="pm-label">Error Rate</div></div>
                    <div><div class="pm-value">99</div><div class="pm-label">Vendors</div></div>
                </div>
            </div>
        </div>
    </div>''', unsafe_allow_html=True)


def render_work():
    st.markdown('''<div class="work-hero">
        <h1 class="work-hero-title">SELECTED WORK</h1>
        <p class="work-hero-sub">Deep dives into problems I have solved</p>
    </div>''', unsafe_allow_html=True)
    
    # Case 1 - split into chunks
    st.markdown('''<div class="case-study"><div class="case-inner">
        <span class="case-label">FLAGSHIP PROJECT</span>
        <h2 class="case-title">UNIFIED EXECUTIVE INTELLIGENCE</h2>
        <p class="case-subtitle">Advantage Solutions - 6 weeks - $12M impact - 250 users</p>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="case-results">
            <div><div class="cr-value">9%</div><div class="cr-label">Quarterly Revenue Lift</div></div>
            <div><div class="cr-value">70%</div><div class="cr-label">Fewer KPI Conflicts</div></div>
            <div><div class="cr-value">5-1</div><div class="cr-label">Decision Cycle Days</div></div>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="case-section">
            <h3 class="case-section-title">THE MESS</h3>
            <p>After the merger, I inherited 5 sales systems that did not talk to each other. Each region defined revenue differently. The CFO was getting 5 different numbers in every board meeting.</p>
            <ul>
                <li>CFO getting 5 different revenue numbers at every board meeting</li>
                <li>Field teams created 47 shadow Excel trackers</li>
                <li>Previous BI lead quit mid-project</li>
            </ul>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="case-section">
            <h3 class="case-section-title">WHY THIS WAS HARD</h3>
            <p>This was not a technical problem - it was political. Each regional VP had built metrics to make their team look good. Standardizing meant someones numbers would go down.</p>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="case-section">
            <h3 class="case-section-title">MY APPROACH</h3>
            <p><strong>Week 1-2:</strong> Discovery. Asked every stakeholder: What decision are you trying to make?</p>
            <p><strong>Week 3:</strong> Forced alignment meeting. Locked 5 VPs in a room until we agreed on 12 golden metrics.</p>
            <p><strong>Week 4-5:</strong> Built unified Snowflake schema. Wrote 40+ DAX measures.</p>
            <p><strong>Week 6:</strong> Trained 250 users. Killed old reports.</p>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="case-section">
            <h3 class="case-section-title">WHAT WENT WRONG</h3>
            <p>APAC had an undocumented custom field that their entire commission structure depended on. Their numbers broke Day 1. I had to patch the data model live while the regional VP was on a CEO call.</p>
        </div>''', unsafe_allow_html=True)
    
    st.markdown('''<div class="case-quote">
            <p>"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
            <cite>- CFO</cite>
        </div>
    </div></div>''', unsafe_allow_html=True)
    
    # Case 2
    st.markdown('''<div class="case-study"><div class="case-inner">
        <span class="case-label">CASE STUDY 02</span>
        <h2 class="case-title">+33% CONVERSION THROUGH A/B TESTING</h2>
        <p class="case-subtitle">Modern Home Station - 8 weeks - Cross-Channel Analytics</p>
        <div class="case-results">
            <div><div class="cr-value">+33%</div><div class="cr-label">Conversion Rate</div></div>
            <div><div class="cr-value">-18%</div><div class="cr-label">CPA Reduction</div></div>
            <div><div class="cr-value">2x</div><div class="cr-label">ROAS</div></div>
        </div>
        <div class="case-section">
            <h3 class="case-section-title">THE MESS</h3>
            <p>Marketing was sending the same promotion to everyone. Data scattered across Facebook, Shopify, Google Analytics - no unified customer view.</p>
        </div>
        <div class="case-section">
            <h3 class="case-section-title">MY APPROACH</h3>
            <p>Built cross-channel attribution integrating GA4, Shopify, Meta, Klaviyo. Applied K-Means segmentation. Led multivariate testing across 12 ad combinations.</p>
        </div>
        <div class="case-section">
            <h3 class="case-section-title">WHAT WENT WRONG</h3>
            <p>Saw spike in content views but no page views. Spent days debugging - mobile video sound settings were wrong, causing users to scroll past.</p>
        </div>
    </div></div>''', unsafe_allow_html=True)
    
    # Case 3
    st.markdown('''<div class="case-study"><div class="case-inner">
        <span class="case-label">CASE STUDY 03</span>
        <h2 class="case-title">160 HOURS SAVED VIA AUTOMATION</h2>
        <p class="case-subtitle">99 Vendor Data Sources - 4 weeks - Python + SQL</p>
        <div class="case-results">
            <div><div class="cr-value">160 hrs</div><div class="cr-label">Saved Quarterly</div></div>
            <div><div class="cr-value">0%</div><div class="cr-label">Error Rate</div></div>
            <div><div class="cr-value">99</div><div class="cr-label">Vendors</div></div>
        </div>
        <div class="case-section">
            <h3 class="case-section-title">THE MESS</h3>
            <p>Automation meant 47 Excel macros that one person understood. Every Monday, 3 analysts spent 4 hours manually processing vendor reports. Error rate: 15%.</p>
        </div>
        <div class="case-section">
            <h3 class="case-section-title">MY APPROACH</h3>
            <p>Built dynamic column mapping in Python. Created normalization buckets aligned with GL codes. Combined Python + VBA for hybrid automation.</p>
        </div>
        <div class="case-quote">
            <p>"Finance finally trusts the automated reports. That has not happened in years."</p>
            <cite>- VP of Finance</cite>
        </div>
    </div></div>''', unsafe_allow_html=True)


def render_about():
    st.markdown('''<div class="about-hero">
        <div class="about-photo">Your Photo<br>280x280</div>
        <div class="about-intro">
            <h1>HI, I AM JASON.</h1>
            <p>I have spent the last decade helping companies <strong>stop guessing and start knowing</strong>.</p>
            <p>Most BI teams build dashboards. I build clarity - the kind where a CEO can walk into a board meeting and actually trust the numbers.</p>
            <p><strong>What I have learned:</strong> The hard part is never the SQL. It is getting humans to agree on what revenue means.</p>
        </div>
    </div>''', unsafe_allow_html=True)
    
    # Experience
    st.markdown('''<div class="about-section">
        <h2 class="section-title">EXPERIENCE</h2>
        <div class="timeline">
            <div class="tl-item">
                <div class="tl-year">2021 - Present</div>
                <div><p class="tl-role">BI MANAGER</p><p class="tl-company">Advantage Solutions</p><p class="tl-desc">Built national Power BI ecosystem. Unified 5 sales domains. Automated 99+ vendor pipelines.</p></div>
            </div>
            <div class="tl-item">
                <div class="tl-year">2017 - 2021</div>
                <div><p class="tl-role">BI STRATEGY MANAGER</p><p class="tl-company">Modern Home Station</p><p class="tl-desc">Cross-channel attribution. A/B testing program. Revenue: +45% FY19, +85% FY20.</p></div>
            </div>
            <div class="tl-item">
                <div class="tl-year">2016 - 2017</div>
                <div><p class="tl-role">BI STRATEGY MANAGER</p><p class="tl-company">China Unicom America</p><p class="tl-desc">GTM pricing models. $2M+ revenue projections.</p></div>
            </div>
            <div class="tl-item">
                <div class="tl-year">2014 - 2016</div>
                <div><p class="tl-role">BI PROJECT ANALYST</p><p class="tl-company">Marshall Electronics</p><p class="tl-desc">50+ product launches, $5M annual sales.</p></div>
            </div>
            <div class="tl-item">
                <div class="tl-year">2010 - 2014</div>
                <div><p class="tl-role">SENIOR BUSINESS ANALYST</p><p class="tl-company">Cadence Acoustic Ltd.</p><p class="tl-desc">Migrated Excel to SQL dashboards. Managed $500M product lines.</p></div>
            </div>
        </div>
    </div>''', unsafe_allow_html=True)
    
    # Education
    st.markdown('''<div class="about-section">
        <h2 class="section-title">EDUCATION</h2>
        <div class="timeline">
            <div class="tl-item">
                <div class="tl-year">2010</div>
                <div><p class="tl-role">B.S. BUSINESS ADMINISTRATION</p><p class="tl-company">University of California, Riverside</p></div>
            </div>
        </div>
    </div>''', unsafe_allow_html=True)
    
    # Skills
    st.markdown('''<div class="about-section">
        <h2 class="section-title">SKILLS</h2>
        <div class="skills-grid">
            <div class="skill-card"><div class="skill-card-title">DAILY DRIVERS</div><div class="skill-card-list">SQL (10+ years)<br>Power BI / DAX<br>Python<br>Snowflake<br>Excel + VBA</div></div>
            <div class="skill-card"><div class="skill-card-title">FLUENT</div><div class="skill-card-list">BigQuery<br>GA4<br>Looker<br>Qlik<br>Power Query</div></div>
            <div class="skill-card"><div class="skill-card-title">STATISTICAL</div><div class="skill-card-list">A/B Testing<br>Regression<br>K-Means<br>Cohort Analysis<br>Forecasting</div></div>
        </div>
    </div>''', unsafe_allow_html=True)
    
    # Certs
    st.markdown('''<div class="about-section">
        <h2 class="section-title">CERTIFICATIONS</h2>
        <div class="cert-grid">
            <div class="cert-card"><p class="cert-name">Supervised Machine Learning</p><p class="cert-issuer">Stanford Online - 2024</p></div>
            <div class="cert-card"><p class="cert-name">Neural Networks</p><p class="cert-issuer">DeepLearning.AI - 2024</p></div>
            <div class="cert-card"><p class="cert-name">Power BI Data Visualization</p><p class="cert-issuer">edX - 2019</p></div>
        </div>
    </div>''', unsafe_allow_html=True)


def render_connect():
    st.markdown(f'''<div class="connect-hero">
        <h1>LETS TALK</h1>
        <p>Open to Senior BI Manager and Analytics Lead roles. Best way to reach me is email.</p>
        <div class="connect-cards">
            <div class="connect-card"><div class="cc-icon">📧</div><div class="cc-label">Email</div><div class="cc-value"><a href="mailto:{CONFIG.EMAIL}">{CONFIG.EMAIL}</a></div></div>
            <div class="connect-card"><div class="cc-icon">💼</div><div class="cc-label">LinkedIn</div><div class="cc-value"><a href="{CONFIG.LINKEDIN_URL}">{CONFIG.LINKEDIN}</a></div></div>
            <div class="connect-card"><div class="cc-icon">📱</div><div class="cc-label">Phone</div><div class="cc-value">{CONFIG.PHONE}</div></div>
            <div class="connect-card"><div class="cc-icon">📍</div><div class="cc-label">Location</div><div class="cc-value">{CONFIG.LOCATION}</div></div>
        </div>
    </div>''', unsafe_allow_html=True)
    
    # Testimonials
    st.markdown('''<div class="testimonials">
        <h2 class="testimonials-title">WHAT COLLEAGUES SAY</h2>
        <div class="testimonials-grid">
            <div class="tc"><p class="tc-quote">"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p><p class="tc-author">[Name]</p><p class="tc-role">CFO, Advantage Solutions</p></div>
            <div class="tc"><p class="tc-quote">"Jason has a rare ability to translate complex data into stories that executives actually act on."</p><p class="tc-author">[Name]</p><p class="tc-role">VP of Sales</p></div>
            <div class="tc"><p class="tc-quote">"Most analysts give you data. Jason gives you decisions."</p><p class="tc-author">[Name]</p><p class="tc-role">Director of Operations</p></div>
            <div class="tc"><p class="tc-quote">"Finance finally trusts the automated reports. That has not happened in years."</p><p class="tc-author">[Name]</p><p class="tc-role">VP of Finance</p></div>
        </div>
    </div>''', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
