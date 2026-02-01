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
    SIDEBAR_WIDTH: int = 280
    
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
    /* Refined neutral palette */
    --bg: #f8f9fa;
    --bg-subtle: #f1f3f4;
    --fg: #1a1a2e;
    --fg-secondary: #2d3436;
    --muted: #636e72;
    --muted-light: #b2bec3;
    --border: #dfe6e9;
    --border-light: #ecf0f1;
    
    /* Professional accent - deep teal/navy */
    --accent: #0a3d62;
    --accent-hover: #1e5f74;
    --accent-light: #e8f4f8;
    --accent-glow: rgba(10, 61, 98, 0.12);
    
    /* Secondary accent - warm gold */
    --gold: #b8860b;
    --gold-light: #fef9e7;
    
    /* Surfaces */
    --surface: #ffffff;
    --surface-elevated: #ffffff;
    --surface-hover: #fafbfc;
    
    /* Dark mode sidebar */
    --dark: #1a1a2e;
    --dark-secondary: #16213e;
    --dark-muted: #a4b0be;
    --dark-border: rgba(255,255,255,0.08);
    
    /* Typography */
    --font-display: 'Outfit', sans-serif;
    --font-body: 'Source Sans 3', sans-serif;
    --font-accent: 'Playfair Display', serif;
    --font-mono: 'JetBrains Mono', monospace;
    
    /* Spacing */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 32px;
    --space-2xl: 48px;
    --space-3xl: 64px;
    
    /* Radius */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;
    --radius-2xl: 24px;
    
    /* Shadows - layered depth */
    --shadow-xs: 0 1px 2px rgba(0,0,0,0.04);
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.06);
    --shadow-lg: 0 10px 15px rgba(0,0,0,0.04), 0 4px 6px rgba(0,0,0,0.06);
    --shadow-xl: 0 20px 25px rgba(0,0,0,0.06), 0 10px 10px rgba(0,0,0,0.04);
    --shadow-glow: 0 0 40px var(--accent-glow);
    
    /* Transitions */
    --ease-out: cubic-bezier(0.25, 0.46, 0.45, 0.94);
    --ease-in-out: cubic-bezier(0.645, 0.045, 0.355, 1);
    --transition-fast: 150ms var(--ease-out);
    --transition-base: 250ms var(--ease-out);
    --transition-slow: 400ms var(--ease-in-out);
}

/* === ANIMATIONS === */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.6; }
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
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
    background: linear-gradient(180deg, var(--dark) 0%, var(--dark-secondary) 100%) !important;
    min-width: 280px !important;
    max-width: 280px !important;
    width: 280px !important;
    box-shadow: 4px 0 24px rgba(0,0,0,0.15);
}

section[data-testid="stSidebar"] > div:first-child,
[data-testid="stSidebar"] > div:first-child {
    padding: 0 !important;
    padding-bottom: 100px !important;
    background: transparent !important;
}

[data-testid="stSidebarNav"], .stSidebarNav {
    display: none !important;
}

.sidebar-brand {
    padding: var(--space-3xl) var(--space-xl) var(--space-2xl);
    border-bottom: 1px solid var(--dark-border);
    animation: fadeIn 600ms var(--ease-out);
}

.sidebar-logo {
    width: 56px;
    height: 56px;
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-display);
    font-size: 20px;
    font-weight: 700;
    color: #fff;
    margin-bottom: var(--space-lg);
    box-shadow: 0 4px 12px rgba(10, 61, 98, 0.3);
    transition: var(--transition-base);
    position: relative;
    overflow: hidden;
}

.sidebar-logo::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, transparent 50%);
    border-radius: inherit;
}

.sidebar-logo:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 8px 20px rgba(10, 61, 98, 0.4);
}

.sidebar-name {
    font-family: var(--font-display);
    font-size: 20px;
    font-weight: 600;
    color: #fff;
    margin: 0 0 4px;
    letter-spacing: -0.02em;
}

.sidebar-title {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--dark-muted);
    margin: 0;
    font-weight: 400;
}

/* === NAVIGATION === */
[data-testid="stSidebar"] .stRadio > div {
    flex-direction: column !important;
    gap: 0 !important;
    padding: var(--space-lg) 0 !important;
}

