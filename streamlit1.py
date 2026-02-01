"""
Jason C. Chang | BI Manager Portfolio
======================================
Nike-inspired minimalist design: black, white, gray palette.
"""

import streamlit as st
from dataclasses import dataclass
from typing import Optional

# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass(frozen=True)
class Config:
    PAGE_TITLE: str = "Jason C. Chang | BI Manager"
    PAGE_ICON: str = "◆"
    SIDEBAR_WIDTH: int = 300
    
    NAME: str = "Jason C. Chang"
    INITIALS: str = "JC"
    TITLE: str = "BI Manager"
    EMAIL: str = "jason.chang01022024@gmail.com"
    PHONE: str = "(626) 203-3319"
    LINKEDIN: str = "linkedin.com/in/jchang0102"
    LINKEDIN_URL: str = "https://linkedin.com/in/jchang0102"
    LOCATION: str = "Hacienda Heights, CA"
    
    PAGES: tuple = ("Home", "Work", "About", "Connect")

CONFIG = Config()

# =============================================================================
# NIKE-INSPIRED STYLES
# =============================================================================

def get_css() -> str:
    """
    Nike Design DNA:
    - Pure black/white/gray - stark contrast
    - Bold condensed typography, ALL CAPS headlines
    - Generous whitespace
    - Large imagery
    - Minimal, confident aesthetic
    """
    return """
<style>
/* === NIKE-INSPIRED DESIGN TOKENS === */
:root {
    /* Monochrome palette */
    --black: #000000;
    --white: #ffffff;
    --gray-100: #f5f5f5;
    --gray-200: #e5e5e5;
    --gray-300: #d4d4d4;
    --gray-400: #a3a3a3;
    --gray-500: #737373;
    --gray-600: #525252;
    --gray-700: #404040;
    --gray-800: #262626;
    --gray-900: #171717;
    
    /* Semantic colors */
    --bg: var(--white);
    --bg-alt: var(--gray-100);
    --fg: var(--black);
    --muted: var(--gray-500);
    --border: var(--gray-200);
    --surface: var(--white);
    
    /* Typography - Nike uses Futura, we use similar condensed fonts */
    --font-display: 'Bebas Neue', 'Impact', sans-serif;
    --font-body: 'Inter', 'Helvetica Neue', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    
    /* Spacing */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 40px;
    --space-2xl: 64px;
    --space-3xl: 96px;
    
    /* Radius - minimal, sharp */
    --radius-sm: 2px;
    --radius-md: 4px;
    --radius-lg: 8px;
    
    /* Shadows - subtle */
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
    --shadow-lg: 0 12px 40px rgba(0,0,0,0.12);
    
    /* Transitions */
    --ease: cubic-bezier(0.16, 1, 0.3, 1);
    --transition-fast: 200ms var(--ease);
    --transition-base: 350ms var(--ease);
}

/* === ANIMATIONS === */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.95);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* === RESET === */
.stApp, [data-testid="stAppViewContainer"], .main {
    background: var(--bg) !important;
}

#MainMenu, footer, header, .stDeployButton, 
div[data-testid="stDecoration"], 
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    display: none !important;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* === SIDEBAR - NIKE DARK === */
section[data-testid="stSidebar"],
[data-testid="stSidebar"] {
    background: var(--black) !important;
    min-width: 300px !important;
    max-width: 300px !important;
    width: 300px !important;
}

section[data-testid="stSidebar"] > div:first-child,
[data-testid="stSidebar"] > div:first-child {
    padding: 0 !important;
    padding-bottom: 100px !important;
    background: var(--black) !important;
}

[data-testid="stSidebarNav"], .stSidebarNav {
    display: none !important;
}

.sidebar-brand {
    padding: var(--space-3xl) var(--space-xl) var(--space-2xl);
    border-bottom: 1px solid var(--gray-800);
}

.sidebar-logo {
    width: 72px;
    height: 72px;
    background: var(--white);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-display);
    font-size: 32px;
    font-weight: 400;
    color: var(--black);
    margin-bottom: var(--space-lg);
    letter-spacing: 2px;
    transition: var(--transition-base);
}

.sidebar-logo:hover {
    transform: scale(1.05);
}

.sidebar-name {
    font-family: var(--font-display);
    font-size: 28px;
    font-weight: 400;
    color: var(--white);
    margin: 0 0 4px;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.sidebar-title {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--gray-400);
    margin: 0;
    font-weight: 400;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* === NAVIGATION === */
[data-testid="stSidebar"] .stRadio > div {
    flex-direction: column !important;
    gap: 0 !important;
    padding: var(--space-xl) 0 !important;
}

[data-testid="stSidebar"] .stRadio label > div:first-child,
[data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
    display: none !important;
}

[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] [role="radiogroup"] label {
    background: transparent !important;
    padding: 18px var(--space-xl) !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: var(--transition-fast) !important;
    border-left: 3px solid transparent !important;
    position: relative;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: var(--gray-900) !important;
    border-left-color: var(--gray-600) !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked),
[data-testid="stSidebar"] [role="radiogroup"] label[aria-checked="true"],
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] {
    background: var(--gray-900) !important;
    border-left-color: var(--white) !important;
}

[data-testid="stSidebar"] .stRadio label p,
[data-testid="stSidebar"] .stRadio label span,
[data-testid="stSidebar"] [role="radiogroup"] label p,
[data-testid="stSidebar"] [role="radiogroup"] label span {
    font-family: var(--font-display) !important;
    font-size: 20px !important;
    font-weight: 400 !important;
    color: var(--gray-500) !important;
    margin: 0 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    transition: var(--transition-fast) !important;
}

[data-testid="stSidebar"] .stRadio label:hover p,
[data-testid="stSidebar"] .stRadio label:hover span {
    color: var(--gray-300) !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked) p,
[data-testid="stSidebar"] .stRadio label:has(input:checked) span,
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] p,
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] span {
    color: var(--white) !important;
}

/* === SIDEBAR FOOTER === */
.sidebar-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 300px;
    padding: var(--space-lg) var(--space-xl);
    border-top: 1px solid var(--gray-800);
    background: var(--black);
    z-index: 100;
}

.sidebar-status {
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 500;
    color: var(--white);
    text-transform: uppercase;
    letter-spacing: 2px;
}

.sidebar-status::before {
    content: '';
    width: 10px;
    height: 10px;
    background: var(--white);
    border-radius: 50%;
}

/* === TYPOGRAPHY - ENLARGED +4 === */
.eyebrow {
    font-family: var(--font-body);
    font-size: 15px; /* was 11 */
    font-weight: 600;
    color: var(--gray-500);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: var(--space-lg);
}

.headline {
    font-family: var(--font-display);
    font-size: clamp(52px, 7vw, 80px); /* enlarged from 48-56 */
    font-weight: 400;
    color: var(--black);
    line-height: 0.95;
    margin: 0 0 var(--space-xl);
    letter-spacing: 4px;
    text-transform: uppercase;
}

.headline-accent {
    color: var(--gray-400);
}

.subhead {
    font-family: var(--font-body);
    font-size: 22px; /* was 18 */
    color: var(--gray-600);
    line-height: 1.6;
    max-width: 600px;
    font-weight: 400;
}

.section-title {
    font-family: var(--font-display);
    font-size: 36px; /* was 28 */
    font-weight: 400;
    color: var(--black);
    margin: 0 0 var(--space-xl);
    letter-spacing: 4px;
    text-transform: uppercase;
}

/* === HERO === */
.hero {
    min-height: calc(100vh - 80px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--space-3xl) 80px;
    position: relative;
}

.hero-content {
    max-width: 800px;
    animation: fadeInUp 1000ms var(--ease);
}

.stats-bar {
    display: flex;
    gap: 80px;
    margin-top: var(--space-3xl);
    padding-top: var(--space-xl);
    border-top: 2px solid var(--black);
    animation: fadeInUp 1000ms var(--ease) 200ms both;
}

.stat-value {
    font-family: var(--font-display);
    font-size: 52px; /* was 36, +4 scaled */
    font-weight: 400;
    color: var(--black);
    letter-spacing: 2px;
    line-height: 1;
}

.stat-label {
    font-family: var(--font-body);
    font-size: 15px; /* was 11 */
    color: var(--gray-500);
    margin-top: 8px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* === FEATURED PROJECT === */
.featured-project {
    background: var(--black);
    padding: var(--space-3xl);
    margin: var(--space-3xl) 80px var(--space-xl);
    color: var(--white);
    position: relative;
    animation: fadeInUp 1000ms var(--ease) 400ms both;
}

.featured-label {
    font-family: var(--font-body);
    font-size: 15px; /* was 11 */
    font-weight: 600;
    color: var(--gray-400);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: var(--space-lg);
    display: inline-block;
    padding-bottom: var(--space-sm);
    border-bottom: 2px solid var(--white);
}

.featured-title {
    font-family: var(--font-display);
    font-size: 44px; /* was 32, +12 for impact */
    font-weight: 400;
    color: var(--white);
    line-height: 1.1;
    margin: 0 0 var(--space-lg);
    max-width: 700px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.featured-desc {
    font-family: var(--font-body);
    font-size: 20px; /* was 16 */
    color: var(--gray-400);
    line-height: 1.7;
    max-width: 560px;
    margin-bottom: var(--space-xl);
}

.featured-metrics {
    display: flex;
    gap: 64px;
}

.featured-metric {
    border-left: 2px solid var(--white);
    padding-left: var(--space-lg);
}

.featured-metric-value {
    font-family: var(--font-display);
    font-size: 48px; /* was 32, +16 */
    font-weight: 400;
    color: var(--white);
    letter-spacing: 2px;
}

.featured-metric-label {
    font-family: var(--font-body);
    font-size: 15px; /* was 11 */
    color: var(--gray-400);
    margin-top: 4px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.featured-tags {
    display: flex;
    gap: 12px;
    margin-top: var(--space-xl);
    flex-wrap: wrap;
}

.featured-tag {
    font-family: var(--font-mono);
    font-size: 15px; /* was 11 */
    color: var(--gray-400);
    background: var(--gray-800);
    padding: 10px 18px;
    transition: var(--transition-fast);
}

.featured-tag:hover {
    background: var(--gray-700);
    color: var(--white);
}

/* === PROJECT CARDS === */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-lg);
    padding: 0 80px var(--space-3xl);
}

.project-card {
    background: var(--white);
    border: 2px solid var(--gray-200);
    padding: var(--space-xl);
    transition: var(--transition-base);
    position: relative;
}

.project-card::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--black);
    transform: scaleX(0);
    transform-origin: left;
    transition: var(--transition-base);
}

.project-card:hover {
    border-color: var(--black);
}

.project-card:hover::after {
    transform: scaleX(1);
}

.project-company {
    font-family: var(--font-body);
    font-size: 15px; /* was 11 */
    font-weight: 600;
    color: var(--gray-500);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: var(--space-sm);
}

.project-title {
    font-family: var(--font-display);
    font-size: 28px; /* was 20, +8 */
    font-weight: 400;
    color: var(--black);
    line-height: 1.2;
    margin: 0 0 var(--space-sm);
    letter-spacing: 1px;
    text-transform: uppercase;
}

.project-desc {
    font-family: var(--font-body);
    font-size: 18px; /* was 14 */
    color: var(--gray-600);
    line-height: 1.6;
    margin-bottom: var(--space-lg);
}

.project-metrics {
    display: flex;
    gap: var(--space-xl);
    padding-top: var(--space-md);
    border-top: 1px solid var(--gray-200);
}

.project-metric-value {
    font-family: var(--font-display);
    font-size: 28px; /* was 20 */
    font-weight: 400;
    color: var(--black);
    letter-spacing: 1px;
}

.project-metric-label {
    font-family: var(--font-body);
    font-size: 14px; /* was 10 */
    color: var(--gray-500);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* === QUOTE === */
.quote-section {
    background: var(--gray-100);
    padding: var(--space-3xl);
    margin: 0 80px var(--space-3xl);
    text-align: center;
    position: relative;
}

.quote-section::before {
    content: '"';
    position: absolute;
    top: var(--space-xl);
    left: 50%;
    transform: translateX(-50%);
    font-family: var(--font-display);
    font-size: 120px;
    color: var(--gray-300);
    line-height: 1;
}

.quote-text {
    font-family: var(--font-body);
    font-size: 30px; /* was 26 */
    font-weight: 400;
    font-style: italic;
    color: var(--black);
    line-height: 1.5;
    max-width: 700px;
    margin: var(--space-2xl) auto var(--space-lg);
    position: relative;
}

.quote-author {
    font-family: var(--font-body);
    font-size: 17px; /* was 13 */
    color: var(--gray-500);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* === WORK PAGE === */
.work-hero {
    background: var(--black);
    padding: 120px 80px;
    text-align: center;
}

.work-hero-title {
    font-family: var(--font-display);
    font-size: 64px; /* was 48, +16 */
    font-weight: 400;
    color: var(--white);
    margin: 0 0 var(--space-md);
    letter-spacing: 6px;
    text-transform: uppercase;
}

.work-hero-sub {
    font-family: var(--font-body);
    font-size: 20px; /* was 16 */
    color: var(--gray-400);
    letter-spacing: 2px;
}

/* === CASE STUDIES === */
.case-study {
    padding: var(--space-3xl) 80px;
    border-bottom: 1px solid var(--gray-200);
}

.case-study:nth-child(even) {
    background: var(--gray-100);
}

.case-inner {
    max-width: 800px;
    margin: 0 auto;
}

.case-number {
    font-family: var(--font-mono);
    font-size: 15px; /* was 11 */
    font-weight: 600;
    color: var(--gray-500);
    letter-spacing: 4px;
    margin-bottom: var(--space-md);
}

.case-title {
    font-family: var(--font-display);
    font-size: 48px; /* was 36, +12 */
    font-weight: 400;
    color: var(--black);
    line-height: 1.1;
    margin: 0 0 8px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.case-subtitle {
    font-family: var(--font-body);
    font-size: 19px; /* was 15 */
    color: var(--gray-500);
    margin-bottom: var(--space-xl);
}

.case-results {
    background: var(--black);
    padding: var(--space-xl);
    margin-bottom: var(--space-2xl);
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-lg);
    text-align: center;
}

.case-result-value {
    font-family: var(--font-display);
    font-size: 48px; /* was 36, +12 */
    font-weight: 400;
    color: var(--white);
    letter-spacing: 2px;
}

.case-result-label {
    font-family: var(--font-body);
    font-size: 15px; /* was 11 */
    color: var(--gray-400);
    margin-top: 4px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.case-section {
    margin-bottom: var(--space-xl);
}

.case-section-title {
    font-family: var(--font-display);
    font-size: 24px; /* was 18, +6 */
    font-weight: 400;
    color: var(--black);
    margin-bottom: var(--space-md);
    letter-spacing: 2px;
    text-transform: uppercase;
    padding-left: var(--space-md);
    border-left: 4px solid var(--black);
}

.case-section p {
    font-family: var(--font-body);
    font-size: 19px; /* was 15 */
    color: var(--gray-600);
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
    font-size: 19px; /* was 15 */
    color: var(--gray-600);
    line-height: 1.8;
    margin-bottom: 8px;
    padding-left: 28px;
    position: relative;
}

.case-section li::before {
    content: '—';
    position: absolute;
    left: 0;
    color: var(--black);
    font-weight: 700;
}

.case-quote {
    background: var(--gray-100);
    padding: var(--space-xl);
    margin: var(--space-xl) 0;
    border-left: 4px solid var(--black);
}

.case-quote p {
    font-family: var(--font-body);
    font-size: 21px; /* was 17 */
    font-style: italic;
    color: var(--black);
    line-height: 1.6;
    margin: 0;
}

.case-quote cite {
    font-family: var(--font-body);
    font-size: 16px; /* was 12 */
    color: var(--gray-500);
    font-style: normal;
    display: block;
    margin-top: var(--space-md);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* === ABOUT PAGE === */
.about-hero {
    display: grid;
    grid-template-columns: 280px 1fr; /* enlarged from 240 */
    gap: var(--space-3xl);
    padding: var(--space-3xl) 80px;
    align-items: start;
}

.about-photo {
    width: 260px; /* was 220, +40 */
    height: 260px; /* was 220, +40 */
    background: var(--gray-200);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-body);
    font-size: 17px; /* was 13 */
    color: var(--gray-500);
    text-align: center;
    border: 4px solid var(--black);
    transition: var(--transition-base);
}

.about-photo:hover {
    transform: scale(1.02);
}

.about-intro h1 {
    font-family: var(--font-display);
    font-size: 56px; /* was 40, +16 */
    font-weight: 400;
    color: var(--black);
    margin: 0 0 var(--space-xl);
    letter-spacing: 3px;
    text-transform: uppercase;
}

.about-intro p {
    font-family: var(--font-body);
    font-size: 21px; /* was 17 */
    color: var(--gray-600);
    line-height: 1.8;
    margin: 0 0 var(--space-md);
}

.about-section {
    padding: var(--space-2xl) 80px;
    border-top: 1px solid var(--gray-200);
}

.about-section:nth-child(even) {
    background: var(--gray-100);
}

/* === TIMELINE === */
.timeline {
    max-width: 720px;
    position: relative;
    padding-left: var(--space-xl);
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--black);
}

.timeline-item {
    padding: var(--space-lg) 0;
    border-bottom: 1px solid var(--gray-200);
    display: grid;
    grid-template-columns: 160px 1fr;
    gap: var(--space-xl);
    position: relative;
    transition: var(--transition-fast);
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -29px;
    top: 32px;
    width: 16px;
    height: 16px;
    background: var(--white);
    border: 3px solid var(--black);
    transition: var(--transition-fast);
}

.timeline-item:hover::before {
    background: var(--black);
}

.timeline-item:last-child {
    border-bottom: none;
}

.timeline-year {
    font-family: var(--font-mono);
    font-size: 16px; /* was 12 */
    font-weight: 500;
    color: var(--gray-500);
}

.timeline-role {
    font-family: var(--font-display);
    font-size: 24px; /* was 17, +7 */
    font-weight: 400;
    color: var(--black);
    margin: 0 0 4px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.timeline-company {
    font-family: var(--font-body);
    font-size: 18px; /* was 14 */
    color: var(--gray-500);
}

.timeline-desc {
    font-family: var(--font-body);
    font-size: 18px; /* was 14 */
    color: var(--gray-600);
    line-height: 1.65;
    margin-top: var(--space-sm);
}

/* === SKILLS === */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-lg);
    max-width: 920px;
}

.skill-card {
    background: var(--white);
    border: 2px solid var(--gray-200);
    padding: var(--space-xl);
    transition: var(--transition-base);
    position: relative;
}

.skill-card::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--black);
    transform: scaleX(0);
    transform-origin: left;
    transition: var(--transition-base);
}

.skill-card:hover {
    border-color: var(--black);
}

.skill-card:hover::after {
    transform: scaleX(1);
}

.skill-card-title {
    font-family: var(--font-display);
    font-size: 18px; /* was 11, significantly larger */
    font-weight: 400;
    color: var(--black);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: var(--space-md);
}

.skill-card-list {
    font-family: var(--font-body);
    font-size: 18px; /* was 14 */
    color: var(--gray-600);
    line-height: 2.2;
}

/* === CERTIFICATIONS === */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-md);
    max-width: 920px;
}

.cert-card {
    background: var(--white);
    border: 2px solid var(--gray-200);
    padding: var(--space-xl);
    transition: var(--transition-base);
}

.cert-card:hover {
    border-color: var(--black);
}

.cert-name {
    font-family: var(--font-body);
    font-size: 19px; /* was 15 */
    font-weight: 600;
    color: var(--black);
    margin-bottom: 4px;
}

.cert-issuer {
    font-family: var(--font-body);
    font-size: 17px; /* was 13 */
    color: var(--gray-500);
}

/* === CONNECT PAGE === */
.connect-hero {
    background: var(--black);
    padding: 120px 80px;
    text-align: center;
}

.connect-hero h1 {
    font-family: var(--font-display);
    font-size: 64px; /* was 48, +16 */
    font-weight: 400;
    color: var(--white);
    margin: 0 0 var(--space-lg);
    letter-spacing: 6px;
    text-transform: uppercase;
}

.connect-hero p {
    font-family: var(--font-body);
    font-size: 21px; /* was 17 */
    color: var(--gray-400);
    max-width: 520px;
    margin: 0 auto;
}

.connect-cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-md);
    max-width: 960px;
    margin: var(--space-2xl) auto 0;
}

.connect-card {
    background: var(--gray-900);
    border: 1px solid var(--gray-800);
    padding: var(--space-xl) var(--space-lg);
    text-align: center;
    transition: var(--transition-base);
}

.connect-card:hover {
    background: var(--gray-800);
    border-color: var(--white);
    transform: translateY(-4px);
}

.connect-card-icon {
    font-size: 32px; /* was 24, +8 */
    margin-bottom: var(--space-sm);
}

.connect-card-label {
    font-family: var(--font-body);
    font-size: 14px; /* was 10 */
    color: var(--gray-500);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
    font-weight: 600;
}

.connect-card-value {
    font-family: var(--font-body);
    font-size: 17px; /* was 13 */
    color: var(--white);
    word-break: break-all;
}

.connect-card-value a {
    color: var(--gray-300);
    text-decoration: none;
    transition: var(--transition-fast);
}

.connect-card-value a:hover {
    color: var(--white);
}

/* === TESTIMONIALS === */
.testimonials {
    padding: var(--space-3xl) 80px;
}

.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-lg);
    max-width: 1000px;
    margin: 0 auto;
}

.testimonial-card {
    background: var(--white);
    border: 2px solid var(--gray-200);
    padding: var(--space-xl);
    transition: var(--transition-base);
    position: relative;
}

.testimonial-card::before {
    content: '"';
    position: absolute;
    top: var(--space-md);
    right: var(--space-lg);
    font-family: var(--font-display);
    font-size: 80px;
    color: var(--gray-200);
    line-height: 1;
}

.testimonial-card:hover {
    border-color: var(--black);
}

.testimonial-quote {
    font-family: var(--font-body);
    font-size: 19px; /* was 15 */
    color: var(--gray-600);
    line-height: 1.75;
    font-style: italic;
    margin-bottom: var(--space-md);
    position: relative;
}

.testimonial-author {
    font-family: var(--font-body);
    font-size: 18px; /* was 14 */
    font-weight: 600;
    color: var(--black);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.testimonial-role {
    font-family: var(--font-body);
    font-size: 17px; /* was 13 */
    color: var(--gray-500);
    margin-top: 2px;
}

/* === BUTTONS === */
.stButton > button {
    font-family: var(--font-display) !important;
    font-size: 18px !important; /* was 14 */
    font-weight: 400 !important;
    padding: 16px 32px !important;
    border-radius: 0 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    transition: var(--transition-base) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
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
    .stats-bar { flex-wrap: wrap; gap: var(--space-xl) var(--space-2xl); }
    .featured-project { margin: var(--space-xl); padding: var(--space-lg); }
    .featured-metrics { flex-wrap: wrap; gap: var(--space-lg); }
    .projects-grid { grid-template-columns: 1fr; padding: 0 var(--space-xl) var(--space-xl); }
    .quote-section { margin: 0 var(--space-xl) var(--space-xl); padding: var(--space-lg); }
    .quote-text { font-size: 24px; }
    .case-study { padding: var(--space-xl); }
    .case-results { grid-template-columns: 1fr; }
    .about-hero { grid-template-columns: 1fr; gap: var(--space-xl); padding: var(--space-xl); }
    .about-photo { width: 200px; height: 200px; }
    .about-section { padding: var(--space-xl); }
    .skills-grid, .cert-grid { grid-template-columns: 1fr; }
    .timeline-item { grid-template-columns: 1fr; gap: var(--space-sm); }
    .work-hero, .connect-hero { padding: var(--space-2xl) var(--space-xl); }
    .work-hero-title, .connect-hero h1 { font-size: 44px; }
    .connect-cards { grid-template-columns: repeat(2, 1fr); }
    .testimonials { padding: var(--space-xl); }
    .testimonials-grid { grid-template-columns: 1fr; }
}
</style>
<link href='https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap' rel='stylesheet'>
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
    
    st.markdown(f'<div style="padding:0 80px"><div class="stats-bar">{stats_html}</div></div>', unsafe_allow_html=True)
    
    metrics = [("9%", "Revenue Lift"), ("70%", "Fewer Conflicts"), ("$12M", "Annual Impact"), ("6 wks", "Timeline")]
    metrics_html = ''.join(render_metric(v, l, "featured") for v, l in metrics)
    tags = ["Snowflake", "Power BI", "Python", "250+ Users"]
    tags_html = ''.join(render_tag(t) for t in tags)
    
    st.markdown(f"""
    <div class="featured-project">
        <div class="featured-label">Flagship Project</div>
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
            <h3 class="project-title">+33% Conversion via A/B Testing</h3>
            <p class="project-desc">Built cross-channel attribution across GA4, Shopify, Meta. Led A/B testing program optimizing marketing spend.</p>
            <div class="project-metrics">
                <div><div class="project-metric-value">+33%</div><div class="project-metric-label">Conversion</div></div>
                <div><div class="project-metric-value">-18%</div><div class="project-metric-label">CPA</div></div>
                <div><div class="project-metric-value">2x</div><div class="project-metric-label">ROAS</div></div>
            </div>
        </div>
        <div class="project-card">
            <div class="project-company">Operations Automation</div>
            <h3 class="project-title">160 Hours Saved Quarterly</h3>
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
                <div><div class="case-result-value">5→1</div><div class="case-result-label">Decision Cycle (Days)</div></div>
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
        <div class="about-photo">Your Photo<br>260×260</div>
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
# MAIN
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
