import streamlit as st

st.set_page_config(layout="wide", page_title="Jason Chang", page_icon="◆", initial_sidebar_state="expanded")

st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=Fraunces:ital,wght@0,400;0,600;1,400&display=swap' rel='stylesheet'>
<style>
/* === RESET & BASE === */
*, *::before, *::after {box-sizing:border-box}
:root {
    --bg: #fafaf9;
    --fg: #1c1917;
    --muted: #78716c;
    --border: #e7e5e4;
    --accent: #0d9488;
    --accent-light: #ccfbf1;
    --surface: #ffffff;
    --dark: #1c1917;
    --dark-muted: #a8a29e;
}

/* === SCROLLBAR === */
::-webkit-scrollbar {width:8px}
::-webkit-scrollbar-track {background:var(--bg)}
::-webkit-scrollbar-thumb {background:var(--border);border-radius:4px}
::-webkit-scrollbar-thumb:hover {background:var(--muted)}

/* === APP === */
.stApp {background:var(--bg)!important}
#MainMenu, footer, header, .stDeployButton {display:none!important}
.block-container {padding:0!important;max-width:100%!important}

/* === SIDEBAR === */
section[data-testid="stSidebar"] {
    background:var(--dark)!important;
    min-width:280px!important;max-width:280px!important
}
section[data-testid="stSidebar"]>div:first-child {padding:0!important}
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {display:none!important}

/* Sidebar brand */
.sidebar-brand {
    padding:60px 40px 50px;
    border-bottom:1px solid rgba(255,255,255,0.06)
}
.sidebar-logo {
    width:48px;height:48px;
    background:var(--accent);
    border-radius:12px;
    display:flex;align-items:center;justify-content:center;
    font-family:'Space Grotesk',sans-serif;
    font-size:20px;font-weight:700;color:#fff;
    margin-bottom:20px
}
.sidebar-name {
    font-family:'Space Grotesk',sans-serif;
    font-size:20px;font-weight:600;color:#fff;
    margin:0 0 4px
}
.sidebar-title {
    font-family:'Inter',sans-serif;
    font-size:13px;color:var(--dark-muted);
    margin:0
}

/* Sidebar nav */
div.stRadio>div {flex-direction:column!important;gap:0!important;padding:20px 0!important}
div[role="radiogroup"]>label[data-baseweb="radio"]>div:first-child {display:none!important}
section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"] {
    background:transparent!important;
    padding:14px 40px!important;
    margin:0!important;
    cursor:pointer!important;
    transition:all 0.2s ease!important
}
section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]:hover {
    background:rgba(255,255,255,0.03)!important
}
section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"][data-checked="true"] {
    background:rgba(255,255,255,0.06)!important
}
section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"] p {
    font-family:'Inter',sans-serif!important;
    font-size:14px!important;
    font-weight:400!important;
    color:var(--dark-muted)!important;
    margin:0!important;
    transition:color 0.2s ease!important
}
section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]:hover p {
    color:#fff!important
}
section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"][data-checked="true"] p {
    color:#fff!important;font-weight:500!important
}

/* Sidebar footer */
.sidebar-footer {
    position:fixed;bottom:0;left:0;width:280px;
    padding:24px 40px;
    border-top:1px solid rgba(255,255,255,0.06);
    background:var(--dark)
}
.sidebar-status {
    display:flex;align-items:center;gap:10px;
    font-family:'Inter',sans-serif;
    font-size:12px;color:var(--accent)
}
.sidebar-status::before {
    content:'';width:8px;height:8px;
    background:var(--accent);border-radius:50%
}

/* === PAGE CONTAINER === */
.page {padding:60px 80px 100px;max-width:1100px;margin:0 auto}
.page-wide {padding:0;max-width:100%}

