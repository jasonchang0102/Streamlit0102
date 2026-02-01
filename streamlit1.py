import streamlit as st

st.set_page_config(layout="wide", page_title="Jason C. Chang | BI Manager", page_icon="◆", initial_sidebar_state="expanded")

# CSS - using robust selectors for modern Streamlit
css = """
<link href='https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=Fraunces:ital,wght@0,400;0,600;1,400&display=swap' rel='stylesheet'>
<style>
:root {
    --bg: #fafaf9;
    --fg: #1c1917;
    --muted: #78716c;
    --border: #e7e5e4;
    --accent: #0d9488;
    --accent-light: #ccfbf1;
    --surface: #ffffff;
    --dark: #171717;
    --dark-muted: #a8a29e;
}

/* Scrollbar */
::-webkit-scrollbar {width:6px}
::-webkit-scrollbar-track {background:transparent}
::-webkit-scrollbar-thumb {background:var(--border);border-radius:3px}

/* Main app background */
.stApp, [data-testid="stAppViewContainer"] {background:var(--bg) !important}

/* Hide default Streamlit elements */
#MainMenu, footer, header, .stDeployButton, 
div[data-testid="stDecoration"],
[data-testid="stToolbar"],
[data-testid="stStatusWidget"] {display:none !important}

/* Main container */
.block-container, [data-testid="stMainBlockContainer"] {
    padding:0 !important;
    max-width:100% !important
}

/* Sidebar styling */
section[data-testid="stSidebar"],
[data-testid="stSidebar"] {
    background:var(--dark) !important;
    min-width:260px !important;
    max-width:260px !important
}

section[data-testid="stSidebar"]>div:first-child,
[data-testid="stSidebar"]>div:first-child {
    padding:0 !important;
    padding-bottom:80px !important
}

[data-testid="stSidebarNav"],
[data-testid="stSidebarNavItems"] {display:none !important}

/* Sidebar brand */
.sidebar-brand {padding:48px 32px 40px;border-bottom:1px solid rgba(255,255,255,0.06)}
.sidebar-logo {
    width:44px;height:44px;background:var(--accent);border-radius:10px;
    display:flex;align-items:center;justify-content:center;
    font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:700;color:#fff;margin-bottom:16px
}
.sidebar-name {font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:600;color:#fff;margin:0 0 2px}
.sidebar-title {font-family:'Inter',sans-serif;font-size:12px;color:var(--dark-muted);margin:0}

/* Radio button container - using data-testid */
[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    flex-direction:column !important;
    gap:0 !important;
    padding:16px 0 !important
}

/* Hide radio circles */
[data-testid="stSidebar"] [data-testid="stRadio"] [data-baseweb="radio"] > div:first-child,
[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display:none !important
}

/* Radio labels base style */
[data-testid="stSidebar"] [data-testid="stRadio"] label,
[data-testid="stSidebar"] div[role="radiogroup"] label {
    background:transparent !important;
    padding:12px 32px !important;
    margin:0 !important;
    cursor:pointer !important;
    transition:all 0.15s ease !important;
    border-left:2px solid transparent !important;
    border-radius:0 !important
}

/* Radio labels hover */
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover,
[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background:rgba(255,255,255,0.03) !important
}

/* Radio labels checked - using aria-checked */
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked),
[data-testid="stSidebar"] div[role="radiogroup"] label[aria-checked="true"],
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background:rgba(255,255,255,0.05) !important;
    border-left-color:var(--accent) !important
}

/* Radio label text */
[data-testid="stSidebar"] [data-testid="stRadio"] label p,
[data-testid="stSidebar"] div[role="radiogroup"] label p,
[data-testid="stSidebar"] [data-testid="stRadio"] label span {
    font-family:'Inter',sans-serif !important;
    font-size:13px !important;
    font-weight:400 !important;
    color:var(--dark-muted) !important;
    margin:0 !important
}

/* Radio label text hover */
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover p,
[data-testid="stSidebar"] div[role="radiogroup"] label:hover p {
    color:rgba(255,255,255,0.8) !important
}

/* Radio label text checked */
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) p,
[data-testid="stSidebar"] div[role="radiogroup"] label[aria-checked="true"] p,
[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
    color:#fff !important;
    font-weight:500 !important
}

/* Hide radio widget label */
[data-testid="stSidebar"] [data-testid="stRadio"] > label,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    display:none !important
}

/* Sidebar footer */
.sidebar-footer {
    position:fixed;bottom:0;left:0;width:260px;padding:20px 32px;
    border-top:1px solid rgba(255,255,255,0.06);background:var(--dark);z-index:100
}
.sidebar-status {display:flex;align-items:center;gap:8px;font-family:'Inter',sans-serif;font-size:11px;color:var(--accent)}
.sidebar-status::before {content:'';width:6px;height:6px;background:var(--accent);border-radius:50%}

/* Typography */
.eyebrow {font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:var(--accent);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px}
.headline {font-family:'Space Grotesk',sans-serif;font-size:clamp(36px,4.5vw,52px);font-weight:700;color:var(--fg);line-height:1.1;margin:0 0 20px}
.headline-accent {color:var(--accent)}
.subhead {font-family:'Inter',sans-serif;font-size:17px;color:var(--muted);line-height:1.7;max-width:520px}
.section-title {font-family:'Space Grotesk',sans-serif;font-size:28px;font-weight:600;color:var(--fg);margin:0 0 32px}

/* Hero section */
.hero {min-height:calc(100vh - 100px);display:flex;flex-direction:column;justify-content:center;padding:48px 60px}
.hero-content {max-width:640px}
.stats-bar {display:flex;gap:48px;margin-top:48px;padding-top:32px;border-top:1px solid var(--border)}
.stat-value {font-family:'Space Grotesk',sans-serif;font-size:32px;font-weight:700;color:var(--fg)}
.stat-label {font-family:'Inter',sans-serif;font-size:11px;color:var(--muted);margin-top:2px}

/* Featured project */
.featured-project {
    background:var(--dark);border-radius:20px;padding:48px;
    margin:60px 60px 32px;color:#fff;position:relative;overflow:hidden
}
.featured-label {display:inline-flex;align-items:center;gap:6px;font-family:'Inter',sans-serif;font-size:10px;font-weight:600;color:var(--accent);letter-spacing:1px;text-transform:uppercase;margin-bottom:16px}
.featured-title {font-family:'Space Grotesk',sans-serif;font-size:28px;font-weight:600;color:#fff;line-height:1.25;margin:0 0 12px;max-width:560px}
.featured-desc {font-family:'Inter',sans-serif;font-size:15px;color:var(--dark-muted);line-height:1.7;max-width:480px;margin-bottom:32px}
.featured-metrics {display:flex;gap:40px}
.featured-metric-value {font-family:'Space Grotesk',sans-serif;font-size:28px;font-weight:700;color:#fff}
.featured-metric-label {font-family:'Inter',sans-serif;font-size:11px;color:var(--dark-muted);margin-top:2px}
.featured-tags {display:flex;gap:8px;margin-top:32px;flex-wrap:wrap}
.featured-tag {font-family:'Inter',sans-serif;font-size:11px;color:var(--dark-muted);background:rgba(255,255,255,0.08);padding:6px 12px;border-radius:4px}

/* Projects grid */
.projects-grid {display:grid;grid-template-columns:repeat(2,1fr);gap:20px;padding:0 60px 60px}
.project-card {background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:28px;transition:all 0.25s ease}
.project-card:hover {border-color:var(--accent);box-shadow:0 12px 32px rgba(0,0,0,0.06);transform:translateY(-3px)}
.project-company {font-family:'Inter',sans-serif;font-size:10px;font-weight:600;color:var(--accent);letter-spacing:1px;text-transform:uppercase;margin-bottom:10px}
.project-title {font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:600;color:var(--fg);line-height:1.3;margin:0 0 10px}
.project-desc {font-family:'Inter',sans-serif;font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:20px}
.project-metrics {display:flex;gap:20px;padding-top:16px;border-top:1px solid var(--border)}
.project-metric-value {font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:700;color:var(--fg)}
.project-metric-label {font-family:'Inter',sans-serif;font-size:10px;color:var(--muted)}

/* Quote section */
.quote-section {background:var(--accent-light);padding:60px;margin:0 60px 60px;border-radius:20px;text-align:center}
.quote-text {font-family:'Fraunces',serif;font-size:24px;font-style:italic;color:var(--fg);line-height:1.5;max-width:600px;margin:0 auto 20px}
.quote-author {font-family:'Inter',sans-serif;font-size:13px;color:var(--muted)}

/* Work page */
.work-hero {background:var(--dark);padding:80px 60px;text-align:center}
.work-hero-title {font-family:'Space Grotesk',sans-serif;font-size:42px;font-weight:700;color:#fff;margin:0 0 8px}
.work-hero-sub {font-family:'Inter',sans-serif;font-size:15px;color:var(--dark-muted)}

/* Case studies */
.case-study {padding:60px;border-bottom:1px solid var(--border)}
.case-study:nth-child(even) {background:var(--surface)}
.case-inner {max-width:720px;margin:0 auto}
.case-number {font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:var(--accent);letter-spacing:2px;margin-bottom:12px}
.case-title {font-family:'Space Grotesk',sans-serif;font-size:32px;font-weight:700;color:var(--fg);line-height:1.2;margin:0 0 6px}
.case-subtitle {font-family:'Inter',sans-serif;font-size:14px;color:var(--muted);margin-bottom:32px}
.case-results {background:var(--dark);border-radius:14px;padding:32px;margin-bottom:40px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;text-align:center}
.case-result-value {font-family:'Space Grotesk',sans-serif;font-size:32px;font-weight:700;color:#fff}
.case-result-label {font-family:'Inter',sans-serif;font-size:11px;color:var(--dark-muted);margin-top:2px}
.case-section {margin-bottom:32px}
.case-section-title {font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:600;color:var(--fg);margin-bottom:12px;display:flex;align-items:center;gap:10px}
.case-section-title::before {content:'';width:3px;height:18px;background:var(--accent);border-radius:2px}
.case-section p {font-family:'Inter',sans-serif;font-size:15px;color:var(--muted);line-height:1.8;margin:0 0 12px}
.case-section ul {margin:0;padding-left:0;list-style:none}
.case-section li {font-family:'Inter',sans-serif;font-size:15px;color:var(--muted);line-height:1.8;margin-bottom:8px;padding-left:24px;position:relative}
.case-section li::before {content:'→';position:absolute;left:0;color:var(--accent)}
.case-quote {background:var(--accent-light);border-radius:10px;padding:24px 28px;margin:32px 0}
.case-quote p {font-family:'Fraunces',serif;font-size:16px;font-style:italic;color:var(--fg);line-height:1.6;margin:0}
.case-quote cite {font-family:'Inter',sans-serif;font-size:12px;color:var(--muted);font-style:normal;display:block;margin-top:12px}

/* About page */
.about-hero {display:grid;grid-template-columns:220px 1fr;gap:48px;padding:60px;align-items:start}
.about-photo {
    width:200px;height:200px;background:linear-gradient(135deg,var(--accent) 0%,#0f766e 100%);
    border-radius:16px;display:flex;align-items:center;justify-content:center;
    font-family:'Space Grotesk',sans-serif;font-size:64px;font-weight:700;color:#fff;
    border:3px solid var(--surface);box-shadow:0 8px 24px rgba(0,0,0,0.08)
}
.about-intro h1 {font-family:'Space Grotesk',sans-serif;font-size:36px;font-weight:700;color:var(--fg);margin:0 0 20px}
.about-intro p {font-family:'Inter',sans-serif;font-size:16px;color:var(--muted);line-height:1.8;margin:0 0 14px}
.about-section {padding:48px 60px;border-top:1px solid var(--border)}
.about-section:nth-child(even) {background:var(--surface)}

/* Timeline */
.timeline {max-width:640px;position:relative;padding-left:20px}
.timeline::before {content:'';position:absolute;left:0;top:8px;bottom:8px;width:2px;background:var(--border)}
.timeline-item {padding:20px 0;border-bottom:1px solid var(--border);display:grid;grid-template-columns:120px 1fr;gap:20px;position:relative}
.timeline-item::before {content:'';position:absolute;left:-20px;top:28px;width:10px;height:10px;background:var(--surface);border:2px solid var(--accent);border-radius:50%}
.timeline-item:last-child {border-bottom:none}
.timeline-year {font-family:'Inter',sans-serif;font-size:12px;font-weight:500;color:var(--accent)}
.timeline-role {font-family:'Space Grotesk',sans-serif;font-size:16px;font-weight:600;color:var(--fg);margin:0 0 2px}
.timeline-company {font-family:'Inter',sans-serif;font-size:13px;color:var(--muted)}
.timeline-desc {font-family:'Inter',sans-serif;font-size:13px;color:var(--muted);line-height:1.6;margin-top:10px}

/* Skills */
.skills-grid {display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:800px}
.skill-card {background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:24px;transition:all 0.2s ease}
.skill-card:hover {border-color:var(--accent);box-shadow:0 4px 16px rgba(13,148,136,0.08)}
.skill-card-title {font-family:'Inter',sans-serif;font-size:10px;font-weight:600;color:var(--accent);letter-spacing:1px;text-transform:uppercase;margin-bottom:12px}
.skill-card-list {font-family:'Inter',sans-serif;font-size:13px;color:var(--fg);line-height:2}

/* Certifications */
.cert-grid {display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:800px}
.cert-card {background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:20px;transition:all 0.2s ease}
.cert-card:hover {border-color:var(--accent)}
.cert-name {font-family:'Inter',sans-serif;font-size:14px;font-weight:600;color:var(--fg);margin-bottom:4px}
.cert-issuer {font-family:'Inter',sans-serif;font-size:12px;color:var(--muted)}

/* Connect page */
.connect-hero {background:var(--dark);padding:80px 60px;text-align:center}
.connect-hero h1 {font-family:'Space Grotesk',sans-serif;font-size:42px;font-weight:700;color:#fff;margin:0 0 12px}
.connect-hero p {font-family:'Inter',sans-serif;font-size:16px;color:var(--dark-muted);max-width:460px;margin:0 auto}
.connect-cards {display:grid;grid-template-columns:repeat(4,1fr);gap:12px;max-width:800px;margin:48px auto 0}
.connect-card {background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:24px 16px;text-align:center;transition:all 0.2s ease}
.connect-card:hover {background:rgba(255,255,255,0.08);border-color:var(--accent);transform:translateY(-2px)}
.connect-card-icon {font-size:20px;margin-bottom:10px}
.connect-card-label {font-family:'Inter',sans-serif;font-size:10px;color:var(--dark-muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}
.connect-card-value {font-family:'Inter',sans-serif;font-size:12px;color:#fff;word-break:break-all}
.connect-card-value a {color:var(--accent);text-decoration:none}
.connect-card-value a:hover {color:#fff}

/* Testimonials */
.testimonials {padding:60px}
.testimonials-grid {display:grid;grid-template-columns:repeat(2,1fr);gap:20px;max-width:900px;margin:0 auto}
.testimonial-card {background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:28px;transition:all 0.2s ease}
.testimonial-card:hover {border-color:var(--accent);box-shadow:0 8px 24px rgba(0,0,0,0.04)}
.testimonial-quote {font-family:'Inter',sans-serif;font-size:14px;color:var(--muted);line-height:1.7;font-style:italic;margin-bottom:16px}
.testimonial-author {font-family:'Inter',sans-serif;font-size:13px;font-weight:600;color:var(--fg)}
.testimonial-role {font-family:'Inter',sans-serif;font-size:12px;color:var(--muted);margin-top:2px}

/* Streamlit button override */
.stButton>button {
    font-family:'Inter',sans-serif !important;
    font-size:13px !important;
    font-weight:500 !important;
    padding:10px 20px !important;
    border-radius:6px !important
}

/* Responsive */
@media (max-width:768px) {
    .hero {padding:32px 24px;min-height:auto}
    .stats-bar {flex-wrap:wrap;gap:24px 40px}
    .featured-project {margin:40px 24px;padding:32px}
    .featured-metrics {flex-wrap:wrap;gap:24px}
    .projects-grid {grid-template-columns:1fr;padding:0 24px 40px}
    .quote-section {margin:0 24px 40px;padding:40px 24px}
    .case-study {padding:40px 24px}
    .case-results {grid-template-columns:1fr;gap:16px}
    .about-hero {grid-template-columns:1fr;gap:32px;padding:40px 24px}
    .about-section {padding:40px 24px}
    .skills-grid, .cert-grid {grid-template-columns:1fr}
    .timeline-item {grid-template-columns:1fr;gap:8px}
    .connect-hero {padding:60px 24px}
    .connect-cards {grid-template-columns:repeat(2,1fr)}
    .testimonials {padding:40px 24px}
    .testimonials-grid {grid-template-columns:1fr}
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# === SIDEBAR ===
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-logo">JC</div>
        <p class="sidebar-name">Jason C. Chang</p>
        <p class="sidebar-title">BI Manager</p>
    </div>
    """, unsafe_allow_html=True)
    
    page = st.radio("Nav", ["Home", "Work", "About", "Connect"], label_visibility="collapsed", key="nav_radio")
    
    st.markdown("""
    <div class="sidebar-footer">
        <div class="sidebar-status">Open to opportunities</div>
    </div>
    """, unsafe_allow_html=True)

