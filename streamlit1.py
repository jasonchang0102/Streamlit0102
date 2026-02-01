"""
Jason C. Chang | BI Manager Portfolio
======================================
A professional portfolio built with Streamlit showcasing BI expertise.
"""

import streamlit as st
from dataclasses import dataclass
from typing import Optional

# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass(frozen=True)
class Config:
    """Application configuration constants."""
    PAGE_TITLE: str = "Jason C. Chang | BI Manager"
    PAGE_ICON: str = "◆"
    SIDEBAR_WIDTH: int = 260
    
    # Personal Info
    NAME: str = "Jason C. Chang"
    INITIALS: str = "JC"
    TITLE: str = "BI Manager"
    EMAIL: str = "jason.chang01022024@gmail.com"
    PHONE: str = "(626) 203-3319"
    LINKEDIN: str = "linkedin.com/in/jchang0102"
    LINKEDIN_URL: str = "https://linkedin.com/in/jchang0102"
    LOCATION: str = "Hacienda Heights, CA"
    
    # Navigation
    PAGES: tuple = ("Home", "Work", "About", "Connect")

CONFIG = Config()

# =============================================================================
# STYLES
# =============================================================================

def get_css() -> str:
    """Return the complete CSS stylesheet."""
    return """
<style>
/* === DESIGN TOKENS === */
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
    
    --font-display: 'Space Grotesk', sans-serif;
    --font-body: 'Inter', sans-serif;
    --font-accent: 'Fraunces', serif;
    
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
    --radius-xl: 20px;
    
    --shadow-sm: 0 4px 16px rgba(0,0,0,0.04);
    --shadow-md: 0 8px 24px rgba(0,0,0,0.06);
    --shadow-lg: 0 12px 32px rgba(0,0,0,0.08);
    
    --transition: all 0.2s ease;
}

/* === RESET & BASE === */
.stApp, [data-testid="stAppViewContainer"], .main {
    background: var(--bg) !important;
}

#MainMenu, footer, header, .stDeployButton, 
div[data-testid="stDecoration"], 
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* === SIDEBAR === */
section[data-testid="stSidebar"],
[data-testid="stSidebar"] {
    background: var(--dark) !important;
    min-width: 260px !important;
    max-width: 260px !important;
    width: 260px !important;
}

section[data-testid="stSidebar"] > div:first-child,
[data-testid="stSidebar"] > div:first-child {
    padding: 0 !important;
    padding-bottom: 80px !important;
    background: var(--dark) !important;
}

[data-testid="stSidebarNav"], .stSidebarNav {
    display: none !important;
}

.sidebar-brand {
    padding: 48px 32px 40px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}

.sidebar-logo {
    width: 44px;
    height: 44px;
    background: var(--accent);
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-display);
    font-size: 18px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 16px;
}

.sidebar-name {
    font-family: var(--font-display);
    font-size: 18px;
    font-weight: 600;
    color: #fff;
    margin: 0 0 2px;
}

.sidebar-title {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--dark-muted);
    margin: 0;
}

/* === NAVIGATION RADIO BUTTONS === */
[data-testid="stSidebar"] .stRadio > div {
    flex-direction: column !important;
    gap: 0 !important;
    padding: 16px 0 !important;
}

[data-testid="stSidebar"] .stRadio label > div:first-child,
[data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
    display: none !important;
}

[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] [role="radiogroup"] label {
    background: transparent !important;
    padding: 12px 32px !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: var(--transition) !important;
    border-left: 2px solid transparent !important;
    border-radius: 0 !important;
}

[data-testid="stSidebar"] .stRadio label:hover,
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.03) !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked),
[data-testid="stSidebar"] [role="radiogroup"] label[aria-checked="true"],
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] {
    background: rgba(255,255,255,0.05) !important;
    border-left-color: var(--accent) !important;
}

[data-testid="stSidebar"] .stRadio label p,
[data-testid="stSidebar"] .stRadio label span,
[data-testid="stSidebar"] [role="radiogroup"] label p,
[data-testid="stSidebar"] [role="radiogroup"] label span {
    font-family: var(--font-body) !important;
    font-size: 13px !important;
    font-weight: 400 !important;
    color: var(--dark-muted) !important;
    margin: 0 !important;
}

[data-testid="stSidebar"] .stRadio label:hover p,
[data-testid="stSidebar"] .stRadio label:hover span {
    color: rgba(255,255,255,0.8) !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked) p,
[data-testid="stSidebar"] .stRadio label:has(input:checked) span,
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] p,
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] span {
    color: #fff !important;
    font-weight: 500 !important;
}

/* === SIDEBAR FOOTER === */
.sidebar-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 260px;
    padding: 20px 32px;
    border-top: 1px solid rgba(255,255,255,0.06);
    background: var(--dark);
    z-index: 100;
}

.sidebar-status {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: var(--font-body);
    font-size: 11px;
    color: var(--accent);
}

.sidebar-status::before {
    content: '';
    width: 6px;
    height: 6px;
    background: var(--accent);
    border-radius: 50%;
}

/* === TYPOGRAPHY === */
.eyebrow {
    font-family: var(--font-body);
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.headline {
    font-family: var(--font-display);
    font-size: clamp(36px, 4.5vw, 52px);
    font-weight: 700;
    color: var(--fg);
    line-height: 1.1;
    margin: 0 0 20px;
}

.headline-accent { color: var(--accent); }

.subhead {
    font-family: var(--font-body);
    font-size: 17px;
    color: var(--muted);
    line-height: 1.7;
    max-width: 520px;
}

.section-title {
    font-family: var(--font-display);
    font-size: 28px;
    font-weight: 600;
    color: var(--fg);
    margin: 0 0 32px;
}

/* === HERO SECTION === */
.hero {
    min-height: calc(100vh - 100px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 48px 60px;
}

.hero-content { max-width: 640px; }

.stats-bar {
    display: flex;
    gap: 48px;
    margin-top: 48px;
    padding-top: 32px;
    border-top: 1px solid var(--border);
}

.stat-value {
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 700;
    color: var(--fg);
}

.stat-label {
    font-family: var(--font-body);
    font-size: 11px;
    color: var(--muted);
    margin-top: 2px;
}

/* === FEATURED PROJECT === */
.featured-project {
    background: var(--dark);
    border-radius: var(--radius-xl);
    padding: 48px;
    margin: 60px 60px 32px;
    color: #fff;
    position: relative;
    overflow: hidden;
}

.featured-label {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: var(--font-body);
    font-size: 10px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.featured-title {
    font-family: var(--font-display);
    font-size: 28px;
    font-weight: 600;
    color: #fff;
    line-height: 1.25;
    margin: 0 0 12px;
    max-width: 560px;
}

.featured-desc {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--dark-muted);
    line-height: 1.7;
    max-width: 480px;
    margin-bottom: 32px;
}

.featured-metrics { display: flex; gap: 40px; }

.featured-metric-value {
    font-family: var(--font-display);
    font-size: 28px;
    font-weight: 700;
    color: #fff;
}

.featured-metric-label {
    font-family: var(--font-body);
    font-size: 11px;
    color: var(--dark-muted);
    margin-top: 2px;
}

.featured-tags {
    display: flex;
    gap: 8px;
    margin-top: 32px;
    flex-wrap: wrap;
}

.featured-tag {
    font-family: var(--font-body);
    font-size: 11px;
    color: var(--dark-muted);
    background: rgba(255,255,255,0.08);
    padding: 6px 12px;
    border-radius: 4px;
}

/* === PROJECT CARDS === */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 0 60px 60px;
}

.project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 28px;
    transition: var(--transition);
}

.project-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-lg);
    transform: translateY(-3px);
}

.project-company {
    font-family: var(--font-body);
    font-size: 10px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.project-title {
    font-family: var(--font-display);
    font-size: 18px;
    font-weight: 600;
    color: var(--fg);
    line-height: 1.3;
    margin: 0 0 10px;
}

.project-desc {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
    line-height: 1.6;
    margin-bottom: 20px;
}

.project-metrics {
    display: flex;
    gap: 20px;
    padding-top: 16px;
    border-top: 1px solid var(--border);
}

.project-metric-value {
    font-family: var(--font-display);
    font-size: 18px;
    font-weight: 700;
    color: var(--fg);
}

.project-metric-label {
    font-family: var(--font-body);
    font-size: 10px;
    color: var(--muted);
}

/* === QUOTE SECTION === */
.quote-section {
    background: var(--accent-light);
    padding: 60px;
    margin: 0 60px 60px;
    border-radius: var(--radius-xl);
    text-align: center;
}

.quote-text {
    font-family: var(--font-accent);
    font-size: 24px;
    font-style: italic;
    color: var(--fg);
    line-height: 1.5;
    max-width: 600px;
    margin: 0 auto 20px;
}

.quote-author {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
}

/* === WORK PAGE === */
.work-hero {
    background: var(--dark);
    padding: 80px 60px;
    text-align: center;
}

.work-hero-title {
    font-family: var(--font-display);
    font-size: 42px;
    font-weight: 700;
    color: #fff;
    margin: 0 0 8px;
}

.work-hero-sub {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--dark-muted);
}

/* === CASE STUDIES === */
.case-study {
    padding: 60px;
    border-bottom: 1px solid var(--border);
}

.case-study:nth-child(even) { background: var(--surface); }

.case-inner { max-width: 720px; margin: 0 auto; }

.case-number {
    font-family: var(--font-body);
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.case-title {
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 700;
    color: var(--fg);
    line-height: 1.2;
    margin: 0 0 6px;
}

.case-subtitle {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--muted);
    margin-bottom: 32px;
}

.case-results {
    background: var(--dark);
    border-radius: var(--radius-lg);
    padding: 32px;
    margin-bottom: 40px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    text-align: center;
}

.case-result-value {
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 700;
    color: #fff;
}

.case-result-label {
    font-family: var(--font-body);
    font-size: 11px;
    color: var(--dark-muted);
    margin-top: 2px;
}

.case-section { margin-bottom: 32px; }

.case-section-title {
    font-family: var(--font-display);
    font-size: 18px;
    font-weight: 600;
    color: var(--fg);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.case-section-title::before {
    content: '';
    width: 3px;
    height: 18px;
    background: var(--accent);
    border-radius: 2px;
}

.case-section p {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--muted);
    line-height: 1.8;
    margin: 0 0 12px;
}

.case-section ul {
    margin: 0;
    padding-left: 0;
    list-style: none;
}

.case-section li {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--muted);
    line-height: 1.8;
    margin-bottom: 8px;
    padding-left: 18px;
    position: relative;
}

.case-quote {
    background: var(--accent-light);
    border-radius: var(--radius-md);
    padding: 24px 28px;
    margin: 32px 0;
}

.case-quote p {
    font-family: var(--font-accent);
    font-size: 16px;
    font-style: italic;
    color: var(--fg);
    line-height: 1.6;
    margin: 0;
}

.case-quote cite {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--muted);
    font-style: normal;
    display: block;
    margin-top: 12px;
}

/* === ABOUT PAGE === */
.about-hero {
    display: grid;
    grid-template-columns: 220px 1fr;
    gap: 48px;
    padding: 60px;
    align-items: start;
}

.about-photo {
    width: 200px;
    height: 200px;
    background: linear-gradient(135deg, var(--border) 0%, #d6d3d1 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--muted);
    text-align: center;
    border: 3px solid var(--surface);
    box-shadow: var(--shadow-md);
}

.about-intro h1 {
    font-family: var(--font-display);
    font-size: 36px;
    font-weight: 700;
    color: var(--fg);
    margin: 0 0 20px;
}

.about-intro p {
    font-family: var(--font-body);
    font-size: 16px;
    color: var(--muted);
    line-height: 1.8;
    margin: 0 0 14px;
}

.about-section {
    padding: 48px 60px;
    border-top: 1px solid var(--border);
}

.about-section:nth-child(even) { background: var(--surface); }

/* === TIMELINE === */
.timeline {
    max-width: 640px;
    position: relative;
    padding-left: 20px;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 8px;
    bottom: 8px;
    width: 2px;
    background: var(--border);
}

.timeline-item {
    padding: 20px 0;
    border-bottom: 1px solid var(--border);
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 20px;
    position: relative;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -20px;
    top: 28px;
    width: 10px;
    height: 10px;
    background: var(--surface);
    border: 2px solid var(--accent);
    border-radius: 50%;
}

.timeline-item:last-child { border-bottom: none; }

.timeline-year {
    font-family: var(--font-body);
    font-size: 12px;
    font-weight: 500;
    color: var(--accent);
}

.timeline-role {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 600;
    color: var(--fg);
    margin: 0 0 2px;
}

.timeline-company {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
}

.timeline-desc {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
    line-height: 1.6;
    margin-top: 10px;
}

/* === SKILLS === */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    max-width: 800px;
}

.skill-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 24px;
    transition: var(--transition);
}

.skill-card:hover {
    border-color: var(--accent);
    box-shadow: 0 4px 16px rgba(13,148,136,0.08);
}

.skill-card-title {
    font-family: var(--font-body);
    font-size: 10px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.skill-card-list {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--fg);
    line-height: 2;
}

/* === CERTIFICATIONS === */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    max-width: 800px;
}

.cert-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 20px;
    transition: var(--transition);
}

.cert-card:hover { border-color: var(--accent); }

.cert-name {
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 600;
    color: var(--fg);
    margin-bottom: 4px;
}

.cert-issuer {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--muted);
}

/* === CONNECT PAGE === */
.connect-hero {
    background: var(--dark);
    padding: 80px 60px;
    text-align: center;
}

.connect-hero h1 {
    font-family: var(--font-display);
    font-size: 42px;
    font-weight: 700;
    color: #fff;
    margin: 0 0 12px;
}

.connect-hero p {
    font-family: var(--font-body);
    font-size: 16px;
    color: var(--dark-muted);
    max-width: 460px;
    margin: 0 auto;
}

.connect-cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    max-width: 800px;
    margin: 48px auto 0;
}

.connect-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: var(--radius-md);
    padding: 24px 16px;
    text-align: center;
    transition: var(--transition);
}

.connect-card:hover {
    background: rgba(255,255,255,0.08);
    border-color: var(--accent);
    transform: translateY(-2px);
}

.connect-card-icon { font-size: 20px; margin-bottom: 10px; }

.connect-card-label {
    font-family: var(--font-body);
    font-size: 10px;
    color: var(--dark-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

.connect-card-value {
    font-family: var(--font-body);
    font-size: 12px;
    color: #fff;
    word-break: break-all;
}

.connect-card-value a { color: var(--accent); text-decoration: none; }
.connect-card-value a:hover { color: #fff; }

/* === TESTIMONIALS === */
.testimonials { padding: 60px; }

.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    max-width: 900px;
    margin: 0 auto;
}

.testimonial-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 28px;
    transition: var(--transition);
}

.testimonial-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-sm);
}

.testimonial-quote {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--muted);
    line-height: 1.7;
    font-style: italic;
    margin-bottom: 16px;
}

.testimonial-author {
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 600;
    color: var(--fg);
}

.testimonial-role {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--muted);
    margin-top: 2px;
}

/* === BUTTON OVERRIDES === */
.stButton > button {
    font-family: var(--font-body) !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 10px 20px !important;
    border-radius: var(--radius-sm) !important;
}

/* === RESPONSIVE === */
@media (max-width: 768px) {
    .hero { padding: 32px 24px; min-height: auto; }
    .stats-bar { flex-wrap: wrap; gap: 24px 40px; }
    .featured-project { margin: 40px 24px; padding: 32px; }
    .featured-metrics { flex-wrap: wrap; gap: 24px; }
    .projects-grid { grid-template-columns: 1fr; padding: 0 24px 40px; }
    .quote-section { margin: 0 24px 40px; padding: 40px 24px; }
    .case-study { padding: 40px 24px; }
    .about-hero { grid-template-columns: 1fr; gap: 32px; padding: 40px 24px; }
    .about-section { padding: 40px 24px; }
    .skills-grid, .cert-grid { grid-template-columns: 1fr; }
    .timeline-item { grid-template-columns: 1fr; gap: 8px; }
    .connect-hero { padding: 60px 24px; }
    .connect-cards { grid-template-columns: repeat(2, 1fr); }
    .testimonials { padding: 40px 24px; }
    .testimonials-grid { grid-template-columns: 1fr; }
}
</style>
<link href='https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=Fraunces:ital,wght@0,400;0,600;1,400&display=swap' rel='stylesheet'>
"""