/* === TYPOGRAPHY === */
.eyebrow {
    font-family:'Inter',sans-serif;
    font-size:12px;font-weight:500;
    color:var(--accent);
    letter-spacing:1.5px;
    text-transform:uppercase;
    margin-bottom:16px
}
.headline {
    font-family:'Space Grotesk',sans-serif;
    font-size:clamp(42px,5vw,56px);
    font-weight:700;
    color:var(--fg);
    line-height:1.1;
    margin:0 0 24px
}
.headline-accent {color:var(--accent)}
.subhead {
    font-family:'Inter',sans-serif;
    font-size:18px;
    color:var(--muted);
    line-height:1.7;
    max-width:560px
}
.section-title {
    font-family:'Space Grotesk',sans-serif;
    font-size:32px;font-weight:600;
    color:var(--fg);
    margin:0 0 40px
}

/* === HERO === */
.hero {
    min-height:calc(100vh - 120px);
    display:flex;flex-direction:column;justify-content:center;
    padding:60px 80px
}
.hero-content {max-width:700px}
.hero-cta {
    display:flex;gap:16px;margin-top:40px
}
.btn {
    font-family:'Inter',sans-serif;
    font-size:14px;font-weight:500;
    padding:14px 28px;
    border-radius:8px;
    text-decoration:none;
    transition:all 0.2s ease;
    cursor:pointer;border:none
}
.btn-primary {
    background:var(--fg);color:#fff
}
.btn-primary:hover {background:var(--accent)}
.btn-secondary {
    background:transparent;color:var(--fg);
    border:1.5px solid var(--border)
}
.btn-secondary:hover {border-color:var(--fg)}

/* === STATS BAR === */
.stats-bar {
    display:flex;gap:60px;
    margin-top:60px;padding-top:40px;
    border-top:1px solid var(--border)
}
.stat {text-align:left}
.stat-value {
    font-family:'Space Grotesk',sans-serif;
    font-size:36px;font-weight:700;color:var(--fg)
}
.stat-label {
    font-family:'Inter',sans-serif;
    font-size:12px;color:var(--muted);
    margin-top:4px
}

/* === FEATURED PROJECT (Big Card) === */
.featured-project {
    background:var(--dark);
    border-radius:24px;
    padding:60px;
    margin:80px 80px 40px;
    color:#fff;
    position:relative;overflow:hidden
}
.featured-project::before {
    content:'';position:absolute;
    top:-50%;right:-20%;
    width:60%;height:200%;
    background:radial-gradient(ellipse,rgba(13,148,136,0.15) 0%,transparent 70%);
    pointer-events:none
}
.featured-label {
    display:inline-flex;align-items:center;gap:8px;
    font-family:'Inter',sans-serif;
    font-size:11px;font-weight:600;
    color:var(--accent);
    letter-spacing:1px;text-transform:uppercase;
    margin-bottom:20px
}
.featured-label::before {content:'★'}
.featured-title {
    font-family:'Space Grotesk',sans-serif;
    font-size:36px;font-weight:600;color:#fff;
    line-height:1.2;margin:0 0 16px;
    max-width:600px
}
.featured-desc {
    font-family:'Inter',sans-serif;
    font-size:16px;color:var(--dark-muted);
    line-height:1.7;max-width:500px;
    margin-bottom:40px
}
.featured-metrics {
    display:flex;gap:48px
}
.featured-metric-value {
    font-family:'Space Grotesk',sans-serif;
    font-size:32px;font-weight:700;color:#fff
}
.featured-metric-label {
    font-family:'Inter',sans-serif;
    font-size:12px;color:var(--dark-muted);margin-top:4px
}
.featured-tags {
    display:flex;gap:10px;margin-top:40px;flex-wrap:wrap
}
.featured-tag {
    font-family:'Inter',sans-serif;
    font-size:12px;color:var(--dark-muted);
    background:rgba(255,255,255,0.08);
    padding:8px 14px;border-radius:6px
}