[data-testid="stSidebar"] .stRadio label > div:first-child,
[data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
    display: none !important;
}

[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] [role="radiogroup"] label {
    background: transparent !important;
    padding: 14px var(--space-xl) !important;
    margin: 2px 12px !important;
    cursor: pointer !important;
    transition: var(--transition-base) !important;
    border-left: 3px solid transparent !important;
    border-radius: 0 var(--radius-md) var(--radius-md) 0 !important;
    position: relative;
}

[data-testid="stSidebar"] .stRadio label::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 0;
    background: var(--accent);
    transition: var(--transition-base);
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.04) !important;
}

[data-testid="stSidebar"] .stRadio label:hover::before {
    width: 3px;
    opacity: 0.5;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked),
[data-testid="stSidebar"] [role="radiogroup"] label[aria-checked="true"],
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] {
    background: rgba(10, 61, 98, 0.15) !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked)::before {
    width: 3px;
    opacity: 1;
}

[data-testid="stSidebar"] .stRadio label p,
[data-testid="stSidebar"] .stRadio label span,
[data-testid="stSidebar"] [role="radiogroup"] label p,
[data-testid="stSidebar"] [role="radiogroup"] label span {
    font-family: var(--font-body) !important;
    font-size: 14px !important;
    font-weight: 400 !important;
    color: var(--dark-muted) !important;
    margin: 0 !important;
    transition: var(--transition-fast) !important;
}

[data-testid="stSidebar"] .stRadio label:hover p,
[data-testid="stSidebar"] .stRadio label:hover span {
    color: rgba(255,255,255,0.9) !important;
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
    width: 280px;
    padding: var(--space-lg) var(--space-xl);
    border-top: 1px solid var(--dark-border);
    background: linear-gradient(180deg, transparent 0%, var(--dark-secondary) 100%);
    backdrop-filter: blur(8px);
    z-index: 100;
}

.sidebar-status {
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: var(--font-body);
    font-size: 12px;
    font-weight: 500;
    color: #4ade80;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.sidebar-status::before {
    content: '';
    width: 8px;
    height: 8px;
    background: #4ade80;
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(74, 222, 128, 0.6);
    animation: pulse 2s ease-in-out infinite;
}

/* === TYPOGRAPHY === */
.eyebrow {
    font-family: var(--font-body);
    font-size: 12px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: var(--space-md);
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.eyebrow::before {
    content: '';
    width: 24px;
    height: 2px;
    background: var(--accent);
}

.headline {
    font-family: var(--font-display);
    font-size: clamp(40px, 5vw, 56px);
    font-weight: 700;
    color: var(--fg);
    line-height: 1.08;
    margin: 0 0 var(--space-lg);
    letter-spacing: -0.03em;
}

.headline-accent {
    color: var(--accent);
    position: relative;
}

.headline-accent::after {
    content: '';
    position: absolute;
    bottom: 4px;
    left: 0;
    right: 0;
    height: 8px;
    background: var(--accent-light);
    z-index: -1;
    transform: skewX(-12deg);
}

.subhead {
    font-family: var(--font-body);
    font-size: 18px;
    color: var(--muted);
    line-height: 1.7;
    max-width: 540px;
    font-weight: 400;
}

.section-title {
    font-family: var(--font-display);
    font-size: 28px;
    font-weight: 600;
    color: var(--fg);
    margin: 0 0 var(--space-xl);
    letter-spacing: -0.02em;
    position: relative;
    display: inline-block;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 40px;
    height: 3px;
    background: var(--accent);
    border-radius: 2px;
}

/* === HERO SECTION === */
.hero {
    min-height: calc(100vh - 80px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--space-3xl) 72px;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 800px;
    height: 800px;
    background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
    pointer-events: none;
}

.hero-content {
    max-width: 680px;
    animation: fadeInUp 800ms var(--ease-out);
    position: relative;
    z-index: 1;
}

.stats-bar {
    display: flex;
    gap: 56px;
    margin-top: var(--space-3xl);
    padding-top: var(--space-xl);
    border-top: 1px solid var(--border);
    animation: fadeInUp 800ms var(--ease-out) 200ms both;
}

.stat {
    position: relative;
}

.stat::after {
    content: '';
    position: absolute;
    right: -28px;
    top: 50%;
    transform: translateY(-50%);
    width: 1px;
    height: 40px;
    background: var(--border);
}

.stat:last-child::after {
    display: none;
}

.stat-value {
    font-family: var(--font-display);
    font-size: 36px;
    font-weight: 700;
    color: var(--fg);
    letter-spacing: -0.02em;
    line-height: 1;
}

.stat-label {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--muted);
    margin-top: 6px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* === FEATURED PROJECT === */
.featured-project {
    background: linear-gradient(135deg, var(--dark) 0%, var(--dark-secondary) 100%);
    border-radius: var(--radius-2xl);
    padding: var(--space-3xl);
    margin: var(--space-3xl) 72px var(--space-xl);
    color: #fff;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-xl);
    animation: fadeInUp 800ms var(--ease-out) 400ms both;
}

.featured-project::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(10, 61, 98, 0.3) 0%, transparent 70%);
    pointer-events: none;
}

