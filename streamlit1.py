import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Jason Chang", page_icon="◆")

# ULTIMATE AWARD-WINNING CSS
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap' rel='stylesheet'>
<style>
    :root {
        --black: #050505;
        --white: #fafafa;
        --cream: #f7f3ef;
        --cream-dark: #ebe5dd;
        --grey-50: #fafafa;
        --grey-100: #f4f4f5;
        --grey-200: #e4e4e7;
        --grey-300: #d4d4d8;
        --grey-400: #a1a1aa;
        --grey-500: #71717a;
        --grey-600: #52525b;
        --grey-700: #3f3f46;
        --grey-800: #27272a;
        --grey-900: #18181b;
        --ease: cubic-bezier(0.16, 1, 0.3, 1);
        --ease-back: cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    
    /* === SCROLLBAR === */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: var(--black); }
    ::-webkit-scrollbar-thumb { background: var(--grey-700); }
    ::-webkit-scrollbar-thumb:hover { background: var(--grey-500); }
    
    /* === BASE === */
    .stApp { background: var(--white) !important; overflow-x: hidden !important; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    /* === NOISE === */
    .stApp::before {
        content: '';
        position: fixed;
        inset: 0;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 2048 2048' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='5' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
        opacity: 0.018;
        pointer-events: none;
        z-index: 10000;
    }
    
    /* === KEYFRAMES === */
    @keyframes heroReveal {
        0% { clip-path: inset(0 0 100% 0); opacity: 0; }
        100% { clip-path: inset(0); opacity: 1; }
    }
    @keyframes heroSlide {
        0% { transform: translateY(150px) skewY(7deg); opacity: 0; }
        100% { transform: translateY(0) skewY(0); opacity: 1; }
    }
    @keyframes fadeSlideUp {
        0% { transform: translateY(60px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    @keyframes fadeSlideLeft {
        0% { transform: translateX(-40px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    @keyframes scaleIn {
        0% { transform: scale(0.8); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    @keyframes lineGrow {
        0% { transform: scaleX(0); }
        100% { transform: scaleX(1); }
    }
    @keyframes marquee {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        25% { transform: translateY(-20px) rotate(3deg); }
        75% { transform: translateY(10px) rotate(-2deg); }
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.3); opacity: 0.5; }
    }
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes dash {
        0% { stroke-dashoffset: 1000; }
        100% { stroke-dashoffset: 0; }
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes breathe {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    @keyframes borderFlow {
        0% { background-position: 0% 0%; }
        100% { background-position: 200% 0%; }
    }
    
    /* ========== SIDEBAR ========== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--black) 0%, #0d0d0d 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.03) !important;
    }
    
    section[data-testid="stSidebar"] * {
        color: var(--grey-500) !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div {
        gap: 0 !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label {
        background: transparent !important;
        color: var(--grey-500) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        padding: 22px 35px !important;
        letter-spacing: 1px !important;
        transition: all 0.6s var(--ease) !important;
        border-left: 2px solid transparent !important;
        position: relative !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label::before {
        content: '';
        position: absolute;
        left: 35px;
        bottom: 18px;
        width: 0;
        height: 1px;
        background: var(--white);
        transition: width 0.6s var(--ease);
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label:hover {
        color: var(--white) !important;
        padding-left: 45px !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label:hover::before {
        width: 20px;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] {
        color: var(--white) !important;
        font-weight: 700 !important;
        border-left-color: var(--white) !important;
        background: linear-gradient(90deg, rgba(255,255,255,0.05) 0%, transparent 100%) !important;
    }
    
    section[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"]::before {
        width: 30px;
    }
    
    .nav-brand {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 56px !important;
        color: var(--white) !important;
        letter-spacing: 8px !important;
        padding: 60px 35px 50px 35px !important;
        border-bottom: 1px solid rgba(255,255,255,0.05) !important;
        margin-bottom: 25px !important;
        position: relative;
        background: linear-gradient(90deg, var(--white) 0%, var(--grey-400) 50%, var(--white) 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 8s ease infinite;
    }
    
    .nav-year {
        position: absolute;
        bottom: 20px;
        right: 35px;
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        font-weight: 600;
        color: var(--grey-700);
        letter-spacing: 2px;
    }
    
    .nav-label {
        font-family: 'Inter', sans-serif !important;
        font-size: 9px !important;
        font-weight: 700 !important;
        color: var(--grey-700) !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        padding: 30px 35px 18px 35px !important;
    }
    
    /* ========== HERO SECTION ========== */
    .hero-container {
        display: grid;
        grid-template-columns: 58% 42%;
        min-height: 100vh;
        position: relative;
    }
    
    .hero-left {
        background: var(--black);
        padding: 100px 90px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    /* Giant background watermark */
    .hero-left::before {
        content: 'JC';
        position: absolute;
        bottom: -150px;
        right: -80px;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 700px;
        color: rgba(255,255,255,0.012);
        line-height: 0.75;
        pointer-events: none;
        letter-spacing: -30px;
    }
    
    /* Gradient line accent */
    .hero-left::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 1px;
        height: 100%;
        background: linear-gradient(180deg, transparent 0%, rgba(255,255,255,0.1) 50%, transparent 100%);
    }
    
    .hero-right {
        background: linear-gradient(145deg, var(--cream) 0%, var(--cream-dark) 100%);
        padding: 100px 80px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    /* Decorative elements */
    .deco-ring {
        position: absolute;
        width: 220px;
        height: 220px;
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 50%;
        top: 100px;
        right: 100px;
        animation: rotate 40s linear infinite;
    }
    
    .deco-ring::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 10px;
        height: 10px;
        background: var(--white);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        animation: breathe 4s ease infinite;
    }
    
    .deco-ring::after {
        content: '';
        position: absolute;
        top: -1px;
        left: 50%;
        width: 1px;
        height: 50px;
        background: linear-gradient(180deg, rgba(255,255,255,0.3) 0%, transparent 100%);
    }
    
    .deco-box {
        position: absolute;
        width: 120px;
        height: 120px;
        border: 1px solid rgba(0,0,0,0.04);
        bottom: 140px;
        right: 100px;
        animation: float 10s ease-in-out infinite;
    }
    
    .deco-box::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 6px;
        height: 6px;
        background: var(--black);
        transform: translate(-50%, -50%);
    }
    
    .deco-grid {
        position: absolute;
        top: 120px;
        left: 80px;
        display: grid;
        grid-template-columns: repeat(6, 10px);
        gap: 15px;
        opacity: 0.12;
    }
    
    .deco-dot {
        width: 3px;
        height: 3px;
        background: var(--black);
        border-radius: 50%;
    }
    
    .deco-lines {
        position: absolute;
        bottom: 100px;
        left: 80px;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    
    .deco-line {
        height: 1px;
        background: rgba(0,0,0,0.08);
    }
    
    .deco-line:nth-child(1) { width: 60px; }
    .deco-line:nth-child(2) { width: 40px; }
    .deco-line:nth-child(3) { width: 80px; }
    
    /* Badge */
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 14px;
        padding: 14px 26px;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 50px;
        margin-bottom: 80px;
        animation: fadeSlideLeft 0.8s var(--ease) 0.2s both;
        position: relative;
        overflow: hidden;
    }
    
    .hero-badge::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent);
        animation: borderFlow 3s linear infinite;
    }
    
    .badge-dot {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        animation: pulse 2s ease infinite;
        box-shadow: 0 0 20px rgba(34, 197, 94, 0.4);
    }
    
    .badge-text {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 600;
        color: var(--grey-400);
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    
    /* Hero name - MASSIVE */
    .hero-name-wrap {
        overflow: hidden;
        perspective: 1000px;
    }
    
    .hero-name {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 240px !important;
        font-weight: 400 !important;
        color: var(--white) !important;
        letter-spacing: -6px !important;
        line-height: 0.78 !important;
        margin: 0 !important;
        animation: heroSlide 1.4s var(--ease) both !important;
        transform-origin: bottom left;
    }
    
    .hero-name-2 { animation-delay: 0.12s !important; }
    
    .hero-name-stroke {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 240px !important;
        color: transparent !important;
        -webkit-text-stroke: 1px rgba(255,255,255,0.15) !important;
        letter-spacing: -6px !important;
        line-height: 0.78 !important;
        margin: 0 !important;
        animation: heroSlide 1.4s var(--ease) 0.24s both !important;
        transform-origin: bottom left;
    }
    
    .hero-role-wrap {
        display: flex;
        align-items: center;
        gap: 30px;
        margin-top: 70px;
    }
    
    .hero-line {
        width: 100px;
        height: 1px;
        background: linear-gradient(90deg, var(--grey-500), transparent);
        animation: lineGrow 1s var(--ease) 0.8s both;
        transform-origin: left;
    }
    
    .hero-role {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 700;
        color: var(--grey-500);
        letter-spacing: 6px;
        text-transform: uppercase;
        animation: fadeSlideLeft 0.8s var(--ease) 0.9s both;
    }
    
    /* Hero right content */
    .hero-eyebrow {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 800;
        color: var(--grey-500);
        letter-spacing: 6px;
        text-transform: uppercase;
        margin-bottom: 40px;
        animation: fadeSlideLeft 0.8s var(--ease) 0.3s both;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .hero-eyebrow::before {
        content: '';
        width: 30px;
        height: 1px;
        background: var(--grey-400);
    }
    
    .hero-headline {
        font-family: 'Playfair Display', serif !important;
        font-size: 64px !important;
        font-weight: 500 !important;
        color: var(--black) !important;
        line-height: 1.1 !important;
        margin-bottom: 40px !important;
        animation: fadeSlideUp 1s var(--ease) 0.4s both !important;
    }
    
    .hero-headline em {
        font-style: italic;
        font-weight: 400;
    }
    
    .hero-body {
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        color: var(--grey-600) !important;
        line-height: 2 !important;
        max-width: 400px !important;
        animation: fadeSlideUp 1s var(--ease) 0.6s both !important;
    }
    
    .hero-cta {
        display: inline-flex;
        align-items: center;
        gap: 18px;
        margin-top: 60px;
        padding: 22px 45px;
        background: var(--black);
        color: var(--white) !important;
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        text-decoration: none !important;
        transition: all 0.6s var(--ease);
        animation: fadeSlideUp 1s var(--ease) 0.8s both;
        position: relative;
        overflow: hidden;
    }
    
    .hero-cta::before {
        content: '';
        position: absolute;
        inset: 0;
        background: var(--white);
        transform: translateX(-100%);
        transition: transform 0.6s var(--ease);
    }
    
    .hero-cta:hover::before {
        transform: translateX(0);
    }
    
    .hero-cta:hover {
        color: var(--black) !important;
    }
    
    .hero-cta span {
        position: relative;
        z-index: 1;
    }
    
    .hero-cta-arrow {
        transition: transform 0.6s var(--ease);
    }
    
    .hero-cta:hover .hero-cta-arrow {
        transform: translateX(8px);
    }
    
    /* ========== MARQUEE ========== */
    .marquee-wrap {
        background: var(--black);
        padding: 35px 0;
        overflow: hidden;
        border-top: 1px solid rgba(255,255,255,0.03);
        border-bottom: 1px solid rgba(255,255,255,0.03);
        position: relative;
    }
    
    .marquee-wrap::before,
    .marquee-wrap::after {
        content: '';
        position: absolute;
        top: 0;
        width: 150px;
        height: 100%;
        z-index: 2;
        pointer-events: none;
    }
    
    .marquee-wrap::before {
        left: 0;
        background: linear-gradient(90deg, var(--black), transparent);
    }
    
    .marquee-wrap::after {
        right: 0;
        background: linear-gradient(-90deg, var(--black), transparent);
    }
    
    .marquee-track {
        display: flex;
        animation: marquee 40s linear infinite;
        width: max-content;
    }
    
    .marquee-item {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 15px;
        color: var(--grey-600);
        letter-spacing: 10px;
        white-space: nowrap;
        padding: 0 35px;
        display: flex;
        align-items: center;
        gap: 35px;
    }
    
    .marquee-dot {
        width: 4px;
        height: 4px;
        background: var(--grey-700);
        border-radius: 50%;
    }
    
    /* ========== STATS ========== */
    .stats-wrap {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        background: var(--white);
    }
    
    .stat-box {
        padding: 120px 60px;
        text-align: center;
        border-right: 1px solid var(--grey-200);
        position: relative;
        overflow: hidden;
        transition: all 0.8s var(--ease);
    }
    
    .stat-box:last-child { border-right: none; }
    
    .stat-box::before {
        content: '';
        position: absolute;
        inset: 0;
        background: var(--black);
        transform: translateY(100%);
        transition: transform 0.8s var(--ease);
    }
    
    .stat-box::after {
        content: attr(data-label);
        position: absolute;
        top: 30px;
        left: 30px;
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: var(--grey-300);
        transition: color 0.8s var(--ease);
    }
    
    .stat-box:hover::before { transform: translateY(0); }
    .stat-box:hover::after { color: var(--grey-600); }
    .stat-box:hover .stat-num, .stat-box:hover .stat-label { color: var(--white) !important; }
    
    .stat-num {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 180px !important;
        color: var(--black) !important;
        line-height: 0.85 !important;
        position: relative;
        z-index: 1;
        transition: color 0.8s var(--ease);
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 700 !important;
        color: var(--grey-500) !important;
        margin-top: 30px !important;
        text-transform: uppercase !important;
        letter-spacing: 6px !important;
        position: relative;
        z-index: 1;
        transition: color 0.8s var(--ease);
    }
    
    /* ========== SECTIONS ========== */
    .section-dark {
        background: var(--black);
        padding: 200px 100px 140px 100px;
        position: relative;
        overflow: hidden;
    }
    
    .section-dark::before {
        content: attr(data-num);
        position: absolute;
        top: 100px;
        right: 80px;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 400px;
        color: rgba(255,255,255,0.015);
        line-height: 1;
        pointer-events: none;
    }
    
    .section-dark::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 100px;
        right: 100px;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
    }
    
    .section-light {
        padding: 200px 100px 140px 100px;
        position: relative;
        overflow: hidden;
    }
    
    .section-light::before {
        content: attr(data-num);
        position: absolute;
        top: 100px;
        right: 80px;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 400px;
        color: rgba(0,0,0,0.02);
        line-height: 1;
        pointer-events: none;
    }
    
    .section-tag {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 50px;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .section-tag-dark { color: var(--grey-600); }
    .section-tag-light { color: var(--grey-400); }
    
    .section-tag::before {
        content: '';
        width: 50px;
        height: 1px;
        background: currentColor;
    }
    
    .section-title {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 200px !important;
        letter-spacing: -6px !important;
        line-height: 0.82 !important;
        margin: 0 !important;
    }
    
    .section-title-dark { color: var(--white) !important; }
    .section-title-light { color: var(--black) !important; }
    
    /* ========== CONTENT ========== */
    .content-dark {
        background: var(--black);
        padding: 0 100px 180px 100px;
    }
    
    .content-light {
        padding: 0 100px 180px 100px;
    }
    
    /* ========== SUBSECTION ========== */
    .sub-wrap {
        display: grid;
        grid-template-columns: 160px 1fr;
        gap: 60px;
        margin-top: 140px;
        margin-bottom: 60px;
    }
    
    .sub-num {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 140px;
        line-height: 0.75;
    }
    
    .sub-num-dark { color: rgba(255,255,255,0.06); }
    .sub-num-light { color: var(--grey-200); }
    
    .sub-content { padding-top: 20px; }
    
    .sub-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 800 !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        margin-bottom: 35px !important;
        padding-bottom: 18px !important;
        display: inline-block !important;
        position: relative;
    }
    
    .sub-title::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
    }
    
    .sub-title-dark { color: var(--white) !important; }
    .sub-title-dark::after { background: var(--grey-800); }
    .sub-title-light { color: var(--black) !important; }
    .sub-title-light::after { background: var(--grey-300); }
    
    /* ========== BODY ========== */
    .body {
        font-family: 'Inter', sans-serif !important;
        font-size: 17px !important;
        line-height: 2 !important;
        max-width: 580px !important;
    }
    
    .body-dark { color: var(--grey-400) !important; }
    .body-dark strong { color: var(--white) !important; font-weight: 600 !important; }
    .body-light { color: var(--grey-600) !important; }
    .body-light strong { color: var(--black) !important; font-weight: 600 !important; }
    
    /* ========== BULLETS ========== */
    .bullet {
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        line-height: 2 !important;
        margin-bottom: 20px !important;
        padding-left: 55px !important;
        position: relative !important;
        transition: all 0.6s var(--ease) !important;
    }
    
    .bullet::before {
        content: '';
        position: absolute;
        left: 0;
        top: 14px;
        width: 30px;
        height: 1px;
        transition: all 0.6s var(--ease);
    }
    
    .bullet:hover { padding-left: 85px !important; }
    .bullet:hover::before { width: 60px; }
    
    .bullet-dark { color: var(--grey-400) !important; }
    .bullet-dark::before { background: var(--grey-700); }
    .bullet-dark:hover { color: var(--white) !important; }
    .bullet-dark:hover::before { background: var(--white); }
    .bullet-dark strong { color: var(--white) !important; font-weight: 600 !important; }
    
    .bullet-light { color: var(--grey-600) !important; }
    .bullet-light::before { background: var(--grey-300); }
    .bullet-light:hover { color: var(--black) !important; }
    .bullet-light:hover::before { background: var(--black); }
    .bullet-light strong { color: var(--black) !important; font-weight: 600 !important; }
    
    /* ========== RESULT CARDS ========== */
    .result-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 40px;
        margin-top: 80px;
    }
    
    .result-card {
        background: var(--grey-100);
        padding: 90px 70px;
        position: relative;
        overflow: hidden;
        transition: all 0.8s var(--ease);
    }
    
    .result-card::before {
        content: '';
        position: absolute;
        left: 0;
        bottom: 0;
        width: 100%;
        height: 6px;
        background: var(--black);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.8s var(--ease);
    }
    
    .result-card::after {
        content: '+';
        position: absolute;
        top: 50px;
        right: 50px;
        font-family: 'Inter', sans-serif;
        font-size: 28px;
        font-weight: 300;
        color: var(--grey-300);
        transition: all 0.8s var(--ease);
    }
    
    .result-card:hover {
        transform: translateY(-25px);
        box-shadow: 0 60px 120px rgba(0,0,0,0.12);
    }
    
    .result-card:hover::before { transform: scaleX(1); }
    .result-card:hover::after { transform: rotate(45deg); color: var(--black); }
    
    .result-num {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 140px !important;
        color: var(--black) !important;
        line-height: 0.85 !important;
    }
    
    .result-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 800 !important;
        color: var(--black) !important;
        margin: 35px 0 18px 0 !important;
        text-transform: uppercase !important;
        letter-spacing: 5px !important;
    }
    
    .result-desc {
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        color: var(--grey-500) !important;
        line-height: 1.8 !important;
    }
    
    /* ========== INFO CARDS ========== */
    .info-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 35px;
        margin-top: 70px;
    }
    
    .info-card {
        background: var(--grey-100);
        padding: 60px;
        transition: all 0.7s var(--ease);
        position: relative;
        overflow: hidden;
    }
    
    .info-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: var(--black);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.7s var(--ease);
    }
    
    .info-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 40px 80px rgba(0,0,0,0.1);
    }
    
    .info-card:hover::after { transform: scaleX(1); }
    
    .info-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 800 !important;
        color: var(--black) !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        margin-bottom: 20px !important;
    }
    
    .info-desc {
        font-family: 'Inter', sans-serif !important;
        font-size: 15px !important;
        color: var(--grey-500) !important;
        line-height: 1.9 !important;
    }
    
    /* ========== SKILLS ========== */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }
    
    .skill-card {
        background: var(--grey-100);
        padding: 55px;
        transition: all 0.7s var(--ease);
        position: relative;
        overflow: hidden;
    }
    
    .skill-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 0;
        background: var(--black);
        transition: height 0.7s var(--ease);
    }
    
    .skill-card:hover { transform: translateX(20px); }
    .skill-card:hover::before { height: 100%; }
    
    .skill-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 800 !important;
        color: var(--black) !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        margin-bottom: 20px !important;
    }
    
    .skill-list {
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        color: var(--grey-500) !important;
        line-height: 2.2 !important;
    }
    
    /* ========== CERTS ========== */
    .cert-item {
        display: grid;
        grid-template-columns: 140px 1fr auto;
        gap: 60px;
        align-items: center;
        padding: 55px 0;
        border-bottom: 1px solid var(--grey-200);
        transition: all 0.6s var(--ease);
    }
    
    .cert-item:hover { padding-left: 30px; }
    
    .cert-num {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 100px;
        color: var(--grey-200);
        line-height: 0.9;
    }
    
    .cert-content { flex: 1; }
    
    .cert-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 22px !important;
        font-weight: 600 !important;
        color: var(--black) !important;
        margin-bottom: 10px !important;
    }
    
    .cert-org {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        color: var(--grey-500) !important;
    }
    
    .cert-link {
        font-family: 'Inter', sans-serif !important;
        font-size: 10px !important;
        font-weight: 800 !important;
        color: var(--black) !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        text-decoration: none !important;
        padding: 18px 35px !important;
        border: 1px solid var(--grey-300) !important;
        transition: all 0.5s var(--ease) !important;
    }
    
    .cert-link:hover {
        background: var(--black) !important;
        color: var(--white) !important;
        border-color: var(--black) !important;
    }
    
    /* ========== CONTACT ========== */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 35px;
    }
    
    .contact-card {
        background: var(--grey-100);
        padding: 55px 60px;
        transition: all 0.6s var(--ease);
        position: relative;
        overflow: hidden;
    }
    
    .contact-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: var(--black);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.6s var(--ease);
    }
    
    .contact-card:hover::after { transform: scaleX(1); }
    
    .contact-label {
        font-family: 'Inter', sans-serif !important;
        font-size: 9px !important;
        font-weight: 800 !important;
        color: var(--grey-400) !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        margin-bottom: 18px !important;
    }
    
    .contact-value {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 24px !important;
        font-weight: 500 !important;
        color: var(--black) !important;
    }
    
    /* ========== QUOTE ========== */
    .quote-section {
        background: linear-gradient(145deg, var(--cream) 0%, var(--cream-dark) 100%);
        padding: 180px 100px;
        position: relative;
        overflow: hidden;
    }
    
    .quote-mark {
        font-family: 'Playfair Display', serif;
        font-size: 500px;
        color: rgba(0,0,0,0.02);
        position: absolute;
        top: -50px;
        left: 30px;
        line-height: 1;
        pointer-events: none;
    }
    
    .quote-text {
        font-family: 'Playfair Display', serif !important;
        font-size: 50px !important;
        font-weight: 400 !important;
        font-style: italic !important;
        color: var(--black) !important;
        line-height: 1.35 !important;
        max-width: 800px !important;
        position: relative;
        z-index: 1;
    }
    
    /* ========== MISC ========== */
    .code-label {
        font-family: 'Inter', sans-serif !important;
        font-size: 9px !important;
        font-weight: 800 !important;
        color: var(--grey-400) !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        margin-bottom: 30px !important;
    }
    
    .divider {
        width: 100%;
        height: 1px;
        background: var(--grey-200);
        margin: 140px 0;
    }
    
    a {
        color: var(--black) !important;
        text-decoration: none !important;
        transition: opacity 0.3s ease !important;
    }
    
    a:hover { opacity: 0.6 !important; }
    
    .stImage img {
        transition: all 0.9s var(--ease) !important;
    }
    
    .stImage img:hover {
        transform: scale(1.025) !important;
        box-shadow: 0 70px 140px rgba(0,0,0,0.15) !important;
    }
    
    h1, h2, h3 { font-family: 'Bebas Neue', sans-serif !important; }
    p, li { font-family: 'Inter', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

def scroll_to_top():
    components.html("""<script>
        const c = [window.parent.document.querySelector('.main'),window.parent.document.querySelector('[data-testid="stAppViewContainer"]'),window.parent.document.body,window.parent.document.documentElement];
        c.forEach(x=>{if(x){x.scrollTop=0;x.scrollTo({top:0,behavior:'instant'});}});
    </script>""", height=0, width=0)

with st.sidebar:
    st.markdown('<div class="nav-brand">JC<span class="nav-year">©2025</span></div>', unsafe_allow_html=True)
    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    page = st.radio("", ["Home","Engagement","Executive","Warehouse","Automation","Skills","Certs","Contact"], label_visibility="collapsed")

scroll_to_top()

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

data = load_data("https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv")

# ===================== HOME =====================
if page == "Home":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-left">
            <div class="deco-ring"></div>
            <div class="hero-badge">
                <span class="badge-dot"></span>
                <span class="badge-text">Open to Work</span>
            </div>
            <div class="hero-name-wrap"><p class="hero-name">JASON</p></div>
            <div class="hero-name-wrap"><p class="hero-name hero-name-2">CHANG</p></div>
            <div class="hero-name-wrap"><p class="hero-name-stroke">PORTFOLIO</p></div>
            <div class="hero-role-wrap">
                <div class="hero-line"></div>
                <span class="hero-role">Data Analytics</span>
            </div>
        </div>
        <div class="hero-right">
            <div class="deco-box"></div>
            <div class="deco-grid">
                <span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span>
                <span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span>
                <span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span><span class="deco-dot"></span>
            </div>
            <div class="deco-lines">
                <span class="deco-line"></span>
                <span class="deco-line"></span>
                <span class="deco-line"></span>
            </div>
            <p class="hero-eyebrow">About Me</p>
            <p class="hero-headline">Turning <em>complex data</em> into strategic growth.</p>
            <p class="hero-body">Revenue Growth Leader with 10+ years scaling national programs. Proficient in Snowflake, SQL, Power BI, and Python.</p>
            <a href="#" class="hero-cta"><span>View Work</span> <span class="hero-cta-arrow">→</span></a>
        </div>
    </div>
    
    <div class="marquee-wrap">
        <div class="marquee-track">
            <span class="marquee-item">ANALYTICS <span class="marquee-dot"></span> SNOWFLAKE <span class="marquee-dot"></span> PYTHON <span class="marquee-dot"></span> SQL <span class="marquee-dot"></span> POWER BI <span class="marquee-dot"></span> DATA ENGINEERING <span class="marquee-dot"></span> VISUALIZATION <span class="marquee-dot"></span></span>
            <span class="marquee-item">ANALYTICS <span class="marquee-dot"></span> SNOWFLAKE <span class="marquee-dot"></span> PYTHON <span class="marquee-dot"></span> SQL <span class="marquee-dot"></span> POWER BI <span class="marquee-dot"></span> DATA ENGINEERING <span class="marquee-dot"></span> VISUALIZATION <span class="marquee-dot"></span></span>
        </div>
    </div>
    
    <div class="stats-wrap">
        <div class="stat-box" data-label="01">
            <p class="stat-num">10+</p>
            <p class="stat-label">Years Experience</p>
        </div>
        <div class="stat-box" data-label="02">
            <p class="stat-num">85%</p>
            <p class="stat-label">Efficiency Gains</p>
        </div>
        <div class="stat-box" data-label="03">
            <p class="stat-num">21%</p>
            <p class="stat-label">Revenue Growth</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== ENGAGEMENT =====================
elif page == "Engagement":
    st.markdown('<div class="section-dark" data-num="01"><p class="section-tag section-tag-dark"><span>Case Study</span></p><p class="section-title section-title-dark">PLAYER<br>ENGAGEMENT</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-dark">', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-dark">01</span><div class="sub-content"><p class="sub-title sub-title-dark">Situation</p><p class="body body-dark">Tasked with maximizing revenue and player engagement for Warcraft during two key in-game events. Challenge: understanding player segment behavior and identifying monetization opportunities.</p></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-dark">02</span><div class="sub-content"><p class="sub-title sub-title-dark">Task</p><p class="bullet bullet-dark">Identify high-spending player segments for targeted promotions</p><p class="bullet bullet-dark">Analyze low spending trends by region and platform</p><p class="bullet bullet-dark">Conduct exploratory analysis on spending behaviors</p></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-dark">03</span><div class="sub-content"><p class="sub-title sub-title-dark">Action</p><p class="bullet bullet-dark"><strong>EDA & Clustering</strong> — Python-based analysis with K-Means segmentation</p><p class="bullet bullet-dark"><strong>Heatmap Analysis</strong> — Identified spending patterns across segments</p><p class="bullet bullet-dark"><strong>Strategic Output</strong> — Prioritized Platform 3, Region 1</p></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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

    heatmap_data = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    fig1, ax1 = plt.subplots(figsize=(9, 5))
    fig1.patch.set_facecolor('#050505')
    ax1.set_facecolor('#050505')
    sns.heatmap(heatmap_data, annot=True, cmap="Greys", fmt=".2f", linewidths=5, ax=ax1, annot_kws={"color": "#fafafa", "fontsize": 13, "fontweight": "bold"}, linecolor='#050505', cbar=False)
    ax1.tick_params(colors='#fafafa', labelsize=11)
    ax1.set_xlabel('', fontsize=0)
    ax1.set_ylabel('', fontsize=0)
    for spine in ax1.spines.values():
        spine.set_visible(False)
    st.pyplot(fig1)
    plt.close(fig1)

    e1 = data[(data['Date'] >= '2017-01-24') & (data['Date'] <= '2017-02-14')]
    e2 = data[(data['Date'] >= '2017-02-28') & (data['Date'] <= '2017-03-21')]
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    fig.patch.set_facecolor('#fafafa')
    for ax in axes.flat:
        ax.set_facecolor('#fafafa')
        ax.tick_params(colors='#050505', labelsize=9)
        for spine in ax.spines.values():
            spine.set_visible(False)
    for idx, (col, title) in enumerate([('games_played', 'GAMES'), ('skill_last', 'SKILL'), ('items_crafted', 'ITEMS'), ('dollars_spent', 'SPEND')]):
        ax = axes[idx // 2, idx % 2]
        sns.kdeplot(e1[col], fill=True, color="#050505", label="Event 1", ax=ax, alpha=0.12)
        sns.kdeplot(e2[col], fill=True, color="#71717a", label="Event 2", ax=ax, alpha=0.2)
        ax.set_title(title, fontsize=11, fontweight='700', color='#050505')
        ax.legend(fontsize=8, frameon=False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', use_container_width=True)

    st.markdown('<div class="content-light"><div class="sub-wrap"><span class="sub-num sub-num-light">04</span><div class="sub-content"><p class="sub-title sub-title-light">Results</p></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="result-grid">
        <div class="result-card">
            <p class="result-num">+21%</p>
            <p class="result-title">Engagement Increase</p>
            <p class="result-desc">Targeted promotions in high-value segments</p>
        </div>
        <div class="result-card">
            <p class="result-num">-15%</p>
            <p class="result-title">Churn Reduction</p>
            <p class="result-desc">Strategic adjustments improved retention</p>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# ===================== EXECUTIVE =====================
elif page == "Executive":
    st.markdown('<div class="section-light" data-num="02"><p class="section-tag section-tag-light"><span>Case Study</span></p><p class="section-title section-title-light">EXECUTIVE<br>INTELLIGENCE</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-light">', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">01</span><div class="sub-content"><p class="sub-title sub-title-light">Situation</p><p class="body body-light">Post-merger environment with fragmented data across systems. Finance lacked unified performance measurement.</p></div></div>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', use_container_width=True)
    
    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">02</span><div class="sub-content"><p class="sub-title sub-title-light">Task</p><p class="body body-light">Design dynamic reporting solution with accurate KPIs for executive decision-making.</p></div></div>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', use_container_width=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">03</span><div class="sub-content"><p class="sub-title sub-title-light">Action</p><p class="bullet bullet-light"><strong>Data Engineering</strong> — SQL extraction, deduplication, normalization</p><p class="bullet bullet-light"><strong>Schema Design</strong> — Flexible architecture for evolving needs</p><p class="bullet bullet-light"><strong>Dashboard</strong> — Stakeholder collaboration on key metrics</p></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">04</span><div class="sub-content"><p class="sub-title sub-title-light">Results</p></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-grid">
        <div class="info-card">
            <p class="info-title">Strategic Planning</p>
            <p class="info-desc">Enhanced management decision-making with real-time insights</p>
        </div>
        <div class="info-card">
            <p class="info-title">Adaptive Reporting</p>
            <p class="info-desc">Scalable system that evolves with business changes</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ===================== WAREHOUSE =====================
elif page == "Warehouse":
    st.markdown('<div class="section-dark" data-num="03"><p class="section-tag section-tag-dark"><span>Case Study</span></p><p class="section-title section-title-dark">WAREHOUSE<br>OPTIMIZATION</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-dark">', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-dark">01</span><div class="sub-content"><p class="sub-title sub-title-dark">Situation</p><p class="body body-dark">Escalating logistics costs impacting bottom line. SKYLAB and 3PL Logistics identified as key areas for potential inefficiency.</p></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-dark">02</span><div class="sub-content"><p class="sub-title sub-title-dark">Task</p><p class="body body-dark">Conduct detailed cost analysis to identify waste and optimization opportunities.</p></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-dark">03</span><div class="sub-content"><p class="sub-title sub-title-dark">Action</p><p class="bullet bullet-dark"><strong>Financial Analysis</strong> — Python deep dive into expenditure patterns</p><p class="bullet bullet-dark"><strong>Inefficiency Mapping</strong> — Pinpointed cost drivers in both divisions</p><p class="bullet bullet-dark"><strong>Strategy</strong> — Recommendations for operations and vendor contracts</p></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', use_container_width=True)

    st.markdown('<div class="content-light"><div class="sub-wrap"><span class="sub-num sub-num-light">04</span><div class="sub-content"><p class="sub-title sub-title-light">Results</p><p class="bullet bullet-light"><strong>Cost Reduction</strong> — Identified inefficiencies leading to significant savings</p><p class="bullet bullet-light"><strong>Streamlined Ops</strong> — Process improvements with positive P&L impact</p><p class="bullet bullet-light"><strong>Framework</strong> — Established ongoing optimization process</p></div></div></div>', unsafe_allow_html=True)

# ===================== AUTOMATION =====================
elif page == "Automation":
    st.markdown('<div class="section-light" data-num="04"><p class="section-tag section-tag-light"><span>Case Study</span></p><p class="section-title section-title-light">ROYALTY<br>AUTOMATION</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-light">', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">01</span><div class="sub-content"><p class="sub-title sub-title-light">Situation</p><p class="body body-light">Month-long manual Excel lookups across years of unorganized data. High error risk, significant analyst burden.</p></div></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="code-label">PYTHON AUTOMATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', use_container_width=True)
    with col2:
        st.markdown('<p class="code-label">VBA INTEGRATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', use_container_width=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">02</span><div class="sub-content"><p class="sub-title sub-title-light">Task</p><p class="body body-light">Transform month-long manual process into automated workflow while maintaining accuracy.</p></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">03</span><div class="sub-content"><p class="sub-title sub-title-light">Action</p><p class="bullet bullet-light"><strong>Data Audit</strong> — Mapped historical structures and requirements</p><p class="bullet bullet-light"><strong>Python Pipeline</strong> — Automated consolidation and validation</p><p class="bullet bullet-light"><strong>VBA</strong> — Automated Excel report generation</p></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-wrap"><span class="sub-num sub-num-light">04</span><div class="sub-content"><p class="sub-title sub-title-light">Results</p></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stats-wrap" style="margin-top:60px;">
        <div class="stat-box" data-label="A">
            <p class="stat-num">85%</p>
            <p class="stat-label">Time Saved</p>
        </div>
        <div class="stat-box" data-label="B">
            <p class="stat-num">2</p>
            <p class="stat-label">FTEs Freed</p>
        </div>
        <div class="stat-box" data-label="C">
            <p class="stat-num">↑</p>
            <p class="stat-label">Accuracy</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ===================== SKILLS =====================
elif page == "Skills":
    st.markdown('<div class="section-dark" data-num="★"><p class="section-tag section-tag-dark"><span>Expertise</span></p><p class="section-title section-title-dark">TECHNICAL<br>SKILLS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-light">', unsafe_allow_html=True)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=180)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skills-grid">
        <div class="skill-card">
            <p class="skill-title">Languages</p>
            <p class="skill-list">Python<br>SQL<br>VBA</p>
        </div>
        <div class="skill-card">
            <p class="skill-title">Engineering</p>
            <p class="skill-list">Snowflake<br>ETL / ELT<br>SSMS / AS400</p>
        </div>
        <div class="skill-card">
            <p class="skill-title">Analytics</p>
            <p class="skill-list">Pandas / NumPy<br>Seaborn<br>Matplotlib</p>
        </div>
        <div class="skill-card">
            <p class="skill-title">Statistics</p>
            <p class="skill-list">A/B Testing<br>Regression<br>Time Series</p>
        </div>
        <div class="skill-card">
            <p class="skill-title">Visualization</p>
            <p class="skill-list">Power BI<br>Looker Studio<br>Google Analytics</p>
        </div>
        <div class="skill-card">
            <p class="skill-title">Modeling</p>
            <p class="skill-list">Star Schema<br>DAG / ERD<br>Normalization</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ===================== CERTS =====================
elif page == "Certs":
    st.markdown('<div class="section-light" data-num="✓"><p class="section-tag section-tag-light"><span>Credentials</span></p><p class="section-title section-title-light">CERTIFICATIONS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-light">', unsafe_allow_html=True)
    
    certs = [
        ("01", "Supervised Machine Learning", "Stanford / Coursera · 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/STANDFORD.PNG", "https://www.coursera.org/account/accomplishments/verify/YHLXRW3TL569"),
        ("02", "Neural Networks & Deep Learning", "DeepLearning.AI · 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/DeepAI", "https://www.coursera.org/account/accomplishments/verify/P3MNNDS44DLL"),
        ("03", "Power BI Data Visualization", "EdX · 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/edx", "https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79"),
        ("04", "AWS Cloud Practitioner", "Amazon Web Services · 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/AWS1", None),
        ("05", "SQL Certification", "Sololearn · 2017", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/SQLsololearn", "https://www.sololearn.com/en/certificates/CT-YUFRJBUH")
    ]
    
    for num, title, org, img, link in certs:
        link_html = f'<a href="{link}" target="_blank" class="cert-link">Verify</a>' if link else '<span class="cert-link" style="opacity:0.3;pointer-events:none;">—</span>'
        st.markdown(f'<div class="cert-item"><span class="cert-num">{num}</span><div class="cert-content"><p class="cert-title">{title}</p><p class="cert-org">{org}</p></div>{link_html}</div>', unsafe_allow_html=True)
        st.image(img, width=360)
    st.markdown('</div>', unsafe_allow_html=True)

# ===================== CONTACT =====================
elif page == "Contact":
    st.markdown('<div class="section-dark" data-num="→"><p class="section-tag section-tag-dark"><span>Get in Touch</span></p><p class="section-title section-title-dark">LET\'S<br>CONNECT</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote-section">
        <span class="quote-mark">"</span>
        <p class="quote-text">In God we trust; for all else, we turn to the validation of data.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="content-light">', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-grid">
        <div class="contact-card">
            <p class="contact-label">Phone</p>
            <p class="contact-value">(626) 203-3319</p>
        </div>
        <div class="contact-card">
            <p class="contact-label">Email</p>
            <p class="contact-value">jason.chang01022021@gmail.com</p>
        </div>
        <div class="contact-card">
            <p class="contact-label">LinkedIn</p>
            <p class="contact-value"><a href="https://linkedin.com/in/jchang0102">linkedin.com/in/jchang0102</a></p>
        </div>
        <div class="contact-card">
            <p class="contact-label">Location</p>
            <p class="contact-value">Irvine, CA</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