# =============================================================================
# COMPONENT HELPERS
# =============================================================================

def render_stat(value: str, label: str) -> str:
    """Render a single stat item."""
    return f'<div class="stat"><div class="stat-value">{value}</div><div class="stat-label">{label}</div></div>'

def render_metric(value: str, label: str, prefix: str = "project") -> str:
    """Render a metric item for projects or featured sections."""
    return f'<div><div class="{prefix}-metric-value">{value}</div><div class="{prefix}-metric-label">{label}</div></div>'

def render_tag(text: str) -> str:
    """Render a tag element."""
    return f'<span class="featured-tag">{text}</span>'

def render_timeline_item(years: str, role: str, company: str, desc: Optional[str] = None, last: bool = False) -> str:
    """Render a timeline entry."""
    style = ' style="border-bottom:none"' if last else ''
    desc_html = f'<p class="timeline-desc">{desc}</p>' if desc else ''
    return f'''
    <div class="timeline-item"{style}>
        <div class="timeline-year">{years}</div>
        <div class="timeline-content">
            <p class="timeline-role">{role}</p>
            <p class="timeline-company">{company}</p>
            {desc_html}
        </div>
    </div>'''

def render_skill_card(title: str, skills: list[str]) -> str:
    """Render a skill category card."""
    skills_html = '<br>'.join(skills)
    return f'''
    <div class="skill-card">
        <div class="skill-card-title">{title}</div>
        <div class="skill-card-list">{skills_html}</div>
    </div>'''

