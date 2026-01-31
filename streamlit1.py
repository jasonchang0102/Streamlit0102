import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Jason Chang", page_icon="◆")

# Track page changes
if 'prev_page' not in st.session_state:
    st.session_state.prev_page = None

st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Sans:wght@400;500;600;700&display=swap' rel='stylesheet'>
<style>
    :root {
        --b: #111111;
        --w: #ffffff;
        --c1: #f5f5f5;
        --c2: #e5e5e5;
        --g1: #e5e5e5;
        --g2: #d4d4d4;
        --g3: #a3a3a3;
        --g4: #737373;
        --g5: #525252;
        --g6: #404040;
        --g7: #262626;
        --g8: #171717;
        --g9: #111111;
    }
    
    ::-webkit-scrollbar{width:4px}
    ::-webkit-scrollbar-track{background:var(--b)}
    ::-webkit-scrollbar-thumb{background:var(--g6)}
    
    .stApp{background:var(--w)!important;overflow-x:hidden!important}
    #MainMenu,footer,header{visibility:hidden}
    .block-container{padding:0!important;max-width:100%!important}
    
    .stApp::before{content:'';position:fixed;inset:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");opacity:0.012;pointer-events:none;z-index:10000}
    
    /* === ANIMATIONS === */
    @keyframes heroIn{
        0%{transform:translateY(50px) rotateX(-6deg);opacity:0;filter:blur(10px)}
        100%{transform:translateY(0) rotateX(0);opacity:1;filter:blur(0)}
    }
    @keyframes fadeUp{
        0%{opacity:0;transform:translateY(25px)}
        100%{opacity:1;transform:translateY(0)}
    }
    @keyframes fadeIn{
        0%{opacity:0}
        100%{opacity:1}
    }
    @keyframes slideLeft{
        0%{opacity:0;transform:translateX(-25px)}
        100%{opacity:1;transform:translateX(0)}
    }
    @keyframes slideRight{
        0%{opacity:0;transform:translateX(25px)}
        100%{opacity:1;transform:translateX(0)}
    }
    @keyframes scaleIn{
        0%{opacity:0;transform:scale(0.95)}
        100%{opacity:1;transform:scale(1)}
    }
    @keyframes lineGrow{0%{transform:scaleX(0)}100%{transform:scaleX(1)}}
    @keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
    @keyframes float{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-12px) rotate(2deg)}}
    @keyframes pulse{0%,100%{transform:scale(1);box-shadow:0 0 0 0 rgba(34,197,94,0.4)}50%{transform:scale(1.15);box-shadow:0 0 0 6px rgba(34,197,94,0)}}
    @keyframes rotate{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}
    @keyframes breathe{0%,100%{opacity:0.4}50%{opacity:1}}
    @keyframes numberPop{
        0%{transform:scale(0.8);opacity:0}
        50%{transform:scale(1.05)}
        100%{transform:scale(1);opacity:1}
    }
    @keyframes clipReveal{
        0%{clip-path:inset(0 100% 0 0)}
        100%{clip-path:inset(0 0 0 0)}
    }
    @keyframes glowPulse{
        0%,100%{box-shadow:0 0 0 0 rgba(255,255,255,0.1)}
        50%{box-shadow:0 0 20px 5px rgba(255,255,255,0.05)}
    }
    
    /* === SIDEBAR === */
    section[data-testid="stSidebar"]{background:var(--b)!important}
    section[data-testid="stSidebar"] .stRadio>div{gap:0!important}
    section[data-testid="stSidebar"] .stRadio>div>label{background:transparent!important;color:#ffffff!important;font-family:'DM Sans',sans-serif!important;font-size:13px!important;font-weight:500!important;padding:16px 28px!important;transition:all .4s cubic-bezier(.16,1,.3,1)!important;border-left:2px solid transparent!important}
    section[data-testid="stSidebar"] .stRadio>div>label:hover{color:#ffffff!important;padding-left:36px!important;background:rgba(255,255,255,0.05)!important}
    section[data-testid="stSidebar"] .stRadio>div>label[data-checked="true"]{color:#ffffff!important;font-weight:600!important;border-left-color:#ffffff!important;background:rgba(255,255,255,0.03)!important}
    section[data-testid="stSidebar"] .stRadio>div>label span,section[data-testid="stSidebar"] .stRadio>div>label p{color:inherit!important}
    .nb{font-family:'Outfit',sans-serif!important;font-size:28px!important;font-weight:700!important;color:#ffffff!important;letter-spacing:2px!important;padding:36px 28px 32px!important;border-bottom:1px solid rgba(255,255,255,0.04)!important;margin-bottom:12px!important;animation:fadeIn .6s ease both}
    .nl{font-family:'DM Sans',sans-serif!important;font-size:14px!important;font-weight:600!important;color:#a3a3a3!important;letter-spacing:3px!important;text-transform:uppercase!important;padding:18px 28px 10px!important}
    
    /* === HERO === */
    .hs{display:grid;grid-template-columns:54% 46%;min-height:100vh}
    .hl{background:var(--b)!important;padding:60px 55px;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden}
    .hl::before{content:'JC';position:absolute;bottom:-70px;right:-35px;font-family:'Outfit',sans-serif;font-size:350px;font-weight:900;color:rgba(255,255,255,0.006);line-height:.8;pointer-events:none;animation:fadeIn 1.5s ease 0.5s both}
    .hr{background:linear-gradient(155deg,var(--c1) 0%,var(--c2) 100%)!important;padding:60px 55px;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden}
    .dr{position:absolute;width:120px;height:120px;border:1px solid rgba(255,255,255,0.035);border-radius:50%;top:60px;right:60px;animation:rotate 28s linear infinite,glowPulse 4s ease infinite}
    .dr::before{content:'';position:absolute;top:50%;left:50%;width:4px;height:4px;background:var(--w);border-radius:50%;transform:translate(-50%,-50%);animation:breathe 3s ease infinite}
    .db{position:absolute;width:70px;height:70px;border:1px solid rgba(0,0,0,0.025);bottom:80px;right:55px;animation:float 6s ease-in-out infinite}
    .dg{position:absolute;top:70px;left:55px;display:grid;grid-template-columns:repeat(4,7px);gap:8px;opacity:.06;animation:fadeIn 1s ease 0.8s both}
    .dd{width:2px;height:2px;background:var(--b);border-radius:50%}
    .hb{display:inline-flex;align-items:center;gap:9px;padding:9px 16px;border:1px solid rgba(255,255,255,0.05);border-radius:28px;margin-bottom:35px;animation:slideLeft .6s cubic-bezier(.16,1,.3,1) .1s both}
    .hbd{width:6px;height:6px;background:#22c55e;border-radius:50%;animation:pulse 2s ease infinite}
    .hbt{font-family:'DM Sans',sans-serif;font-size:9px;font-weight:600;color:var(--g5);letter-spacing:1.5px;text-transform:uppercase}
    
    /* HERO NAME - 115px (reduced by 5 from 120) */
    .hn{font-family:'Outfit',sans-serif!important;font-size:115px!important;font-weight:800!important;color:var(--w)!important;letter-spacing:-2px!important;line-height:.92!important;margin:0!important;animation:heroIn .9s cubic-bezier(.16,1,.3,1) both!important}
    .hn2{animation-delay:.07s!important}
    .hns{font-family:'Outfit',sans-serif!important;font-size:115px!important;font-weight:800!important;color:transparent!important;-webkit-text-stroke:1px rgba(255,255,255,0.08)!important;letter-spacing:-2px!important;line-height:.92!important;margin:0!important;animation:heroIn .9s cubic-bezier(.16,1,.3,1) .14s both!important}
    .hrw{display:flex;align-items:center;gap:15px;margin-top:30px}
    .hrl{width:45px;height:1px;background:var(--g6);animation:lineGrow .5s cubic-bezier(.16,1,.3,1) .35s both;transform-origin:left}
    .hro{font-family:'DM Sans',sans-serif;font-size:10px;font-weight:600;color:var(--g5);letter-spacing:3px;text-transform:uppercase;animation:slideLeft .5s cubic-bezier(.16,1,.3,1) .4s both}
    .he{font-family:'DM Sans',sans-serif;font-size:9px;font-weight:700;color:var(--g5);letter-spacing:3px;text-transform:uppercase;margin-bottom:22px;animation:slideLeft .5s cubic-bezier(.16,1,.3,1) .15s both}
    .hh{font-family:'Playfair Display',serif!important;font-size:40px!important;font-weight:500!important;color:var(--b)!important;line-height:1.2!important;margin-bottom:18px!important;animation:fadeUp .6s cubic-bezier(.16,1,.3,1) .25s both!important}
    .hh em{font-style:italic;font-weight:400}
    .hp{font-family:'DM Sans',sans-serif!important;font-size:14px!important;color:var(--g6)!important;line-height:1.75!important;max-width:340px!important;animation:fadeUp .6s cubic-bezier(.16,1,.3,1) .35s both!important}
    
    /* === MARQUEE === */
    .mw{background:var(--b)!important;padding:18px 0;overflow:hidden;position:relative}
    .mw::before,.mw::after{content:'';position:absolute;top:0;width:50px;height:100%;z-index:2}
    .mw::before{left:0;background:linear-gradient(90deg,var(--b),transparent)}
    .mw::after{right:0;background:linear-gradient(-90deg,var(--b),transparent)}
    .mt{display:flex;animation:marquee 28s linear infinite;width:max-content}
    .mi{font-family:'Outfit',sans-serif;font-size:11px;font-weight:600;color:var(--g6);letter-spacing:4px;text-transform:uppercase;white-space:nowrap;padding:0 18px;display:flex;align-items:center;gap:18px}
    .md{width:3px;height:3px;background:var(--g7);border-radius:50%}
    
    /* === STATS === */
    .sw{display:grid;grid-template-columns:repeat(3,1fr);background:var(--w)!important}
    .sb{padding:60px 35px;text-align:center;border-right:1px solid var(--g2);position:relative;overflow:hidden;transition:all .5s cubic-bezier(.16,1,.3,1);background:var(--w)!important}
    .sb:last-child{border-right:none}
    .sb::before{content:'';position:absolute;inset:0;background:var(--b);transform:translateY(100%);transition:transform .5s cubic-bezier(.16,1,.3,1)}
    .sb:hover::before{transform:translateY(0)}
    .sb:hover .sn,.sb:hover .sl{color:var(--w)!important}
    .sn{font-family:'Outfit',sans-serif!important;font-size:85px!important;font-weight:700!important;color:var(--b)!important;line-height:1!important;position:relative;z-index:1;transition:color .5s cubic-bezier(.16,1,.3,1);animation:numberPop .6s ease both}
    .sb:nth-child(1) .sn{animation-delay:.1s}
    .sb:nth-child(2) .sn{animation-delay:.2s}
    .sb:nth-child(3) .sn{animation-delay:.3s}
    .sl{font-family:'DM Sans',sans-serif!important;font-size:9px!important;font-weight:600!important;color:var(--g5)!important;margin-top:14px!important;text-transform:uppercase!important;letter-spacing:3px!important;position:relative;z-index:1;transition:color .5s cubic-bezier(.16,1,.3,1)}
    
    /* === SECTION HEADERS === */
    .sd{background:var(--b)!important;padding:55px 70px 40px!important}
    .sdt{font-family:'DM Sans',sans-serif!important;font-size:9px!important;font-weight:700!important;color:var(--g5)!important;letter-spacing:3px!important;text-transform:uppercase!important;margin-bottom:18px!important;animation:slideLeft .5s ease both}
    .sdn{font-family:'Outfit',sans-serif!important;font-size:85px!important;font-weight:800!important;color:var(--w)!important;letter-spacing:-2px!important;line-height:.95!important;margin:0!important;animation:clipReveal .8s ease .1s both}
    
    .sl2{background:var(--w)!important;padding:55px 70px 40px!important}
    .slt{font-family:'DM Sans',sans-serif!important;font-size:9px!important;font-weight:700!important;color:var(--g4)!important;letter-spacing:3px!important;text-transform:uppercase!important;margin-bottom:18px!important;animation:slideLeft .5s ease both}
    .sln{font-family:'Outfit',sans-serif!important;font-size:85px!important;font-weight:800!important;color:var(--b)!important;letter-spacing:-2px!important;line-height:.95!important;margin:0!important;animation:clipReveal .8s ease .1s both}
    
    /* === DARK CONTENT === */
    .cd{background:var(--b)!important;padding:25px 70px 55px!important}
    .cd .sr{display:flex;gap:28px;margin-bottom:25px;animation:fadeUp .5s ease both}
    .cd .sr:nth-child(1){animation-delay:.1s}
    .cd .sr:nth-child(2){animation-delay:.2s}
    .cd .sr:nth-child(3){animation-delay:.3s}
    .cd .snum{font-family:'Outfit',sans-serif;font-size:48px;font-weight:700;color:rgba(255,255,255,0.2);line-height:1;min-width:55px;animation:numberPop .5s ease both}
    .cd .sc{flex:1;padding-top:6px}
    .cd .st{font-family:'DM Sans',sans-serif;font-size:9px;font-weight:700;color:var(--w);letter-spacing:2.5px;text-transform:uppercase;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid var(--g8);display:inline-block}
    .cd .bt{font-family:'DM Sans',sans-serif;font-size:14px;color:var(--g4);line-height:1.75;max-width:480px}
    .cd .bt strong{color:var(--w);font-weight:600}
    .cd .bi{font-family:'DM Sans',sans-serif;font-size:13px;color:var(--g4);line-height:1.75;margin-bottom:10px;padding-left:24px;position:relative;transition:all .3s ease}
    .cd .bi::before{content:'';position:absolute;left:0;top:9px;width:14px;height:1px;background:var(--g7);transition:all .3s ease}
    .cd .bi:hover{padding-left:32px;color:var(--w)}
    .cd .bi:hover::before{width:22px;background:var(--w)}
    .cd .bi strong{color:var(--w);font-weight:600}
    
    /* === LIGHT CONTENT === */
    .cl{background:var(--w)!important;padding:25px 70px 55px!important}
    .cl .sr{display:flex;gap:28px;margin-bottom:25px;animation:fadeUp .5s ease both}
    .cl .sr:nth-child(1){animation-delay:.1s}
    .cl .sr:nth-child(2){animation-delay:.2s}
    .cl .sr:nth-child(3){animation-delay:.3s}
    .cl .snum{font-family:'Outfit',sans-serif;font-size:48px;font-weight:700;color:var(--g3);line-height:1;min-width:55px;animation:numberPop .5s ease both}
    .cl .sc{flex:1;padding-top:6px}
    .cl .st{font-family:'DM Sans',sans-serif;font-size:9px;font-weight:700;color:var(--b);letter-spacing:2.5px;text-transform:uppercase;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid var(--g2);display:inline-block}
    .cl .bt{font-family:'DM Sans',sans-serif;font-size:14px;color:var(--g6);line-height:1.75;max-width:480px}
    .cl .bt strong{color:var(--b);font-weight:600}
    .cl .bi{font-family:'DM Sans',sans-serif;font-size:13px;color:var(--g6);line-height:1.75;margin-bottom:10px;padding-left:24px;position:relative;transition:all .3s ease}
    .cl .bi::before{content:'';position:absolute;left:0;top:9px;width:14px;height:1px;background:var(--g3);transition:all .3s ease}
    .cl .bi:hover{padding-left:32px;color:var(--b)}
    .cl .bi:hover::before{width:22px;background:var(--b)}
    .cl .bi strong{color:var(--b);font-weight:600}
    
    /* === IMAGE PADDING - 2rem LEFT/RIGHT === */
    .stImage{padding:0.5rem 2rem!important;animation:scaleIn .5s ease both}
    .stImage img{transition:all .5s cubic-bezier(.16,1,.3,1)!important;border-radius:2px}
    .stImage img:hover{transform:scale(1.01)!important;box-shadow:0 25px 50px rgba(0,0,0,0.06)!important}
    
    /* === RESULT CARDS === */
    .rg{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:30px}
    .rc{background:var(--g1);padding:45px 38px;position:relative;overflow:hidden;transition:all .5s cubic-bezier(.16,1,.3,1);animation:scaleIn .5s ease both}
    .rc:nth-child(1){animation-delay:.1s}
    .rc:nth-child(2){animation-delay:.2s}
    .rc::before{content:'';position:absolute;left:0;bottom:0;width:100%;height:3px;background:var(--b);transform:scaleX(0);transform-origin:left;transition:transform .5s cubic-bezier(.16,1,.3,1)}
    .rc:hover{transform:translateY(-10px);box-shadow:0 28px 55px rgba(0,0,0,0.06)}
    .rc:hover::before{transform:scaleX(1)}
    .rcn{font-family:'Outfit',sans-serif!important;font-size:60px!important;font-weight:700!important;color:var(--b)!important;line-height:1!important}
    .rct{font-family:'DM Sans',sans-serif!important;font-size:9px!important;font-weight:700!important;color:var(--b)!important;margin:16px 0 8px!important;text-transform:uppercase!important;letter-spacing:2px!important}
    .rcd{font-family:'DM Sans',sans-serif!important;font-size:12px!important;color:var(--g5)!important;line-height:1.55!important}
    
    /* === INFO CARDS === */
    .ig{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:25px}
    .ic{background:var(--g1);padding:35px;transition:all .45s cubic-bezier(.16,1,.3,1);position:relative;overflow:hidden;animation:slideRight .5s ease both}
    .ic:nth-child(1){animation-delay:.1s}
    .ic:nth-child(2){animation-delay:.2s}
    .ic::after{content:'';position:absolute;bottom:0;left:0;width:100%;height:3px;background:var(--b);transform:scaleX(0);transform-origin:left;transition:transform .45s cubic-bezier(.16,1,.3,1)}
    .ic:hover{transform:translateY(-7px);box-shadow:0 20px 40px rgba(0,0,0,0.05)}
    .ic:hover::after{transform:scaleX(1)}
    .ict{font-family:'DM Sans',sans-serif!important;font-size:9px!important;font-weight:700!important;color:var(--b)!important;letter-spacing:2px!important;text-transform:uppercase!important;margin-bottom:10px!important}
    .icd{font-family:'DM Sans',sans-serif!important;font-size:12px!important;color:var(--g5)!important;line-height:1.65!important}
    
    /* === SKILLS === */
    .sg{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    .skc{background:var(--g1);padding:32px;transition:all .45s cubic-bezier(.16,1,.3,1);position:relative;overflow:hidden;animation:fadeUp .4s ease both}
    .skc:nth-child(1){animation-delay:.05s}
    .skc:nth-child(2){animation-delay:.1s}
    .skc:nth-child(3){animation-delay:.15s}
    .skc:nth-child(4){animation-delay:.2s}
    .skc:nth-child(5){animation-delay:.25s}
    .skc:nth-child(6){animation-delay:.3s}
    .skc::before{content:'';position:absolute;top:0;left:0;width:3px;height:0;background:var(--b);transition:height .45s cubic-bezier(.16,1,.3,1)}
    .skc:hover{transform:translateX(8px)}
    .skc:hover::before{height:100%}
    .skt{font-family:'DM Sans',sans-serif!important;font-size:14px!important;font-weight:700!important;color:var(--b)!important;letter-spacing:2px!important;text-transform:uppercase!important;margin-bottom:10px!important}
    .skl{font-family:'DM Sans',sans-serif!important;font-size:17px!important;color:var(--g5)!important;line-height:1.85!important}
    
    /* === CERTS === */
    .ci{display:grid;grid-template-columns:65px 1fr auto;gap:25px;align-items:center;padding:30px 0;border-bottom:1px solid var(--g2);transition:all .35s cubic-bezier(.16,1,.3,1);animation:slideLeft .4s ease both}
    .ci:nth-child(1){animation-delay:.1s}
    .ci:nth-child(2){animation-delay:.15s}
    .ci:nth-child(3){animation-delay:.2s}
    .ci:nth-child(4){animation-delay:.25s}
    .ci:nth-child(5){animation-delay:.3s}
    .ci:hover{padding-left:12px}
    .cin{font-family:'Outfit',sans-serif;font-size:42px;font-weight:700;color:var(--g2);line-height:1}
    .cit{font-family:'DM Sans',sans-serif!important;font-size:14px!important;font-weight:600!important;color:var(--b)!important;margin-bottom:3px!important}
    .cio{font-family:'DM Sans',sans-serif!important;font-size:11px!important;color:var(--g5)!important}
    .cil{font-family:'DM Sans',sans-serif!important;font-size:9px!important;font-weight:700!important;color:var(--b)!important;letter-spacing:1.5px!important;text-transform:uppercase!important;text-decoration:none!important;padding:10px 18px!important;border:1px solid var(--g3)!important;transition:all .35s cubic-bezier(.16,1,.3,1)!important;display:inline-block!important}
    .cil:hover{background:var(--b)!important;color:var(--w)!important;border-color:var(--b)!important}
    .cina{font-family:'DM Sans',sans-serif!important;font-size:10px!important;color:var(--g3)!important}
    
    /* === CONTACT === */
    .cg{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
    .cc{background:var(--g1);padding:32px 36px;transition:all .35s cubic-bezier(.16,1,.3,1);position:relative;overflow:hidden;animation:fadeUp .4s ease both}
    .cc:nth-child(1){animation-delay:.1s}
    .cc:nth-child(2){animation-delay:.15s}
    .cc:nth-child(3){animation-delay:.2s}
    .cc:nth-child(4){animation-delay:.25s}
    .cc::after{content:'';position:absolute;bottom:0;left:0;width:100%;height:3px;background:var(--b);transform:scaleX(0);transform-origin:left;transition:transform .35s cubic-bezier(.16,1,.3,1)}
    .cc:hover::after{transform:scaleX(1)}
    .ccl{font-family:'DM Sans',sans-serif!important;font-size:8px!important;font-weight:700!important;color:var(--g4)!important;letter-spacing:2px!important;text-transform:uppercase!important;margin-bottom:8px!important}
    .ccv{font-family:'Space Grotesk',sans-serif!important;font-size:15px!important;font-weight:500!important;color:var(--b)!important}
    .ccv a{color:var(--b)!important;text-decoration:none!important;border-bottom:1px solid var(--g3)!important;transition:border-color .3s ease!important}
    .ccv a:hover{border-color:var(--b)!important}
    
    /* === QUOTE === */
    .qs{background:linear-gradient(155deg,var(--c1) 0%,var(--c2) 100%)!important;padding:75px 70px;position:relative;animation:fadeIn .5s ease both}
    .qm{font-family:'Playfair Display',serif;font-size:220px;color:rgba(0,0,0,0.015);position:absolute;top:-15px;left:15px;line-height:1;pointer-events:none}
    .qt{font-family:'Playfair Display',serif!important;font-size:28px!important;font-weight:400!important;font-style:italic!important;color:var(--b)!important;line-height:1.5!important;max-width:520px!important;position:relative;z-index:1}
    
    /* === MISC === */
    .cdl{font-family:'DM Sans',sans-serif!important;font-size:8px!important;font-weight:700!important;color:var(--g4)!important;letter-spacing:2px!important;text-transform:uppercase!important;margin-bottom:14px!important;padding-left:2rem!important}
    .dv{width:calc(100% - 4rem)!important;height:1px;background:var(--g2);margin:55px 2rem!important}
    
    h1,h2,h3{font-family:'Outfit',sans-serif!important}
    p,li{font-family:'DM Sans',sans-serif!important}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown('<div class="nb">JC</div>', unsafe_allow_html=True)
    st.markdown('<p class="nl">Menu</p>', unsafe_allow_html=True)
    page = st.radio("", ["Home","Engagement","Executive","Warehouse","Automation","Skills","Certs","Contact"], label_visibility="collapsed")

# Scroll to top on page change
if st.session_state.prev_page != page:
    st.session_state.prev_page = page
    components.html(
        """<script>
        var main = window.parent.document.querySelector('.main');
        if(main) main.scrollTo({top: 0, behavior: 'instant'});
        </script>""",
        height=0
    )

@st.cache_data
def load_data(url):
    d = pd.read_csv(url)
    d['Date'] = pd.to_datetime(d['Date'])
    return d

data = load_data("https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv")

if page == "Home":
    st.markdown("""
    <div class="hs">
        <div class="hl">
            <div class="dr"></div>
            <div class="hb"><span class="hbd"></span><span class="hbt">Open to Work</span></div>
            <p class="hn">JASON</p>
            <p class="hn hn2">CHANG</p>
            <p class="hns">PORTFOLIO</p>
            <div class="hrw"><div class="hrl"></div><span class="hro">Revenue & Growth Analytics</span></div>
        </div>
        <div class="hr">
            <div class="db"></div>
            <div class="dg"><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span><span class="dd"></span></div>
            <p class="he">About Me</p>
            <p class="hh">Turning <em>complex data</em> into strategic growth.</p>
            <p class="hp">Data-driven leader with 10+ years scaling national programs through market strategy, analytics, and channel expansion. I translate complex data into actionable insights to accelerate decisions and drive measurable revenue growth.</p>
        </div>
    </div>
    <div class="mw"><div class="mt"><span class="mi">SNOWFLAKE <span class="md"></span> POWER BI <span class="md"></span> PYTHON <span class="md"></span> SQL <span class="md"></span> GA4 <span class="md"></span> BIGQUERY <span class="md"></span> A/B TESTING <span class="md"></span> ATTRIBUTION</span><span class="mi">SNOWFLAKE <span class="md"></span> POWER BI <span class="md"></span> PYTHON <span class="md"></span> SQL <span class="md"></span> GA4 <span class="md"></span> BIGQUERY <span class="md"></span> A/B TESTING <span class="md"></span> ATTRIBUTION</span></div></div>
    <div class="sw"><div class="sb"><p class="sn">10+</p><p class="sl">Years Experience</p></div><div class="sb"><p class="sn">70%</p><p class="sl">Faster Data Refresh</p></div><div class="sb"><p class="sn">36%</p><p class="sl">ROAS Increase</p></div></div>
    """, unsafe_allow_html=True)

elif page == "Engagement":
    st.markdown("""
    <div class="sd"><p class="sdt">Case Study</p><p class="sdn">PLAYER<br>ENGAGEMENT</p></div>
    <div class="cd">
        <div class="sr"><span class="snum">01</span><div class="sc"><p class="st">Situation</p><p class="bt">Tasked with maximizing revenue and player engagement for Warcraft during two key in-game events. Challenge: understanding player segment behavior and identifying monetization opportunities.</p></div></div>
        <div class="sr"><span class="snum">02</span><div class="sc"><p class="st">Task</p><p class="bi">Identify high-spending player segments for targeted promotions</p><p class="bi">Analyze low spending trends by region and platform</p><p class="bi">Conduct exploratory analysis on spending behaviors</p></div></div>
        <div class="sr"><span class="snum">03</span><div class="sc"><p class="st">Action</p><p class="bi"><strong>EDA & Clustering</strong> — Python-based analysis with K-Means segmentation</p><p class="bi"><strong>Heatmap Analysis</strong> — Identified spending patterns across segments</p><p class="bi"><strong>Strategic Output</strong> — Prioritized Platform 3, Region 1</p></div></div>
    </div>
    """, unsafe_allow_html=True)

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

    hm = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    f1, a1 = plt.subplots(figsize=(9, 5))
    f1.patch.set_facecolor('#080808')
    a1.set_facecolor('#080808')
    sns.heatmap(hm, annot=True, cmap="Greys", fmt=".2f", linewidths=4, ax=a1, annot_kws={"color": "#fafafa", "fontsize": 11, "fontweight": "bold"}, linecolor='#080808', cbar=False)
    a1.tick_params(colors='#fafafa', labelsize=10)
    a1.set_xlabel('', fontsize=0)
    a1.set_ylabel('', fontsize=0)
    for s in a1.spines.values():
        s.set_visible(False)
    st.pyplot(f1)
    plt.close(f1)

    e1 = data[(data['Date'] >= '2017-01-24') & (data['Date'] <= '2017-02-14')]
    e2 = data[(data['Date'] >= '2017-02-28') & (data['Date'] <= '2017-03-21')]
    f, ax = plt.subplots(2, 2, figsize=(10, 7))
    f.patch.set_facecolor('#fafafa')
    for a in ax.flat:
        a.set_facecolor('#fafafa')
        a.tick_params(colors='#080808', labelsize=9)
        for s in a.spines.values():
            s.set_visible(False)
    for i, (c, t) in enumerate([('games_played', 'GAMES'), ('skill_last', 'SKILL'), ('items_crafted', 'ITEMS'), ('dollars_spent', 'SPEND')]):
        a = ax[i // 2, i % 2]
        sns.kdeplot(e1[c], fill=True, color="#080808", label="Event 1", ax=a, alpha=0.12)
        sns.kdeplot(e2[c], fill=True, color="#737373", label="Event 2", ax=a, alpha=0.2)
        a.set_title(t, fontsize=11, fontweight='700', color='#080808')
        a.legend(fontsize=8, frameon=False)
    plt.tight_layout()
    st.pyplot(f)
    plt.close(f)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', use_container_width=True)

    st.markdown("""
    <div class="cl">
        <div class="sr"><span class="snum">04</span><div class="sc"><p class="st">Results</p></div></div>
        <div class="rg"><div class="rc"><p class="rcn">+33%</p><p class="rct">Conversion Lift</p><p class="rcd">A/B testing program across product, content, and UX</p></div><div class="rc"><p class="rcn">-18%</p><p class="rct">CPA Reduction</p><p class="rcd">Improved funnel visibility and budget allocation</p></div></div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Executive":
    st.markdown('<div class="sl2"><p class="slt">Case Study</p><p class="sln">EXECUTIVE<br>INTELLIGENCE</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="cl"><div class="sr"><span class="snum">01</span><div class="sc"><p class="st">Situation</p><p class="bt">Post-merger environment with 5 fragmented sales domains and inconsistent metrics. Finance and marketing leadership lacked unified performance visibility.</p></div></div></div>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', use_container_width=True)
    st.markdown('<div class="cl"><div class="sr"><span class="snum">02</span><div class="sc"><p class="st">Task</p><p class="bt">Design scalable data pipelines and semantic layers translating C-suite requirements into actionable dashboards with real-time insights.</p></div></div></div>', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', use_container_width=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', use_container_width=True)
    st.markdown("""
    <div class="cl">
        <div class="sr"><span class="snum">03</span><div class="sc"><p class="st">Action</p><p class="bi"><strong>Schema Design</strong> — Optimized Snowflake schemas consolidating POS, field, compliance, and promo data</p><p class="bi"><strong>KPI Standardization</strong> — Unified metrics across domains, reducing conflicts 70%</p><p class="bi"><strong>ELT Automation</strong> — Automated pipelines cutting decision cycle from 5 days → 24 hrs</p></div></div>
        <div class="sr"><span class="snum">04</span><div class="sc"><p class="st">Results</p></div></div>
        <div class="ig"><div class="ic"><p class="ict">9% Quarterly Revenue Lift</p><p class="icd">Faster decisions enabled by real-time executive dashboards</p></div><div class="ic"><p class="ict">250+ Users Enabled</p><p class="icd">Sales/ops staff with near-real-time performance visibility</p></div></div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Warehouse":
    st.markdown("""
    <div class="sd"><p class="sdt">Case Study</p><p class="sdn">FULFILLMENT<br>FORECASTING</p></div>
    <div class="cd">
        <div class="sr"><span class="snum">01</span><div class="sc"><p class="st">Situation</p><p class="bt">Marketing, warehouse, purchasing, and customer service operated on disconnected data sources. Late shipments impacted customer satisfaction and promotion execution.</p></div></div>
        <div class="sr"><span class="snum">02</span><div class="sc"><p class="st">Task</p><p class="bt">Build demand forecasting dashboards to align cross-functional teams and improve fulfillment accuracy.</p></div></div>
        <div class="sr"><span class="snum">03</span><div class="sc"><p class="st">Action</p><p class="bi"><strong>Demand Modeling</strong> — Built forecasting models integrating sales velocity, promo calendars, and seasonality</p><p class="bi"><strong>Cross-Functional Alignment</strong> — Unified marketing, warehouse, purchasing data into single view</p><p class="bi"><strong>SLA Tracking</strong> — Automated alerts for inventory thresholds and fulfillment bottlenecks</p></div></div>
    </div>
    """, unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', use_container_width=True)
    st.markdown("""
    <div class="cl"><div class="sr"><span class="snum">04</span><div class="sc"><p class="st">Results</p></div></div>
        <div class="rg"><div class="rc"><p class="rcn">-22%</p><p class="rct">Late Shipments</p><p class="rcd">Improved fulfillment accuracy via predictive modeling</p></div><div class="rc"><p class="rcn">↑</p><p class="rct">Promo Readiness</p><p class="rcd">Teams aligned on inventory before campaign launches</p></div></div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Automation":
    st.markdown('<div class="sl2"><p class="slt">Case Study</p><p class="sln">DATA<br>AUTOMATION</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="cl"><div class="sr"><span class="snum">01</span><div class="sc"><p class="st">Situation</p><p class="bt">99+ vendor data sources with inconsistent formats. Manual ingestion consumed analyst bandwidth and introduced refresh errors impacting downstream reporting.</p></div></div></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="cdl">PYTHON AUTOMATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', use_container_width=True)
    with col2:
        st.markdown('<p class="cdl">VBA INTEGRATION</p>', unsafe_allow_html=True)
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', use_container_width=True)
    st.markdown("""
    <div class="cl">
        <div class="sr"><span class="snum">02</span><div class="sc"><p class="st">Task</p><p class="bt">Automate ingestion pipelines across all vendor sources to eliminate manual work and ensure data quality.</p></div></div>
        <div class="sr"><span class="snum">03</span><div class="sc"><p class="st">Action</p><p class="bi"><strong>Python/SQL Pipeline</strong> — Built automated ingestion for 99+ vendor formats</p><p class="bi"><strong>Exception Logic</strong> — Automated audit and validation rules catching errors pre-refresh</p><p class="bi"><strong>VBA Integration</strong> — Legacy Excel report automation for stakeholder delivery</p></div></div>
        <div class="sr"><span class="snum">04</span><div class="sc"><p class="st">Results</p></div></div>
    </div>
    <div class="sw"><div class="sb"><p class="sn">160+</p><p class="sl">Hours Saved / Quarter</p></div><div class="sb"><p class="sn">-80%</p><p class="sl">Refresh Errors</p></div><div class="sb"><p class="sn">99+</p><p class="sl">Vendors Automated</p></div></div>
    """, unsafe_allow_html=True)

elif page == "Skills":
    st.markdown('<div class="sd"><p class="sdt">Expertise</p><p class="sdn">TECHNICAL<br>SKILLS</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="cl">', unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=110)
    st.markdown('<div class="dv"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sg">
        <div class="skc"><p class="skt">BI & Visualization</p><p class="skl">Power BI / DAX<br>Looker / Qlik<br>Google Data Studio</p></div>
        <div class="skc"><p class="skt">Languages</p><p class="skl">SQL<br>Python<br>VBA / Power Query</p></div>
        <div class="skc"><p class="skt">Cloud & Warehousing</p><p class="skl">Snowflake<br>BigQuery<br>SQL Server (SSMS)</p></div>
        <div class="skc"><p class="skt">SaaS & Platforms</p><p class="skl">GA4 / Meta Ads<br>Shopify / HubSpot<br>Klaviyo</p></div>
        <div class="skc"><p class="skt">Statistical Analysis</p><p class="skl">A/B Testing<br>Regression / Cohort<br>Predictive Modeling</p></div>
        <div class="skc"><p class="skt">Frameworks</p><p class="skl">Attribution Modeling<br>Funnel Analysis<br>Demand Forecasting</p></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Certs":
    st.markdown('<div class="sl2"><p class="slt">Credentials</p><p class="sln">CERTIFICATIONS</p></div><div class="cl">', unsafe_allow_html=True)
    certs = [
        ("01", "Supervised Machine Learning", "Stanford / Coursera · 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/STANDFORD.PNG", "https://www.coursera.org/account/accomplishments/verify/YHLXRW3TL569"),
        ("02", "Neural Networks & Deep Learning", "DeepLearning.AI · 2024", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/DeepAI", "https://www.coursera.org/account/accomplishments/verify/P3MNNDS44DLL"),
        ("03", "Power BI Data Visualization", "EdX · 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/edx", "https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79"),
        ("04", "AWS Cloud Practitioner", "Amazon Web Services · 2019", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/AWS1", None),
        ("05", "SQL Certification", "Sololearn · 2017", "https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/SQLsololearn", "https://www.sololearn.com/en/certificates/CT-YUFRJBUH")
    ]
    for n, t, o, img, l in certs:
        lh = f'<a href="{l}" target="_blank" class="cil">Verify</a>' if l else '<span class="cina">—</span>'
        st.markdown(f'<div class="ci"><span class="cin">{n}</span><div class="cic"><p class="cit">{t}</p><p class="cio">{o}</p></div>{lh}</div>', unsafe_allow_html=True)
        st.image(img, width=280)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("""
    <div class="sd"><p class="sdt">Get in Touch</p><p class="sdn">LET'S<br>CONNECT</p></div>
    <div class="qs"><span class="qm">"</span><p class="qt">In God we trust; for all else, we turn to the validation of data.</p></div>
    <div class="cl">
        <div class="cg">
            <div class="cc"><p class="ccl">Phone</p><p class="ccv">(626) 203-3319</p></div>
            <div class="cc"><p class="ccl">Email</p><p class="ccv">jason.chang01022024@gmail.com</p></div>
            <div class="cc"><p class="ccl">LinkedIn</p><p class="ccv"><a href="https://linkedin.com/in/jchang0102" target="_blank">linkedin.com/in/jchang0102</a></p></div>
            <div class="cc"><p class="ccl">Location</p><p class="ccv">Rowland Heights, CA</p></div>
        </div>
        <div style="margin-top:30px;padding:35px;background:#f5f5f5;animation:fadeUp .5s ease .3s both">
            <p style="font-family:'DM Sans',sans-serif;font-size:8px;font-weight:700;color:#a3a3a3;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px">Education</p>
            <p style="font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#080808;margin-bottom:4px">B.S. Business Administration</p>
            <p style="font-family:'DM Sans',sans-serif;font-size:12px;color:#737373">University of California, Riverside</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