/* === PROJECT CARDS === */
.projects-grid {
    display:grid;grid-template-columns:repeat(2,1fr);
    gap:24px;padding:0 80px 80px
}
.project-card {
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:16px;
    padding:36px;
    transition:all 0.3s ease
}
.project-card:hover {
    border-color:var(--accent);
    box-shadow:0 20px 40px rgba(0,0,0,0.06);
    transform:translateY(-4px)
}
.project-company {
    font-family:'Inter',sans-serif;
    font-size:11px;font-weight:600;
    color:var(--accent);
    letter-spacing:1px;text-transform:uppercase;
    margin-bottom:12px
}
.project-title {
    font-family:'Space Grotesk',sans-serif;
    font-size:20px;font-weight:600;color:var(--fg);
    line-height:1.3;margin:0 0 12px
}
.project-desc {
    font-family:'Inter',sans-serif;
    font-size:14px;color:var(--muted);
    line-height:1.6;margin-bottom:24px
}
.project-metrics {
    display:flex;gap:24px;
    padding-top:20px;border-top:1px solid var(--border)
}
.project-metric-value {
    font-family:'Space Grotesk',sans-serif;
    font-size:20px;font-weight:700;color:var(--fg)
}
.project-metric-label {
    font-family:'Inter',sans-serif;
    font-size:11px;color:var(--muted)
}

/* === QUOTE === */
.quote-section {
    background:var(--accent-light);
    padding:80px;
    margin:0 80px 80px;
    border-radius:24px;
    text-align:center
}
.quote-text {
    font-family:'Fraunces',serif;
    font-size:28px;font-style:italic;
    color:var(--fg);line-height:1.5;
    max-width:700px;margin:0 auto 24px
}
.quote-author {
    font-family:'Inter',sans-serif;
    font-size:14px;color:var(--muted)
}

/* === WORK PAGE === */
.work-hero {
    background:var(--dark);
    padding:100px 80px;
    text-align:center
}
.work-hero-title {
    font-family:'Space Grotesk',sans-serif;
    font-size:48px;font-weight:700;color:#fff;
    margin:0 0 12px
}
.work-hero-sub {
    font-family:'Inter',sans-serif;
    font-size:16px;color:var(--dark-muted)
}

.case-study {
    padding:80px;
    border-bottom:1px solid var(--border)
}
.case-study:nth-child(even) {background:var(--surface)}
.case-inner {max-width:800px;margin:0 auto}
.case-number {
    font-family:'Inter',sans-serif;
    font-size:12px;font-weight:500;
    color:var(--accent);
    letter-spacing:2px;margin-bottom:16px
}
.case-title {
    font-family:'Space Grotesk',sans-serif;
    font-size:36px;font-weight:700;color:var(--fg);
    line-height:1.2;margin:0 0 8px
}
.case-subtitle {
    font-family:'Inter',sans-serif;
    font-size:16px;color:var(--muted);margin-bottom:40px
}
.case-results {
    background:var(--dark);
    border-radius:16px;
    padding:40px;margin-bottom:48px;
    display:grid;grid-template-columns:repeat(3,1fr);
    gap:24px;text-align:center
}
.case-result-value {
    font-family:'Space Grotesk',sans-serif;
    font-size:36px;font-weight:700;color:#fff
}
.case-result-label {
    font-family:'Inter',sans-serif;
    font-size:12px;color:var(--dark-muted);margin-top:4px
}
.case-section {margin-bottom:40px}
.case-section-title {
    font-family:'Space Grotesk',sans-serif;
    font-size:20px;font-weight:600;color:var(--fg);
    margin-bottom:16px;
    display:flex;align-items:center;gap:12px
}
.case-section-title::before {
    content:'';width:4px;height:20px;
    background:var(--accent);border-radius:2px
}
.case-section p {
    font-family:'Inter',sans-serif;
    font-size:16px;color:var(--muted);
    line-height:1.8;margin:0 0 16px
}
.case-section ul {
    margin:0;padding-left:0;list-style:none
}
.case-section li {
    font-family:'Inter',sans-serif;
    font-size:16px;color:var(--muted);
    line-height:1.8;margin-bottom:12px;
    padding-left:20px;position:relative
}
.case-section li::before {
    content:'→';position:absolute;left:0;color:var(--accent)
}
.case-quote {
    background:var(--accent-light);
    border-radius:12px;
    padding:32px;margin:40px 0
}
.case-quote p {
    font-family:'Fraunces',serif;
    font-size:18px;font-style:italic;
    color:var(--fg);line-height:1.6;margin:0!important
}
.case-quote cite {
    font-family:'Inter',sans-serif;
    font-size:13px;color:var(--muted);
    font-style:normal;display:block;margin-top:16px
}

