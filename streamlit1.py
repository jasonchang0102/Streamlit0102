import streamlit as st

st.set_page_config(layout="wide", page_title="Jason Chang | BI Manager", page_icon="◆")

# === GLOBAL STYLES ===
st.markdown("""
<link href='https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400;500&display=swap' rel='stylesheet'>
<style>
    :root{
        --b:#0a0a0a;--w:#ffffff;
        --g1:#fafafa;--g2:#f5f5f5;--g3:#e5e5e5;--g4:#d4d4d4;--g5:#a3a3a3;--g6:#737373;--g7:#525252;--g8:#262626;
        --accent:#3b82f6;--accent2:#8b5cf6;--gradient:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);
    }
    
    .stApp{background:var(--w)!important}
    #MainMenu,footer,header{visibility:hidden}
    .block-container{padding:2rem 3rem!important;max-width:1200px!important}
    
    /* Sidebar */
    section[data-testid="stSidebar"]{background:var(--b)!important;min-width:260px!important}
    section[data-testid="stSidebar"]>div:first-child{padding:0!important}
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"]{display:none!important}
    
    div.stRadio>div{flex-direction:column!important;gap:0!important}
    div[role="radiogroup"]>label[data-baseweb="radio"]>div:first-child{display:none!important}
    
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]{
        background:transparent!important;padding:16px 32px!important;margin:0!important;
        cursor:pointer!important;border-left:3px solid transparent!important;transition:all 0.2s ease!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]:hover{
        background:rgba(255,255,255,0.03)!important;border-left-color:rgba(255,255,255,0.2)!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"][data-checked="true"]{
        background:rgba(255,255,255,0.05)!important;border-left-color:var(--accent)!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"] p{
        font-family:'Inter',sans-serif!important;font-size:14px!important;font-weight:400!important;
        color:rgba(255,255,255,0.5)!important;margin:0!important;transition:all 0.2s ease!important
    }
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"]:hover p{color:rgba(255,255,255,0.8)!important}
    section[data-testid="stSidebar"] div[role="radiogroup"]>label[data-baseweb="radio"][data-checked="true"] p{color:#fff!important;font-weight:500!important}
    
    .sb-brand{padding:48px 32px 40px;border-bottom:1px solid rgba(255,255,255,0.06)}
    .sb-name{font-family:'Outfit',sans-serif;font-size:18px;font-weight:600;color:#fff;letter-spacing:1px;margin:0 0 6px}
    .sb-title{font-family:'Inter',sans-serif;font-size:12px;color:rgba(255,255,255,0.4);margin:0}
    .sb-status{display:inline-flex;align-items:center;gap:8px;margin-top:16px;padding:6px 12px;background:rgba(34,197,94,0.1);border-radius:20px;font-family:'Inter',sans-serif;font-size:11px;color:#22c55e}
    .sb-status::before{content:'';width:6px;height:6px;background:#22c55e;border-radius:50%}
    
    /* Typography */
    .hero-eyebrow{font-family:'Inter',sans-serif;font-size:12px;font-weight:500;color:var(--accent);letter-spacing:2px;text-transform:uppercase;margin-bottom:16px}
    .hero-title{font-family:'Outfit',sans-serif;font-size:52px;font-weight:700;color:var(--b);line-height:1.1;margin-bottom:20px}
    .hero-title span{background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
    .hero-sub{font-family:'Inter',sans-serif;font-size:18px;color:var(--g6);line-height:1.7;margin-bottom:32px}
    
    .section-label{font-family:'Inter',sans-serif;font-size:12px;font-weight:500;color:var(--accent);letter-spacing:2px;text-transform:uppercase;margin-bottom:8px}
    .section-title{font-family:'Outfit',sans-serif;font-size:36px;font-weight:600;color:var(--b);margin-bottom:8px}
    .section-sub{font-family:'Inter',sans-serif;font-size:16px;color:var(--g6)}
    
    /* Cards */
    .stat-card{background:var(--b);border-radius:16px;padding:32px;text-align:center}
    .stat-value{font-family:'Outfit',sans-serif;font-size:42px;font-weight:700;color:#fff}
    .stat-label{font-family:'Inter',sans-serif;font-size:13px;color:rgba(255,255,255,0.5);margin-top:8px}
    
    .work-card{background:#fff;border:1px solid var(--g3);border-radius:16px;padding:32px;transition:all 0.3s ease;height:100%}
    .work-card:hover{border-color:var(--accent);box-shadow:0 20px 40px rgba(0,0,0,0.08);transform:translateY(-4px)}
    .work-card-company{font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:var(--accent);letter-spacing:1px;text-transform:uppercase;margin-bottom:12px}
    .work-card-title{font-family:'Outfit',sans-serif;font-size:20px;font-weight:600;color:var(--b);line-height:1.3;margin-bottom:12px}
    .work-card-desc{font-family:'Inter',sans-serif;font-size:14px;color:var(--g6);line-height:1.6;margin-bottom:20px}
    .work-card-metrics{display:flex;gap:20px;padding-top:16px;border-top:1px solid var(--g3)}
    .work-metric{text-align:left}
    .work-metric-value{font-family:'Outfit',sans-serif;font-size:20px;font-weight:700;color:var(--b)}
    .work-metric-label{font-family:'Inter',sans-serif;font-size:11px;color:var(--g6)}
    .work-card-tags{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}
    .work-tag{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--g6);background:var(--g1);padding:4px 10px;border-radius:4px}
    
    .result-box{background:var(--b);border-radius:16px;padding:40px;margin:24px 0}
    .result-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;text-align:center}
    .result-value{font-family:'Outfit',sans-serif;font-size:36px;font-weight:700;color:#fff}
    .result-label{font-family:'Inter',sans-serif;font-size:12px;color:rgba(255,255,255,0.5);margin-top:4px}
    
    .quote-card{background:linear-gradient(135deg,rgba(59,130,246,0.05) 0%,rgba(139,92,246,0.05) 100%);border-left:4px solid var(--accent);border-radius:0 12px 12px 0;padding:24px 32px;margin:24px 0}
    .quote-text{font-family:'Playfair Display',serif;font-size:18px;font-style:italic;color:var(--accent);line-height:1.6;margin:0}
    .quote-author{font-family:'Inter',sans-serif;font-size:13px;color:var(--g6);margin-top:12px}
    
    /* Timeline */
    .timeline-item{padding:24px 0;border-bottom:1px solid var(--g3)}
    .timeline-item:last-child{border-bottom:none}
    .timeline-year{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--accent);margin-bottom:8px}
    .timeline-role{font-family:'Outfit',sans-serif;font-size:18px;font-weight:600;color:var(--b)}
    .timeline-company{font-family:'Inter',sans-serif;font-size:14px;color:var(--g6);margin-top:4px}
    .timeline-desc{font-family:'Inter',sans-serif;font-size:14px;color:var(--g6);margin-top:12px;line-height:1.6}
    
    /* Skills */
    .skill-box{background:var(--g1);border-radius:12px;padding:24px}
    .skill-title{font-family:'Inter',sans-serif;font-size:12px;font-weight:600;color:var(--accent);letter-spacing:1px;text-transform:uppercase;margin-bottom:12px}
    .skill-list{font-family:'Inter',sans-serif;font-size:14px;color:var(--b);line-height:1.8}
    
    /* Connect */
    .connect-card{background:var(--g1);border-radius:12px;padding:24px;text-align:center;height:100%}
    .connect-icon{font-size:24px;margin-bottom:12px}
    .connect-label{font-family:'Inter',sans-serif;font-size:11px;color:var(--g6);text-transform:uppercase;letter-spacing:1px;margin-bottom:4px}
    .connect-value{font-family:'Inter',sans-serif;font-size:14px;color:var(--b)}
    .connect-value a{color:var(--accent);text-decoration:none}
    .connect-value a:hover{text-decoration:underline}
    
    .testimonial-card{background:var(--g1);border-radius:16px;padding:32px;margin-bottom:16px}
    .testimonial-quote{font-family:'Inter',sans-serif;font-size:15px;color:var(--g7);line-height:1.7;font-style:italic;margin-bottom:16px}
    .testimonial-author{font-family:'Inter',sans-serif;font-size:14px;color:var(--b);font-weight:600}
    .testimonial-role{font-family:'Inter',sans-serif;font-size:13px;color:var(--g6)}
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"]{gap:8px;background:var(--g1);padding:8px;border-radius:12px}
    .stTabs [data-baseweb="tab"]{font-family:'Inter',sans-serif;font-size:14px;font-weight:500;padding:12px 24px;border-radius:8px}
    .stTabs [data-baseweb="tab-highlight"]{background:var(--accent)!important}
    .stTabs [aria-selected="true"]{color:var(--accent)!important}
    
    /* Expander styling */
    .streamlit-expanderHeader{font-family:'Outfit',sans-serif!important;font-size:16px!important;font-weight:600!important}
    
    /* Metric styling */
    [data-testid="stMetricValue"]{font-family:'Outfit',sans-serif!important;font-size:32px!important;font-weight:700!important}
    [data-testid="stMetricLabel"]{font-family:'Inter',sans-serif!important;font-size:12px!important;color:var(--g6)!important}
    
    /* Button */
    .stButton>button{font-family:'Inter',sans-serif!important;font-weight:500!important;border-radius:8px!important;padding:12px 24px!important}
    
    /* Hide default streamlit elements */
    .stDeployButton{display:none}
    div[data-testid="stDecoration"]{display:none}
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
    
    page = st.radio("Navigation", ["Home", "Work", "About", "Connect"], label_visibility="collapsed")

# === HOME PAGE ===
if page == "Home":
    # Hero
    st.markdown('<p class="hero-eyebrow">◆ BI Manager · 10+ Years Experience</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">I turn messy data into <span>executive decisions</span></h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">From Blizzard to Fortune 500 — I help companies find the revenue hiding in their data. I don\'t just build dashboards. I build clarity.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.button("📂 View My Work", type="primary", use_container_width=True)
    with col2:
        st.button("📄 Download Resume", use_container_width=True)
    
    st.divider()
    
    # Stats
    st.markdown('<p class="section-label">Impact Snapshot</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-card"><div class="stat-value">10+</div><div class="stat-label">Years in BI</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><div class="stat-value">$15M+</div><div class="stat-label">Revenue Impact</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><div class="stat-value">250+</div><div class="stat-label">Users Enabled</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-card"><div class="stat-value">70%</div><div class="stat-label">Faster Decisions</div></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Featured Work
    st.markdown('<p class="section-label">Featured Work</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Case Studies</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
        <div class="work-card">
            <div class="work-card-company">★ Flagship · Advantage Solutions</div>
            <h3 class="work-card-title">Unified 5 Data Sources Into Single Source of Truth</h3>
            <p class="work-card-desc">Post-merger chaos: 5 sales domains, 5 definitions of "revenue." CFO getting conflicting numbers. Had 6 weeks to fix it.</p>
            <div class="work-card-metrics">
                <div class="work-metric"><div class="work-metric-value">9%</div><div class="work-metric-label">Revenue Lift</div></div>
                <div class="work-metric"><div class="work-metric-value">70%</div><div class="work-metric-label">Fewer Conflicts</div></div>
                <div class="work-metric"><div class="work-metric-value">6 wks</div><div class="work-metric-label">Timeline</div></div>
            </div>
            <div class="work-card-tags"><span class="work-tag">Snowflake</span><span class="work-tag">Power BI</span><span class="work-tag">Python</span></div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="work-card">
            <div class="work-card-company">Modern Home Station</div>
            <h3 class="work-card-title">+33% Conversion via A/B Testing & Attribution</h3>
            <p class="work-card-desc">Built cross-channel attribution framework and led A/B testing program. Optimized marketing spend across GA4, Meta, Shopify.</p>
            <div class="work-card-metrics">
                <div class="work-metric"><div class="work-metric-value">+33%</div><div class="work-metric-label">Conversion</div></div>
                <div class="work-metric"><div class="work-metric-value">-18%</div><div class="work-metric-label">CPA</div></div>
                <div class="work-metric"><div class="work-metric-value">2x</div><div class="work-metric-label">ROAS</div></div>
            </div>
            <div class="work-card-tags"><span class="work-tag">GA4</span><span class="work-tag">Python</span><span class="work-tag">K-Means</span></div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Testimonial
    st.markdown('''
    <div class="quote-card">
        <p class="quote-text">"Jason doesn't just build dashboards — he asks the questions that change how we think about the business. For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
        <p class="quote-author">— VP of Sales, [Company]</p>
    </div>
    ''', unsafe_allow_html=True)

# === WORK PAGE ===
elif page == "Work":
    st.markdown('<p class="section-label">Selected Work</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Case Studies</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Click each tab to explore the full story behind each project.</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Use Streamlit tabs for interactivity
    tab1, tab2, tab3 = st.tabs(["🏢 Executive BI", "📊 A/B Testing", "⚙️ Automation"])
    
    with tab1:
        st.markdown("### Unified Executive Intelligence")
        st.markdown("*Advantage Solutions · 6 weeks*")
        
        # Results box
        st.markdown('''
        <div class="result-box">
            <div class="result-grid">
                <div><div class="result-value">9%</div><div class="result-label">Quarterly Revenue Lift</div></div>
                <div><div class="result-value">70%</div><div class="result-label">Fewer KPI Conflicts</div></div>
                <div><div class="result-value">5→1 day</div><div class="result-label">Decision Cycle</div></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Metrics row
        c1, c2, c3 = st.columns(3)
        c1.metric("Timeline", "6 weeks")
        c2.metric("Annual Impact", "~$12M")
        c3.metric("Users Trained", "250+")
        
        st.markdown("---")
        
        # Expandable sections for detail
        with st.expander("📍 The Mess", expanded=True):
            st.markdown("""
            After the acquisition, I inherited a nightmare:
            - **5 sales domains**, each with their own "source of truth"
            - APAC counted returns in revenue. EMEA didn't. Nobody knew which was "right"
            - The CFO was getting **5 different revenue numbers** at every board meeting
            - Field teams had created **47 shadow Excel trackers** because they didn't trust official reports
            - The previous BI lead had quit mid-project
            
            The CEO gave me 6 weeks before Q3 close.
            """)
        
        with st.expander("🔥 Why This Was Hard"):
            st.markdown("""
            This wasn't a technical problem. **It was a political one.**
            
            Each regional VP had built their metrics to make their team look good. Standardizing meant someone's numbers would go down — and they knew it.
            
            I also had:
            - No dedicated engineering support (just me and one junior analyst)
            - A Snowflake instance already at 80% capacity
            - Legacy POS systems that hadn't been documented since 2019
            """)
        
        with st.expander("🎯 My Approach"):
            st.markdown("""
            **Week 1-2: Discovery**  
            I didn't touch any code. Spent two weeks in meetings asking one question: *"What decision are you trying to make with this data?"*
            
            What I found: 70% of their "must-have" metrics weren't being used.
            
            **Week 3: The Hard Conversation**  
            Presented CFO with two options and recommended forcing standardization now.
            
            **Week 4-5: Build**  
            - Consolidated POS, field, compliance, and promo data into unified Snowflake schema
            - Created 12 "golden metrics" with documented definitions
            - Built Power BI dashboard with row-level security per region
            
            **Week 6: Rollout**  
            - Trained 250 users in 3 sessions
            - Created self-service documentation
            - Killed access to old reports (this was controversial)
            """)
        
        with st.expander("⚠️ What Went Wrong"):
            st.markdown("""
            Two things I didn't anticipate:
            
            1. **The APAC surprise:** The APAC team had been using a custom field that wasn't in any documentation. Their numbers broke on Day 1. I had to patch it live while the regional VP was on a call with the CEO.
            
            2. **The holdout:** One senior director refused to use the new system and continued sending his own Excel reports. I had to escalate to the CFO to get organizational buy-in.
            
            *Lesson: Technical migrations are easy. Cultural migrations are hard.*
            """)
        
        st.markdown('''
        <div class="quote-card">
            <p class="quote-text">"For the first time in two years, I walked into a board meeting with confidence in our numbers."</p>
            <p class="quote-author">— CFO, [Company]</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### +33% Conversion Through A/B Testing & Attribution")
        st.markdown("*Modern Home Station · Cross-Channel Analytics*")
        
        st.markdown('''
        <div class="result-box">
            <div class="result-grid">
                <div><div class="result-value">+33%</div><div class="result-label">Conversion Rate</div></div>
                <div><div class="result-value">-18%</div><div class="result-label">CPA Reduction</div></div>
                <div><div class="result-value">2x</div><div class="result-label">ROAS Improvement</div></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.metric("FY19 Revenue Growth", "+45%")
        c2.metric("FY20 Revenue Growth", "+85%")
        
        st.markdown("---")
        
        with st.expander("📍 The Mess", expanded=True):
            st.markdown("""
            Marketing was sending the same promotion to every customer — the whale spending $500/month and the casual who visits twice a year.
            
            Data existed but was scattered across:
            - Facebook Ads (JSON)
            - Shopify (CSV)
            - Google Analytics (API)
            
            No unified view of the customer journey. Marketing burning budget. Leadership asking why.
            """)
        
        with st.expander("🎯 My Approach: 7-Layer Data Framework"):
            st.markdown("""
            Applied a systematic approach:
            
            1. **Business Requirements** — Define KPIs with stakeholders
            2. **Data Cleaning** — Validate integrity, handle missing values
            3. **Exploratory Analysis** — Distribution analysis, correlation
            4. **Customer Segmentation** — K-Means clustering on behavioral features
            5. **Validation** — Chi-square tests, sample ratio checks
            6. **Time Series** — Seasonality, trend analysis
            7. **Integration** — Unified pipeline into Snowflake + Power BI
            """)
        
        with st.expander("🧪 A/B Test Design"):
            st.markdown("""
            **Hypothesis:** Value-based messaging drives higher conversion than feature-based.
            
            **Test Setup:**
            - 12 test groups (combinations of meme format, CTA type, interaction prompt)
            - Equal budget allocation
            - Minimum 1,000 impressions per ad set
            - 14-day test period
            
            **Results:**
            - Value-based ads: **8% conversion** vs feature-based: **6%** (p=0.03)
            - Best combination: Meme #2 + Learn More CTA + Comment prompt
            - 36% lower CPM with engagement-driven strategies
            """)
        
        with st.expander("📈 Statistical Analysis"):
            st.markdown("""
            **P-Value Analysis:**  
            We obtained p-value of 0.03 — only 3% probability the difference occurred by chance.
            
            **Conversion Rate Uplift:**  
            2 percentage point increase = 33% relative improvement. For every 10,000 users, 200 more purchases.
            
            **Controls:**
            - Selection bias mitigated via random assignment + chi-square validation
            - 14-day period to minimize seasonality effects
            - Geolocation and time-of-day included in analysis
            """)
    
    with tab3:
        st.markdown("### 160 Hours Saved via Pipeline Automation")
        st.markdown("*99 Vendor Data Sources · Python + SQL*")
        
        st.markdown('''
        <div class="result-box">
            <div class="result-grid">
                <div><div class="result-value">160 hrs</div><div class="result-label">Saved Quarterly</div></div>
                <div><div class="result-value">15%→0%</div><div class="result-label">Error Rate</div></div>
                <div><div class="result-value">99</div><div class="result-label">Vendors Automated</div></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.metric("Timeline", "8 weeks")
        c2.metric("Annual Hours Saved", "640+")
        
        st.markdown("---")
        
        with st.expander("📍 The Mess", expanded=True):
            st.markdown("""
            "Automation" meant a shared folder of **47 Excel macros** that one person (who left) understood.
            
            Every Monday:
            - 3 analysts spent 4 hours manually downloading vendor reports
            - Reformatting them, uploading to database
            - If someone was sick, the weekly report didn't go out
            
            Error rate: **15%**. We'd caught wrong numbers in board decks twice in the past quarter.
            
            The VP of Finance had stopped trusting anything with "automated" in the name.
            """)
        
        with st.expander("🎯 My Approach"):
            st.markdown("""
            **Phase 1 - Audit (Week 1-2):**  
            Mapped every data source, format, frequency, and downstream dependency. Found 12 sources that were never actually used.
            
            **Phase 2 - Build (Week 3-6):**  
            - Built dynamic column mapping dictionary in Python
            - Created vendor normalization buckets aligned with GL codes
            - Each vendor got a config file, not custom code
            - Implemented validation rules that catch anomalies before they hit the database
            
            **Phase 3 - Parallel Run (Week 7):**  
            Ran old and new systems side-by-side. Flagged every discrepancy. Fixed edge cases.
            
            **Phase 4 - Cutover (Week 8):**  
            Killed the macros. Trained the team on monitoring.
            """)
        
        with st.expander("⚠️ What Went Wrong"):
            st.markdown("""
            1. **The PDF vendor:** One vendor only sent PDF reports with no consistent formatting. Spent 2 days building a custom parser.
            
            2. **Timezone bugs:** Three vendors reported in different timezones. Took a week to standardize.
            """)
        
        with st.expander("💡 What I'd Do Differently"):
            st.markdown("""
            - Push vendors to use APIs or standardized formats — some of the manual work was self-inflicted
            - Build monitoring dashboards earlier — we caught issues reactively for the first month
            """)

# === ABOUT PAGE ===
elif page == "About":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div style="width:200px;height:200px;background:linear-gradient(135deg,#e5e7eb 0%,#d1d5db 100%);border-radius:16px;display:flex;align-items:center;justify-content:center;font-family:Inter,sans-serif;font-size:13px;color:#6b7280;">
        Your Photo<br>(200×200px)
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("## Hi, I'm Jason.")
        st.markdown("""
        I've spent the last decade helping companies **stop guessing and start knowing**.
        
        Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers.
        
        I've done this at **Advantage Solutions** (250+ users, $6B+ sales impact), **Modern Home Station** (2x ROAS, 45-85% revenue growth), and earlier at China Unicom and Marshall Electronics.
        
        **What I've learned:** The hard part is never the SQL. It's getting humans to agree on what "revenue" means.
        """)
    
    st.divider()
    
    # Career Timeline
    st.markdown("### Career Timeline")
    
    timeline_data = [
        ("2021 — Present", "BI Manager", "Advantage Solutions", "Built national Power BI ecosystem with Snowflake. Unified 5 fragmented sales domains. Automated ingestion across 99+ vendors. Managed 7 regional managers."),
        ("2017 — 2021", "BI Strategy & Analytics Manager", "Modern Home Station", "Deployed cross-channel attribution (GA4, Shopify, Meta). Led A/B testing program. Revenue growth: 45% (FY19), 85% (FY20)."),
        ("2016 — 2017", "BI & Strategic Development Manager", "China Unicom America", "Built GTM pricing and demand forecast models. $2M+ revenue projections. Automated churn and usage reporting."),
        ("2014 — 2016", "BI Project Analyst", "Marshall Electronics", "50+ international product launches, $5M annual sales. 95% on-time launch rate."),
        ("2010 — 2014", "Senior Business Analyst", "Cadence Acoustic Ltd.", "Migrated forecasting from Excel to SQL dashboards. Managed BI systems tracking $500M in product lines."),
    ]
    
    for year, role, company, desc in timeline_data:
        st.markdown(f'''
        <div class="timeline-item">
            <div class="timeline-year">{year}</div>
            <div class="timeline-role">{role}</div>
            <div class="timeline-company">{company}</div>
            <div class="timeline-desc">{desc}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.divider()
    
    # Skills
    st.markdown("### Technical Skills")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('''
        <div class="skill-box">
            <div class="skill-title">Daily Drivers</div>
            <div class="skill-list">SQL (10+ years)<br>Power BI / DAX<br>Python<br>Snowflake<br>Excel (VBA)</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with c2:
        st.markdown('''
        <div class="skill-box">
            <div class="skill-title">Fluent</div>
            <div class="skill-list">BigQuery<br>GA4<br>Looker<br>Qlik<br>Power Query</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with c3:
        st.markdown('''
        <div class="skill-box">
            <div class="skill-title">Statistical & ML</div>
            <div class="skill-list">A/B Testing<br>Regression<br>K-Means Clustering<br>Cohort Analysis<br>Forecasting</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.divider()
    
    # Certifications
    st.markdown("### Certifications")
    c1, c2, c3 = st.columns(3)
    c1.markdown("🎓 **Supervised ML** — Stanford (2024)")
    c2.markdown("🧠 **Neural Networks** — DeepLearning.AI (2024)")
    c3.markdown("📊 **Power BI** — edX (2019)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("📄 Download Resume (PDF)", use_container_width=False)

# === CONNECT PAGE ===
elif page == "Connect":
    st.markdown('<p class="section-label">Get In Touch</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-title">Let\'s Talk</h1>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">I\'m currently open to Senior BI Manager and Analytics Lead roles.</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact cards
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown('''
        <div class="connect-card">
            <div class="connect-icon">📧</div>
            <div class="connect-label">Email</div>
            <div class="connect-value"><a href="mailto:jason.chang01022024@gmail.com">jason.chang01022024@gmail.com</a></div>
        </div>
        ''', unsafe_allow_html=True)
    
    with c2:
        st.markdown('''
        <div class="connect-card">
            <div class="connect-icon">💼</div>
            <div class="connect-label">LinkedIn</div>
            <div class="connect-value"><a href="https://linkedin.com/in/jchang0102" target="_blank">linkedin.com/in/jchang0102</a></div>
        </div>
        ''', unsafe_allow_html=True)
    
    with c3:
        st.markdown('''
        <div class="connect-card">
            <div class="connect-icon">📱</div>
            <div class="connect-label">Phone</div>
            <div class="connect-value">(626) 203-3319</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with c4:
        st.markdown('''
        <div class="connect-card">
            <div class="connect-icon">📍</div>
            <div class="connect-label">Location</div>
            <div class="connect-value">Hacienda Heights, CA</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.divider()
    
    # Testimonials
    st.markdown("### What Colleagues Say")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('''
        <div class="testimonial-card">
            <p class="testimonial-quote">"Jason has a rare ability to translate complex data into stories that executives actually act on. He doesn't just answer questions — he asks better ones."</p>
            <p class="testimonial-author">[Name]</p>
            <p class="testimonial-role">VP of Sales · [Company]</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="testimonial-card">
            <p class="testimonial-quote">"I've worked with a lot of BI people. Jason is the first one who understood that data without context is just noise."</p>
            <p class="testimonial-author">[Name]</p>
            <p class="testimonial-role">CFO · [Company]</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with c2:
        st.markdown('''
        <div class="testimonial-card">
            <p class="testimonial-quote">"Most analysts give you data. Jason gives you decisions. He saved our team 20+ hours a week and made our CEO actually look forward to reviewing dashboards."</p>
            <p class="testimonial-author">[Name]</p>
            <p class="testimonial-role">Director of Operations · [Company]</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="testimonial-card">
            <p class="testimonial-quote">"Jason doesn't just build dashboards — he changes how teams think about measurement. That's rare."</p>
            <p class="testimonial-author">[Name]</p>
            <p class="testimonial-role">Product Manager · [Company]</p>
        </div>
        ''', unsafe_allow_html=True)
