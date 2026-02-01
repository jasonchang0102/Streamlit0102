import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Jason Chang | BI Manager", page_icon="◆")

# Track page changes
if 'prev_page' not in st.session_state:
    st.session_state.prev_page = None

st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap' rel='stylesheet'>
<style>
    :root{--b:#111111;--w:#ffffff;--g1:#f5f5f5;--g2:#e5e5e5;--g3:#d4d4d4;--g4:#a3a3a3;--g5:#737373;--g6:#525252;--g7:#404040;--g8:#262626;--g9:#171717;--accent:#2563eb}
    
    ::-webkit-scrollbar{width:4px}
    ::-webkit-scrollbar-track{background:var(--b)}
    ::-webkit-scrollbar-thumb{background:var(--g6)}
    
    .stApp{background:var(--w)!important;overflow-x:hidden!important}
    #MainMenu,footer,header{visibility:hidden}
    .block-container{padding:0!important;max-width:100%!important}
    
    /* Subtle texture */
    .stApp::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");opacity:0.012;pointer-events:none;z-index:10000}
    
    /* Animations */
    @keyframes fadeUp{0%{opacity:0;transform:translateY(25px)}100%{opacity:1;transform:translateY(0)}}
    @keyframes fadeIn{0%{opacity:0}100%{opacity:1}}
    @keyframes slideLeft{0%{opacity:0;transform:translateX(-20px)}100%{opacity:1;transform:translateX(0)}}
    @keyframes scaleIn{0%{opacity:0;transform:scale(0.95)}100%{opacity:1;transform:scale(1)}}
    @keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
    
    /* === SIDEBAR === */
    section[data-testid="stSidebar"]{background:#111111!important;border-right:none!important;min-width:240px!important}
    section[data-testid="stSidebar"]>div:first-child{padding:0!important}
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"]{display:none!important}
    
    div.stRadio>div{flex-direction:column!important;gap:0!important}
    div[role="radiogroup"]>label[data-baseweb="radio"]>div:first-child{display:none!important}
    
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]{
        background:transparent!important;padding:14px 32px!important;margin:0!important;cursor:pointer!important;border:none!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"] p{
        font-family:'Inter',sans-serif!important;font-size:14px!important;font-weight:400!important;
        color:rgba(255,255,255,0.5)!important;margin:0!important;transition:color 0.2s ease!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]:hover p{color:#ffffff!important}
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"][data-checked="true"] p{color:#ffffff!important;font-weight:600!important}
    
    .sb-name{font-family:'Outfit',sans-serif!important;font-size:14px!important;font-weight:600!important;color:#ffffff!important;letter-spacing:2px!important;text-transform:uppercase!important;padding:48px 32px 8px!important;margin:0!important}
    .sb-title{font-family:'Inter',sans-serif!important;font-size:12px!important;font-weight:400!important;color:rgba(255,255,255,0.4)!important;padding:0 32px 32px!important;margin:0!important}
    .sb-footer{font-family:'Inter',sans-serif!important;font-size:10px!important;color:rgba(255,255,255,0.25)!important;padding:32px!important}
    
    /* === HOME PAGE === */
    .home-hero{background:linear-gradient(180deg,#f8f9fa 0%,#ffffff 100%);padding:80px 60px;min-height:70vh;display:flex;align-items:center}
    .hero-grid{display:grid;grid-template-columns:1fr 1.2fr;gap:60px;max-width:1200px;margin:0 auto;align-items:center}
    .hero-photo{width:280px;height:280px;border-radius:50%;background:linear-gradient(135deg,#e5e7eb 0%,#d1d5db 100%);display:flex;align-items:center;justify-content:center;font-family:'Inter',sans-serif;font-size:14px;color:#6b7280;border:4px solid #ffffff;box-shadow:0 20px 60px rgba(0,0,0,0.1);animation:scaleIn 0.8s ease}
    .hero-content{animation:fadeUp 0.8s ease}
    .hero-label{font-family:'Inter',sans-serif;font-size:12px;font-weight:500;color:#2563eb;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px}
    .hero-name{font-family:'Outfit',sans-serif;font-size:56px;font-weight:700;color:#111111;line-height:1.1;margin-bottom:20px}
    .hero-tagline{font-family:'Inter',sans-serif;font-size:20px;font-weight:400;color:#4b5563;line-height:1.6;margin-bottom:32px}
    .hero-cta{display:flex;gap:16px;flex-wrap:wrap}
    .btn-primary{font-family:'Inter',sans-serif;font-size:14px;font-weight:600;color:#ffffff;background:#111111;padding:14px 28px;border-radius:6px;text-decoration:none;transition:all 0.2s ease;display:inline-block}
    .btn-primary:hover{background:#2563eb;transform:translateY(-2px)}
    .btn-secondary{font-family:'Inter',sans-serif;font-size:14px;font-weight:500;color:#111111;background:transparent;padding:14px 28px;border:1.5px solid #d1d5db;border-radius:6px;text-decoration:none;transition:all 0.2s ease;display:inline-block}
    .btn-secondary:hover{border-color:#111111}
    .hero-status{display:flex;align-items:center;gap:8px;margin-top:24px;font-family:'Inter',sans-serif;font-size:13px;color:#059669}
    .status-dot{width:8px;height:8px;background:#059669;border-radius:50%;animation:pulse 2s infinite}
    
    /* Featured Work Section */
    .featured-section{padding:80px 60px;background:#ffffff}
    .section-header{max-width:1200px;margin:0 auto 48px}
    .section-label{font-family:'Inter',sans-serif;font-size:12px;font-weight:500;color:#6b7280;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px}
    .section-title{font-family:'Outfit',sans-serif;font-size:36px;font-weight:600;color:#111111}
    .work-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:32px;max-width:1200px;margin:0 auto}
    .work-card{background:#f9fafb;border-radius:12px;overflow:hidden;transition:all 0.3s ease;border:1px solid #e5e7eb}
    .work-card:hover{transform:translateY(-4px);box-shadow:0 20px 40px rgba(0,0,0,0.08)}
    .work-card.flagship{grid-column:span 2;display:grid;grid-template-columns:1.2fr 1fr;background:linear-gradient(135deg,#111111 0%,#1f2937 100%)}
    .work-card.flagship .card-content{color:#ffffff;padding:48px}
    .work-card.flagship .card-label{color:#60a5fa}
    .work-card.flagship .card-title{color:#ffffff}
    .work-card.flagship .card-desc{color:rgba(255,255,255,0.7)}
    .work-card.flagship .card-metrics{border-color:rgba(255,255,255,0.1)}
    .work-card.flagship .metric-value{color:#ffffff}
    .work-card.flagship .metric-label{color:rgba(255,255,255,0.5)}
    .work-card.flagship .card-tags span{background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.8)}
    .card-thumb{height:200px;background:linear-gradient(135deg,#e5e7eb 0%,#d1d5db 100%);display:flex;align-items:center;justify-content:center;font-family:'Inter',sans-serif;font-size:13px;color:#6b7280}
    .work-card.flagship .card-thumb{height:100%;min-height:300px;background:linear-gradient(135deg,#1e3a5f 0%,#0f172a 100%)}
    .card-content{padding:32px}
    .card-label{font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:#2563eb;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px}
    .card-title{font-family:'Outfit',sans-serif;font-size:22px;font-weight:600;color:#111111;line-height:1.3;margin-bottom:12px}
    .card-desc{font-family:'Inter',sans-serif;font-size:14px;color:#6b7280;line-height:1.6;margin-bottom:20px}
    .card-metrics{display:flex;gap:24px;padding-top:20px;border-top:1px solid #e5e7eb}
    .metric{text-align:left}
    .metric-value{font-family:'Outfit',sans-serif;font-size:24px;font-weight:700;color:#111111}
    .metric-label{font-family:'Inter',sans-serif;font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:0.5px}
    .card-tags{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}
    .card-tags span{font-family:'Inter',sans-serif;font-size:11px;color:#6b7280;background:#f3f4f6;padding:4px 10px;border-radius:4px}
    
    /* Stats Section */
    .stats-section{padding:60px;background:#111111}
    .stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:40px;max-width:1000px;margin:0 auto;text-align:center}
    .stat-item .stat-value{font-family:'Outfit',sans-serif;font-size:48px;font-weight:700;color:#ffffff}
    .stat-item .stat-label{font-family:'Inter',sans-serif;font-size:13px;color:rgba(255,255,255,0.5);margin-top:8px}
    
    /* Testimonial Section */
    .testimonial-section{padding:80px 60px;background:#f9fafb}
    .testimonial-card{max-width:800px;margin:0 auto;text-align:center}
    .testimonial-quote{font-family:'Playfair Display',serif;font-size:28px;font-style:italic;color:#111111;line-height:1.5;margin-bottom:32px}
    .testimonial-author{font-family:'Inter',sans-serif;font-size:14px;color:#6b7280}
    .testimonial-author strong{color:#111111;font-weight:600}
    
    /* === WORK PAGE === */
    .work-page{background:#ffffff}
    .work-hero{background:#111111;padding:80px 60px;text-align:center}
    .work-hero-title{font-family:'Outfit',sans-serif;font-size:48px;font-weight:700;color:#ffffff;margin-bottom:16px}
    .work-hero-sub{font-family:'Inter',sans-serif;font-size:16px;color:rgba(255,255,255,0.6)}
    
    .case-study{padding:80px 60px;border-bottom:1px solid #e5e7eb}
    .case-study:nth-child(even){background:#f9fafb}
    .case-container{max-width:900px;margin:0 auto}
    .case-number{font-family:'Outfit',sans-serif;font-size:14px;font-weight:600;color:#2563eb;letter-spacing:2px;margin-bottom:16px}
    .case-title{font-family:'Outfit',sans-serif;font-size:36px;font-weight:700;color:#111111;line-height:1.2;margin-bottom:12px}
    .case-subtitle{font-family:'Inter',sans-serif;font-size:16px;color:#6b7280;margin-bottom:32px}
    
    .case-results{background:#111111;border-radius:12px;padding:40px;margin-bottom:48px}
    .results-title{font-family:'Inter',sans-serif;font-size:12px;font-weight:600;color:rgba(255,255,255,0.5);letter-spacing:2px;text-transform:uppercase;margin-bottom:24px}
    .results-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}
    .result-item .result-value{font-family:'Outfit',sans-serif;font-size:36px;font-weight:700;color:#ffffff}
    .result-item .result-label{font-family:'Inter',sans-serif;font-size:13px;color:rgba(255,255,255,0.5);margin-top:4px}
    .results-meta{display:flex;gap:32px;margin-top:24px;padding-top:24px;border-top:1px solid rgba(255,255,255,0.1)}
    .meta-item{font-family:'Inter',sans-serif;font-size:13px;color:rgba(255,255,255,0.6)}
    .meta-item strong{color:#ffffff}
    
    .case-section{margin-bottom:40px}
    .case-section-title{font-family:'Outfit',sans-serif;font-size:20px;font-weight:600;color:#111111;margin-bottom:16px;display:flex;align-items:center;gap:12px}
    .case-section-title::before{content:'';width:4px;height:20px;background:#2563eb;border-radius:2px}
    .case-section p,.case-section li{font-family:'Inter',sans-serif;font-size:15px;color:#4b5563;line-height:1.8}
    .case-section ul{margin:0;padding-left:20px}
    .case-section li{margin-bottom:8px}
    
    .case-quote{background:#f0f9ff;border-left:4px solid #2563eb;padding:24px 32px;margin:32px 0;border-radius:0 8px 8px 0}
    .case-quote p{font-family:'Inter',sans-serif;font-size:16px;font-style:italic;color:#1e40af;margin:0}
    .case-quote cite{font-family:'Inter',sans-serif;font-size:13px;color:#6b7280;font-style:normal;display:block;margin-top:12px}
    
    /* === ABOUT PAGE === */
    .about-hero{background:linear-gradient(180deg,#f8f9fa 0%,#ffffff 100%);padding:80px 60px}
    .about-grid{display:grid;grid-template-columns:300px 1fr;gap:60px;max-width:1100px;margin:0 auto;align-items:start}
    .about-photo{width:280px;height:280px;border-radius:16px;background:linear-gradient(135deg,#e5e7eb 0%,#d1d5db 100%);display:flex;align-items:center;justify-content:center;font-family:'Inter',sans-serif;font-size:13px;color:#6b7280;box-shadow:0 20px 60px rgba(0,0,0,0.1)}
    .about-content h1{font-family:'Outfit',sans-serif;font-size:42px;font-weight:700;color:#111111;margin-bottom:24px}
    .about-content p{font-family:'Inter',sans-serif;font-size:16px;color:#4b5563;line-height:1.8;margin-bottom:16px}
    
    .about-section{padding:60px;border-top:1px solid #e5e7eb}
    .about-section:nth-child(even){background:#f9fafb}
    .about-section-inner{max-width:900px;margin:0 auto}
    .about-section h2{font-family:'Outfit',sans-serif;font-size:28px;font-weight:600;color:#111111;margin-bottom:32px}
    
    .timeline{position:relative;padding-left:32px}
    .timeline::before{content:'';position:absolute;left:7px;top:8px;bottom:8px;width:2px;background:#e5e7eb}
    .timeline-item{position:relative;margin-bottom:32px}
    .timeline-item::before{content:'';position:absolute;left:-32px;top:8px;width:16px;height:16px;background:#ffffff;border:3px solid #2563eb;border-radius:50%}
    .timeline-year{font-family:'Outfit',sans-serif;font-size:14px;font-weight:600;color:#2563eb;margin-bottom:4px}
    .timeline-role{font-family:'Outfit',sans-serif;font-size:18px;font-weight:600;color:#111111}
    .timeline-company{font-family:'Inter',sans-serif;font-size:14px;color:#6b7280;margin-top:4px}
    .timeline-desc{font-family:'Inter',sans-serif;font-size:14px;color:#6b7280;margin-top:8px}
    
    .skills-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}
    .skill-category h3{font-family:'Inter',sans-serif;font-size:12px;font-weight:600;color:#6b7280;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:16px}
    .skill-category p{font-family:'Inter',sans-serif;font-size:15px;color:#111111;line-height:1.8}
    
    .cert-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
    .cert-card{display:flex;gap:16px;padding:24px;background:#ffffff;border:1px solid #e5e7eb;border-radius:8px}
    .cert-icon{width:48px;height:48px;background:#f3f4f6;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px}
    .cert-info h4{font-family:'Outfit',sans-serif;font-size:16px;font-weight:600;color:#111111;margin-bottom:4px}
    .cert-info p{font-family:'Inter',sans-serif;font-size:13px;color:#6b7280}
    
    .resume-btn{display:inline-flex;align-items:center;gap:8px;font-family:'Inter',sans-serif;font-size:14px;font-weight:600;color:#ffffff;background:#111111;padding:16px 32px;border-radius:8px;text-decoration:none;transition:all 0.2s ease;margin-top:24px}
    .resume-btn:hover{background:#2563eb}
    
    /* === CONNECT PAGE === */
    .connect-hero{background:#111111;padding:80px 60px;text-align:center}
    .connect-hero h1{font-family:'Outfit',sans-serif;font-size:48px;font-weight:700;color:#ffffff;margin-bottom:16px}
    .connect-hero p{font-family:'Inter',sans-serif;font-size:18px;color:rgba(255,255,255,0.6);max-width:600px;margin:0 auto}
    
    .connect-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;max-width:800px;margin:48px auto 0;padding:0 60px}
    .connect-card{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:12px;padding:32px;text-align:left;transition:all 0.2s ease}
    .connect-card:hover{background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2)}
    .connect-card-icon{font-size:24px;margin-bottom:16px}
    .connect-card-label{font-family:'Inter',sans-serif;font-size:12px;font-weight:500;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px}
    .connect-card-value{font-family:'Inter',sans-serif;font-size:16px;color:#ffffff;word-break:break-all}
    .connect-card a{color:#60a5fa;text-decoration:none}
    .connect-card a:hover{text-decoration:underline}
    
    .testimonials-section{padding:80px 60px;background:#ffffff}
    .testimonials-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:32px;max-width:1000px;margin:0 auto}
    .test-card{background:#f9fafb;border-radius:12px;padding:32px;border:1px solid #e5e7eb}
    .test-quote{font-family:'Inter',sans-serif;font-size:15px;color:#4b5563;line-height:1.7;margin-bottom:20px;font-style:italic}
    .test-author{font-family:'Inter',sans-serif;font-size:14px;color:#111111;font-weight:600}
    .test-role{font-family:'Inter',sans-serif;font-size:13px;color:#6b7280}
</style>
""", unsafe_allow_html=True)

# === SIDEBAR ===
with st.sidebar:
    st.markdown('<p class="sb-name">Jason Chang</p>', unsafe_allow_html=True)
    st.markdown('<p class="sb-title">BI Manager</p>', unsafe_allow_html=True)
    page = st.radio("", ["Home", "Work", "About", "Connect"], label_visibility="collapsed")
    st.markdown('<p class="sb-footer">© 2025</p>', unsafe_allow_html=True)

# === HOME PAGE ===
if page == "Home":
    # Hero Section
    st.markdown("""
    <div class="home-hero">
        <div class="hero-grid">
            <div class="hero-photo">
                Your Photo Here<br>(280×280px)
            </div>
            <div class="hero-content">
                <div class="hero-label">BI Manager · 10+ Years Experience</div>
                <h1 class="hero-name">I turn messy data into executive decisions.</h1>
                <p class="hero-tagline">From Blizzard to Fortune 500 — I help companies find the revenue hiding in their data. I don't just build dashboards. I build clarity.</p>
                <div class="hero-cta">
                    <a href="#work" class="btn-primary">View My Work</a>
                    <a href="#" class="btn-secondary">Download Resume</a>
                </div>
                <div class="hero-status">
                    <span class="status-dot"></span>
                    Open to Senior BI / Analytics Manager roles
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured Work Section
    st.markdown("""
    <div class="featured-section" id="work">
        <div class="section-header">
            <div class="section-label">Featured Work</div>
            <h2 class="section-title">Case Studies</h2>
        </div>
        <div class="work-grid">
            <!-- Flagship Project -->
            <div class="work-card flagship">
                <div class="card-thumb">
                    [Dashboard Preview]
                </div>
                <div class="card-content">
                    <div class="card-label">★ Flagship Project</div>
                    <h3 class="card-title">Unified 5 Conflicting Data Sources Into Single Source of Truth</h3>
                    <p class="card-desc">Post-merger chaos: 5 systems, 5 definitions of "revenue." CFO getting conflicting numbers. I had 6 weeks to fix it.</p>
                    <div class="card-metrics">
                        <div class="metric">
                            <div class="metric-value">9%</div>
                            <div class="metric-label">Revenue Lift</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">70%</div>
                            <div class="metric-label">Fewer Conflicts</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">5→1 day</div>
                            <div class="metric-label">Decision Cycle</div>
                        </div>
                    </div>
                    <div class="card-tags">
                        <span>Snowflake</span>
                        <span>Power BI</span>
                        <span>6 Weeks</span>
                        <span>$12M Impact</span>
                    </div>
                </div>
            </div>
            
            <!-- Project 2 -->
            <div class="work-card">
                <div class="card-thumb">[Segmentation Visual]</div>
                <div class="card-content">
                    <div class="card-label">Blizzard Entertainment</div>
                    <h3 class="card-title">+33% Conversion Through Player Segmentation</h3>
                    <p class="card-desc">Transformed one-size-fits-all marketing into precision targeting using K-Means clustering on player behavior.</p>
                    <div class="card-metrics">
                        <div class="metric">
                            <div class="metric-value">+33%</div>
                            <div class="metric-label">Conversion</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">2M+</div>
                            <div class="metric-label">Players</div>
                        </div>
                    </div>
                    <div class="card-tags">
                        <span>Python</span>
                        <span>K-Means</span>
                        <span>Warcraft</span>
                    </div>
                </div>
            </div>
            
            <!-- Project 3 -->
            <div class="work-card">
                <div class="card-thumb">[Pipeline Diagram]</div>
                <div class="card-content">
                    <div class="card-label">Operations</div>
                    <h3 class="card-title">160 Hours Saved Quarterly Via Pipeline Automation</h3>
                    <p class="card-desc">Replaced 47 manual Excel macros with automated Python pipelines. Error rate: 15% → near zero.</p>
                    <div class="card-metrics">
                        <div class="metric">
                            <div class="metric-value">160hrs</div>
                            <div class="metric-label">Saved/Quarter</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value">99</div>
                            <div class="metric-label">Vendors</div>
                        </div>
                    </div>
                    <div class="card-tags">
                        <span>Python</span>
                        <span>SQL</span>
                        <span>Automation</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
    <div class="stats-section">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-value">10+</div>
                <div class="stat-label">Years in BI</div>
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
    
    # Testimonial Section
    st.markdown("""
    <div class="testimonial-section">
        <div class="testimonial-card">
            <p class="testimonial-quote">"Jason doesn't just build dashboards — he asks the questions that change how we think about the business. For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
            <p class="testimonial-author"><strong>[Name]</strong>, VP of Sales · [Company]</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === WORK PAGE ===
elif page == "Work":
    st.markdown("""
    <div class="work-page">
        <div class="work-hero">
            <h1 class="work-hero-title">Selected Work</h1>
            <p class="work-hero-sub">Deep dives into problems I've solved</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Case Study 1: Executive BI
    st.markdown("""
        <div class="case-study">
            <div class="case-container">
                <div class="case-number">CASE STUDY 01</div>
                <h2 class="case-title">Unified Executive Intelligence</h2>
                <p class="case-subtitle">How I turned 5 conflicting data sources into a single source of truth</p>
                
                <div class="case-results">
                    <div class="results-title">The Results</div>
                    <div class="results-grid">
                        <div class="result-item">
                            <div class="result-value">9%</div>
                            <div class="result-label">Quarterly Revenue Lift</div>
                        </div>
                        <div class="result-item">
                            <div class="result-value">70%</div>
                            <div class="result-label">Fewer KPI Conflicts</div>
                        </div>
                        <div class="result-item">
                            <div class="result-value">5 → 1 day</div>
                            <div class="result-label">Decision Cycle</div>
                        </div>
                    </div>
                    <div class="results-meta">
                        <div class="meta-item"><strong>Timeline:</strong> 6 weeks</div>
                        <div class="meta-item"><strong>Impact:</strong> ~$12M annually</div>
                        <div class="meta-item"><strong>Users:</strong> 250+</div>
                    </div>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">The Mess</h3>
                    <p>After the acquisition, I inherited a nightmare:</p>
                    <ul>
                        <li><strong>5 sales domains</strong>, each with their own "source of truth"</li>
                        <li>APAC counted returns in revenue. EMEA didn't. Nobody knew which was "right"</li>
                        <li>The CFO was getting <strong>5 different revenue numbers</strong> at every board meeting — and losing trust in all of them</li>
                        <li>Field teams had created <strong>47 shadow Excel trackers</strong> because they didn't trust official reports</li>
                        <li>The previous BI lead had quit mid-project</li>
                    </ul>
                    <p>The CEO gave me 6 weeks before Q3 close. No pressure.</p>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">Why This Was Hard</h3>
                    <p>This wasn't a technical problem. It was a political one.</p>
                    <p>Each regional VP had built their metrics to make their team look good. Standardizing meant someone's numbers would go down — and they knew it.</p>
                    <p>I also had:</p>
                    <ul>
                        <li>No dedicated engineering support (just me and one junior analyst)</li>
                        <li>A Snowflake instance already at 80% capacity</li>
                        <li>Legacy POS systems that hadn't been documented since 2019</li>
                    </ul>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">My Approach</h3>
                    <p><strong>Week 1-2: Discovery</strong></p>
                    <p>I didn't touch any code. I spent two weeks in meetings with each regional VP, asking one question: "What decision are you trying to make with this data?"</p>
                    <p>What I found: 70% of their "must-have" metrics weren't being used. They'd been cargo-culted from previous roles.</p>
                    
                    <p><strong>Week 3: The Hard Conversation</strong></p>
                    <p>I presented the CFO with two options:</p>
                    <ul>
                        <li><strong>Option A:</strong> Build a "dashboard of dashboards" that showed all 5 versions (fast, but kicks the can)</li>
                        <li><strong>Option B:</strong> Force standardization now, accept that Q3 numbers would look different than Q2 (painful, but correct)</li>
                    </ul>
                    <p>I recommended Option B. The CFO agreed.</p>
                    
                    <p><strong>Week 4-5: Build</strong></p>
                    <ul>
                        <li>Consolidated POS, field, compliance, and promo data into unified Snowflake schema</li>
                        <li>Created 12 "golden metrics" with documented definitions</li>
                        <li>Built Power BI dashboard with row-level security per region</li>
                    </ul>
                    
                    <p><strong>Week 6: Rollout</strong></p>
                    <ul>
                        <li>Trained 250 users in 3 sessions</li>
                        <li>Created self-service documentation</li>
                        <li>Killed access to the old reports (this was controversial)</li>
                    </ul>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">What Went Wrong</h3>
                    <p>Two things I didn't anticipate:</p>
                    <ul>
                        <li><strong>The APAC surprise:</strong> The APAC team had been using a custom field that wasn't in any documentation. Their numbers broke on Day 1. I had to patch it live while the regional VP was on a call with the CEO.</li>
                        <li><strong>The holdout:</strong> One senior director refused to use the new system and continued sending his own Excel reports. I had to escalate to the CFO to get organizational buy-in to enforce the change.</li>
                    </ul>
                    <p><em>Lesson: Technical migrations are easy. Cultural migrations are hard.</em></p>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">What I'd Do Differently</h3>
                    <ul>
                        <li>Get <strong>written sign-off</strong> from each VP on metric definitions BEFORE building</li>
                        <li>Build a "comparison mode" showing old vs new numbers side-by-side for the first month</li>
                        <li>Push back harder on the 6-week timeline — we made it, but documentation suffered</li>
                    </ul>
                </div>
                
                <div class="case-quote">
                    <p>"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
                    <cite>— CFO, [Company]</cite>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Case Study 2: Player Segmentation
    st.markdown("""
        <div class="case-study">
            <div class="case-container">
                <div class="case-number">CASE STUDY 02</div>
                <h2 class="case-title">+33% Conversion Through Player Segmentation</h2>
                <p class="case-subtitle">Blizzard Entertainment · Warcraft</p>
                
                <div class="case-results">
                    <div class="results-title">The Results</div>
                    <div class="results-grid">
                        <div class="result-item">
                            <div class="result-value">+33%</div>
                            <div class="result-label">Conversion Rate</div>
                        </div>
                        <div class="result-item">
                            <div class="result-value">2M+</div>
                            <div class="result-label">Players Analyzed</div>
                        </div>
                        <div class="result-item">
                            <div class="result-value">6</div>
                            <div class="result-label">Distinct Segments</div>
                        </div>
                    </div>
                    <div class="results-meta">
                        <div class="meta-item"><strong>Timeline:</strong> 3 weeks</div>
                        <div class="meta-item"><strong>Tools:</strong> Python, K-Means, SQL</div>
                    </div>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">The Mess</h3>
                    <p>When I joined the project, marketing was sending the same promotion to every player — the whale spending $500/month and the casual who logs in twice a year.</p>
                    <p>The data existed to segment them. But it was scattered across 6 different game event tables, player profiles hadn't been updated since the last expansion, and nobody could agree on what "active player" even meant.</p>
                    <p>Marketing was burning budget. Leadership was asking why. And I had 3 weeks before the next major in-game event.</p>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">Why This Was Hard</h3>
                    <ul>
                        <li><strong>Scale:</strong> 2M+ player records with 50+ behavioral features each</li>
                        <li><strong>Politics:</strong> Marketing had their own "segments" based on intuition. Showing data-driven segments meant telling them they were wrong.</li>
                        <li><strong>Timing:</strong> The in-game event was locked. No time for iteration.</li>
                    </ul>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">My Approach</h3>
                    <p><strong>Feature Engineering:</strong> Distilled 50+ raw features into 12 meaningful behavioral metrics: login frequency, session duration, purchase recency, guild participation, PvP vs PvE preference, etc.</p>
                    <p><strong>Clustering:</strong> Applied K-Means with elbow method validation. Tested 4-10 clusters. 6 emerged as optimal balance of distinctiveness and actionability.</p>
                    <p><strong>Validation:</strong> Named each segment based on behavior patterns. Presented to marketing with specific promotion recommendations per segment.</p>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">The Segments</h3>
                    <ul>
                        <li><strong>Whales:</strong> High spend, high engagement — offer early access, not discounts</li>
                        <li><strong>Social Butterflies:</strong> Guild-focused, moderate spend — promote group content</li>
                        <li><strong>Lapsed Veterans:</strong> Previously active, now dormant — winback campaigns</li>
                        <li><strong>Casuals:</strong> Low frequency, impulse buyers — limited-time offers work best</li>
                        <li><strong>Grinders:</strong> High playtime, low spend — cosmetic rewards, not pay-to-win</li>
                        <li><strong>New Blood:</strong> Recent joiners — onboarding focus, not monetization</li>
                    </ul>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">What I'd Do Differently</h3>
                    <ul>
                        <li>Build a <strong>real-time segmentation pipeline</strong> instead of batch — player behavior shifts fast</li>
                        <li>Include <strong>A/B testing framework</strong> from the start to measure segment-specific lift</li>
                    </ul>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Case Study 3: Pipeline Automation
    st.markdown("""
        <div class="case-study">
            <div class="case-container">
                <div class="case-number">CASE STUDY 03</div>
                <h2 class="case-title">160 Hours Saved Quarterly Via Pipeline Automation</h2>
                <p class="case-subtitle">99 Vendor Data Sources · Python + SQL</p>
                
                <div class="case-results">
                    <div class="results-title">The Results</div>
                    <div class="results-grid">
                        <div class="result-item">
                            <div class="result-value">160 hrs</div>
                            <div class="result-label">Saved Quarterly</div>
                        </div>
                        <div class="result-item">
                            <div class="result-value">15% → 0%</div>
                            <div class="result-label">Error Rate</div>
                        </div>
                        <div class="result-item">
                            <div class="result-value">99</div>
                            <div class="result-label">Vendors Automated</div>
                        </div>
                    </div>
                    <div class="results-meta">
                        <div class="meta-item"><strong>Timeline:</strong> 8 weeks</div>
                        <div class="meta-item"><strong>Tools:</strong> Python, SQL, Airflow</div>
                    </div>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">The Mess</h3>
                    <p>When I inherited the data pipeline, "automation" meant a shared folder of 47 Excel macros that one person (who had left) understood.</p>
                    <p>Every Monday, three analysts spent 4 hours manually downloading vendor reports, reformatting them, and uploading to the database. If someone was sick, the weekly report didn't go out.</p>
                    <p>The error rate was 15%. We'd caught wrong numbers in board decks twice in the past quarter. The VP of Finance had stopped trusting anything with "automated" in the name.</p>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">Why This Was Hard</h3>
                    <ul>
                        <li><strong>99 vendors</strong>, each with their own report format (CSV, Excel, PDF, API)</li>
                        <li><strong>No documentation</strong> on the existing macros</li>
                        <li><strong>Trust deficit:</strong> Finance had been burned before and was skeptical of any "new system"</li>
                        <li><strong>Zero downtime:</strong> Reports had to keep flowing while I rebuilt</li>
                    </ul>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">My Approach</h3>
                    <p><strong>Phase 1 - Audit (Week 1-2):</strong> Mapped every data source, format, frequency, and downstream dependency. Found 12 sources that were never actually used.</p>
                    <p><strong>Phase 2 - Build (Week 3-6):</strong> Created Python ingestion framework with standardized parsers. Each vendor got a config file, not custom code. Implemented validation rules that catch anomalies before they hit the database.</p>
                    <p><strong>Phase 3 - Parallel Run (Week 7):</strong> Ran old and new systems side-by-side. Flagged every discrepancy. Fixed edge cases.</p>
                    <p><strong>Phase 4 - Cutover (Week 8):</strong> Killed the macros. Trained the team on monitoring.</p>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">What Went Wrong</h3>
                    <ul>
                        <li><strong>The PDF vendor:</strong> One vendor only sent PDF reports with no consistent formatting. Spent 2 days building a custom parser.</li>
                        <li><strong>Timezone bugs:</strong> Three vendors reported in different timezones. Took a week to standardize.</li>
                    </ul>
                </div>
                
                <div class="case-section">
                    <h3 class="case-section-title">What I'd Do Differently</h3>
                    <ul>
                        <li>Push vendors to use APIs or standardized formats — some of the manual work was self-inflicted</li>
                        <li>Build monitoring dashboards earlier — we caught issues reactively for the first month</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === ABOUT PAGE ===
elif page == "About":
    st.markdown("""
    <div class="about-hero">
        <div class="about-grid">
            <div class="about-photo">Your Photo Here<br>(280×280px)</div>
            <div class="about-content">
                <h1>Hi, I'm Jason.</h1>
                <p>I've spent the last decade helping companies stop guessing and start knowing.</p>
                <p>Most BI teams build dashboards. I build clarity. The kind where a CEO can walk into a board meeting and actually trust the numbers on the screen.</p>
                <p>I've done this at Blizzard (Warcraft player analytics), at a Fortune 500 post-merger chaos, and at startups where I was the entire data team.</p>
                <p><strong>What I've learned:</strong> The hard part is never the SQL. It's getting humans to agree on what "revenue" means.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Career Timeline
    st.markdown("""
    <div class="about-section">
        <div class="about-section-inner">
            <h2>Career Timeline</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-year">2024 — Present</div>
                    <div class="timeline-role">BI Manager</div>
                    <div class="timeline-company">[Company Name]</div>
                    <div class="timeline-desc">Leading analytics for $XXM business unit. Built executive reporting suite. Unified 5 data sources post-merger.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2021 — 2024</div>
                    <div class="timeline-role">Senior Data Analyst</div>
                    <div class="timeline-company">[Company Name]</div>
                    <div class="timeline-desc">Automated 99 vendor pipelines. Saved 160 hours quarterly. Reduced error rate from 15% to near-zero.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2018 — 2021</div>
                    <div class="timeline-role">Data Analyst</div>
                    <div class="timeline-company">Blizzard Entertainment</div>
                    <div class="timeline-desc">Player behavior analytics for Warcraft. Built segmentation model that drove 33% conversion lift.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2015 — 2018</div>
                    <div class="timeline-role">Business Analyst</div>
                    <div class="timeline-company">[Company Name]</div>
                    <div class="timeline-desc">Started in Excel, discovered SQL. Built first automated reports.</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2014</div>
                    <div class="timeline-role">B.S. Business Administration</div>
                    <div class="timeline-company">UC Riverside</div>
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
                    <p>SQL (10+ years), Power BI / DAX, Python, Snowflake</p>
                </div>
                <div class="skill-category">
                    <h3>Fluent</h3>
                    <p>BigQuery, GA4, Looker, dbt, Tableau</p>
                </div>
                <div class="skill-category">
                    <h3>Working Knowledge</h3>
                    <p>Airflow, AWS, Azure, R, Spark</p>
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
                        <p>Stanford · 2024</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon">🧠</div>
                    <div class="cert-info">
                        <h4>Neural Networks & Deep Learning</h4>
                        <p>DeepLearning.AI · 2024</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon">☁️</div>
                    <div class="cert-info">
                        <h4>AWS Cloud Practitioner</h4>
                        <p>Amazon · 2019</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon">📊</div>
                    <div class="cert-info">
                        <h4>Google Analytics Certified</h4>
                        <p>Google · 2023</p>
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
                <div class="connect-card-value">Rowland Heights, CA</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Testimonials
    st.markdown("""
    <div class="testimonials-section">
        <div class="section-header" style="max-width:1000px;margin:0 auto 48px">
            <div class="section-label">What Colleagues Say</div>
            <h2 class="section-title">Testimonials</h2>
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
                <p class="test-role">Product Manager · Blizzard Entertainment</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