/* === ABOUT PAGE === */
.about-hero {
    display:grid;grid-template-columns:280px 1fr;
    gap:60px;padding:80px;align-items:start
}
.about-photo {
    width:240px;height:240px;
    background:linear-gradient(135deg,var(--border) 0%,#d6d3d1 100%);
    border-radius:20px;
    display:flex;align-items:center;justify-content:center;
    font-family:'Inter',sans-serif;font-size:13px;color:var(--muted)
}
.about-intro h1 {
    font-family:'Space Grotesk',sans-serif;
    font-size:42px;font-weight:700;color:var(--fg);
    margin:0 0 24px
}
.about-intro p {
    font-family:'Inter',sans-serif;
    font-size:17px;color:var(--muted);
    line-height:1.8;margin:0 0 16px
}
.about-section {
    padding:60px 80px;
    border-top:1px solid var(--border)
}
.about-section:nth-child(even) {background:var(--surface)}

/* Timeline */
.timeline {max-width:700px}
.timeline-item {
    padding:28px 0;
    border-bottom:1px solid var(--border);
    display:grid;grid-template-columns:140px 1fr;gap:24px
}
.timeline-item:last-child {border-bottom:none}
.timeline-year {
    font-family:'Inter',sans-serif;
    font-size:13px;font-weight:500;color:var(--accent)
}
.timeline-content {}
.timeline-role {
    font-family:'Space Grotesk',sans-serif;
    font-size:18px;font-weight:600;color:var(--fg);margin:0 0 4px
}
.timeline-company {
    font-family:'Inter',sans-serif;
    font-size:14px;color:var(--muted)
}
.timeline-desc {
    font-family:'Inter',sans-serif;
    font-size:14px;color:var(--muted);
    line-height:1.6;margin-top:12px
}

/* Skills */
.skills-grid {
    display:grid;grid-template-columns:repeat(3,1fr);gap:24px;
    max-width:900px
}
.skill-card {
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:12px;padding:28px
}
.skill-card-title {
    font-family:'Inter',sans-serif;
    font-size:11px;font-weight:600;
    color:var(--accent);
    letter-spacing:1px;text-transform:uppercase;
    margin-bottom:16px
}
.skill-card-list {
    font-family:'Inter',sans-serif;
    font-size:14px;color:var(--fg);line-height:2
}

/* === CONNECT PAGE === */
.connect-hero {
    background:var(--dark);
    padding:100px 80px;
    text-align:center
}
.connect-hero h1 {
    font-family:'Space Grotesk',sans-serif;
    font-size:48px;font-weight:700;color:#fff;margin:0 0 16px
}
.connect-hero p {
    font-family:'Inter',sans-serif;
    font-size:18px;color:var(--dark-muted);
    max-width:500px;margin:0 auto
}
.connect-cards {
    display:grid;grid-template-columns:repeat(4,1fr);
    gap:16px;max-width:900px;margin:60px auto 0
}
.connect-card {
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:12px;padding:28px;text-align:center;
    transition:all 0.2s ease
}
.connect-card:hover {
    background:rgba(255,255,255,0.08);
    border-color:rgba(255,255,255,0.15)
}
.connect-card-icon {font-size:24px;margin-bottom:12px}
.connect-card-label {
    font-family:'Inter',sans-serif;
    font-size:11px;color:var(--dark-muted);
    text-transform:uppercase;letter-spacing:1px;margin-bottom:8px
}
.connect-card-value {
    font-family:'Inter',sans-serif;
    font-size:14px;color:#fff;word-break:break-all
}
.connect-card-value a {color:var(--accent);text-decoration:none}
.connect-card-value a:hover {color:#fff}

.testimonials {padding:80px}
.testimonials-grid {
    display:grid;grid-template-columns:repeat(2,1fr);
    gap:24px;max-width:1000px;margin:0 auto
}
.testimonial-card {
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:16px;padding:36px
}
.testimonial-quote {
    font-family:'Inter',sans-serif;
    font-size:15px;color:var(--muted);
    line-height:1.7;font-style:italic;margin-bottom:20px
}
.testimonial-author {
    font-family:'Inter',sans-serif;
    font-size:14px;font-weight:600;color:var(--fg)
}
.testimonial-role {
    font-family:'Inter',sans-serif;
    font-size:13px;color:var(--muted);margin-top:2px
}
</style>
""", unsafe_allow_html=True)

# === SIDEBAR ===
with st.sidebar:
    st.markdown('''
    <div class="sidebar-brand">
        <div class="sidebar-logo">JC</div>
        <p class="sidebar-name">Jason Chang</p>
        <p class="sidebar-title">BI Manager</p>
    </div>
    ''', unsafe_allow_html=True)
    
    page = st.radio("Nav", ["Home", "Work", "About", "Connect"], label_visibility="collapsed")
    
    st.markdown('''
    <div class="sidebar-footer">
        <div class="sidebar-status">Open to opportunities</div>
    </div>
    ''', unsafe_allow_html=True)

# === HOME PAGE ===
if page == "Home":
    # Hero
    st.markdown('''
    <div class="hero">
        <div class="hero-content">
            <p class="eyebrow">BI Manager · 10+ Years</p>
            <h1 class="headline">I turn messy data into<br><span class="headline-accent">executive decisions</span></h1>
            <p class="subhead">From Blizzard to Fortune 500 — I help companies find the revenue hiding in their data. I don't just build dashboards. I build clarity.</p>
            <div class="hero-cta">
                <button class="btn btn-primary">View My Work</button>
                <button class="btn btn-secondary">Download Resume</button>
            </div>
            <div class="stats-bar">
                <div class="stat">
                    <div class="stat-value">10+</div>
                    <div class="stat-label">Years in BI</div>
                </div>
                <div class="stat">
                    <div class="stat-value">$15M+</div>
                    <div class="stat-label">Revenue Impact</div>
                </div>
                <div class="stat">
                    <div class="stat-value">250+</div>
                    <div class="stat-label">Users Enabled</div>
                </div>
                <div class="stat">
                    <div class="stat-value">70%</div>
                    <div class="stat-label">Faster Decisions</div>
                </div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Featured Project (Big)
    st.markdown('''
    <div class="featured-project">
        <div class="featured-label">Flagship Project</div>
        <h2 class="featured-title">Unified 5 Conflicting Data Sources Into a Single Source of Truth</h2>
        <p class="featured-desc">Post-merger chaos: 5 sales domains, 5 definitions of "revenue." The CFO was getting conflicting numbers at every board meeting. I had 6 weeks to fix it.</p>
        <div class="featured-metrics">
            <div>
                <div class="featured-metric-value">9%</div>
                <div class="featured-metric-label">Revenue Lift</div>
            </div>
            <div>
                <div class="featured-metric-value">70%</div>
                <div class="featured-metric-label">Fewer Conflicts</div>
            </div>
            <div>
                <div class="featured-metric-value">$12M</div>
                <div class="featured-metric-label">Annual Impact</div>
            </div>
            <div>
                <div class="featured-metric-value">6 wks</div>
                <div class="featured-metric-label">Timeline</div>
            </div>
        </div>
        <div class="featured-tags">
            <span class="featured-tag">Snowflake</span>
            <span class="featured-tag">Power BI</span>
            <span class="featured-tag">Python</span>
            <span class="featured-tag">250+ Users</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Other Projects Grid
    st.markdown('''
    <div class="projects-grid">
        <div class="project-card">
            <div class="project-company">Modern Home Station</div>
            <h3 class="project-title">+33% Conversion via A/B Testing & Attribution Modeling</h3>
            <p class="project-desc">Built cross-channel attribution framework across GA4, Shopify, and Meta. Led A/B testing program that optimized marketing spend.</p>
            <div class="project-metrics">
                <div>
                    <div class="project-metric-value">+33%</div>
                    <div class="project-metric-label">Conversion</div>
                </div>
                <div>
                    <div class="project-metric-value">-18%</div>
                    <div class="project-metric-label">CPA</div>
                </div>
                <div>
                    <div class="project-metric-value">2x</div>
                    <div class="project-metric-label">ROAS</div>
                </div>
            </div>
        </div>
        <div class="project-card">
            <div class="project-company">Operations</div>
            <h3 class="project-title">160 Hours Saved Quarterly via Pipeline Automation</h3>
            <p class="project-desc">Replaced 47 manual Excel macros with automated Python pipelines. Error rate dropped from 15% to near zero.</p>
            <div class="project-metrics">
                <div>
                    <div class="project-metric-value">160 hrs</div>
                    <div class="project-metric-label">Saved/Qtr</div>
                </div>
                <div>
                    <div class="project-metric-value">99</div>
                    <div class="project-metric-label">Vendors</div>
                </div>
                <div>
                    <div class="project-metric-value">0%</div>
                    <div class="project-metric-label">Error Rate</div>
                </div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Quote
    st.markdown('''
    <div class="quote-section">
        <p class="quote-text">"Jason doesn't just build dashboards — he asks the questions that change how we think about the business."</p>
        <p class="quote-author">VP of Sales · Fortune 500</p>
    </div>
    ''', unsafe_allow_html=True)

# === WORK PAGE ===
elif page == "Work":
    st.markdown('''
    <div class="work-hero">
        <h1 class="work-hero-title">Selected Work</h1>
        <p class="work-hero-sub">Deep dives into problems I've solved</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Case Study 1
    st.markdown('''
    <div class="case-study">
        <div class="case-inner">
            <p class="case-number">CASE STUDY 01</p>
            <h2 class="case-title">Unified Executive Intelligence</h2>
            <p class="case-subtitle">Advantage Solutions · 6 weeks</p>
            
            <div class="case-results">
                <div>
                    <div class="case-result-value">9%</div>
                    <div class="case-result-label">Quarterly Revenue Lift</div>
                </div>
                <div>
                    <div class="case-result-value">70%</div>
                    <div class="case-result-label">Fewer KPI Conflicts</div>
                </div>
                <div>
                    <div class="case-result-value">5→1 day</div>
                    <div class="case-result-label">Decision Cycle</div>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>After the acquisition, I inherited a nightmare: 5 sales domains, each with their own "source of truth." APAC counted returns in revenue. EMEA didn't.</p>
                <ul>
                    <li>CFO getting 5 different revenue numbers at every board meeting</li>
                    <li>Field teams created 47 shadow Excel trackers</li>
                    <li>Previous BI lead quit mid-project</li>
                </ul>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">Why This Was Hard</h3>
                <p>This wasn't a technical problem — it was political. Each regional VP had built metrics to make their team look good. Standardizing meant someone's numbers would go down.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p><strong>Week 1-2:</strong> Discovery. Asked one question: "What decision are you trying to make with this data?" Found 70% of "must-have" metrics weren't being used.</p>
                <p><strong>Week 3:</strong> The hard conversation. Recommended forcing standardization now rather than building a "dashboard of dashboards."</p>
                <p><strong>Week 4-5:</strong> Built unified Snowflake schema with 12 golden metrics and Power BI dashboard with row-level security.</p>
                <p><strong>Week 6:</strong> Trained 250 users. Killed access to old reports.</p>
            </div>
            
            <div class="case-quote">
                <p>"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
                <cite>— CFO</cite>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Case Study 2
    st.markdown('''
    <div class="case-study">
        <div class="case-inner">
            <p class="case-number">CASE STUDY 02</p>
            <h2 class="case-title">+33% Conversion Through A/B Testing</h2>
            <p class="case-subtitle">Modern Home Station · Cross-Channel Analytics</p>
            
            <div class="case-results">
                <div>
                    <div class="case-result-value">+33%</div>
                    <div class="case-result-label">Conversion Rate</div>
                </div>
                <div>
                    <div class="case-result-value">-18%</div>
                    <div class="case-result-label">CPA Reduction</div>
                </div>
                <div>
                    <div class="case-result-value">2x</div>
                    <div class="case-result-label">ROAS</div>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>Marketing sending same promotion to everyone. Data scattered across Facebook, Shopify, Google Analytics with no unified customer view.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Applied 7-layer data framework: Business requirements → Data cleaning → Exploratory analysis → Customer segmentation (K-Means) → Validation → Time series → Integration.</p>
                <p>Built cross-channel attribution integrating GA4, Shopify, Meta, Klaviyo. Led multivariate testing program across 12 ad combinations.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">Results</h3>
                <ul>
                    <li>Value-based ads beat feature-based by 33% (p=0.03)</li>
                    <li>Best combo: Meme #2 + Learn More CTA + Comment prompt</li>
                    <li>36% lower CPM with engagement-driven strategies</li>
                </ul>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Case Study 3
    st.markdown('''
    <div class="case-study">
        <div class="case-inner">
            <p class="case-number">CASE STUDY 03</p>
            <h2 class="case-title">160 Hours Saved via Automation</h2>
            <p class="case-subtitle">99 Vendor Data Sources · Python + SQL</p>
            
            <div class="case-results">
                <div>
                    <div class="case-result-value">160 hrs</div>
                    <div class="case-result-label">Saved Quarterly</div>
                </div>
                <div>
                    <div class="case-result-value">15%→0%</div>
                    <div class="case-result-label">Error Rate</div>
                </div>
                <div>
                    <div class="case-result-value">99</div>
                    <div class="case-result-label">Vendors</div>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>"Automation" meant 47 Excel macros that one person (who left) understood. Every Monday, 3 analysts spent 4 hours manually processing vendor reports. Error rate: 15%.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Built dynamic column mapping in Python. Created vendor normalization buckets aligned with GL codes. Combined Python + VBA for hybrid automation. Parallel ran for a week before cutover.</p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# === ABOUT PAGE ===
elif page == "About":
    st.markdown('''
    <div class="about-hero">
        <div class="about-photo">Your Photo<br>240×240</div>
        <div class="about-intro">
            <h1>Hi, I'm Jason.</h1>
            <p>I've spent the last decade helping companies <strong>stop guessing and start knowing</strong>.</p>
            <p>Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers on the screen.</p>
            <p>I've done this at Advantage Solutions, Modern Home Station, China Unicom, and Marshall Electronics.</p>
            <p><strong>What I've learned:</strong> The hard part is never the SQL. It's getting humans to agree on what "revenue" means.</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Timeline
    st.markdown('''
    <div class="about-section">
        <h2 class="section-title">Experience</h2>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-year">2021 — Now</div>
                <div class="timeline-content">
                    <p class="timeline-role">BI Manager</p>
                    <p class="timeline-company">Advantage Solutions</p>
                    <p class="timeline-desc">Built national Power BI ecosystem with Snowflake. Unified 5 sales domains. Automated 99+ vendor pipelines. Managed 7 regional managers.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-year">2017 — 2021</div>
                <div class="timeline-content">
                    <p class="timeline-role">BI Strategy & Analytics Manager</p>
                    <p class="timeline-company">Modern Home Station</p>
                    <p class="timeline-desc">Cross-channel attribution (GA4, Shopify, Meta). A/B testing program. Revenue: +45% FY19, +85% FY20.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-year">2016 — 2017</div>
                <div class="timeline-content">
                    <p class="timeline-role">BI & Strategic Development Manager</p>
                    <p class="timeline-company">China Unicom America</p>
                    <p class="timeline-desc">GTM pricing models. $2M+ revenue projections. Automated churn reporting.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-year">2014 — 2016</div>
                <div class="timeline-content">
                    <p class="timeline-role">BI Project Analyst</p>
                    <p class="timeline-company">Marshall Electronics</p>
                    <p class="timeline-desc">50+ product launches, $5M annual sales. 95% on-time rate.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-year">2010 — 2014</div>
                <div class="timeline-content">
                    <p class="timeline-role">Senior Business Analyst</p>
                    <p class="timeline-company">Cadence Acoustic Ltd.</p>
                    <p class="timeline-desc">Migrated Excel to SQL dashboards. Managed $500M product lines.</p>
                </div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Skills
    st.markdown('''
    <div class="about-section">
        <h2 class="section-title">Skills</h2>
        <div class="skills-grid">
            <div class="skill-card">
                <div class="skill-card-title">Daily Drivers</div>
                <div class="skill-card-list">SQL (10+ years)<br>Power BI / DAX<br>Python<br>Snowflake<br>Excel + VBA</div>
            </div>
            <div class="skill-card">
                <div class="skill-card-title">Fluent</div>
                <div class="skill-card-list">BigQuery<br>GA4<br>Looker<br>Qlik<br>Power Query</div>
            </div>
            <div class="skill-card">
                <div class="skill-card-title">Statistical</div>
                <div class="skill-card-list">A/B Testing<br>Regression<br>K-Means<br>Cohort Analysis<br>Forecasting</div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# === CONNECT PAGE ===
elif page == "Connect":
    st.markdown('''
    <div class="connect-hero">
        <h1>Let's Talk</h1>
        <p>I'm open to Senior BI Manager and Analytics Lead roles. Best way to reach me is email.</p>
        <div class="connect-cards">
            <div class="connect-card">
                <div class="connect-card-icon">📧</div>
                <div class="connect-card-label">Email</div>
                <div class="connect-card-value"><a href="mailto:jason.chang01022024@gmail.com">jason.chang01022024@gmail.com</a></div>
            </div>
            <div class="connect-card">
                <div class="connect-card-icon">💼</div>
                <div class="connect-card-label">LinkedIn</div>
                <div class="connect-card-value"><a href="https://linkedin.com/in/jchang0102">linkedin.com/in/jchang0102</a></div>
            </div>
            <div class="connect-card">
                <div class="connect-card-icon">📱</div>
                <div class="connect-card-label">Phone</div>
                <div class="connect-card-value">(626) 203-3319</div>
            </div>
            <div class="connect-card">
                <div class="connect-card-icon">📍</div>
                <div class="connect-card-label">Location</div>
                <div class="connect-card-value">Hacienda Heights, CA</div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="testimonials">
        <h2 class="section-title" style="text-align:center;margin-bottom:48px">What Colleagues Say</h2>
        <div class="testimonials-grid">
            <div class="testimonial-card">
                <p class="testimonial-quote">"Jason has a rare ability to translate complex data into stories that executives actually act on. He doesn't just answer questions — he asks better ones."</p>
                <p class="testimonial-author">[Name]</p>
                <p class="testimonial-role">VP of Sales</p>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-quote">"Most analysts give you data. Jason gives you decisions. He made our CEO actually look forward to reviewing dashboards."</p>
                <p class="testimonial-author">[Name]</p>
                <p class="testimonial-role">Director of Operations</p>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-quote">"I've worked with a lot of BI people. Jason is the first one who understood that data without context is just noise."</p>
                <p class="testimonial-author">[Name]</p>
                <p class="testimonial-role">CFO</p>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-quote">"Jason doesn't just build dashboards — he changes how teams think about measurement. That's rare."</p>
                <p class="testimonial-author">[Name]</p>
                <p class="testimonial-role">Product Manager</p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
