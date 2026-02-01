"""
Jason C. Chang | BI Manager Portfolio
======================================
Rebuilt based on portfolio audit:
- Clear value proposition
- Photo + human connection
- "The Mess" storytelling
- Keywords visible
- Testimonials on first scroll
- 1 flagship project
- Resume download
- Nike-inspired B/W aesthetic
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
    
    NAME: str = "Jason C. Chang"
    INITIALS: str = "JC"
    TITLE: str = "BI Manager"
    TAGLINE: str = "I turn data chaos into executive clarity"
    
    # Clear value prop answering "Why hire Jason?"
    VALUE_PROP: str = "I help executives stop arguing about numbers and start making decisions."
    
    EMAIL: str = "jason.chang01022024@gmail.com"
    PHONE: str = "(626) 203-3319"
    LINKEDIN: str = "linkedin.com/in/jchang0102"
    LINKEDIN_URL: str = "https://linkedin.com/in/jchang0102"
    LOCATION: str = "Hacienda Heights, CA"
    
    # Keywords recruiters scan for (visible in hero)
    KEYWORDS: tuple = ("SQL", "Python", "Power BI", "Snowflake", "DAX")
    
    PAGES: tuple = ("Home", "Work", "About", "Connect")

CONFIG = Config()

# =============================================================================
# STYLES - NIKE B/W + AUDIT FIXES
# =============================================================================

def get_css() -> str:
    return """
<style>
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
    
    --bg: var(--white);
    --fg: var(--black);
    --muted: var(--gray-500);
    --border: var(--gray-200);
    
    --font-display: 'Bebas Neue', 'Impact', sans-serif;
    --font-body: 'Inter', 'Helvetica Neue', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 40px;
    --space-2xl: 64px;
    --space-3xl: 96px;
    
    --ease: cubic-bezier(0.16, 1, 0.3, 1);
    --transition: 300ms var(--ease);
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
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

/* === SIDEBAR === */
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
    padding: var(--space-2xl) var(--space-xl) var(--space-xl);
    border-bottom: 1px solid var(--gray-800);
    text-align: center;
}

/* Sidebar photo placeholder */
.sidebar-photo {
    width: 100px;
    height: 100px;
    background: var(--gray-700);
    border: 3px solid var(--white);
    border-radius: 50%;
    margin: 0 auto var(--space-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-body);
    font-size: 11px;
    color: var(--gray-400);
    transition: var(--transition);
}

.sidebar-photo:hover {
    transform: scale(1.05);
    border-color: var(--gray-300);
}

.sidebar-name {
    font-family: var(--font-display);
    font-size: 24px;
    color: var(--white);
    margin: 0 0 4px;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.sidebar-title {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--gray-400);
    margin: 0 0 var(--space-md);
    letter-spacing: 1px;
}

/* Status badge - "Open to opportunities" */
.sidebar-status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--gray-800);
    padding: 8px 16px;
    font-family: var(--font-body);
    font-size: 11px;
    font-weight: 600;
    color: #4ade80;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.sidebar-status-badge::before {
    content: '';
    width: 8px;
    height: 8px;
    background: #4ade80;
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
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
    padding: 16px var(--space-xl) !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: var(--transition) !important;
    border-left: 3px solid transparent !important;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: var(--gray-900) !important;
    border-left-color: var(--gray-600) !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked),
[data-testid="stSidebar"] [role="radio"][aria-checked="true"] {
    background: var(--gray-900) !important;
    border-left-color: var(--white) !important;
}

[data-testid="stSidebar"] .stRadio label p,
[data-testid="stSidebar"] .stRadio label span {
    font-family: var(--font-display) !important;
    font-size: 18px !important;
    color: var(--gray-500) !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    transition: var(--transition) !important;
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
    display: flex;
    flex-direction: column;
    gap: var(--space-sm);
}

.sidebar-download {
    display: block;
    background: var(--white);
    color: var(--black);
    font-family: var(--font-display);
    font-size: 14px;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-align: center;
    text-decoration: none;
    padding: 12px;
    transition: var(--transition);
}

.sidebar-download:hover {
    background: var(--gray-200);
}

/* === HERO - WITH PHOTO + VALUE PROP + KEYWORDS === */
.hero {
    display: grid;
    grid-template-columns: 1fr 280px;
    gap: var(--space-3xl);
    padding: var(--space-3xl) 80px;
    min-height: calc(100vh - 200px);
    align-items: center;
}