.featured-project::after {
    content: '';
    position: absolute;
    bottom: -100px;
    left: -100px;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(184, 134, 11, 0.15) 0%, transparent 70%);
    pointer-events: none;
}

.featured-label {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--font-body);
    font-size: 11px;
    font-weight: 600;
    color: var(--gold);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: var(--space-lg);
    padding: 6px 14px;
    background: rgba(184, 134, 11, 0.15);
    border-radius: var(--radius-sm);
    border: 1px solid rgba(184, 134, 11, 0.3);
}

.featured-title {
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 600;
    color: #fff;
    line-height: 1.2;
    margin: 0 0 var(--space-md);
    max-width: 600px;
    letter-spacing: -0.02em;
}

.featured-desc {
    font-family: var(--font-body);
    font-size: 16px;
    color: var(--dark-muted);
    line-height: 1.7;
    max-width: 520px;
    margin-bottom: var(--space-xl);
}

.featured-metrics {
    display: flex;
    gap: 48px;
    position: relative;
    z-index: 1;
}

.featured-metric {
    position: relative;
    padding-left: 16px;
}

.featured-metric::before {
    content: '';
    position: absolute;
    left: 0;
    top: 4px;
    bottom: 4px;
    width: 3px;
    background: var(--accent);
    border-radius: 2px;
}

.featured-metric-value {
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.02em;
}

.featured-metric-label {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--dark-muted);
    margin-top: 4px;
    font-weight: 500;
}

.featured-tags {
    display: flex;
    gap: 10px;
    margin-top: var(--space-xl);
    flex-wrap: wrap;
    position: relative;
    z-index: 1;
}

.featured-tag {
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--dark-muted);
    background: rgba(255,255,255,0.06);
    padding: 8px 14px;
    border-radius: var(--radius-sm);
    border: 1px solid rgba(255,255,255,0.08);
    transition: var(--transition-fast);
}

.featured-tag:hover {
    background: rgba(255,255,255,0.1);
    border-color: rgba(255,255,255,0.15);
    color: #fff;
}

/* === PROJECT CARDS === */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-lg);
    padding: 0 72px var(--space-3xl);
}

.project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    padding: var(--space-xl);
    transition: var(--transition-base);
    position: relative;
    overflow: hidden;
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent) 0%, var(--accent-hover) 100%);
    transform: scaleX(0);
    transform-origin: left;
    transition: var(--transition-base);
}

.project-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-lg), var(--shadow-glow);
    transform: translateY(-4px);
}

.project-card:hover::before {
    transform: scaleX(1);
}

.project-company {
    font-family: var(--font-body);
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: var(--space-sm);
}

.project-title {
    font-family: var(--font-display);
    font-size: 20px;
    font-weight: 600;
    color: var(--fg);
    line-height: 1.3;
    margin: 0 0 var(--space-sm);
    letter-spacing: -0.01em;
}

.project-desc {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--muted);
    line-height: 1.65;
    margin-bottom: var(--space-lg);
}

.project-metrics {
    display: flex;
    gap: var(--space-lg);
    padding-top: var(--space-md);
    border-top: 1px solid var(--border-light);
}

