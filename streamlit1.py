import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Jason Chang | BI Manager", page_icon="◆")

# Session state
if 'prev_page' not in st.session_state:
    st.session_state.prev_page = None

st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap' rel='stylesheet'>
<style>
    :root{
        --b:#0a0a0a;--w:#ffffff;
        --g1:#fafafa;--g2:#f5f5f5;--g3:#e5e5e5;--g4:#d4d4d4;--g5:#a3a3a3;--g6:#737373;--g7:#525252;--g8:#262626;--g9:#171717;
        --accent:#3b82f6;--accent2:#8b5cf6;--accent3:#06b6d4;
        --gradient:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);
    }
    
    ::-webkit-scrollbar{width:6px}
    ::-webkit-scrollbar-track{background:transparent}
    ::-webkit-scrollbar-thumb{background:var(--g5);border-radius:3px}
    ::-webkit-scrollbar-thumb:hover{background:var(--g6)}
    
    .stApp{background:var(--w)!important;overflow-x:hidden!important}
    #MainMenu,footer,header{visibility:hidden}
    .block-container{padding:0!important;max-width:100%!important}
    
    /* Subtle grain texture */
    .stApp::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");opacity:0.015;pointer-events:none;z-index:10000}
    
    /* === ANIMATIONS === */
    @keyframes fadeUp{0%{opacity:0;transform:translateY(30px)}100%{opacity:1;transform:translateY(0)}}
    @keyframes fadeIn{0%{opacity:0}100%{opacity:1}}
    @keyframes slideIn{0%{opacity:0;transform:translateX(-20px)}100%{opacity:1;transform:translateX(0)}}
    @keyframes scaleIn{0%{opacity:0;transform:scale(0.95)}100%{opacity:1;transform:scale(1)}}
    @keyframes pulse{0%,100%{opacity:1}50%{opacity:0.5}}
    @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
    @keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
    @keyframes gradient{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
    @keyframes borderGlow{0%,100%{border-color:rgba(59,130,246,0.3)}50%{border-color:rgba(59,130,246,0.6)}}
    @keyframes rotate{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
    @keyframes countUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
    
    /* === SIDEBAR === */
    section[data-testid="stSidebar"]{background:var(--b)!important;border-right:none!important;min-width:260px!important}
    section[data-testid="stSidebar"]>div:first-child{padding:0!important}
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"]{display:none!important}
    
    div.stRadio>div{flex-direction:column!important;gap:0!important}
    div[role="radiogroup"]>label[data-baseweb="radio"]>div:first-child{display:none!important}
    
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]{
        background:transparent!important;padding:16px 32px!important;margin:0!important;cursor:pointer!important;
        border:none!important;position:relative;transition:all 0.3s cubic-bezier(0.4,0,0.2,1)!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]::before{
        content:'';position:absolute;left:0;top:50%;transform:translateY(-50%);width:0;height:2px;
        background:var(--gradient);transition:width 0.3s ease
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]:hover::before{width:16px}
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"][data-checked="true"]::before{width:24px}
    
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"] p{
        font-family:'Inter',sans-serif!important;font-size:14px!important;font-weight:400!important;
        color:rgba(255,255,255,0.4)!important;margin:0!important;transition:all 0.3s ease!important;
        padding-left:8px!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]:hover p{
        color:rgba(255,255,255,0.8)!important;padding-left:16px!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"][data-checked="true"] p{
        color:#ffffff!important;font-weight:500!important;padding-left:20px!important
    }
    
    .sb-brand{padding:48px 32px 40px;border-bottom:1px solid rgba(255,255,255,0.06)}
    .sb-name{font-family:'Outfit',sans-serif;font-size:18px;font-weight:600;color:#fff;letter-spacing:1px;margin:0 0 6px}
    .sb-title{font-family:'Inter',sans-serif;font-size:12px;font-weight:400;color:rgba(255,255,255,0.4);margin:0}
    .sb-status{display:flex;align-items:center;gap:8px;margin-top:16px;font-family:'Inter',sans-serif;font-size:11px;color:#22c55e}
    .sb-status::before{content:'';width:6px;height:6px;background:#22c55e;border-radius:50%;animation:pulse 2s infinite}
    .sb-footer{position:absolute;bottom:0;left:0;right:0;padding:24px 32px;font-family:'Inter',sans-serif;font-size:10px;color:rgba(255,255,255,0.2);border-top:1px solid rgba(255,255,255,0.04)}
    
    /* === HOME HERO === */
    .home-hero{
        min-height:90vh;padding:80px;display:flex;align-items:center;
        background:linear-gradient(135deg,#fafafa 0%,#f0f0f0 50%,#fafafa 100%);
        position:relative;overflow:hidden
    }
    .home-hero::before{
        content:'';position:absolute;top:-50%;right:-20%;width:80%;height:200%;
        background:radial-gradient(ellipse,rgba(59,130,246,0.03) 0%,transparent 70%);
        pointer-events:none
    }
    .hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;max-width:1400px;margin:0 auto;align-items:center}
    
    .hero-content{animation:fadeUp 0.8s ease}
    .hero-eyebrow{
        display:inline-flex;align-items:center;gap:8px;
        font-family:'Inter',sans-serif;font-size:12px;font-weight:500;
        color:var(--accent);letter-spacing:2px;text-transform:uppercase;margin-bottom:24px;
        padding:8px 16px;background:rgba(59,130,246,0.08);border-radius:100px
    }
    .hero-eyebrow::before{content:'◆';font-size:8px}
    
    .hero-title{
        font-family:'Outfit',sans-serif;font-size:clamp(40px,5vw,64px);font-weight:700;
        color:var(--b);line-height:1.1;margin-bottom:24px;
        background:linear-gradient(135deg,var(--b) 0%,var(--g7) 100%);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text
    }
    .hero-title span{
        background:var(--gradient);-webkit-background-clip:text;background-clip:text;
        -webkit-text-fill-color:transparent
    }
    
    .hero-subtitle{
        font-family:'Inter',sans-serif;font-size:18px;font-weight:400;
        color:var(--g6);line-height:1.7;margin-bottom:40px;max-width:500px
    }
    
    .hero-cta{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:32px}
    .btn{
        font-family:'Inter',sans-serif;font-size:14px;font-weight:500;
        padding:14px 28px;border-radius:8px;text-decoration:none;
        transition:all 0.3s cubic-bezier(0.4,0,0.2,1);display:inline-flex;align-items:center;gap:8px;
        position:relative;overflow:hidden
    }
    .btn-primary{
        color:#fff;background:var(--b);border:none;
        box-shadow:0 4px 14px rgba(0,0,0,0.1)
    }
    .btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,0,0,0.15)}
    .btn-primary::after{
        content:'→';transition:transform 0.3s ease;display:inline-block
    }
    .btn-primary:hover::after{transform:translateX(4px)}
    
    .btn-secondary{
        color:var(--b);background:transparent;border:1.5px solid var(--g4)
    }
    .btn-secondary:hover{border-color:var(--b);background:rgba(0,0,0,0.02)}
    
    .hero-stats{display:flex;gap:40px;padding-top:32px;border-top:1px solid var(--g3)}
    .hero-stat{text-align:left}
    .hero-stat-value{
        font-family:'Outfit',sans-serif;font-size:32px;font-weight:700;color:var(--b);
        background:var(--gradient);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent
    }
    .hero-stat-label{font-family:'Inter',sans-serif;font-size:12px;color:var(--g6);margin-top:4px}
    
    /* Hero Visual */
    .hero-visual{animation:fadeUp 0.8s ease 0.2s both;position:relative}
    .hero-card{
        background:#fff;border-radius:20px;padding:40px;
        box-shadow:0 25px 80px rgba(0,0,0,0.08),0 10px 30px rgba(0,0,0,0.04);
        position:relative;overflow:hidden;
        border:1px solid rgba(0,0,0,0.04)
    }
    .hero-card::before{
        content:'';position:absolute;top:0;left:0;right:0;height:4px;
        background:var(--gradient)
    }
    .card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:32px}
    .card-dots{display:flex;gap:6px}
    .card-dot{width:10px;height:10px;border-radius:50%;background:var(--g3)}
    .card-dot:first-child{background:#ef4444}
    .card-dot:nth-child(2){background:#f59e0b}
    .card-dot:last-child{background:#22c55e}
    .card-title{font-family:'Inter',sans-serif;font-size:12px;color:var(--g5);font-weight:500}
    
    .metric-row{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:24px}
    .metric-card{
        background:var(--g1);border-radius:12px;padding:20px;text-align:center;
        transition:all 0.3s ease;cursor:default
    }
    .metric-card:hover{transform:translateY(-4px);box-shadow:0 8px 25px rgba(0,0,0,0.06)}
    .metric-card-value{font-family:'Outfit',sans-serif;font-size:28px;font-weight:700;color:var(--b)}
    .metric-card-label{font-family:'Inter',sans-serif;font-size:11px;color:var(--g6);margin-top:4px;text-transform:uppercase;letter-spacing:0.5px}
    
    .chart-placeholder{
        height:120px;background:linear-gradient(90deg,var(--g1) 0%,var(--g2) 50%,var(--g1) 100%);
        background-size:200% 100%;animation:shimmer 2s infinite;border-radius:12px;
        display:flex;align-items:center;justify-content:center;
        font-family:'Inter',sans-serif;font-size:12px;color:var(--g5)
    }
    
    /* Floating elements */
    .float-badge{
        position:absolute;padding:12px 16px;background:#fff;border-radius:12px;
        box-shadow:0 8px 30px rgba(0,0,0,0.1);font-family:'Inter',sans-serif;font-size:12px;
        display:flex;align-items:center;gap:8px;animation:float 4s ease-in-out infinite
    }
    .float-badge.top-left{top:-20px;left:-20px;animation-delay:0s}
    .float-badge.bottom-right{bottom:-20px;right:-20px;animation-delay:1s}
    .float-badge-icon{font-size:16px}
    .float-badge-text{color:var(--g7);font-weight:500}
    .float-badge-value{color:var(--accent);font-weight:600}
    
    /* === FEATURED WORK === */
    .section{padding:100px 80px}
    .section-dark{background:var(--b);color:#fff}
    .section-alt{background:var(--g1)}
    
    .section-header{max-width:1400px;margin:0 auto 60px;display:flex;justify-content:space-between;align-items:end}
    .section-header-left{}
    .section-label{
        font-family:'Inter',sans-serif;font-size:12px;font-weight:500;
        color:var(--accent);letter-spacing:2px;text-transform:uppercase;margin-bottom:12px
    }
    .section-dark .section-label{color:var(--accent3)}
    .section-title{font-family:'Outfit',sans-serif;font-size:42px;font-weight:600;color:var(--b)}
    .section-dark .section-title{color:#fff}
    .section-subtitle{font-family:'Inter',sans-serif;font-size:16px;color:var(--g6);margin-top:12px;max-width:500px}
    .section-dark .section-subtitle{color:rgba(255,255,255,0.5)}
    
    /* Work Cards */
    .work-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:32px;max-width:1400px;margin:0 auto}
    
    .work-card{
        background:#fff;border-radius:16px;overflow:hidden;
        transition:all 0.4s cubic-bezier(0.4,0,0.2,1);
        border:1px solid var(--g3);position:relative;cursor:pointer
    }
    .work-card:hover{transform:translateY(-8px);box-shadow:0 25px 60px rgba(0,0,0,0.12)}
    .work-card:hover .card-thumb{transform:scale(1.05)}
    .work-card:hover .card-arrow{transform:translate(4px,-4px)}
    
    .work-card.featured{
        grid-column:span 2;display:grid;grid-template-columns:1.1fr 1fr;
        background:linear-gradient(135deg,var(--b) 0%,#1a1a2e 100%);border:none
    }
    .work-card.featured .card-content{color:#fff;padding:48px}
    .work-card.featured .card-label{color:var(--accent3)}
    .work-card.featured .card-title{color:#fff}
    .work-card.featured .card-desc{color:rgba(255,255,255,0.6)}
    .work-card.featured .card-meta{border-color:rgba(255,255,255,0.1)}
    .work-card.featured .card-meta span{color:rgba(255,255,255,0.5)}
    .work-card.featured .card-meta strong{color:#fff}
    .work-card.featured .card-arrow{color:#fff}
    .work-card.featured:hover{transform:translateY(-8px);box-shadow:0 30px 80px rgba(0,0,0,0.3)}
    
    .card-thumb-wrap{overflow:hidden;height:220px}
    .work-card.featured .card-thumb-wrap{height:100%;min-height:350px}
    .card-thumb{
        height:100%;background:linear-gradient(135deg,var(--g2) 0%,var(--g3) 100%);
        display:flex;align-items:center;justify-content:center;
        transition:transform 0.6s cubic-bezier(0.4,0,0.2,1)
    }
    .work-card.featured .card-thumb{background:linear-gradient(135deg,#1e3a5f 0%,#0f172a 100%)}
    .card-thumb-text{font-family:'Inter',sans-serif;font-size:13px;color:var(--g5)}
    .work-card.featured .card-thumb-text{color:rgba(255,255,255,0.3)}
    
    .card-content{padding:32px}
    .card-label{
        font-family:'Inter',sans-serif;font-size:11px;font-weight:600;
        color:var(--accent);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px;
        display:flex;align-items:center;gap:8px
    }
    .card-label-badge{
        padding:4px 8px;background:rgba(59,130,246,0.1);border-radius:4px;font-size:10px
    }
    .work-card.featured .card-label-badge{background:rgba(6,182,212,0.2)}
    
    .card-title{font-family:'Outfit',sans-serif;font-size:22px;font-weight:600;color:var(--b);line-height:1.3;margin-bottom:12px}
    .card-desc{font-family:'Inter',sans-serif;font-size:14px;color:var(--g6);line-height:1.6;margin-bottom:20px}
    
    .card-meta{
        display:flex;gap:24px;padding-top:20px;border-top:1px solid var(--g3);
        font-family:'Inter',sans-serif;font-size:12px
    }
    .card-meta span{color:var(--g5)}
    .card-meta strong{color:var(--b);font-weight:600}
    
    .card-footer{display:flex;justify-content:space-between;align-items:center;margin-top:20px}
    .card-tags{display:flex;gap:8px;flex-wrap:wrap}
    .card-tag{
        font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--g6);
        background:var(--g1);padding:6px 10px;border-radius:6px
    }
    .work-card.featured .card-tag{background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.7)}
    
    .card-arrow{
        width:40px;height:40px;border-radius:50%;background:var(--g1);
        display:flex;align-items:center;justify-content:center;
        font-size:18px;color:var(--b);transition:all 0.3s ease
    }
    .work-card.featured .card-arrow{background:rgba(255,255,255,0.1)}
    
    /* === STATS SECTION === */
    .stats-section{padding:80px;background:var(--b)}
    .stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:40px;max-width:1200px;margin:0 auto}
    .stat-item{text-align:center;padding:40px;position:relative}
    .stat-item::after{
        content:'';position:absolute;right:0;top:20%;height:60%;width:1px;
        background:linear-gradient(180deg,transparent,rgba(255,255,255,0.1),transparent)
    }
    .stat-item:last-child::after{display:none}
    .stat-value{
        font-family:'Outfit',sans-serif;font-size:56px;font-weight:700;
        background:linear-gradient(135deg,#fff 0%,rgba(255,255,255,0.7) 100%);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text
    }
    .stat-label{font-family:'Inter',sans-serif;font-size:14px;color:rgba(255,255,255,0.4);margin-top:8px}
    
    /* === TESTIMONIAL === */
    .testimonial-section{padding:100px 80px;background:var(--g1)}
    .testimonial-card{
        max-width:900px;margin:0 auto;text-align:center;
        background:#fff;border-radius:24px;padding:60px;
        box-shadow:0 20px 60px rgba(0,0,0,0.05);position:relative
    }
    .testimonial-card::before{
        content:'"';position:absolute;top:30px;left:50px;
        font-family:'Playfair Display',serif;font-size:120px;color:var(--g2);line-height:1
    }
    .testimonial-quote{
        font-family:'Playfair Display',serif;font-size:28px;font-style:italic;
        color:var(--b);line-height:1.6;margin-bottom:40px;position:relative;z-index:1
    }
    .testimonial-author{display:flex;align-items:center;justify-content:center;gap:16px}
    .testimonial-avatar{
        width:56px;height:56px;border-radius:50%;background:var(--gradient);
        display:flex;align-items:center;justify-content:center;color:#fff;font-weight:600
    }
    .testimonial-info{text-align:left}
    .testimonial-name{font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:var(--b)}
    .testimonial-role{font-family:'Inter',sans-serif;font-size:13px;color:var(--g6)}
    
    /* === WORK PAGE === */
    .page-hero{padding:80px;background:var(--b);text-align:center}
    .page-hero-title{font-family:'Outfit',sans-serif;font-size:56px;font-weight:700;color:#fff;margin-bottom:16px}
    .page-hero-sub{font-family:'Inter',sans-serif;font-size:18px;color:rgba(255,255,255,0.5)}
    
    .case-study{padding:100px 80px;border-bottom:1px solid var(--g3)}
    .case-study:nth-child(even){background:var(--g1)}
    .case-container{max-width:1000px;margin:0 auto}
    
    .case-header{margin-bottom:48px}
    .case-number{
        font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:500;
        color:var(--accent);letter-spacing:2px;margin-bottom:16px
    }
    .case-title{font-family:'Outfit',sans-serif;font-size:42px;font-weight:700;color:var(--b);line-height:1.2;margin-bottom:12px}
    .case-subtitle{font-family:'Inter',sans-serif;font-size:18px;color:var(--g6)}
    
    .case-results{
        background:var(--b);border-radius:20px;padding:48px;margin-bottom:60px;
        display:grid;grid-template-columns:repeat(3,1fr);gap:32px
    }
    .case-result{text-align:center;padding:20px}
    .case-result-value{font-family:'Outfit',sans-serif;font-size:48px;font-weight:700;color:#fff}
    .case-result-label{font-family:'Inter',sans-serif;font-size:13px;color:rgba(255,255,255,0.5);margin-top:8px}
    .case-results-meta{
        grid-column:span 3;display:flex;justify-content:center;gap:40px;
        padding-top:24px;border-top:1px solid rgba(255,255,255,0.1);
        font-family:'Inter',sans-serif;font-size:14px;color:rgba(255,255,255,0.6)
    }
    .case-results-meta strong{color:#fff}
    
    .case-section{margin-bottom:48px}
    .case-section-title{
        font-family:'Outfit',sans-serif;font-size:24px;font-weight:600;color:var(--b);
        margin-bottom:20px;display:flex;align-items:center;gap:12px
    }
    .case-section-title::before{
        content:'';width:4px;height:24px;background:var(--gradient);border-radius:2px
    }
    .case-section p{font-family:'Inter',sans-serif;font-size:16px;color:var(--g7);line-height:1.8;margin-bottom:16px}
    .case-section ul{margin:0 0 16px;padding-left:0;list-style:none}
    .case-section li{
        font-family:'Inter',sans-serif;font-size:16px;color:var(--g7);line-height:1.8;
        margin-bottom:12px;padding-left:24px;position:relative
    }
    .case-section li::before{
        content:'';position:absolute;left:0;top:10px;width:8px;height:8px;
        background:var(--gradient);border-radius:50%
    }
    
    .case-quote{
        background:linear-gradient(135deg,rgba(59,130,246,0.05) 0%,rgba(139,92,246,0.05) 100%);
        border-left:4px solid var(--accent);padding:32px 40px;margin:40px 0;border-radius:0 16px 16px 0
    }
    .case-quote p{font-family:'Inter',sans-serif;font-size:18px;font-style:italic;color:var(--accent);margin:0!important}
    .case-quote cite{font-family:'Inter',sans-serif;font-size:14px;color:var(--g6);font-style:normal;display:block;margin-top:16px}
    
    /* === ABOUT PAGE === */
    .about-hero{padding:80px;background:linear-gradient(180deg,var(--g1) 0%,#fff 100%)}
    .about-grid{display:grid;grid-template-columns:320px 1fr;gap:80px;max-width:1200px;margin:0 auto;align-items:start}
    
    .about-photo-wrap{position:sticky;top:100px}
    .about-photo{
        width:280px;height:280px;border-radius:20px;
        background:linear-gradient(135deg,var(--g2) 0%,var(--g3) 100%);
        display:flex;align-items:center;justify-content:center;
        font-family:'Inter',sans-serif;font-size:13px;color:var(--g5);
        box-shadow:0 25px 80px rgba(0,0,0,0.1);position:relative;overflow:hidden
    }
    .about-photo::before{
        content:'';position:absolute;inset:0;background:var(--gradient);opacity:0.1
    }
    
    .about-content h1{
        font-family:'Outfit',sans-serif;font-size:48px;font-weight:700;
        color:var(--b);margin-bottom:32px;line-height:1.2
    }
    .about-content p{font-family:'Inter',sans-serif;font-size:17px;color:var(--g7);line-height:1.8;margin-bottom:20px}
    
    .about-section{padding:80px;border-top:1px solid var(--g3)}
    .about-section:nth-child(even){background:var(--g1)}
    .about-section-inner{max-width:1000px;margin:0 auto}
    .about-section h2{font-family:'Outfit',sans-serif;font-size:32px;font-weight:600;color:var(--b);margin-bottom:40px}
    
    /* Timeline */
    .timeline{position:relative;padding-left:40px}
    .timeline::before{content:'';position:absolute;left:11px;top:8px;bottom:8px;width:2px;background:var(--g3)}
    .timeline-item{position:relative;margin-bottom:40px;padding-bottom:40px;border-bottom:1px solid var(--g3)}
    .timeline-item:last-child{margin-bottom:0;padding-bottom:0;border-bottom:none}
    .timeline-item::before{
        content:'';position:absolute;left:-40px;top:6px;width:24px;height:24px;
        background:#fff;border:3px solid var(--accent);border-radius:50%;z-index:1
    }
    .timeline-year{font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:500;color:var(--accent);margin-bottom:8px}
    .timeline-role{font-family:'Outfit',sans-serif;font-size:20px;font-weight:600;color:var(--b)}
    .timeline-company{font-family:'Inter',sans-serif;font-size:14px;color:var(--g6);margin-top:4px}
    .timeline-desc{font-family:'Inter',sans-serif;font-size:14px;color:var(--g6);margin-top:12px;line-height:1.6}
    
    /* Skills */
    .skills-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:40px}
    .skill-category{
        background:#fff;border-radius:16px;padding:32px;
        border:1px solid var(--g3);transition:all 0.3s ease
    }
    .skill-category:hover{border-color:var(--accent);box-shadow:0 10px 40px rgba(59,130,246,0.1)}
    .skill-category h3{
        font-family:'Inter',sans-serif;font-size:12px;font-weight:600;
        color:var(--accent);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:16px
    }
    .skill-category p{font-family:'Inter',sans-serif;font-size:15px;color:var(--b);line-height:1.8}
    
    /* Certifications */
    .cert-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
    .cert-card{
        display:flex;gap:20px;padding:28px;background:#fff;
        border:1px solid var(--g3);border-radius:16px;transition:all 0.3s ease
    }
    .cert-card:hover{border-color:var(--accent);transform:translateY(-4px);box-shadow:0 15px 40px rgba(0,0,0,0.08)}
    .cert-icon{
        width:56px;height:56px;background:linear-gradient(135deg,var(--g1) 0%,var(--g2) 100%);
        border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0
    }
    .cert-info h4{font-family:'Outfit',sans-serif;font-size:16px;font-weight:600;color:var(--b);margin-bottom:6px}
    .cert-info p{font-family:'Inter',sans-serif;font-size:13px;color:var(--g6)}
    
    .resume-btn{
        display:inline-flex;align-items:center;gap:10px;
        font-family:'Inter',sans-serif;font-size:14px;font-weight:600;
        color:#fff;background:var(--b);padding:18px 36px;border-radius:12px;
        text-decoration:none;transition:all 0.3s ease;margin-top:32px
    }
    .resume-btn:hover{background:var(--accent);transform:translateY(-2px);box-shadow:0 10px 30px rgba(59,130,246,0.3)}
    
    /* === CONNECT PAGE === */
    .connect-hero{padding:100px 80px;background:var(--b);text-align:center}
    .connect-hero h1{font-family:'Outfit',sans-serif;font-size:56px;font-weight:700;color:#fff;margin-bottom:20px}
    .connect-hero p{font-family:'Inter',sans-serif;font-size:18px;color:rgba(255,255,255,0.5);max-width:600px;margin:0 auto}
    
    .connect-grid{
        display:grid;grid-template-columns:repeat(4,1fr);gap:20px;
        max-width:1000px;margin:60px auto 0
    }
    .connect-card{
        background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
        border-radius:16px;padding:32px;text-align:center;transition:all 0.3s ease
    }
    .connect-card:hover{background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.15);transform:translateY(-4px)}
    .connect-card-icon{font-size:28px;margin-bottom:16px}
    .connect-card-label{font-family:'Inter',sans-serif;font-size:11px;font-weight:500;color:rgba(255,255,255,0.4);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px}
    .connect-card-value{font-family:'Inter',sans-serif;font-size:14px;color:#fff;word-break:break-all}
    .connect-card a{color:var(--accent3);text-decoration:none;transition:color 0.3s}
    .connect-card a:hover{color:#fff}
    
    .testimonials-section{padding:100px 80px;background:#fff}
    .testimonials-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:32px;max-width:1100px;margin:0 auto}
    .test-card{
        background:var(--g1);border-radius:20px;padding:40px;
        border:1px solid var(--g3);transition:all 0.3s ease;position:relative
    }
    .test-card:hover{border-color:var(--accent);box-shadow:0 15px 50px rgba(59,130,246,0.08)}
    .test-card::before{
        content:'"';position:absolute;top:20px;right:30px;
        font-family:'Playfair Display',serif;font-size:80px;color:var(--g3);line-height:1
    }
    .test-quote{font-family:'Inter',sans-serif;font-size:15px;color:var(--g7);line-height:1.7;margin-bottom:24px;font-style:italic;position:relative;z-index:1}
    .test-author{font-family:'Inter',sans-serif;font-size:14px;color:var(--b);font-weight:600}
    .test-role{font-family:'Inter',sans-serif;font-size:13px;color:var(--g6);margin-top:4px}
</style>
""", unsafe_allow_html=True)

# === SIDEBAR ===
with st.sidebar:
    st.markdown('''
    <div class="sb-brand">
        <p class="sb-name">Jason Chang</p>
        <p class="sb-title">BI Manager</p>
        <div class="sb-status">Open to opportunities</div>
    </div>
    ''', unsafe_allow_html=True)
    page = st.radio("", ["Home", "Work", "About", "Connect"], label_visibility="collapsed")
    st.markdown('<p class="sb-footer">© 2025 · Built with passion</p>', unsafe_allow_html=True)

# === HOME PAGE ===
if page == "Home":
    st.markdown("""
    <div class="home-hero">
        <div class="hero-grid">
            <div class="hero-content">
                <div class="hero-eyebrow">BI Manager · 10+ Years</div>
                <h1 class="hero-title">I turn messy data into <span>executive decisions</span></h1>
                <p class="hero-subtitle">From Blizzard to Fortune 500 — I help companies find the revenue hiding in their data. I don't just build dashboards. I build clarity.</p>
                <div class="hero-cta">
                    <a href="#" class="btn btn-primary">View My Work</a>
                    <a href="#" class="btn btn-secondary">Download Resume</a>
                </div>
                <div class="hero-stats">
                    <div class="hero-stat">
                        <div class="hero-stat-value">10+</div>
                        <div class="hero-stat-label">Years Experience</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-value">$15M+</div>
                        <div class="hero-stat-label">Revenue Impact</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-value">250+</div>
                        <div class="hero-stat-label">Users Enabled</div>
                    </div>
                </div>
            </div>
            <div class="hero-visual">
                <div class="hero-card">
                    <div class="card-header">
                        <div class="card-dots"><span class="card-dot"></span><span class="card-dot"></span><span class="card-dot"></span></div>
                        <span class="card-title">Executive Dashboard</span>
                    </div>
                    <div class="metric-row">
                        <div class="metric-card">
                            <div class="metric-card-value">9%</div>
                            <div class="metric-card-label">Revenue Lift</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-value">70%</div>
                            <div class="metric-card-label">Fewer Conflicts</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-card-value">5→1</div>
                            <div class="metric-card-label">Day Decision</div>
                        </div>
                    </div>
                    <div class="chart-placeholder">📊 Interactive Chart Preview</div>
                </div>
                <div class="float-badge top-left">
                    <span class="float-badge-icon">⚡</span>
                    <span class="float-badge-text">Query Time</span>
                    <span class="float-badge-value">-70%</span>
                </div>
                <div class="float-badge bottom-right">
                    <span class="float-badge-icon">📈</span>
                    <span class="float-badge-text">ROAS</span>
                    <span class="float-badge-value">+36%</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured Work
    st.markdown("""
    <div class="section">
        <div class="section-header">
            <div class="section-header-left">
                <div class="section-label">Featured Work</div>
                <h2 class="section-title">Case Studies</h2>
                <p class="section-subtitle">Deep dives into problems I've solved and the business impact delivered.</p>
            </div>
        </div>
        <div class="work-grid">
            <div class="work-card featured">
                <div class="card-thumb-wrap">
                    <div class="card-thumb"><span class="card-thumb-text">[Dashboard Preview]</span></div>
                </div>
                <div class="card-content">
                    <div class="card-label"><span class="card-label-badge">★ FLAGSHIP</span> Advantage Solutions</div>
                    <h3 class="card-title">Unified 5 Conflicting Data Sources Into Single Source of Truth</h3>
                    <p class="card-desc">Post-merger chaos: 5 sales domains, 5 definitions of "revenue." CFO getting conflicting numbers every board meeting. I had 6 weeks to fix it.</p>
                    <div class="card-meta">
                        <span><strong>9%</strong> Revenue Lift</span>
                        <span><strong>70%</strong> Fewer Conflicts</span>
                        <span><strong>6 weeks</strong> Timeline</span>
                    </div>
                    <div class="card-footer">
                        <div class="card-tags">
                            <span class="card-tag">Snowflake</span>
                            <span class="card-tag">Power BI</span>
                            <span class="card-tag">Python</span>
                        </div>
                        <div class="card-arrow">↗</div>
                    </div>
                </div>
            </div>
            
            <div class="work-card">
                <div class="card-thumb-wrap">
                    <div class="card-thumb"><span class="card-thumb-text">[A/B Test Visual]</span></div>
                </div>
                <div class="card-content">
                    <div class="card-label">Modern Home Station</div>
                    <h3 class="card-title">+33% Conversion via A/B Testing & Attribution Modeling</h3>
                    <p class="card-desc">Built cross-channel attribution framework and led A/B testing program that optimized marketing spend and increased site conversion.</p>
                    <div class="card-meta">
                        <span><strong>+33%</strong> Conversion</span>
                        <span><strong>-18%</strong> CPA</span>
                    </div>
                    <div class="card-footer">
                        <div class="card-tags">
                            <span class="card-tag">GA4</span>
                            <span class="card-tag">Python</span>
                            <span class="card-tag">K-Means</span>
                        </div>
                        <div class="card-arrow">↗</div>
                    </div>
                </div>
            </div>
            
            <div class="work-card">
                <div class="card-thumb-wrap">
                    <div class="card-thumb"><span class="card-thumb-text">[Pipeline Diagram]</span></div>
                </div>
                <div class="card-content">
                    <div class="card-label">Operations Automation</div>
                    <h3 class="card-title">160 Hours Saved Quarterly via Pipeline Automation</h3>
                    <p class="card-desc">Replaced 47 manual Excel macros with automated Python pipelines. Error rate dropped from 15% to near zero.</p>
                    <div class="card-meta">
                        <span><strong>160 hrs</strong> Saved/Qtr</span>
                        <span><strong>99</strong> Vendors</span>
                    </div>
                    <div class="card-footer">
                        <div class="card-tags">
                            <span class="card-tag">Python</span>
                            <span class="card-tag">SQL</span>
                            <span class="card-tag">VBA</span>
                        </div>
                        <div class="card-arrow">↗</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats
    st.markdown("""
    <div class="stats-section">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-value">10+</div>
                <div class="stat-label">Years in BI & Analytics</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">$15M+</div>
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
    
    # Testimonial
    st.markdown("""
    <div class="testimonial-section">
        <div class="testimonial-card">
            <p class="testimonial-quote">Jason doesn't just build dashboards — he asks the questions that change how we think about the business. For the first time in two years, I walked into a board meeting with confidence in our numbers.</p>
            <div class="testimonial-author">
                <div class="testimonial-avatar">VP</div>
                <div class="testimonial-info">
                    <p class="testimonial-name">[Name]</p>
                    <p class="testimonial-role">VP of Sales · [Company]</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === WORK PAGE ===
elif page == "Work":
    st.markdown("""
    <div class="page-hero">
        <h1 class="page-hero-title">Selected Work</h1>
        <p class="page-hero-sub">Deep dives into problems I've solved</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 1
    st.markdown("""
    <div class="case-study">
        <div class="case-container">
            <div class="case-header">
                <div class="case-number">// CASE STUDY 01</div>
                <h2 class="case-title">Unified Executive Intelligence</h2>
                <p class="case-subtitle">How I turned 5 conflicting data sources into a single source of truth</p>
            </div>
            
            <div class="case-results">
                <div class="case-result">
                    <div class="case-result-value">9%</div>
                    <div class="case-result-label">Quarterly Revenue Lift</div>
                </div>
                <div class="case-result">
                    <div class="case-result-value">70%</div>
                    <div class="case-result-label">Fewer KPI Conflicts</div>
                </div>
                <div class="case-result">
                    <div class="case-result-value">5→1</div>
                    <div class="case-result-label">Day Decision Cycle</div>
                </div>
                <div class="case-results-meta">
                    <span><strong>Timeline:</strong> 6 weeks</span>
                    <span><strong>Impact:</strong> ~$12M annually</span>
                    <span><strong>Users:</strong> 250+</span>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>After the acquisition, I inherited a nightmare: 5 sales domains, each with their own "source of truth." APAC counted returns in revenue. EMEA didn't. Nobody knew which was right.</p>
                <ul>
                    <li>The CFO was getting 5 different revenue numbers at every board meeting</li>
                    <li>Field teams had created 47 shadow Excel trackers</li>
                    <li>The previous BI lead had quit mid-project</li>
                </ul>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">Why This Was Hard</h3>
                <p>This wasn't a technical problem. It was a political one. Each regional VP had built metrics to make their team look good. Standardizing meant someone's numbers would go down.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p><strong>Week 1-2: Discovery</strong> — Spent two weeks asking one question: "What decision are you trying to make with this data?"</p>
                <p><strong>Week 3: The Hard Conversation</strong> — Presented CFO with options and recommended forcing standardization now.</p>
                <p><strong>Week 4-5: Build</strong> — Consolidated into unified Snowflake schema, created 12 golden metrics.</p>
                <p><strong>Week 6: Rollout</strong> — Trained 250 users, killed access to old reports.</p>
            </div>
            
            <div class="case-quote">
                <p>"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
                <cite>— CFO, [Company]</cite>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 2
    st.markdown("""
    <div class="case-study">
        <div class="case-container">
            <div class="case-header">
                <div class="case-number">// CASE STUDY 02</div>
                <h2 class="case-title">+33% Conversion Through A/B Testing & Attribution</h2>
                <p class="case-subtitle">Modern Home Station · Cross-Channel Analytics</p>
            </div>
            
            <div class="case-results">
                <div class="case-result">
                    <div class="case-result-value">+33%</div>
                    <div class="case-result-label">Conversion Rate</div>
                </div>
                <div class="case-result">
                    <div class="case-result-value">-18%</div>
                    <div class="case-result-label">CPA Reduction</div>
                </div>
                <div class="case-result">
                    <div class="case-result-value">2x</div>
                    <div class="case-result-label">ROAS Improvement</div>
                </div>
                <div class="case-results-meta">
                    <span><strong>Timeline:</strong> Ongoing</span>
                    <span><strong>Revenue:</strong> +45% (FY19), +85% (FY20)</span>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>Marketing was sending the same ads to everyone. Data existed but was scattered across Facebook, Shopify, and Google Analytics with no unified view of the customer journey.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Applied a 7-layer data framework: Business requirements → Data cleaning → Exploratory analysis → Customer segmentation (K-Means) → Validation → Time series → Integration.</p>
                <p>Built cross-channel attribution framework integrating GA4, Shopify, Meta, and Klaviyo. Led A/B testing program testing meme formats, CTAs, and interaction prompts.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">A/B Test Results</h3>
                <ul>
                    <li>Value-based ads outperformed feature-based by 33% (p-value 0.03)</li>
                    <li>Best combination: Meme #2 + Learn More CTA + Comment prompt</li>
                    <li>36% lower CPM with engagement-driven strategies</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Case Study 3
    st.markdown("""
    <div class="case-study">
        <div class="case-container">
            <div class="case-header">
                <div class="case-number">// CASE STUDY 03</div>
                <h2 class="case-title">160 Hours Saved via Pipeline Automation</h2>
                <p class="case-subtitle">99 Vendor Data Sources · Python + SQL</p>
            </div>
            
            <div class="case-results">
                <div class="case-result">
                    <div class="case-result-value">160 hrs</div>
                    <div class="case-result-label">Saved Quarterly</div>
                </div>
                <div class="case-result">
                    <div class="case-result-value">15%→0%</div>
                    <div class="case-result-label">Error Rate</div>
                </div>
                <div class="case-result">
                    <div class="case-result-value">99</div>
                    <div class="case-result-label">Vendors Automated</div>
                </div>
                <div class="case-results-meta">
                    <span><strong>Timeline:</strong> 8 weeks</span>
                    <span><strong>Tools:</strong> Python, SQL, VBA</span>
                </div>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">The Mess</h3>
                <p>"Automation" meant 47 Excel macros that one person (who left) understood. Every Monday, 3 analysts spent 4 hours manually downloading vendor reports. Error rate: 15%.</p>
            </div>
            
            <div class="case-section">
                <h3 class="case-section-title">My Approach</h3>
                <p>Built dynamic column mapping in Python to handle non-standardized headers. Created vendor normalization buckets aligned with GL codes. Combined Python and VBA for hybrid automation.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === ABOUT PAGE ===
elif page == "About":
    st.markdown("""
    <div class="about-hero">
        <div class="about-grid">
            <div class="about-photo-wrap">
                <div class="about-photo">Your Photo Here<br>(280×280px)</div>
            </div>
            <div class="about-content">
                <h1>Hi, I'm Jason.</h1>
                <p>I've spent the last decade helping companies stop guessing and start knowing. Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers.</p>
                <p>I've done this at Advantage Solutions (250+ users, $6B+ sales impact), Modern Home Station (2x ROAS, 45-85% revenue growth), and earlier at China Unicom and Marshall Electronics.</p>
                <p><strong>What I've learned:</strong> The hard part is never the SQL. It's getting humans to agree on what "revenue" means.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline
    st.markdown("""
    <div class="about-section">
        <div class="about-section-inner">
            <h2>Career Timeline</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-year">2021 — Present</div>
                    <div class="timeline-role">BI Manager</div>
                    <div class="timeline-company">Advantage Solutions</div>
                    <div class="timeline-desc">Built national Power BI ecosystem with Snowflake. Unified 5 fragmented sales domains. Automated ingestion across 99+ vendors. Managed 7 regional managers.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2017 — 2021</div>
                    <div class="timeline-role">BI Strategy & Analytics Manager</div>
                    <div class="timeline-company">Modern Home Station</div>
                    <div class="timeline-desc">Deployed cross-channel attribution (GA4, Shopify, Meta). Led A/B testing program. Built lead-scoring and intent models. Revenue growth: 45% (FY19), 85% (FY20).</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2016 — 2017</div>
                    <div class="timeline-role">BI & Strategic Development Manager</div>
                    <div class="timeline-company">China Unicom America</div>
                    <div class="timeline-desc">Built GTM pricing and demand forecast models. $2M+ revenue projections. Automated churn and usage reporting.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2014 — 2016</div>
                    <div class="timeline-role">BI Project Analyst</div>
                    <div class="timeline-company">Marshall Electronics</div>
                    <div class="timeline-desc">50+ international product launches, $5M annual sales. 95% on-time launch rate.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2010 — 2014</div>
                    <div class="timeline-role">Senior Business Analyst</div>
                    <div class="timeline-company">Cadence Acoustic Ltd.</div>
                    <div class="timeline-desc">Migrated forecasting from Excel to SQL dashboards. Managed BI systems tracking $500M in product lines.</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills
    st.markdown("""
    <div class="about-section">
        <div class="about-section-inner">
            <h2>Technical Skills</h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <h3>Daily Drivers</h3>
                    <p>SQL (10+ years), Power BI / DAX, Python, Snowflake, Excel (Advanced + VBA)</p>
                </div>
                <div class="skill-category">
                    <h3>Fluent</h3>
                    <p>BigQuery, GA4, Looker, Qlik, Google Data Studio, Power Query</p>
                </div>
                <div class="skill-category">
                    <h3>Statistical & ML</h3>
                    <p>A/B Testing, Regression, K-Means Clustering, Cohort Analysis, Forecasting, Causal Inference</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("""
    <div class="about-section">
        <div class="about-section-inner">
            <h2>Certifications</h2>
            <div class="cert-grid">
                <div class="cert-card">
                    <div class="cert-icon">🎓</div>
                    <div class="cert-info">
                        <h4>Supervised Machine Learning</h4>
                        <p>Stanford Online · June 2024</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon">🧠</div>
                    <div class="cert-info">
                        <h4>Neural Networks & Deep Learning</h4>
                        <p>DeepLearning.AI · April 2024</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon">📊</div>
                    <div class="cert-info">
                        <h4>Analyzing & Visualizing Data with Power BI</h4>
                        <p>edX · July 2019</p>
                    </div>
                </div>
            </div>
            <a href="#" class="resume-btn">📄 Download Resume (PDF)</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === CONNECT PAGE ===
elif page == "Connect":
    st.markdown("""
    <div class="connect-hero">
        <h1>Let's Talk</h1>
        <p>I'm currently open to Senior BI Manager and Analytics Lead roles. Best way to reach me is email.</p>
        <div class="connect-grid">
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
    
    # Testimonials
    st.markdown("""
    <div class="testimonials-section">
        <div class="section-header" style="max-width:1100px;margin:0 auto 48px">
            <div class="section-header-left">
                <div class="section-label">What Colleagues Say</div>
                <h2 class="section-title">Testimonials</h2>
            </div>
        </div>
        <div class="testimonials-grid">
            <div class="test-card">
                <p class="test-quote">"Jason has a rare ability to translate complex data into stories that executives actually act on. He doesn't just answer questions — he asks better ones."</p>
                <p class="test-author">[Name]</p>
                <p class="test-role">VP of Sales · [Company]</p>
            </div>
            <div class="test-card">
                <p class="test-quote">"Most analysts give you data. Jason gives you decisions. He saved our team 20+ hours a week and made our CEO actually look forward to reviewing dashboards."</p>
                <p class="test-author">[Name]</p>
                <p class="test-role">Director of Operations · [Company]</p>
            </div>
            <div class="test-card">
                <p class="test-quote">"I've worked with a lot of BI people. Jason is the first one who understood that data without context is just noise."</p>
                <p class="test-author">[Name]</p>
                <p class="test-role">CFO · [Company]</p>
            </div>
            <div class="test-card">
                <p class="test-quote">"Jason doesn't just build dashboards — he changes how teams think about measurement. That's rare."</p>
                <p class="test-author">[Name]</p>
                <p class="test-role">Product Manager · [Company]</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