.hero-content {
    animation: fadeInUp 800ms var(--ease);
}

.hero-eyebrow {
    font-family: var(--font-body);
    font-size: 15px;
    font-weight: 600;
    color: var(--gray-500);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: var(--space-lg);
}

.hero-headline {
    font-family: var(--font-display);
    font-size: clamp(48px, 6vw, 72px);
    font-weight: 400;
    color: var(--black);
    line-height: 0.95;
    margin: 0 0 var(--space-lg);
    letter-spacing: 3px;
    text-transform: uppercase;
}

/* Value proposition - answers "Why hire Jason?" */
.hero-value-prop {
    font-family: var(--font-body);
    font-size: 22px;
    color: var(--gray-600);
    line-height: 1.6;
    max-width: 560px;
    margin-bottom: var(--space-xl);
}

/* Keywords visible (recruiter scan) */
.hero-keywords {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: var(--space-xl);
}

.hero-keyword {
    font-family: var(--font-mono);
    font-size: 14px;
    color: var(--black);
    background: var(--gray-100);
    padding: 10px 18px;
    border: 2px solid var(--gray-200);
    transition: var(--transition);
}

.hero-keyword:hover {
    border-color: var(--black);
    background: var(--white);
}

/* Hero photo */
.hero-photo-container {
    animation: fadeInUp 800ms var(--ease) 200ms both;
}

.hero-photo {
    width: 260px;
    height: 260px;
    background: var(--gray-200);
    border: 4px solid var(--black);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 8px;
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--gray-500);
    text-align: center;
    transition: var(--transition);
}

.hero-photo:hover {
    transform: scale(1.02);
}

.hero-photo-hint {
    font-size: 12px;
    color: var(--gray-400);
}

/* === STATS === */
.stats-section {
    padding: 0 80px var(--space-2xl);
    animation: fadeInUp 800ms var(--ease) 400ms both;
}

.stats-bar {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-xl);
    padding: var(--space-xl) 0;
    border-top: 2px solid var(--black);
    border-bottom: 2px solid var(--black);
}

.stat-item {
    text-align: center;
}

.stat-value {
    font-family: var(--font-display);
    font-size: 48px;
    color: var(--black);
    letter-spacing: 2px;
    line-height: 1;
}

.stat-label {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--gray-500);
    margin-top: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* === FLAGSHIP PROJECT (DEEP DIVE) === */
.flagship {
    background: var(--black);
    padding: var(--space-3xl) 80px;
    color: var(--white);
}

.flagship-label {
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 600;
    color: var(--gray-400);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: var(--space-md);
    padding-bottom: var(--space-sm);
    border-bottom: 2px solid var(--white);
    display: inline-block;
}

.flagship-title {
    font-family: var(--font-display);
    font-size: 44px;
    color: var(--white);
    line-height: 1.1;
    margin: 0 0 var(--space-md);
    letter-spacing: 2px;
    text-transform: uppercase;
    max-width: 700px;
}

/* Timeline/Scope - audit requirement */
.flagship-meta {
    display: flex;
    gap: var(--space-xl);
    margin-bottom: var(--space-xl);
    font-family: var(--font-mono);
    font-size: 14px;
    color: var(--gray-400);
}

.flagship-meta-item {
    display: flex;
    align-items: center;
    gap: 8px;
}

.flagship-meta-item::before {
    content: '→';
    color: var(--white);
}

/* THE MESS - storytelling format */
.flagship-mess {
    background: var(--gray-900);
    padding: var(--space-xl);
    margin-bottom: var(--space-xl);
    border-left: 4px solid var(--white);
}

.flagship-mess-label {
    font-family: var(--font-display);
    font-size: 20px;
    color: var(--white);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: var(--space-md);
}

.flagship-mess-text {
    font-family: var(--font-body);
    font-size: 18px;
    color: var(--gray-300);
    line-height: 1.8;
}

/* Results grid */
.flagship-results {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-lg);
    margin-bottom: var(--space-xl);
}

.flagship-result {
    border-left: 3px solid var(--white);
    padding-left: var(--space-lg);
}

.flagship-result-value {
    font-family: var(--font-display);
    font-size: 44px;
    color: var(--white);
    letter-spacing: 1px;
}