.project-metric-value {
    font-family: var(--font-display);
    font-size: 20px;
    font-weight: 700;
    color: var(--fg);
    letter-spacing: -0.01em;
}

.project-metric-label {
    font-family: var(--font-body);
    font-size: 11px;
    color: var(--muted);
    font-weight: 500;
}

/* === QUOTE SECTION === */
.quote-section {
    background: linear-gradient(135deg, var(--accent-light) 0%, #fff 100%);
    padding: var(--space-3xl);
    margin: 0 72px var(--space-3xl);
    border-radius: var(--radius-2xl);
    text-align: center;
    position: relative;
    border: 1px solid var(--border);
}

.quote-section::before {
    content: '"';
    position: absolute;
    top: 24px;
    left: 40px;
    font-family: var(--font-accent);
    font-size: 120px;
    color: var(--accent);
    opacity: 0.1;
    line-height: 1;
}

.quote-text {
    font-family: var(--font-accent);
    font-size: 26px;
    font-style: italic;
    color: var(--fg);
    line-height: 1.5;
    max-width: 640px;
    margin: 0 auto var(--space-lg);
    position: relative;
    z-index: 1;
}

.quote-author {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--muted);
    font-weight: 500;
}

/* === WORK PAGE === */
.work-hero {
    background: linear-gradient(135deg, var(--dark) 0%, var(--dark-secondary) 100%);
    padding: 100px 72px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.work-hero::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(10, 61, 98, 0.2) 0%, transparent 70%);
    pointer-events: none;
}

.work-hero-title {
    font-family: var(--font-display);
    font-size: 48px;
    font-weight: 700;
    color: #fff;
    margin: 0 0 12px;
    letter-spacing: -0.03em;
    position: relative;
    z-index: 1;
}

.work-hero-sub {
    font-family: var(--font-body);
    font-size: 16px;
    color: var(--dark-muted);
    position: relative;
    z-index: 1;
}

/* === CASE STUDIES === */
.case-study {
    padding: var(--space-3xl) 72px;
    border-bottom: 1px solid var(--border);
    transition: var(--transition-slow);
}

.case-study:hover {
    background: var(--surface-hover);
}

.case-study:nth-child(even) {
    background: var(--surface);
}

.case-inner {
    max-width: 760px;
    margin: 0 auto;
}

.case-number {
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 2px;
    margin-bottom: var(--space-md);
}

.case-title {
    font-family: var(--font-display);
    font-size: 36px;
    font-weight: 700;
    color: var(--fg);
    line-height: 1.15;
    margin: 0 0 8px;
    letter-spacing: -0.02em;
}

.case-subtitle {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--muted);
    margin-bottom: var(--space-xl);
}

.case-results {
    background: linear-gradient(135deg, var(--dark) 0%, var(--dark-secondary) 100%);
    border-radius: var(--radius-xl);
    padding: var(--space-xl);
    margin-bottom: var(--space-2xl);
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-lg);
    text-align: center;
    box-shadow: var(--shadow-lg);
}

.case-result-value {
    font-family: var(--font-display);
    font-size: 36px;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.02em;
}

.case-result-label {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--dark-muted);
    margin-top: 4px;
    font-weight: 500;
}

.case-section {
    margin-bottom: var(--space-xl);
}

.case-section-title {
    font-family: var(--font-display);
    font-size: 18px;
    font-weight: 600;
    color: var(--fg);
    margin-bottom: var(--space-md);
    display: flex;
    align-items: center;
    gap: 12px;
}

.case-section-title::before {
    content: '';
    width: 4px;
    height: 20px;
    background: linear-gradient(180deg, var(--accent) 0%, var(--accent-hover) 100%);
    border-radius: 2px;
}

.case-section p {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--muted);
    line-height: 1.8;
    margin: 0 0 var(--space-md);
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
    padding-left: 24px;
    position: relative;
}

.case-section li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: var(--accent);
    font-weight: 600;
}