# === HOME ===
if page == "Home":
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <p class="eyebrow">BI Manager · 10+ Years</p>
            <h1 class="headline">I turn messy data into<br><span class="headline-accent">executive decisions</span></h1>
            <p class="subhead">I help companies find the revenue hiding in their data. From startup to Fortune 500 — I don't just build dashboards. I build clarity.</p>
            <div class="stats-bar">
                <div class="stat"><div class="stat-value">10+</div><div class="stat-label">Years in BI</div></div>
                <div class="stat"><div class="stat-value">$15M+</div><div class="stat-label">Revenue Impact</div></div>
                <div class="stat"><div class="stat-value">250+</div><div class="stat-label">Users Enabled</div></div>
                <div class="stat"><div class="stat-value">70%</div><div class="stat-label">Faster Decisions</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="featured-project">
        <div class="featured-label">★ Flagship Project</div>
        <h2 class="featured-title">Unified 5 Conflicting Data Sources Into a Single Source of Truth</h2>
        <p class="featured-desc">Post-merger chaos: 5 sales domains, 5 definitions of "revenue." The CFO was getting conflicting numbers at every board meeting. I had 6 weeks to fix it.</p>
        <div class="featured-metrics">
            <div><div class="featured-metric-value">9%</div><div class="featured-metric-label">Revenue Lift</div></div>
            <div><div class="featured-metric-value">70%</div><div class="featured-metric-label">Fewer Conflicts</div></div>
            <div><div class="featured-metric-value">$12M</div><div class="featured-metric-label">Annual Impact</div></div>
            <div><div class="featured-metric-value">6 wks</div><div class="featured-metric-label">Timeline</div></div>
        </div>
        <div class="featured-tags">
            <span class="featured-tag">Snowflake</span>
            <span class="featured-tag">Power BI</span>
            <span class="featured-tag">Python</span>
            <span class="featured-tag">250+ Users</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="projects-grid">
        <div class="project-card">
            <div class="project-company">Modern Home Station</div>
            <h3 class="project-title">+33% Conversion via A/B Testing & Attribution</h3>
            <p class="project-desc">Built cross-channel attribution across GA4, Shopify, Meta. Led A/B testing program optimizing marketing spend.</p>
            <div class="project-metrics">
                <div><div class="project-metric-value">+33%</div><div class="project-metric-label">Conversion</div></div>
                <div><div class="project-metric-value">-18%</div><div class="project-metric-label">CPA</div></div>
                <div><div class="project-metric-value">2x</div><div class="project-metric-label">ROAS</div></div>
            </div>
        </div>
        <div class="project-card">
            <div class="project-company">Operations Automation</div>
            <h3 class="project-title">160 Hours Saved Quarterly via Pipeline Automation</h3>
            <p class="project-desc">Replaced 47 manual Excel macros with automated Python pipelines. Error rate: 15% to 0%.</p>
            <div class="project-metrics">
                <div><div class="project-metric-value">160 hrs</div><div class="project-metric-label">Saved/Qtr</div></div>
                <div><div class="project-metric-value">99</div><div class="project-metric-label">Vendors</div></div>
                <div><div class="project-metric-value">0%</div><div class="project-metric-label">Error Rate</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote-section">
        <p class="quote-text">"Jason doesn't just build dashboards — he asks the questions that change how we think about the business."</p>
        <p class="quote-author">— VP of Sales, Advantage Solutions</p>
    </div>
    """, unsafe_allow_html=True)

# === WORK ===
elif page == "Work":
    st.markdown("""
    <div class="work-hero">
        <h1 class="work-hero-title">Selected Work</h1>
        <p class="work-hero-sub">Deep dives into problems I've solved</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="case-study">
        <div class="case-inner">
            <p class="case-number">CASE STUDY 01</p>
            <h2 class="case-title">Unified Executive Intelligence</h2>
            <p class="case-subtitle">Advantage Solutions · 6 weeks</p>
            <div class="case-results">
                <div><div class="case-result-value">9%</div><div class="case-result-label">Quarterly Revenue Lift</div></div>
                <div><div class="case-result-value">70%</div><div class="case-result-label">Fewer KPI Conflicts</div></div>
                <div><div class="case-result-value">5→1 day</div><div class="case-result-label">Decision Cycle</div></div>
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
                <p><strong>Week 1-2:</strong> Discovery. Asked: "What decision are you trying to make?" Found 70% of "must-have" metrics weren't used.</p>
                <p><strong>Week 3:</strong> Recommended forcing standardization now.</p>
                <p><strong>Week 4-5:</strong> Built unified Snowflake schema with 12 golden metrics.</p>
                <p><strong>Week 6:</strong> Trained 250 users. Killed old reports.</p>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">What Went Wrong</h3>
                <p>APAC had an undocumented custom field — their numbers broke Day 1. Had to patch live while regional VP was on a CEO call.</p>
            </div>
            <div class="case-quote">
                <p>"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
                <cite>— CFO, Advantage Solutions</cite>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="case-study">
        <div class="case-inner">
            <p class="case-number">CASE STUDY 02</p>
            <h2 class="case-title">+33% Conversion Through A/B Testing</h2>
            <p class="case-subtitle">Modern Home Station · Cross-Channel Analytics</p>
            <div class="case-results">
                <div><div class="case-result-value">+33%</div><div class="case-result-label">Conversion Rate</div></div>
                <div><div class="case-result-value">-18%</div><div class="case-result-label">CPA Reduction</div></div>
                <div><div class="case-result-value">2x</div><div class="case-result-label">ROAS</div></div>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>Marketing sending same promotion to everyone. Data scattered across Facebook, Shopify, Google Analytics with no unified customer view.</p>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Applied 7-layer data framework: Business requirements → Data cleaning → Exploratory analysis → K-Means segmentation → Validation → Time series → Integration.</p>
                <p>Built cross-channel attribution integrating GA4, Shopify, Meta, Klaviyo. Led multivariate testing across 12 ad combinations.</p>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">Results</h3>
                <ul>
                    <li>Value-based ads beat feature-based by 33% (p=0.03)</li>
                    <li>Best combo: Meme #2 + Learn More CTA + Comment prompt</li>
                    <li>36% lower CPM with engagement-driven strategies</li>
                </ul>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">What Went Wrong</h3>
                <p>Saw spike in content views but no page views. Spent days debugging — mobile video sound settings were wrong, causing users to scroll past.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="case-study">
        <div class="case-inner">
            <p class="case-number">CASE STUDY 03</p>
            <h2 class="case-title">160 Hours Saved via Automation</h2>
            <p class="case-subtitle">99 Vendor Data Sources · Python + SQL</p>
            <div class="case-results">
                <div><div class="case-result-value">160 hrs</div><div class="case-result-label">Saved Quarterly</div></div>
                <div><div class="case-result-value">15%→0%</div><div class="case-result-label">Error Rate</div></div>
                <div><div class="case-result-value">99</div><div class="case-result-label">Vendors</div></div>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>"Automation" meant 47 Excel macros that one person (who left) understood. Every Monday, 3 analysts spent 4 hours manually processing vendor reports. Error rate: 15%.</p>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Built dynamic column mapping in Python. Created vendor normalization buckets aligned with GL codes. Combined Python + VBA for hybrid automation. Parallel ran for a week before cutover.</p>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">What Went Wrong</h3>
                <p>One vendor only sent PDF reports with inconsistent formatting — spent 2 days building a custom parser. Three vendors reported in different timezones — took a week to standardize.</p>
            </div>
            <div class="case-quote">
                <p>"Finance finally trusts the 'automated' reports. That hasn't happened in years."</p>
                <cite>— VP of Finance, Advantage Solutions</cite>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === ABOUT ===