.flagship-result-label {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--gray-400);
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Tags */
.flagship-tags {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.flagship-tag {
    font-family: var(--font-mono);
    font-size: 13px;
    color: var(--gray-400);
    background: var(--gray-800);
    padding: 10px 16px;
    transition: var(--transition);
}

.flagship-tag:hover {
    background: var(--gray-700);
    color: var(--white);
}

/* === HOME TESTIMONIAL (first scroll) === */
.home-testimonial {
    background: var(--gray-100);
    padding: var(--space-2xl) 80px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: var(--space-2xl);
    align-items: center;
}

.testimonial-content {
    max-width: 700px;
}

.testimonial-quote {
    font-family: var(--font-body);
    font-size: 26px;
    font-style: italic;
    color: var(--black);
    line-height: 1.5;
    margin: 0 0 var(--space-lg);
    position: relative;
    padding-left: var(--space-xl);
}

.testimonial-quote::before {
    content: '"';
    position: absolute;
    left: 0;
    top: -10px;
    font-family: var(--font-display);
    font-size: 80px;
    color: var(--gray-300);
    line-height: 1;
}

.testimonial-author {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 600;
    color: var(--black);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.testimonial-role {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--gray-500);
    margin-top: 2px;
}

.testimonial-cta {
    text-align: right;
}

.testimonial-cta-text {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--gray-500);
    margin-bottom: var(--space-sm);
}

.testimonial-cta-link {
    font-family: var(--font-display);
    font-size: 18px;
    color: var(--black);
    letter-spacing: 2px;
    text-transform: uppercase;
    text-decoration: none;
    border-bottom: 2px solid var(--black);
    padding-bottom: 4px;
    transition: var(--transition);
}

.testimonial-cta-link:hover {
    color: var(--gray-600);
    border-color: var(--gray-600);
}

/* === SECONDARY PROJECTS === */
.projects-section {
    padding: var(--space-2xl) 80px var(--space-3xl);
}

.projects-header {
    margin-bottom: var(--space-xl);
}

.projects-title {
    font-family: var(--font-display);
    font-size: 32px;
    color: var(--black);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 0;
}

.projects-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-lg);
}

.project-card {
    background: var(--white);
    border: 2px solid var(--gray-200);
    padding: var(--space-xl);
    transition: var(--transition);
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
    transition: var(--transition);
}

.project-card:hover {
    border-color: var(--black);
}

.project-card:hover::after {
    transform: scaleX(1);
}

.project-company {
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 600;
    color: var(--gray-500);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: var(--space-sm);
}

.project-title {
    font-family: var(--font-display);
    font-size: 26px;
    color: var(--black);
    line-height: 1.2;
    margin: 0 0 var(--space-sm);
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Timeline on project cards */
.project-meta {
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--gray-500);
    margin-bottom: var(--space-md);
}

.project-desc {
    font-family: var(--font-body);
    font-size: 16px;
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
    font-size: 26px;
    color: var(--black);
    letter-spacing: 1px;
}

.project-metric-label {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--gray-500);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* === WORK PAGE === */
.work-hero {
    background: var(--black);
    padding: 100px 80px;
    text-align: center;
}

.work-hero-title {
    font-family: var(--font-display);
    font-size: 56px;
    color: var(--white);
    margin: 0 0 var(--space-md);
    letter-spacing: 5px;
    text-transform: uppercase;
}

.work-hero-sub {
    font-family: var(--font-body);
    font-size: 18px;
    color: var(--gray-400);
}

/* Case study - THE MESS format */
.case-study {
    padding: var(--space-3xl) 80px;
    border-bottom: 1px solid var(--gray-200);
}

.case-study:nth-child(even) {
    background: var(--gray-50);
}

.case-inner {
    max-width: 800px;
    margin: 0 auto;
}

.case-label {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 13px;
    font-weight: 600;
    color: var(--white);
    background: var(--black);
    padding: 8px 16px;
    letter-spacing: 2px;
    margin-bottom: var(--space-lg);
}

.case-title {
    font-family: var(--font-display);
    font-size: 44px;
    color: var(--black);
    line-height: 1.1;
    margin: 0 0 var(--space-sm);
    letter-spacing: 2px;
    text-transform: uppercase;
}

.case-subtitle {
    font-family: var(--font-body);
    font-size: 17px;
    color: var(--gray-500);
    margin-bottom: var(--space-xl);
}

/* Results box */
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
    font-size: 44px;
    color: var(--white);
    letter-spacing: 1px;
}