.case-quote {
    background: linear-gradient(135deg, var(--accent-light) 0%, #fff 100%);
    border-radius: var(--radius-lg);
    padding: var(--space-lg) var(--space-xl);
    margin: var(--space-xl) 0;
    border-left: 4px solid var(--accent);
}

.case-quote p {
    font-family: var(--font-accent);
    font-size: 17px;
    font-style: italic;
    color: var(--fg);
    line-height: 1.6;
    margin: 0;
}

.case-quote cite {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
    font-style: normal;
    display: block;
    margin-top: var(--space-md);
    font-weight: 500;
}

/* === ABOUT PAGE === */
.about-hero {
    display: grid;
    grid-template-columns: 240px 1fr;
    gap: var(--space-3xl);
    padding: var(--space-3xl) 72px;
    align-items: start;
}

.about-photo {
    width: 220px;
    height: 220px;
    background: linear-gradient(135deg, var(--border) 0%, var(--muted-light) 100%);
    border-radius: var(--radius-xl);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
    text-align: center;
    border: 4px solid var(--surface);
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
}

.about-photo::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.3) 0%, transparent 50%);
}

.about-intro h1 {
    font-family: var(--font-display);
    font-size: 40px;
    font-weight: 700;
    color: var(--fg);
    margin: 0 0 var(--space-lg);
    letter-spacing: -0.02em;
}

.about-intro p {
    font-family: var(--font-body);
    font-size: 17px;
    color: var(--muted);
    line-height: 1.8;
    margin: 0 0 var(--space-md);
}

.about-section {
    padding: var(--space-2xl) 72px;
    border-top: 1px solid var(--border);
}

.about-section:nth-child(even) {
    background: var(--surface);
}

/* === TIMELINE === */
.timeline {
    max-width: 680px;
    position: relative;
    padding-left: var(--space-lg);
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 8px;
    bottom: 8px;
    width: 2px;
    background: linear-gradient(180deg, var(--accent) 0%, var(--border) 100%);
}

.timeline-item {
    padding: var(--space-lg) 0;
    border-bottom: 1px solid var(--border-light);
    display: grid;
    grid-template-columns: 140px 1fr;
    gap: var(--space-lg);
    position: relative;
    transition: var(--transition-base);
}

.timeline-item:hover {
    background: var(--surface-hover);
    margin: 0 -var(--space-md);
    padding-left: var(--space-md);
    padding-right: var(--space-md);
    border-radius: var(--radius-md);
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -24px;
    top: 28px;
    width: 12px;
    height: 12px;
    background: var(--surface);
    border: 3px solid var(--accent);
    border-radius: 50%;
    transition: var(--transition-fast);
}

.timeline-item:hover::before {
    background: var(--accent);
    transform: scale(1.2);
}

.timeline-item:last-child {
    border-bottom: none;
}

.timeline-year {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 500;
    color: var(--accent);
}

.timeline-role {
    font-family: var(--font-display);
    font-size: 17px;
    font-weight: 600;
    color: var(--fg);
    margin: 0 0 4px;
}

.timeline-company {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--muted);
}

.timeline-desc {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--muted);
    line-height: 1.65;
    margin-top: var(--space-sm);
}

/* === SKILLS === */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-lg);
    max-width: 860px;
}

.skill-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: var(--space-lg);
    transition: var(--transition-base);
    position: relative;
    overflow: hidden;
}

.skill-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent) 0%, var(--accent-hover) 100%);
    transform: scaleX(0);
    transform-origin: left;
    transition: var(--transition-base);
}

.skill-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-md), 0 0 20px var(--accent-glow);
    transform: translateY(-2px);
}

.skill-card:hover::before {
    transform: scaleX(1);
}

.skill-card-title {
    font-family: var(--font-body);
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: var(--space-md);
}

.skill-card-list {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--fg);
    line-height: 2.2;
}

/* === CERTIFICATIONS === */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-md);
    max-width: 860px;
}

.cert-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: var(--space-lg);
    transition: var(--transition-base);
}

.cert-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-sm);
    transform: translateY(-2px);
}

.cert-name {
    font-family: var(--font-body);
    font-size: 15px;
    font-weight: 600;
    color: var(--fg);
    margin-bottom: 4px;
}

.cert-issuer {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
}

/* === CONNECT PAGE === */
.connect-hero {
    background: linear-gradient(135deg, var(--dark) 0%, var(--dark-secondary) 100%);
    padding: 100px 72px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.connect-hero::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 800px;
    height: 800px;
    background: radial-gradient(circle, rgba(10, 61, 98, 0.2) 0%, transparent 60%);
    pointer-events: none;
}