def render_cert_card(name: str, issuer: str) -> str:
    """Render a certification card."""
    return f'''
    <div class="cert-card">
        <p class="cert-name">{name}</p>
        <p class="cert-issuer">{issuer}</p>
    </div>'''

def render_testimonial(quote: str, author: str, role: str) -> str:
    """Render a testimonial card."""
    return f'''
    <div class="testimonial-card">
        <p class="testimonial-quote">"{quote}"</p>
        <p class="testimonial-author">{author}</p>
        <p class="testimonial-role">{role}</p>
    </div>'''

# =============================================================================
# PAGE CONTENT
# =============================================================================

def render_home():
    """Render the Home page."""
    st.markdown(f"""
    <div class="hero">
        <div class="hero-content">
            <p class="eyebrow">{CONFIG.TITLE} · 10+ Years</p>
            <h1 class="headline">I turn messy data into<br><span class="headline-accent">executive decisions</span></h1>
            <p class="subhead">I help companies find the revenue hiding in their data. From startup to Fortune 500 — I don't just build dashboards. I build clarity.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, _ = st.columns([1.2, 1.2, 4])
    with col1:
        st.button("View My Work", type="primary")
    with col2:
        st.button("Download Resume")
    
    stats = [
        ("10+", "Years in BI"),
        ("$15M+", "Revenue Impact"),
        ("250+", "Users Enabled"),
        ("70%", "Faster Decisions"),
    ]
    stats_html = ''.join(render_stat(v, l) for v, l in stats)
    
    st.markdown(f"""
    <div style="padding:0 60px">
        <div class="stats-bar">{stats_html}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured Project
    metrics = [("9%", "Revenue Lift"), ("70%", "Fewer Conflicts"), ("$12M", "Annual Impact"), ("6 wks", "Timeline")]
    metrics_html = ''.join(render_metric(v, l, "featured") for v, l in metrics)
    tags = ["Snowflake", "Power BI", "Python", "250+ Users"]
    tags_html = ''.join(render_tag(t) for t in tags)
    
    st.markdown(f"""
    <div class="featured-project">
        <div class="featured-label">★ Flagship Project</div>
        <h2 class="featured-title">Unified 5 Conflicting Data Sources Into a Single Source of Truth</h2>
        <p class="featured-desc">Post-merger chaos: 5 sales domains, 5 definitions of "revenue." The CFO was getting conflicting numbers at every board meeting. I had 6 weeks to fix it.</p>
        <div class="featured-metrics">{metrics_html}</div>
        <div class="featured-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Cards
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
        <p class="quote-author">— VP of Sales</p>
    </div>
    """, unsafe_allow_html=True)


def render_work():
    """Render the Work page with case studies."""
    st.markdown("""
    <div class="work-hero">
        <h1 class="work-hero-title">Selected Work</h1>
        <p class="work-hero-sub">Deep dives into problems I've solved</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 1
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
                    <li>→ CFO getting 5 different revenue numbers at every board meeting</li>
                    <li>→ Field teams created 47 shadow Excel trackers</li>
                    <li>→ Previous BI lead quit mid-project</li>
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
                <cite>— CFO</cite>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 2
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
                    <li>→ Value-based ads beat feature-based by 33% (p=0.03)</li>
                    <li>→ Best combo: Meme #2 + Learn More CTA + Comment prompt</li>
                    <li>→ 36% lower CPM with engagement-driven strategies</li>
                </ul>
            </div>
            <div class="case-section">
                <h3 class="case-section-title">What Went Wrong</h3>
                <p>Saw spike in content views but no page views. Spent days debugging — mobile video sound settings were wrong, causing users to scroll past.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 3
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
                <cite>— VP of Finance</cite>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_about():
    """Render the About page."""
    st.markdown(f"""
    <div class="about-hero">
        <div class="about-photo">Your Photo<br>200×200</div>
        <div class="about-intro">
            <h1>Hi, I'm Jason.</h1>
            <p>I've spent the last decade helping companies <strong>stop guessing and start knowing</strong>.</p>
            <p>Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers.</p>
            <p>I've done this at Advantage Solutions, Modern Home Station, China Unicom, and Marshall Electronics.</p>
            <p><strong>What I've learned:</strong> The hard part is never the SQL. It's getting humans to agree on what "revenue" means.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience Timeline
    experience = [
        ("2021 — Present", "BI Manager", "Advantage Solutions", 
         "Built national Power BI ecosystem with Snowflake. Unified 5 sales domains. Automated 99+ vendor pipelines. Managed 7 regional managers."),
        ("2017 — 2021", "BI Strategy & Analytics Manager", "Modern Home Station",
         "Cross-channel attribution (GA4, Shopify, Meta). A/B testing program. Revenue: +45% FY19, +85% FY20."),
        ("2016 — 2017", "BI & Strategic Development Manager", "China Unicom America",
         "GTM pricing models. $2M+ revenue projections. Automated churn reporting."),
        ("2014 — 2016", "BI Project Analyst", "Marshall Electronics",
         "50+ product launches, $5M annual sales. 95% on-time rate."),
        ("2010 — 2014", "Senior Business Analyst", "Cadence Acoustic Ltd.",
         "Migrated Excel to SQL dashboards. Managed $500M product lines."),
    ]
    timeline_html = ''.join(render_timeline_item(*exp) for exp in experience)
    
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Experience</h2>
        <div class="timeline">{timeline_html}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Education
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Education</h2>
        <div class="timeline">
            {render_timeline_item("2010", "B.S. Business Administration", "University of California, Riverside", last=True)}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills
    skills_data = [
        ("Daily Drivers", ["SQL (10+ years)", "Power BI / DAX", "Python", "Snowflake", "Excel + VBA"]),
        ("Fluent", ["BigQuery", "GA4", "Looker", "Qlik", "Power Query"]),
        ("Statistical", ["A/B Testing", "Regression", "K-Means", "Cohort Analysis", "Forecasting"]),
    ]
    skills_html = ''.join(render_skill_card(t, s) for t, s in skills_data)
    
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Skills</h2>
        <div class="skills-grid">{skills_html}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications
    certs = [
        ("Supervised Machine Learning", "Stanford Online · 2024"),
        ("Neural Networks & Deep Learning", "DeepLearning.AI · 2024"),
        ("Power BI Data Visualization", "edX · 2019"),
    ]
    certs_html = ''.join(render_cert_card(n, i) for n, i in certs)
    
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Certifications</h2>
        <div class="cert-grid">{certs_html}</div>
    </div>
    """, unsafe_allow_html=True)


def render_connect():
    """Render the Connect page."""
    st.markdown(f"""
    <div class="connect-hero">
        <h1>Let's Talk</h1>
        <p>I'm open to Senior BI Manager and Analytics Lead roles. Best way to reach me is email.</p>
        <div class="connect-cards">
            <div class="connect-card">
                <div class="connect-card-icon">📧</div>
                <div class="connect-card-label">Email</div>
                <div class="connect-card-value"><a href="mailto:{CONFIG.EMAIL}">{CONFIG.EMAIL}</a></div>
            </div>
            <div class="connect-card">
                <div class="connect-card-icon">💼</div>
                <div class="connect-card-label">LinkedIn</div>
                <div class="connect-card-value"><a href="{CONFIG.LINKEDIN_URL}" target="_blank">{CONFIG.LINKEDIN}</a></div>
            </div>
            <div class="connect-card">
                <div class="connect-card-icon">📱</div>
                <div class="connect-card-label">Phone</div>
                <div class="connect-card-value">{CONFIG.PHONE}</div>
            </div>
            <div class="connect-card">
                <div class="connect-card-icon">📍</div>
                <div class="connect-card-label">Location</div>
                <div class="connect-card-value">{CONFIG.LOCATION}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Testimonials
    testimonials = [
        ("Jason has a rare ability to translate complex data into stories that executives actually act on. He doesn't just answer questions — he asks better ones.",
         "[Name]", "VP of Sales"),
        ("Most analysts give you data. Jason gives you decisions. He made our CEO actually look forward to reviewing dashboards.",
         "[Name]", "Director of Operations"),
        ("I've worked with a lot of BI people. Jason is the first one who understood that data without context is just noise.",
         "[Name]", "CFO"),
        ("Jason doesn't just build dashboards — he changes how teams think about measurement. That's rare.",
         "[Name]", "Product Manager"),
    ]
    testimonials_html = ''.join(render_testimonial(*t) for t in testimonials)
    
    st.markdown(f"""
    <div class="testimonials">
        <h2 class="section-title" style="text-align:center;margin-bottom:40px">What Colleagues Say</h2>
        <div class="testimonials-grid">{testimonials_html}</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN APP
# =============================================================================

def main():
    """Main application entry point."""
    # Page config
    st.set_page_config(
        layout="wide",
        page_title=CONFIG.PAGE_TITLE,
        page_icon=CONFIG.PAGE_ICON,
        initial_sidebar_state="expanded"
    )
    
    # Inject styles
    st.markdown(get_css(), unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-brand">
            <div class="sidebar-logo">{CONFIG.INITIALS}</div>
            <p class="sidebar-name">{CONFIG.NAME}</p>
            <p class="sidebar-title">{CONFIG.TITLE}</p>
        </div>
        """, unsafe_allow_html=True)
        
        page = st.radio("Nav", CONFIG.PAGES, label_visibility="collapsed")
        
        st.markdown("""
        <div class="sidebar-footer">
            <div class="sidebar-status">Open to opportunities</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Route to page
    page_routes = {
        "Home": render_home,
        "Work": render_work,
        "About": render_about,
        "Connect": render_connect,
    }
    
    page_routes.get(page, render_home)()


if __name__ == "__main__":
    main()