.case-result-label {
    font-family: var(--font-body);
    font-size: 13px;
    color: var(--gray-400);
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Story sections */
.case-section {
    margin-bottom: var(--space-xl);
}

.case-section-title {
    font-family: var(--font-display);
    font-size: 22px;
    color: var(--black);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: var(--space-md);
    padding-left: var(--space-md);
    border-left: 4px solid var(--black);
}

.case-section p {
    font-family: var(--font-body);
    font-size: 17px;
    color: var(--gray-600);
    line-height: 1.8;
    margin: 0 0 var(--space-md);
}

.case-section ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

.case-section li {
    font-family: var(--font-body);
    font-size: 17px;
    color: var(--gray-600);
    line-height: 1.8;
    margin-bottom: 8px;
    padding-left: 24px;
    position: relative;
}

.case-section li::before {
    content: '—';
    position: absolute;
    left: 0;
    color: var(--black);
    font-weight: 700;
}

/* Stakeholder quote */
.case-quote {
    background: var(--gray-100);
    padding: var(--space-xl);
    margin: var(--space-xl) 0;
    border-left: 4px solid var(--black);
}

.case-quote p {
    font-family: var(--font-body);
    font-size: 20px;
    font-style: italic;
    color: var(--black);
    line-height: 1.6;
    margin: 0;
}

.case-quote cite {
    font-family: var(--font-body);
    font-size: 14px;
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
    grid-template-columns: 300px 1fr;
    gap: var(--space-3xl);
    padding: var(--space-3xl) 80px;
    align-items: start;
}

.about-photo {
    width: 280px;
    height: 280px;
    background: var(--gray-200);
    border: 4px solid var(--black);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 8px;
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--gray-500);
    text-align: center;
    transition: var(--transition);
}

.about-photo:hover {
    transform: scale(1.02);
}

.about-intro h1 {
    font-family: var(--font-display);
    font-size: 52px;
    color: var(--black);
    margin: 0 0 var(--space-lg);
    letter-spacing: 2px;
    text-transform: uppercase;
}

.about-intro p {
    font-family: var(--font-body);
    font-size: 19px;
    color: var(--gray-600);
    line-height: 1.8;
    margin: 0 0 var(--space-md);
}

.about-section {
    padding: var(--space-2xl) 80px;
    border-top: 1px solid var(--gray-200);
}

.about-section:nth-child(even) {
    background: var(--gray-50);
}

.section-title {
    font-family: var(--font-display);
    font-size: 32px;
    color: var(--black);
    margin: 0 0 var(--space-xl);
    letter-spacing: 3px;
    text-transform: uppercase;
}

/* Timeline */
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
    transition: var(--transition);
}

.timeline-item:hover::before {
    background: var(--black);
}

.timeline-item:last-child {
    border-bottom: none;
}

.timeline-year {
    font-family: var(--font-mono);
    font-size: 14px;
    color: var(--gray-500);
}

.timeline-role {
    font-family: var(--font-display);
    font-size: 22px;
    color: var(--black);
    margin: 0 0 4px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.timeline-company {
    font-family: var(--font-body);
    font-size: 16px;
    color: var(--gray-500);
}

.timeline-desc {
    font-family: var(--font-body);
    font-size: 16px;
    color: var(--gray-600);
    line-height: 1.6;
    margin-top: var(--space-sm);
}

/* Skills */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-lg);
    max-width: 900px;
}

.skill-card {
    background: var(--white);
    border: 2px solid var(--gray-200);
    padding: var(--space-xl);
    transition: var(--transition);
}

.skill-card:hover {
    border-color: var(--black);
}

.skill-card-title {
    font-family: var(--font-display);
    font-size: 18px;
    color: var(--black);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: var(--space-md);
}

.skill-card-list {
    font-family: var(--font-body);
    font-size: 16px;
    color: var(--gray-600);
    line-height: 2.2;
}

/* Certifications */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-md);
    max-width: 900px;
}

.cert-card {
    background: var(--white);
    border: 2px solid var(--gray-200);
    padding: var(--space-lg);
    transition: var(--transition);
}

.cert-card:hover {
    border-color: var(--black);
}

.cert-name {
    font-family: var(--font-body);
    font-size: 17px;
    font-weight: 600;
    color: var(--black);
    margin-bottom: 4px;
}

.cert-issuer {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--gray-500);
}

/* === CONNECT PAGE === */
.connect-hero {
    background: var(--black);
    padding: 100px 80px;
    text-align: center;
}