elif page == "About":
    st.markdown("""
    <div class="about-hero">
        <div class="about-photo">JC</div>
        <div class="about-intro">
            <h1>Hi, I'm Jason.</h1>
            <p>I've spent the last decade helping companies <strong>stop guessing and start knowing</strong>.</p>
            <p>Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers.</p>
            <p>I've done this at Advantage Solutions, Modern Home Station, China Unicom, and Marshall Electronics.</p>
            <p><strong>What I've learned:</strong> The hard part is never the SQL. It's getting humans to agree on what "revenue" means.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-section">
        <h2 class="section-title">Experience</h2>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-year">2021 — Present</div>
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
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-section">
        <h2 class="section-title">Education</h2>
        <div class="timeline">
            <div class="timeline-item" style="border-bottom:none">
                <div class="timeline-year">2010</div>
                <div class="timeline-content">
                    <p class="timeline-role">B.S. Business Administration</p>
                    <p class="timeline-company">University of California, Riverside</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
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
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-section">
        <h2 class="section-title">Certifications</h2>
        <div class="cert-grid">
            <div class="cert-card">
                <p class="cert-name">Supervised Machine Learning</p>
                <p class="cert-issuer">Stanford Online · 2024</p>
            </div>
            <div class="cert-card">
                <p class="cert-name">Neural Networks & Deep Learning</p>
                <p class="cert-issuer">DeepLearning.AI · 2024</p>
            </div>
            <div class="cert-card">
                <p class="cert-name">Power BI Data Visualization</p>
                <p class="cert-issuer">edX · 2019</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === CONNECT ===
elif page == "Connect":
    st.markdown("""
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
                <div class="connect-card-value"><a href="https://linkedin.com/in/jchang0102" target="_blank">linkedin.com/in/jchang0102</a></div>
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
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="testimonials">
        <h2 class="section-title" style="text-align:center;margin-bottom:40px">What Colleagues Say</h2>
        <div class="testimonials-grid">
            <div class="testimonial-card">
                <p class="testimonial-quote">"Jason has a rare ability to translate complex data into stories that executives actually act on. He doesn't just answer questions — he asks better ones."</p>
                <p class="testimonial-author">Former VP of Sales</p>
                <p class="testimonial-role">Advantage Solutions</p>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-quote">"Most analysts give you data. Jason gives you decisions. He made our CEO actually look forward to reviewing dashboards."</p>
                <p class="testimonial-author">Former Director of Operations</p>
                <p class="testimonial-role">Modern Home Station</p>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-quote">"I've worked with a lot of BI people. Jason is the first one who understood that data without context is just noise."</p>
                <p class="testimonial-author">Former CFO</p>
                <p class="testimonial-role">China Unicom America</p>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-quote">"Jason doesn't just build dashboards — he changes how teams think about measurement. That's rare."</p>
                <p class="testimonial-author">Senior Product Manager</p>
                <p class="testimonial-role">Advantage Solutions</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