.connect-hero h1 {
    font-family: var(--font-display);
    font-size: 48px;
    font-weight: 700;
    color: #fff;
    margin: 0 0 var(--space-md);
    letter-spacing: -0.03em;
    position: relative;
    z-index: 1;
}

.connect-hero p {
    font-family: var(--font-body);
    font-size: 17px;
    color: var(--dark-muted);
    max-width: 480px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.connect-cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-md);
    max-width: 880px;
    margin: var(--space-2xl) auto 0;
    position: relative;
    z-index: 1;
}

.connect-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: var(--radius-lg);
    padding: var(--space-lg) var(--space-md);
    text-align: center;
    transition: var(--transition-base);
    position: relative;
    overflow: hidden;
}

.connect-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(10, 61, 98, 0.1) 0%, transparent 100%);
    opacity: 0;
    transition: var(--transition-base);
}

.connect-card:hover {
    background: rgba(255,255,255,0.06);
    border-color: var(--accent);
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.2);
}

.connect-card:hover::before {
    opacity: 1;
}

.connect-card-icon {
    font-size: 24px;
    margin-bottom: var(--space-sm);
    position: relative;
    z-index: 1;
}

.connect-card-label {
    font-family: var(--font-body);
    font-size: 10px;
    color: var(--dark-muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 6px;
    font-weight: 600;
    position: relative;
    z-index: 1;
}

.connect-card-value {
    font-family: var(--font-body);
    font-size: 13px;
    color: #fff;
    word-break: break-all;
    position: relative;
    z-index: 1;
}

.connect-card-value a {
    color: var(--accent-hover);
    text-decoration: none;
    transition: var(--transition-fast);
}

.connect-card-value a:hover {
    color: #fff;
}

/* === TESTIMONIALS === */
.testimonials {
    padding: var(--space-3xl) 72px;
}

.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-lg);
    max-width: 960px;
    margin: 0 auto;
}

.testimonial-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    padding: var(--space-xl);
    transition: var(--transition-base);
    position: relative;
}

.testimonial-card::before {
    content: '"';
    position: absolute;
    top: 16px;
    right: 24px;
    font-family: var(--font-accent);
    font-size: 64px;
    color: var(--accent);
    opacity: 0.1;
    line-height: 1;
}

.testimonial-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
}

.testimonial-quote {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--muted);
    line-height: 1.75;
    font-style: italic;
    margin-bottom: var(--space-md);
    position: relative;
    z-index: 1;
}

.testimonial-author {
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 600;
    color: var(--fg);
}

.testimonial-role {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--muted);
    margin-top: 2px;
}

/* === BUTTON OVERRIDES === */
.stButton > button {
    font-family: var(--font-body) !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
    border-radius: var(--radius-md) !important;
    transition: var(--transition-base) !important;
    letter-spacing: 0.3px !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-md) !important;
}

/* === RESPONSIVE === */
@media (max-width: 1024px) {
    .hero { padding: var(--space-2xl) var(--space-xl); }
    .featured-project { margin: var(--space-2xl) var(--space-xl); padding: var(--space-xl); }
    .projects-grid { padding: 0 var(--space-xl) var(--space-2xl); }
    .quote-section { margin: 0 var(--space-xl) var(--space-2xl); padding: var(--space-xl); }
    .case-study { padding: var(--space-2xl) var(--space-xl); }
    .about-section { padding: var(--space-xl); }
    .work-hero, .connect-hero { padding: var(--space-3xl) var(--space-xl); }
    .testimonials { padding: var(--space-2xl) var(--space-xl); }
}