.connect-hero h1 {
    font-family: var(--font-display);
    font-size: 56px;
    color: var(--white);
    margin: 0 0 var(--space-lg);
    letter-spacing: 5px;
    text-transform: uppercase;
}

.connect-hero p {
    font-family: var(--font-body);
    font-size: 19px;
    color: var(--gray-400);
    max-width: 500px;
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
    transition: var(--transition);
}

.connect-card:hover {
    background: var(--gray-800);
    border-color: var(--white);
    transform: translateY(-4px);
}

.connect-card-icon {
    font-size: 28px;
    margin-bottom: var(--space-sm);
}

.connect-card-label {
    font-family: var(--font-body);
    font-size: 12px;
    color: var(--gray-500);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
    font-weight: 600;
}

.connect-card-value {
    font-family: var(--font-body);
    font-size: 15px;
    color: var(--white);
    word-break: break-all;
}

.connect-card-value a {
    color: var(--gray-300);
    text-decoration: none;
    transition: var(--transition);
}

.connect-card-value a:hover {
    color: var(--white);
}

/* Testimonials grid */
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
    transition: var(--transition);
    position: relative;
}

.testimonial-card::before {
    content: '"';
    position: absolute;
    top: var(--space-md);
    right: var(--space-lg);
    font-family: var(--font-display);
    font-size: 72px;
    color: var(--gray-200);
    line-height: 1;
}

.testimonial-card:hover {
    border-color: var(--black);
}

.testimonial-card-quote {
    font-family: var(--font-body);
    font-size: 17px;
    color: var(--gray-600);
    line-height: 1.7;
    font-style: italic;
    margin-bottom: var(--space-md);
    position: relative;
}

