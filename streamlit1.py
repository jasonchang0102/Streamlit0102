"""
Jason C. Chang | Senior BI & Analytics Manager Portfolio
Rebuilt: Professional editorial layout, defensible metrics, real testimonials only
Key design rule: Each st.markdown() is self-contained (own background/colors)
"""

import streamlit as st
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    PAGE_TITLE: str = "Jason C. Chang | Senior BI & Analytics Manager"
    PAGE_ICON: str = "📊"
    NAME: str = "Jason C. Chang"
    TITLE: str = "Senior BI & Analytics Manager"
    EMAIL: str = "jason.chang01022024@gmail.com"
    PHONE: str = "(626) 203-3319"
    LINKEDIN: str = "linkedin.com/in/jchang0102"
    LINKEDIN_URL: str = "https://linkedin.com/in/jchang0102"
    LOCATION: str = "Hacienda Heights, CA"
    RESUME_URL: str = "https://github.com/jasonchang0102/Streamlit0102/raw/main/--Jason_Chang_Sr_BI_Analytics_Manager_Resume--03-17-26.pdf"
    KEYWORDS: tuple = ("SQL", "Python", "Power BI", "Snowflake", "DAX", "BigQuery")
    PAGES: tuple = ("Home", "Work", "About", "Connect")

CONFIG = Config()

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
:root { --bk:#0a0a0a; --wh:#ffffff; --g1:#f5f5f5; --g2:#e5e5e5; --g3:#d4d4d4; --g4:#a3a3a3; --g5:#737373; --g6:#525252; --g7:#404040; --g8:#262626; --g9:#171717; --acc:#ca8a04; --fd:'Bebas Neue',Impact,sans-serif; --fb:'Inter',-apple-system,sans-serif; --fm:'JetBrains Mono',monospace; }
.stApp,[data-testid="stAppViewContainer"],.main{background:#ffffff!important}
#MainMenu,footer,.stDeployButton,div[data-testid="stDecoration"],[data-testid="stToolbar"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
section[data-testid="stSidebar"]{background:#0a0a0a!important;min-width:280px!important;max-width:280px!important}
section[data-testid="stSidebar"]>div:first-child{padding:0!important;padding-bottom:100px!important;background:#0a0a0a!important}
[data-testid="stSidebarNav"]{display:none!important}
button[data-testid="stSidebarCollapseButton"]{display:none!important}
[data-testid="collapsedControl"]{display:flex!important;visibility:visible!important;opacity:1!important;z-index:999999!important;background:#0a0a0a!important;padding:12px!important}
[data-testid="collapsedControl"] svg{fill:white!important;color:white!important;stroke:white!important}
[data-testid="collapsedControl"] button{background:#0a0a0a!important;color:white!important}
.sb-brand{padding:56px 32px 32px;border-bottom:1px solid #262626}
.sb-name{font-family:var(--fd);font-size:22px;color:#fff;margin:0 0 4px;letter-spacing:3px}
.sb-title{font-family:var(--fb);font-size:12px;color:#a3a3a3;margin:0 0 20px}
.sb-status{display:inline-flex;align-items:center;gap:8px;background:#262626;padding:6px 14px;font-family:var(--fm);font-size:11px;color:#4ade80;letter-spacing:1px}
.sb-status::before{content:'';width:6px;height:6px;background:#4ade80;border-radius:50%}
[data-testid="stSidebar"] .stRadio>div{flex-direction:column!important;gap:0!important;padding:20px 0!important}
[data-testid="stSidebar"] .stRadio label>div:first-child{display:none!important}
[data-testid="stSidebar"] .stRadio label{background:transparent!important;padding:14px 32px!important;margin:0!important;border-left:2px solid transparent!important}
[data-testid="stSidebar"] .stRadio label:hover{background:#1a1a1a!important}
[data-testid="stSidebar"] .stRadio label:has(input:checked){background:#1a1a1a!important;border-left-color:#fff!important}
[data-testid="stSidebar"] .stRadio label p{font-family:var(--fd)!important;font-size:16px!important;color:#737373!important;letter-spacing:3px!important}
[data-testid="stSidebar"] .stRadio label:hover p{color:#d4d4d4!important}
[data-testid="stSidebar"] .stRadio label:has(input:checked) p{color:#fff!important}
.sb-footer{position:fixed;bottom:0;left:0;width:280px;padding:20px 32px;border-top:1px solid #262626;background:#0a0a0a}
.sb-dl{display:block;background:#fff;color:#0a0a0a;font-family:var(--fd);font-size:13px;letter-spacing:2px;text-align:center;text-decoration:none;padding:10px}
.hero{padding:80px 72px;min-height:70vh;display:flex;flex-direction:column;justify-content:center;max-width:720px}
.hero-ey{font-family:var(--fm);font-size:13px;color:#525252!important;letter-spacing:2px;text-transform:uppercase;margin-bottom:20px}
.hero-h{font-family:var(--fd);font-size:64px;color:#0a0a0a!important;line-height:.95;margin:0 0 28px;letter-spacing:2px}
.hero-sub{font-family:var(--fb);font-size:20px;color:#525252!important;line-height:1.7;margin-bottom:16px;font-weight:300}
.hero-tags{display:flex;flex-wrap:wrap;gap:10px;margin-top:32px}
.hero-tag{font-family:var(--fm);font-size:12px;color:#0a0a0a!important;background:#f5f5f5;padding:8px 14px;border:1px solid #e5e5e5}
.proof{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:2px solid #0a0a0a;border-bottom:2px solid #0a0a0a;background:#fff;padding:0 72px}
.proof-i{text-align:center;padding:36px 16px;border-right:1px solid #e5e5e5}
.proof-i:last-child{border-right:none}
.proof-v{font-family:var(--fd);font-size:42px;color:#0a0a0a!important;line-height:1}
.proof-l{font-family:var(--fb);font-size:12px;color:#737373!important;margin-top:8px;text-transform:uppercase;letter-spacing:1px;font-weight:500}
.fh{background:#0a0a0a;padding:64px 72px 40px}
.fh-label{font-family:var(--fm);font-size:12px;color:#a3a3a3;letter-spacing:2px;text-transform:uppercase;margin-bottom:20px}
.fh-h{font-family:var(--fd);font-size:40px;color:#fff!important;line-height:1.1;margin:0 0 20px;letter-spacing:1px;max-width:640px}
.fh-meta{display:flex;flex-wrap:wrap;gap:24px;font-family:var(--fm);font-size:13px;color:#a3a3a3}
.fs{background:#171717;padding:40px 72px;border-left:4px solid #ca8a04}
.fs-label{font-family:var(--fd);font-size:18px;color:#ca8a04!important;letter-spacing:2px;margin-bottom:12px}
.fs-text{font-family:var(--fb);font-size:17px;color:#d4d4d4!important;line-height:1.8}
.fr{background:#0a0a0a;padding:40px 72px;display:grid;grid-template-columns:repeat(4,1fr);gap:0}
.fr-i{border-left:2px solid #ca8a04;padding-left:20px}
.fr-v{font-family:var(--fd);font-size:40px;color:#fff!important}
.fr-l{font-family:var(--fb);font-size:12px;color:#a3a3a3!important;margin-top:4px;text-transform:uppercase;letter-spacing:1px}
.ff{background:#0a0a0a;padding:20px 72px 56px}
.ff-tags{display:flex;gap:10px;flex-wrap:wrap}
.ff-tag{font-family:var(--fm);font-size:12px;color:#a3a3a3;background:#262626;padding:8px 14px}
.ps{padding:64px 72px;background:#fff}
.ps-title{font-family:var(--fd);font-size:28px;color:#0a0a0a!important;letter-spacing:3px;margin:0 0 32px}
.pg{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
.pc{background:#fff;border:1px solid #e5e5e5;padding:36px}
.pc-co{font-family:var(--fm);font-size:11px;color:#737373;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px}
.pc-t{font-family:var(--fd);font-size:22px;color:#0a0a0a!important;line-height:1.2;margin:0 0 12px;letter-spacing:1px}
.pc-d{font-family:var(--fb);font-size:15px;color:#525252!important;line-height:1.7;margin-bottom:20px}
.pc-m{display:flex;gap:32px;padding-top:16px;border-top:1px solid #e5e5e5}
.pc-mv{font-family:var(--fd);font-size:24px;color:#0a0a0a!important}
.pc-ml{font-family:var(--fb);font-size:11px;color:#737373!important;text-transform:uppercase;letter-spacing:1px}
.pov{background:#f5f5f5;padding:56px 72px;border-left:4px solid #0a0a0a}
.pov-label{font-family:var(--fd);font-size:20px;color:#0a0a0a!important;letter-spacing:2px;margin-bottom:16px}
.pov-text{font-family:var(--fb);font-size:18px;color:#404040!important;line-height:1.8;font-style:italic}
.tr{background:#fafafa;padding:56px 72px;border-top:1px solid #e5e5e5}
.tr-q{font-family:var(--fb);font-size:22px;font-style:italic;color:#0a0a0a!important;line-height:1.6;margin:0 0 20px;max-width:700px}
.tr-a{font-family:var(--fb);font-size:15px;font-weight:600;color:#0a0a0a!important}
.tr-r{font-family:var(--fb);font-size:13px;color:#737373!important;margin-top:2px}
.wh{background:#0a0a0a;padding:80px 72px}
.wh-t{font-family:var(--fd);font-size:52px;color:#fff!important;margin:0 0 12px;letter-spacing:4px}
.wh-s{font-family:var(--fb);font-size:17px;color:#a3a3a3!important;font-weight:300}
.cs{padding:72px;border-bottom:1px solid #e5e5e5}
.cs:nth-child(even){background:#fafafa}
.cs-in{max-width:760px}
.cs-lb{display:inline-block;font-family:var(--fm);font-size:12px;font-weight:600;color:#fff;background:#0a0a0a;padding:6px 14px;letter-spacing:2px;margin-bottom:20px}
.cs-h{font-family:var(--fd);font-size:38px;color:#0a0a0a!important;line-height:1.1;margin:0 0 8px;letter-spacing:1px}
.cs-sub{font-family:var(--fb);font-size:15px;color:#737373!important;margin-bottom:32px;margin-top:12px}
.cs-res{background:#0a0a0a;padding:32px;margin-bottom:48px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;text-align:center}
.cs-rv{font-family:var(--fd);font-size:38px;color:#fff!important}
.cs-rl{font-family:var(--fb);font-size:12px;color:#a3a3a3!important;margin-top:4px;text-transform:uppercase;letter-spacing:1px}
.cs-sec{margin-bottom:36px}
.cs-sec-t{font-family:var(--fd);font-size:20px;color:#0a0a0a!important;letter-spacing:2px;margin-bottom:12px;padding-left:16px;border-left:3px solid #ca8a04}
.cs-sec p{font-family:var(--fb);font-size:16px;color:#525252!important;line-height:1.8;margin:0 0 12px}
.cs-sec ul{margin:0;padding:0;list-style:none}
.cs-sec li{font-family:var(--fb);font-size:16px;color:#525252!important;line-height:1.8;margin-bottom:6px;padding-left:20px;position:relative}
.cs-sec li::before{content:'—';position:absolute;left:0;color:#ca8a04;font-weight:700}
.cs-qt{background:#f5f5f5;padding:32px;margin:32px 0;border-left:3px solid #0a0a0a}
.cs-qt p{font-family:var(--fb);font-size:18px;font-style:italic;color:#0a0a0a!important;line-height:1.6;margin:0}
.cs-qt cite{font-family:var(--fb);font-size:13px;color:#737373;font-style:normal;display:block;margin-top:12px;font-weight:600}
.ah{padding:80px 72px;max-width:720px}
.ah h1{font-family:var(--fd);font-size:48px;color:#0a0a0a!important;margin:0 0 24px;letter-spacing:2px}
.ah p{font-family:var(--fb);font-size:18px;color:#525252!important;line-height:1.8;margin:0 0 16px;font-weight:300}
.as{padding:56px 72px;border-top:1px solid #e5e5e5}
.as:nth-child(even){background:#fafafa}
.as-t{font-family:var(--fd);font-size:28px;color:#0a0a0a!important;margin:0 0 32px;letter-spacing:3px}
.tl{max-width:680px;position:relative;padding-left:36px}
.tl::before{content:'';position:absolute;left:0;top:0;bottom:0;width:2px;background:#0a0a0a}
.tl-i{padding:20px 0;border-bottom:1px solid #e5e5e5;display:grid;grid-template-columns:140px 1fr;gap:32px;position:relative}
.tl-i::before{content:'';position:absolute;left:-43px;top:28px;width:12px;height:12px;background:#fff;border:2px solid #0a0a0a;border-radius:50%}
.tl-i:last-child{border-bottom:none}
.tl-y{font-family:var(--fm);font-size:13px;color:#737373!important}
.tl-rl{font-family:var(--fd);font-size:20px;color:#0a0a0a!important;margin:0 0 4px;letter-spacing:1px}
.tl-co{font-family:var(--fb);font-size:14px;color:#737373!important}
.tl-d{font-family:var(--fb);font-size:15px;color:#525252!important;line-height:1.6;margin-top:8px}
.sg{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:800px}
.sc{background:#fff;border:1px solid #e5e5e5;padding:32px}
.sc-h{font-family:var(--fd);font-size:16px;color:#0a0a0a!important;letter-spacing:2px;margin-bottom:16px}
.sc-l{font-family:var(--fb);font-size:15px;color:#525252!important;line-height:2.2}
.cg{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:800px}
.cc2{background:#fff;border:1px solid #e5e5e5;padding:20px}
.cc2-n{font-family:var(--fb);font-size:15px;font-weight:600;color:#0a0a0a!important;margin-bottom:4px}
.cc2-i{font-family:var(--fb);font-size:13px;color:#737373!important}
.bel{padding:56px 72px;background:#0a0a0a}
.bel-t{font-family:var(--fd);font-size:28px;color:#fff!important;letter-spacing:3px;margin:0 0 32px}
.bel-p{font-family:var(--fb);font-size:16px;color:#d4d4d4!important;line-height:1.8;margin-bottom:16px;padding-left:20px;border-left:2px solid #ca8a04}
.cn-h{background:#0a0a0a;padding:80px 72px;text-align:center}
.cn-h h1{font-family:var(--fd);font-size:48px;color:#fff!important;margin:0 0 16px;letter-spacing:4px}
.cn-h p{font-family:var(--fb);font-size:17px;color:#a3a3a3!important;max-width:480px;margin:0 auto;font-weight:300}
.cn-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;max-width:880px;margin:48px auto 0}
.cn-c{background:#171717;border:1px solid #262626;padding:32px 20px;text-align:center}
.cn-c-i{font-size:24px;margin-bottom:8px}
.cn-c-l{font-family:var(--fm);font-size:11px;color:#737373;letter-spacing:2px;margin-bottom:8px}
.cn-c-v{font-family:var(--fb);font-size:14px;color:#fff!important;word-break:break-all}
.cn-c-v a{color:#d4d4d4;text-decoration:none}
.cn-test{padding:64px 72px;background:#fff}
.cn-test-t{font-family:var(--fd);font-size:28px;color:#0a0a0a!important;letter-spacing:3px;margin:0 0 32px}
.cn-test-c{background:#fafafa;border:1px solid #e5e5e5;padding:36px;max-width:700px}
.cn-test-q{font-family:var(--fb);font-size:17px;color:#404040!important;line-height:1.7;font-style:italic;margin-bottom:16px}
.cn-test-a{font-family:var(--fb);font-size:14px;font-weight:600;color:#0a0a0a!important}
.cn-test-r{font-family:var(--fb);font-size:13px;color:#737373!important;margin-top:2px}
@media(max-width:1024px){.hero,.ps,.cs,.as,.ah,.cn-test,.pov,.tr,.bel{padding-left:36px;padding-right:36px}.fh,.fs,.fr,.ff,.wh,.cn-h{padding-left:36px;padding-right:36px}.proof{padding:0 36px}.pg{grid-template-columns:1fr}}
@media(max-width:768px){.proof,.fr,.cs-res{grid-template-columns:1fr}.sg,.cg,.cn-cards{grid-template-columns:1fr}.tl-i{grid-template-columns:1fr;gap:4px}.cn-cards{grid-template-columns:repeat(2,1fr)}.hero-h{font-size:44px}}
</style>
<script>
try{var k=Object.keys(localStorage);for(var i=0;i<k.length;i++){if(k[i].indexOf('sidebar')!==-1||k[i].indexOf('Sidebar')!==-1){localStorage.removeItem(k[i])}}var k2=Object.keys(sessionStorage);for(var j=0;j<k2.length;j++){if(k2[j].indexOf('sidebar')!==-1||k2[j].indexOf('Sidebar')!==-1){sessionStorage.removeItem(k2[j])}}}catch(e){}
</script>
"""

def main():
    st.set_page_config(layout="wide",page_title=CONFIG.PAGE_TITLE,page_icon=CONFIG.PAGE_ICON,initial_sidebar_state="expanded")
    st.markdown(CSS,unsafe_allow_html=True)
    with st.sidebar:
        st.markdown(f'<div class="sb-brand"><p class="sb-name">{CONFIG.NAME}</p><p class="sb-title">{CONFIG.TITLE}</p><div class="sb-status">Open to Opportunities</div></div>',unsafe_allow_html=True)
        page=st.radio("Nav",CONFIG.PAGES,label_visibility="collapsed")
        st.markdown(f'<div class="sb-footer"><a href="{CONFIG.RESUME_URL}" target="_blank" class="sb-dl">DOWNLOAD RESUME</a></div>',unsafe_allow_html=True)
    if page=="Home":render_home()
    elif page=="Work":render_work()
    elif page=="About":render_about()
    elif page=="Connect":render_connect()

def render_home():
    tags=''.join(f'<span class="hero-tag">{k}</span>' for k in CONFIG.KEYWORDS)
    st.markdown(f'<div class="hero"><p class="hero-ey">Senior BI & Analytics Manager — 8+ Years</p><h1 class="hero-h">I WALK INTO DATA CHAOS AND BUILD SYSTEMS EXECUTIVES TRUST</h1><p class="hero-sub">Companies hire me when the data exists but nobody believes it. I fix the trust gap between raw data and executive decisions — through platform architecture, metric alignment, and reporting systems that 200+ stakeholders actually use.</p><div class="hero-tags">{tags}</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="proof"><div class="proof-i"><div class="proof-v">250+</div><div class="proof-l">Stakeholders Served</div></div><div class="proof-i"><div class="proof-v">99+</div><div class="proof-l">Data Sources Unified</div></div><div class="proof-i"><div class="proof-v">70%</div><div class="proof-l">Fewer KPI Conflicts</div></div><div class="proof-i"><div class="proof-v">5→1</div><div class="proof-l">Day Reporting Cycle</div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="fh"><p class="fh-label">Flagship — Advantage Solutions</p><h2 class="fh-h">FIVE SALES SYSTEMS. FIVE REVENUE NUMBERS. ONE BOARD MEETING.</h2><div class="fh-meta"><span>6 weeks</span><span>Post-merger unification</span><span>250 users</span></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="fs"><p class="fs-label">THE SITUATION</p><p class="fs-text">After the merger, every region defined revenue differently. The CFO was getting five different numbers in every board meeting. Field teams had created 47 shadow Excel trackers. The previous BI lead quit mid-project. I had 6 weeks before Q3 close to build one source of truth.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="fr"><div class="fr-i"><div class="fr-v">70%</div><div class="fr-l">Fewer KPI Conflicts</div></div><div class="fr-i"><div class="fr-v">5→1</div><div class="fr-l">Day Reporting Cycle</div></div><div class="fr-i"><div class="fr-v">9%</div><div class="fr-l">Quarterly Revenue Growth</div></div><div class="fr-i"><div class="fr-v">250</div><div class="fr-l">Users on Platform</div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="ff"><div class="ff-tags"><span class="ff-tag">Snowflake</span><span class="ff-tag">Power BI</span><span class="ff-tag">DAX</span><span class="ff-tag">Python</span><span class="ff-tag">SQL</span></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="ps"><h2 class="ps-title">MORE WORK</h2><div class="pg"><div class="pc"><div class="pc-co">Modern Home Station</div><h3 class="pc-t">MARKETING WAS SPENDING BLIND</h3><p class="pc-d">No attribution. Same promo to everyone. Data scattered across Facebook, Shopify, GA4. Built cross-channel attribution framework and A/B testing program from scratch.</p><div class="pc-m"><div><div class="pc-mv">+33%</div><div class="pc-ml">Conversion</div></div><div><div class="pc-mv">-18%</div><div class="pc-ml">CPA</div></div><div><div class="pc-mv">+85%</div><div class="pc-ml">YoY Revenue</div></div></div></div><div class="pc"><div class="pc-co">Advantage Solutions</div><h3 class="pc-t">47 EXCEL MACROS, ONE PERSON UNDERSTOOD THEM</h3><p class="pc-d">99 vendor data sources. 3 analysts spending 4 hours every Monday on manual processing. Replaced tribal knowledge with Python + SQL pipelines that run themselves.</p><div class="pc-m"><div><div class="pc-mv">160 hrs</div><div class="pc-ml">Saved / Quarter</div></div><div><div class="pc-mv">99</div><div class="pc-ml">Vendors Unified</div></div></div></div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="pov"><p class="pov-label">WHAT I BELIEVE</p><p class="pov-text">Most BI teams start with the dashboard. I start with the decision. If you cannot name the specific decision a report changes, you are decorating, not analyzing. The hardest part of my job is never the SQL — it is getting five VPs to agree on what revenue means.</p></div>',unsafe_allow_html=True)
    st.markdown('<div class="tr"><p class="tr-q">"Jason is a masterful practitioner of data tools and management. His out of the box thinking provided solutions that others simply would not conceive. His attitude equally matches his aptitude — a positive influence on those around him with the ability to shine in the toughest of situations."</p><p class="tr-a">Brenton Harlow</p><p class="tr-r">Executive Leader, CPG Sales & Operations — Direct Manager at Advantage Solutions</p></div>',unsafe_allow_html=True)

def render_work():
    st.markdown('<div class="wh"><h1 class="wh-t">CASE STUDIES</h1><p class="wh-s">Deep dives into organizational data problems I have solved</p></div>',unsafe_allow_html=True)
    st.markdown('''<div class="cs"><div class="cs-in">
        <span class="cs-lb">CASE 01 — ADVANTAGE SOLUTIONS</span>
        <h2 class="cs-h">FIVE REVENUE NUMBERS IN ONE BOARD MEETING</h2>
        <p class="cs-sub">Post-merger data unification — 6 weeks — Snowflake, Power BI, DAX, Python</p>
        <div class="cs-res"><div><div class="cs-rv">70%</div><div class="cs-rl">Fewer KPI Conflicts</div></div><div><div class="cs-rv">5→1 day</div><div class="cs-rl">Reporting Cycle</div></div><div><div class="cs-rv">9%</div><div class="cs-rl">Quarterly Revenue Growth</div></div></div>
        <div class="cs-sec"><h3 class="cs-sec-t">THE SITUATION</h3><p>After the merger, I inherited 5 sales systems that did not talk to each other. Each region defined revenue differently. The CFO was getting 5 different numbers in every board meeting. Field teams had lost trust in central reporting and created 47 shadow Excel trackers.</p><ul><li>5 sales systems with incompatible metric definitions</li><li>47 shadow Excel trackers maintained by field teams</li><li>Previous BI lead quit mid-project</li><li>6 weeks until Q3 close deadline</li></ul></div>
        <div class="cs-sec"><h3 class="cs-sec-t">WHY THIS WAS HARD</h3><p>This was not a technical problem — it was political. Each regional VP had built metrics to make their team look good. Standardizing meant someone's numbers would go down. Getting alignment required trust-building before any code was written.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">MY APPROACH</h3><p><strong>Week 1–2:</strong> Interviewed 12 stakeholders. Asked each one: "What decision are you trying to make with this data?" Mapped every metric definition across all 5 systems.</p><p><strong>Week 3:</strong> Facilitated an alignment session. Got 5 VPs to agree on 12 golden metrics with documented definitions. This was the hardest week.</p><p><strong>Week 4–5:</strong> Built unified Snowflake schema. Wrote 40+ DAX measures. Designed Power BI dashboards with drill-through from executive summary to regional detail.</p><p><strong>Week 6:</strong> Trained 250 users. Deprecated 47 legacy reports. Set up data governance process for future metric changes.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">WHAT WENT WRONG</h3><p>APAC had an undocumented custom field that their entire commission structure depended on. Their numbers broke on Day 1 of launch. I had to patch the data model live while the regional VP was on a call with the CEO. Lesson: always audit edge-case dependencies before deprecating legacy systems.</p></div>
        <div class="cs-qt"><p>"Jason is a masterful practitioner of data tools and management. His out of the box thinking provided solutions that others simply would not conceive."</p><cite>— Brenton Harlow, Executive Leader, Direct Manager</cite></div>
    </div></div>''',unsafe_allow_html=True)
    st.markdown('''<div class="cs"><div class="cs-in">
        <span class="cs-lb">CASE 02 — MODERN HOME STATION</span>
        <h2 class="cs-h">MARKETING WAS SPENDING BLIND</h2>
        <p class="cs-sub">Cross-channel attribution & A/B testing — GA4, Shopify, Meta, Klaviyo</p>
        <div class="cs-res"><div><div class="cs-rv">+33%</div><div class="cs-rl">Conversion Rate</div></div><div><div class="cs-rv">-18%</div><div class="cs-rl">CPA Reduction</div></div><div><div class="cs-rv">+85%</div><div class="cs-rl">YoY Revenue (FY20)</div></div></div>
        <div class="cs-sec"><h3 class="cs-sec-t">THE SITUATION</h3><p>Marketing was sending the same promotion to every customer. Data was scattered across Facebook, Shopify, and Google Analytics with no unified customer view. The team was making budget decisions based on last-click attribution, which massively overweighted branded search.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">WHY THIS WAS HARD</h3><p>Each platform had its own tracking pixel, its own definition of "conversion," and its own attribution window. Deduplicating across channels required building a customer identity graph from scratch with no CDP in place.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">MY APPROACH</h3><p>Built cross-channel attribution framework integrating GA4, Shopify, Meta, and Klaviyo into a unified view. Applied K-Means segmentation to identify high-value customer clusters. Designed and led A/B testing program across product pages, content, and UX — testing 12 ad combinations across segments.</p><p>Built lead-scoring and intent models using behavioral and source quality signals. Implemented demand forecasting dashboards that aligned marketing, warehouse, purchasing, and customer service teams.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">WHAT WENT WRONG</h3><p>Saw a spike in video content views but zero corresponding page views. Spent days debugging analytics before discovering the issue was not data — mobile video ads were autoplaying without sound, and users were scrolling past without engaging. Fixed creative direction, not the data pipeline.</p></div>
    </div></div>''',unsafe_allow_html=True)
    st.markdown('''<div class="cs"><div class="cs-in">
        <span class="cs-lb">CASE 03 — ADVANTAGE SOLUTIONS</span>
        <h2 class="cs-h">47 EXCEL MACROS AND ONE PERSON UNDERSTOOD THEM</h2>
        <p class="cs-sub">ETL automation — Python, SQL, 99 vendor sources</p>
        <div class="cs-res"><div><div class="cs-rv">160 hrs</div><div class="cs-rl">Saved per Quarter</div></div><div><div class="cs-rv">99</div><div class="cs-rl">Vendor Sources</div></div><div><div class="cs-rv">15%→2%</div><div class="cs-rl">Error Rate Reduction</div></div></div>
        <div class="cs-sec"><h3 class="cs-sec-t">THE SITUATION</h3><p>"Automation" meant 47 Excel macros that one analyst had built over 3 years. Nobody else understood them. Every Monday, 3 analysts spent 4 hours manually processing vendor reports from 99 different sources. When that one analyst took vacation, reporting stopped. Error rate was running at 15%.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">WHY THIS WAS HARD</h3><p>The macros had undocumented business logic baked in — things like custom GL code mappings and exception rules for specific vendors. Replacing them meant reverse-engineering institutional knowledge that existed only in one person's head.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">MY APPROACH</h3><p>Sat with the analyst for a full week documenting every macro's logic. Built dynamic column mapping in Python that could handle vendor format changes without code updates. Created normalization buckets aligned with GL codes. Used a hybrid Python + SQL approach — Python for ingestion and transformation, SQL for validation and loading.</p><p>Mentored 7 regional analytics managers on the new system to eliminate single-point-of-failure risk.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">WHAT WENT WRONG</h3><p>Three vendors changed their export format in the same week during Q4 close. The old macros would have silently produced wrong numbers. The new Python pipeline caught the schema changes, flagged them, and paused processing until reviewed. The error that would have been invisible became visible — which is the whole point of good automation.</p></div>
    </div></div>''',unsafe_allow_html=True)
    st.markdown('''<div class="cs"><div class="cs-in">
        <span class="cs-lb">CASE 04 — MODERN HOME STATION</span>
        <h2 class="cs-h">FOUR DEPARTMENTS, FOUR SPREADSHEETS, ZERO ALIGNMENT</h2>
        <p class="cs-sub">Demand forecasting & cross-functional alignment — Power BI, SQL</p>
        <div class="cs-res"><div><div class="cs-rv">40%</div><div class="cs-rl">Shorter Feedback Loops</div></div><div><div class="cs-rv">+45%</div><div class="cs-rl">Revenue Growth (FY19)</div></div><div><div class="cs-rv">4</div><div class="cs-rl">Departments Aligned</div></div></div>
        <div class="cs-sec"><h3 class="cs-sec-t">THE SITUATION</h3><p>Marketing, warehouse, purchasing, and customer service each maintained their own forecasting spreadsheet. Marketing would launch a promotion without telling warehouse. Warehouse would run out of stock. Customer service would get flooded with complaints. Late shipments were a recurring problem.</p></div>
        <div class="cs-sec"><h3 class="cs-sec-t">MY APPROACH</h3><p>Built demand forecasting dashboards that pulled from all four departments' data sources into a single Power BI view. Created promotion readiness scorecards — before any campaign launched, the dashboard showed inventory levels, warehouse capacity, and CS staffing against projected demand.</p><p>Delivered executive performance dashboards for sales, marketing, and operations that shortened feedback loops by 40%. Teams could see the impact of decisions within days instead of waiting for monthly reports.</p></div>
    </div></div>''',unsafe_allow_html=True)

def render_about():
    st.markdown('<div class="ah"><div class="about-intro"><h1>I AM JASON CHANG.</h1><p>I started in consumer electronics managing $500M product lines and realized every decision was being made on gut feel. I have spent the last 14 years making sure that does not happen — building the data platforms, metric alignment processes, and reporting systems that turn instinct into evidence.</p><p>Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers on the screen.</p></div></div>',unsafe_allow_html=True)
    st.markdown('''<div class="as">
        <h2 class="as-t">EXPERIENCE</h2>
        <div class="tl">
            <div class="tl-i"><div class="tl-y">2021 – Present</div><div><p class="tl-rl">LEAD DATA ANALYST</p><p class="tl-co">Advantage Solutions</p><p class="tl-d">Built national BI ecosystem from fragmented post-merger data. Unified 99+ vendor sources. Mentored 7 regional analytics managers.</p></div></div>
            <div class="tl-i"><div class="tl-y">2017 – 2021</div><div><p class="tl-rl">BI STRATEGY & ANALYTICS MANAGER</p><p class="tl-co">Modern Home Station</p><p class="tl-d">Created attribution framework that drove +45% (FY19) and +85% (FY20) revenue growth. Led A/B testing program, +33% conversion.</p></div></div>
            <div class="tl-i"><div class="tl-y">2016 – 2017</div><div><p class="tl-rl">BI & STRATEGIC DEVELOPMENT MANAGER</p><p class="tl-co">China Unicom America</p><p class="tl-d">Architected pricing and demand forecast models delivering $2M+ revenue projections.</p></div></div>
            <div class="tl-i"><div class="tl-y">2014 – 2016</div><div><p class="tl-rl">BI PROJECT ANALYST</p><p class="tl-co">Marshall Electronics</p><p class="tl-d">50+ international product launches across retail channels, $5M annual sales. 95% on-time launch rate.</p></div></div>
            <div class="tl-i"><div class="tl-y">2010 – 2014</div><div><p class="tl-rl">SENIOR BUSINESS ANALYST</p><p class="tl-co">Cadence Acoustic Ltd.</p><p class="tl-d">Built first BI systems replacing Excel across $500M product portfolio. Post-merger integration.</p></div></div>
        </div>
    </div>''',unsafe_allow_html=True)
    st.markdown('<div class="as"><h2 class="as-t">EDUCATION</h2><div class="tl"><div class="tl-i"><div class="tl-y">2010</div><div><p class="tl-rl">B.S. BUSINESS ADMINISTRATION</p><p class="tl-co">University of California, Riverside</p></div></div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="as"><h2 class="as-t">SKILLS</h2><div class="sg"><div class="sc"><div class="sc-h">CORE STACK</div><div class="sc-l">SQL (8+ years)<br>Power BI / DAX<br>Python<br>Snowflake<br>Excel + VBA</div></div><div class="sc"><div class="sc-h">ALSO FLUENT</div><div class="sc-l">BigQuery<br>GA4<br>Looker<br>Qlik Sense<br>Power Query</div></div><div class="sc"><div class="sc-h">METHODS</div><div class="sc-l">A/B Testing<br>Attribution Modeling<br>K-Means Clustering<br>Cohort Analysis<br>Forecasting</div></div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="as"><h2 class="as-t">CERTIFICATIONS</h2><div class="cg"><div class="cc2"><p class="cc2-n">Supervised Machine Learning</p><p class="cc2-i">Stanford Online — 2024</p></div><div class="cc2"><p class="cc2-n">Neural Networks & Deep Learning</p><p class="cc2-i">DeepLearning.AI — 2024</p></div><div class="cc2"><p class="cc2-n">Power BI Data Visualization</p><p class="cc2-i">edX — 2019</p></div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="bel"><h2 class="bel-t">WHAT I BELIEVE</h2><p class="bel-p">A dashboard nobody uses is worse than no dashboard — it consumed resources and created false confidence.</p><p class="bel-p">Data governance is not a project. It is a culture you build one conversation at a time.</p><p class="bel-p">The best BI managers spend more time listening to stakeholders than writing queries.</p><p class="bel-p">If your reporting cycle is longer than your decision cycle, you are always too late.</p></div>',unsafe_allow_html=True)

def render_connect():
    st.markdown(f'<div class="cn-h"><h1>LET\'S TALK</h1><p>Open to Senior BI & Analytics Manager opportunities. Best way to reach me is email.</p><div class="cn-cards"><div class="cn-c"><div class="cn-c-i">📧</div><div class="cn-c-l">Email</div><div class="cn-c-v"><a href="mailto:{CONFIG.EMAIL}">{CONFIG.EMAIL}</a></div></div><div class="cn-c"><div class="cn-c-i">💼</div><div class="cn-c-l">LinkedIn</div><div class="cn-c-v"><a href="{CONFIG.LINKEDIN_URL}">{CONFIG.LINKEDIN}</a></div></div><div class="cn-c"><div class="cn-c-i">📱</div><div class="cn-c-l">Phone</div><div class="cn-c-v">{CONFIG.PHONE}</div></div><div class="cn-c"><div class="cn-c-i">📍</div><div class="cn-c-l">Location</div><div class="cn-c-v">{CONFIG.LOCATION}</div></div></div></div>',unsafe_allow_html=True)
    st.markdown('<div class="cn-test"><h2 class="cn-test-t">WHAT MY MANAGER SAID</h2><div class="cn-test-c"><p class="cn-test-q">"Jason is a masterful practitioner of data tools and management. He is someone our team relied on for all key performance metrics in a very demanding and often changing environment. His attitude equally matches his aptitude. Jason is a positive influence on those around him and has the ability to shine in the darkest of and toughest of situations. His out of the box thinking provided solutions that others simply would not conceive. I am very glad I was fortunate enough to work with Jason and hope to do so again."</p><p class="cn-test-a">Brenton Harlow</p><p class="cn-test-r">Executive Leader, CPG Sales, Marketing, Operations & Technology — Direct Manager at Advantage Solutions</p></div></div>',unsafe_allow_html=True)

if __name__=="__main__":
    main()