@media (max-width: 768px) {
    .hero { padding: var(--space-xl); min-height: auto; }
    .stats-bar { flex-wrap: wrap; gap: var(--space-lg) var(--space-2xl); }
    .stat::after { display: none; }
    .featured-project { margin: var(--space-xl); padding: var(--space-lg); }
    .featured-metrics { flex-wrap: wrap; gap: var(--space-lg); }
    .projects-grid { grid-template-columns: 1fr; padding: 0 var(--space-xl) var(--space-xl); }
    .quote-section { margin: 0 var(--space-xl) var(--space-xl); padding: var(--space-lg); }
    .quote-text { font-size: 20px; }
    .case-study { padding: var(--space-xl); }
    .case-results { grid-template-columns: 1fr; }
    .about-hero { grid-template-columns: 1fr; gap: var(--space-xl); padding: var(--space-xl); }
    .about-section { padding: var(--space-xl); }
    .skills-grid, .cert-grid { grid-template-columns: 1fr; }
    .timeline-item { grid-template-columns: 1fr; gap: var(--space-sm); }
    .work-hero, .connect-hero { padding: var(--space-2xl) var(--space-xl); }
    .work-hero-title, .connect-hero h1 { font-size: 36px; }
    .connect-cards { grid-template-columns: repeat(2, 1fr); }
    .testimonials { padding: var(--space-xl); }
    .testimonials-grid { grid-template-columns: 1fr; }
}
</style>
<link href='https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Source+Sans+3:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap' rel='stylesheet'>
"""

# =============================================================================
# COMPONENT HELPERS
# =============================================================================

def render_stat(value: str, label: str) -> str:
    return f'<div class="stat"><div class="stat-value">{value}</div><div class="stat-label">{label}</div></div>'

def render_metric(value: str, label: str, prefix: str = "project") -> str:
    if prefix == "featured":
        return f'<div class="featured-metric"><div class="featured-metric-value">{value}</div><div class="featured-metric-label">{label}</div></div>'
    return f'<div><div class="{prefix}-metric-value">{value}</div><div class="{prefix}-metric-label">{label}</div></div>'

def render_tag(text: str) -> str:
    return f'<span class="featured-tag">{text}</span>'

def render_timeline_item(years: str, role: str, company: str, desc: Optional[str] = None, last: bool = False) -> str:
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
    skills_html = '<br>'.join(skills)
    return f'''
    <div class="skill-card">
        <div class="skill-card-title">{title}</div>
        <div class="skill-card-list">{skills_html}</div>
    </div>'''

def render_cert_card(name: str, issuer: str) -> str:
    return f'''
    <div class="cert-card">
        <p class="cert-name">{name}</p>
        <p class="cert-issuer">{issuer}</p>
    </div>'''

def render_testimonial(quote: str, author: str, role: str) -> str:
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
    
    stats = [("10+", "Years in BI"), ("$15M+", "Revenue Impact"), ("250+", "Users Enabled"), ("70%", "Faster Decisions")]
    stats_html = ''.join(render_stat(v, l) for v, l in stats)
    
    st.markdown(f'<div style="padding:0 72px"><div class="stats-bar">{stats_html}</div></div>', unsafe_allow_html=True)
    
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
                <cite>— CFO</cite>
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
                <cite>— VP of Finance</cite>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_about():
    st.markdown(f"""
    <div class="about-hero">
        <div class="about-photo">Your Photo<br>220×220</div>
        <div class="about-intro">
            <h1>Hi, I'm Jason.</h1>
            <p>I've spent the last decade helping companies <strong>stop guessing and start knowing</strong>.</p>
            <p>Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers.</p>
            <p>I've done this at Advantage Solutions, Modern Home Station, China Unicom, and Marshall Electronics.</p>
            <p><strong>What I've learned:</strong> The hard part is never the SQL. It's getting humans to agree on what "revenue" means.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Education</h2>
        <div class="timeline">
            {render_timeline_item("2010", "B.S. Business Administration", "University of California, Riverside", last=True)}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
        <h2 class="section-title" style="text-align:center;margin-bottom:40px;display:block;">What Colleagues Say</h2>
        <div class="testimonials-grid">{testimonials_html}</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN APP
# =============================================================================

def main():
    st.set_page_config(
        layout="wide",
        page_title=CONFIG.PAGE_TITLE,
        page_icon=CONFIG.PAGE_ICON,
        initial_sidebar_state="expanded"
    )
    
    st.markdown(get_css(), unsafe_allow_html=True)
    
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
    
    page_routes = {
        "Home": render_home,
        "Work": render_work,
        "About": render_about,
        "Connect": render_connect,
    }
    
    page_routes.get(page, render_home)()


if __name__ == "__main__":
    main()