.testimonial-card-author {
    font-family: var(--font-body);
    font-size: 15px;
    font-weight: 600;
    color: var(--black);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.testimonial-card-role {
    font-family: var(--font-body);
    font-size: 14px;
    color: var(--gray-500);
    margin-top: 2px;
}

/* === BUTTONS === */
.stButton > button {
    font-family: var(--font-display) !important;
    font-size: 16px !important;
    padding: 14px 28px !important;
    border-radius: 0 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    transition: var(--transition) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
}

/* === RESPONSIVE === */
@media (max-width: 1024px) {
    .hero { grid-template-columns: 1fr; padding: var(--space-2xl) var(--space-xl); }
    .hero-photo-container { display: none; }
    .stats-bar { grid-template-columns: repeat(2, 1fr); }
    .flagship { padding: var(--space-2xl) var(--space-xl); }
    .flagship-results { grid-template-columns: repeat(2, 1fr); }
    .home-testimonial { grid-template-columns: 1fr; padding: var(--space-xl); }
    .projects-section { padding: var(--space-xl); }
    .projects-grid { grid-template-columns: 1fr; }
    .case-study { padding: var(--space-2xl) var(--space-xl); }
    .about-hero { grid-template-columns: 1fr; padding: var(--space-xl); }
    .about-section { padding: var(--space-xl); }
    .work-hero, .connect-hero { padding: var(--space-2xl) var(--space-xl); }
    .testimonials { padding: var(--space-xl); }
}

@media (max-width: 768px) {
    .stats-bar { grid-template-columns: 1fr 1fr; gap: var(--space-lg); }
    .flagship-results { grid-template-columns: 1fr; }
    .case-results { grid-template-columns: 1fr; }
    .skills-grid, .cert-grid { grid-template-columns: 1fr; }
    .timeline-item { grid-template-columns: 1fr; gap: var(--space-sm); }
    .connect-cards { grid-template-columns: repeat(2, 1fr); }
    .testimonials-grid { grid-template-columns: 1fr; }
    .work-hero-title, .connect-hero h1 { font-size: 40px; }
}
</style>
<link href='https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap' rel='stylesheet'>
"""

# =============================================================================
# HELPERS
# =============================================================================

def render_timeline_item(years: str, role: str, company: str, desc: str = None, last: bool = False) -> str:
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

def render_skill_card(title: str, skills: list) -> str:
    return f'''
    <div class="skill-card">
        <div class="skill-card-title">{title}</div>
        <div class="skill-card-list">{'<br>'.join(skills)}</div>
    </div>'''

def render_cert_card(name: str, issuer: str) -> str:
    return f'''
    <div class="cert-card">
        <p class="cert-name">{name}</p>
        <p class="cert-issuer">{issuer}</p>
    </div>'''

def render_testimonial_card(quote: str, author: str, role: str) -> str:
    return f'''
    <div class="testimonial-card">
        <p class="testimonial-card-quote">"{quote}"</p>
        <p class="testimonial-card-author">{author}</p>
        <p class="testimonial-card-role">{role}</p>
    </div>'''

# =============================================================================
# PAGES
# =============================================================================

def render_home():
    # Hero with photo + value prop + keywords
    keywords_html = ''.join(f'<span class="hero-keyword">{k}</span>' for k in CONFIG.KEYWORDS)
    
    st.markdown(f"""
    <div class="hero">
        <div class="hero-content">
            <p class="hero-eyebrow">{CONFIG.TITLE} · 10+ Years · Currently at Advantage Solutions</p>
            <h1 class="hero-headline">I turn data chaos into<br>executive clarity</h1>
            <p class="hero-value-prop">{CONFIG.VALUE_PROP}</p>
            <div class="hero-keywords">{keywords_html}</div>
        </div>
        <div class="hero-photo-container">
            <div class="hero-photo">
                Your Photo<br>260×260
                <span class="hero-photo-hint">Add professional headshot</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats with context
    st.markdown("""
    <div class="stats-section">
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-value">10+</div>
                <div class="stat-label">Years in BI</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">$15M</div>
                <div class="stat-label">Revenue Impact</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">250+</div>
                <div class="stat-label">Users Enabled</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">70%</div>
                <div class="stat-label">Faster Decisions</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Flagship project with "THE MESS" storytelling
    st.markdown("""
    <div class="flagship">
        <div class="flagship-label">Flagship Project</div>
        <h2 class="flagship-title">Unified 5 Conflicting Data Sources Into a Single Source of Truth</h2>
        <div class="flagship-meta">
            <span class="flagship-meta-item">6 weeks</span>
            <span class="flagship-meta-item">$12M annual impact</span>
            <span class="flagship-meta-item">250 users</span>
            <span class="flagship-meta-item">5 stakeholders</span>
        </div>
        
        <div class="flagship-mess">
            <div class="flagship-mess-label">The Mess I Inherited</div>
            <p class="flagship-mess-text">
                After the merger, I found 5 sales systems that didn't talk to each other. Each region defined "revenue" differently — APAC included returns, EMEA didn't. The CFO was getting 5 different numbers in every board meeting. I had 6 weeks before Q3 close to build a single source of truth, with no dedicated engineering support and a Snowflake instance already over capacity.
            </p>
        </div>
        
        <div class="flagship-results">
            <div class="flagship-result">
                <div class="flagship-result-value">9%</div>
                <div class="flagship-result-label">Revenue Lift</div>
            </div>
            <div class="flagship-result">
                <div class="flagship-result-value">70%</div>
                <div class="flagship-result-label">Fewer Conflicts</div>
            </div>
            <div class="flagship-result">
                <div class="flagship-result-value">5→1</div>
                <div class="flagship-result-label">Day Decision Cycle</div>
            </div>
            <div class="flagship-result">
                <div class="flagship-result-value">$12M</div>
                <div class="flagship-result-label">Annual Impact</div>
            </div>
        </div>
        
        <div class="flagship-tags">
            <span class="flagship-tag">Snowflake</span>
            <span class="flagship-tag">Power BI</span>
            <span class="flagship-tag">Python</span>
            <span class="flagship-tag">DAX</span>
            <span class="flagship-tag">Stakeholder Management</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Testimonial on first scroll
    st.markdown("""
    <div class="home-testimonial">
        <div class="testimonial-content">
            <p class="testimonial-quote">For the first time in two years, I walked into a board meeting with confidence in our numbers. Jason didn't just fix our data — he changed how we think about measurement.</p>
            <p class="testimonial-author">[Name]</p>
            <p class="testimonial-role">CFO, Advantage Solutions</p>
        </div>
        <div class="testimonial-cta">
            <p class="testimonial-cta-text">See how I did it</p>
            <a href="#" class="testimonial-cta-link">View Case Study →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Secondary projects
    st.markdown("""
    <div class="projects-section">
        <div class="projects-header">
            <h2 class="projects-title">More Work</h2>
        </div>
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-company">Modern Home Station</div>
                <h3 class="project-title">+33% Conversion via A/B Testing</h3>
                <div class="project-meta">8 weeks · Cross-channel attribution</div>
                <p class="project-desc">Marketing was sending the same promotion to everyone. I built cross-channel attribution across GA4, Shopify, and Meta, then ran multivariate tests on 12 ad combinations.</p>
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
                <div class="project-company">Operations Automation</div>
                <h3 class="project-title">160 Hours Saved Quarterly</h3>
                <div class="project-meta">4 weeks · 99 vendor sources</div>
                <p class="project-desc">"Automation" meant 47 Excel macros that one person (who left) understood. I replaced it with Python pipelines that actually work.</p>
                <div class="project-metrics">
                    <div>
                        <div class="project-metric-value">160 hrs</div>
                        <div class="project-metric-label">Saved/Qtr</div>
                    </div>
                    <div>
                        <div class="project-metric-value">15→0%</div>
                        <div class="project-metric-label">Error Rate</div>
                    </div>
                    <div>
                        <div class="project-metric-value">99</div>
                        <div class="project-metric-label">Vendors</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_work():
    st.markdown("""
    <div class="work-hero">
        <h1 class="work-hero-title">Selected Work</h1>
        <p class="work-hero-sub">Deep dives into problems I've solved — the mess, the struggle, and what I learned</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 1 - Flagship (deep)
    st.markdown("""
    <div class="case-study">
        <div class="case-inner">
            <span class="case-label">Flagship Project</span>
            <h2 class="case-title">Unified Executive Intelligence</h2>
            <p class="case-subtitle">Advantage Solutions · 6 weeks · $12M impact · 250 users</p>
            
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
                    <div class="case-result-value">5→1</div>
                    <div class="case-result-label">Decision Cycle (Days)</div>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>After the merger, I inherited a nightmare: 5 sales systems that didn't talk to each other. Each region defined "revenue" differently — APAC included returns, EMEA didn't. The CFO was getting 5 different numbers in every board meeting.</p>
                <ul>
                    <li>CFO getting 5 different revenue numbers at every board meeting</li>
                    <li>Field teams created 47 shadow Excel trackers</li>
                    <li>Previous BI lead quit mid-project</li>
                    <li>Snowflake instance already over capacity</li>
                </ul>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">Why This Was Hard</h3>
                <p>This wasn't a technical problem — it was political. Each regional VP had built metrics to make their team look good. Standardizing meant someone's numbers would go down. I had to get 5 executives to agree on what "revenue" meant.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Bet</h3>
                <p>I recommended forcing standardization immediately — no parallel systems, no "legacy" reports. Leadership approved, but the timeline was non-negotiable: 6 weeks to Q3 close.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p><strong>Week 1-2:</strong> Discovery. I asked every stakeholder: "What decision are you trying to make?" Found 70% of "must-have" metrics weren't actually used.</p>
                <p><strong>Week 3:</strong> Forced alignment meeting. Locked 5 VPs in a room until we agreed on 12 golden metrics.</p>
                <p><strong>Week 4-5:</strong> Built unified Snowflake schema. Wrote 40+ DAX measures. Created single executive dashboard.</p>
                <p><strong>Week 6:</strong> Trained 250 users. Killed old reports. No going back.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">What Went Wrong</h3>
                <p>APAC had an undocumented custom field that their entire commission structure depended on. Their numbers broke Day 1 of launch. I had to patch the data model live while the regional VP was on a CEO call explaining the discrepancy.</p>
                <p>Lesson: "Undocumented" doesn't mean "unimportant." I now mandate field audits before any migration.</p>
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
            <span class="case-label">Case Study 02</span>
            <h2 class="case-title">+33% Conversion Through A/B Testing</h2>
            <p class="case-subtitle">Modern Home Station · 8 weeks · Cross-Channel Analytics</p>
            
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
                <p>Marketing was sending the same promotion to everyone. Data scattered across Facebook, Shopify, Google Analytics — no unified customer view. "Attribution" meant whoever yelled loudest got credit.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Built cross-channel attribution integrating GA4, Shopify, Meta, Klaviyo. Applied K-Means segmentation to identify 4 distinct customer personas. Led multivariate testing across 12 ad combinations.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">What Went Wrong</h3>
                <p>Saw spike in content views but no page views. Spent days debugging — mobile video sound settings were wrong, causing users to scroll past. The data was right; my interpretation was wrong.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">Results</h3>
                <ul>
                    <li>Value-based ads beat feature-based by 33% (p=0.03)</li>
                    <li>Best combo: Meme creative + Learn More CTA + Comment prompt</li>
                    <li>36% lower CPM with engagement-driven strategies</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 3
    st.markdown("""
    <div class="case-study">
        <div class="case-inner">
            <span class="case-label">Case Study 03</span>
            <h2 class="case-title">160 Hours Saved via Automation</h2>
            <p class="case-subtitle">99 Vendor Data Sources · 4 weeks · Python + SQL</p>
            
            <div class="case-results">
                <div>
                    <div class="case-result-value">160 hrs</div>
                    <div class="case-result-label">Saved Quarterly</div>
                </div>
                <div>
                    <div class="case-result-value">15→0%</div>
                    <div class="case-result-label">Error Rate</div>
                </div>
                <div>
                    <div class="case-result-value">99</div>
                    <div class="case-result-label">Vendors</div>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>"Automation" meant 47 Excel macros that one person (who left) understood. Every Monday, 3 analysts spent 4 hours manually processing vendor reports. Error rate: 15%. Finance didn't trust any of it.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Built dynamic column mapping in Python — no more breaking when vendors changed formats. Created normalization buckets aligned with GL codes. Combined Python + VBA for hybrid automation (some vendors only sent Excel files via email).</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">What Went Wrong</h3>
                <p>One vendor only sent PDF reports with inconsistent formatting — spent 2 days building a custom parser. Three vendors reported in different timezones — took a week to standardize. Never assume vendor data is clean.</p>
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
        <div class="about-photo">
            Your Photo<br>280×280
            <span style="font-size:12px;color:var(--gray-400);margin-top:8px;">Add professional headshot</span>
        </div>
        <div class="about-intro">
            <h1>Hi, I'm Jason.</h1>
            <p>I've spent the last decade helping companies <strong>stop guessing and start knowing</strong>.</p>
            <p>Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers.</p>
            <p>I've done this at Advantage Solutions, Modern Home Station, China Unicom, and Marshall Electronics.</p>
            <p><strong>What I've learned:</strong> The hard part is never the SQL. It's getting humans to agree on what "revenue" means.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience
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
    
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Experience</h2>
        <div class="timeline">
            {''.join(render_timeline_item(*e) for e in experience)}
        </div>
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
    skills = [
        ("Daily Drivers", ["SQL (10+ years)", "Power BI / DAX", "Python", "Snowflake", "Excel + VBA"]),
        ("Fluent", ["BigQuery", "GA4", "Looker", "Qlik", "Power Query"]),
        ("Statistical", ["A/B Testing", "Regression", "K-Means", "Cohort Analysis", "Forecasting"]),
    ]
    
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Skills</h2>
        <div class="skills-grid">
            {''.join(render_skill_card(t, s) for t, s in skills)}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications
    certs = [
        ("Supervised Machine Learning", "Stanford Online · 2024"),
        ("Neural Networks & Deep Learning", "DeepLearning.AI · 2024"),
        ("Power BI Data Visualization", "edX · 2019"),
    ]
    
    st.markdown(f"""
    <div class="about-section">
        <h2 class="section-title">Certifications</h2>
        <div class="cert-grid">
            {''.join(render_cert_card(n, i) for n, i in certs)}
        </div>
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
    
    st.markdown(f"""
    <div class="testimonials">
        <h2 class="section-title" style="text-align:center;margin-bottom:40px;display:block;">What Colleagues Say</h2>
        <div class="testimonials-grid">
            {''.join(render_testimonial_card(*t) for t in testimonials)}
        </div>
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
    
    # Sidebar with photo + resume download
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-brand">
            <div class="sidebar-photo">Photo</div>
            <p class="sidebar-name">{CONFIG.NAME}</p>
            <p class="sidebar-title">{CONFIG.TITLE}</p>
            <div class="sidebar-status-badge">Open to Opportunities</div>
        </div>
        """, unsafe_allow_html=True)
        
        page = st.radio("Nav", CONFIG.PAGES, label_visibility="collapsed")
        
        st.markdown("""
        <div class="sidebar-footer">
            <a href="#" class="sidebar-download">Download Resume ↓</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Route
    routes = {
        "Home": render_home,
        "Work": render_work,
        "About": render_about,
        "Connect": render_connect,
    }
    routes.get(page, render_home)()


if __name__ == "__main__":
    main()

