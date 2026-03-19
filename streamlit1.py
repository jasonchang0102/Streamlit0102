"""
Jason C. Chang | Senior BI & Analytics Manager Portfolio
Built with native Streamlit components + minimal CSS
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# =============================================================================
# CONFIG
# =============================================================================
RESUME_URL = "https://github.com/jasonchang0102/Streamlit0102/raw/main/--Jason_Chang_Sr_BI_Analytics_Manager_Resume--03-19-26.pdf"
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"
DATA = BASE_DIR / "data"

CERTS = {
    "Supervised Machine Learning": {
        "issuer": "Stanford Online / DeepLearning.AI via Coursera",
        "date": "Jun 2024",
        "url": "https://coursera.org/verify/YHLXRW3TL569"
    },
    "Neural Networks & Deep Learning": {
        "issuer": "DeepLearning.AI via Coursera",
        "date": "Apr 2024",
        "url": "https://coursera.org/verify/P3MNNDS44DLL"
    },
    "Analyzing & Visualizing Data with Power BI": {
        "issuer": "edX",
        "date": "2019",
        "url": "https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79"
    },
    "Big Data on AWS": {
        "issuer": "AWS Training & Certification",
        "date": "2019",
        "url": ""
    },
    "Cloud Foundations": {
        "issuer": "AWS Training & Certification",
        "date": "2019",
        "url": ""
    }
}

# =============================================================================
# CSS - minimal, only what Streamlit can't do natively
# =============================================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Hide Streamlit chrome */
#MainMenu, footer, .stDeployButton, div[data-testid="stDecoration"], [data-testid="stToolbar"] {display:none!important}

/* Sidebar */
section[data-testid="stSidebar"] {background:#0a0a0a!important;min-width:280px!important;max-width:280px!important}
section[data-testid="stSidebar"] > div:first-child {padding:0!important;padding-bottom:100px!important;background:#0a0a0a!important}
[data-testid="stSidebarNav"] {display:none!important}
button[data-testid="stSidebarCollapseButton"] {display:none!important}
[data-testid="collapsedControl"] {display:flex!important;visibility:visible!important;opacity:1!important;z-index:999999!important;background:#0a0a0a!important;padding:12px!important}
[data-testid="collapsedControl"] svg {fill:white!important;color:white!important;stroke:white!important}
[data-testid="collapsedControl"] button {background:#0a0a0a!important;color:white!important}

/* Sidebar nav styling */
[data-testid="stSidebar"] .stRadio > div {flex-direction:column!important;gap:0!important;padding:20px 0!important}
[data-testid="stSidebar"] .stRadio label > div:first-child {display:none!important}
[data-testid="stSidebar"] .stRadio label {background:transparent!important;padding:14px 32px!important;margin:0!important;border-left:2px solid transparent!important}
[data-testid="stSidebar"] .stRadio label:hover {background:#1a1a1a!important}
[data-testid="stSidebar"] .stRadio label:has(input:checked) {background:#1a1a1a!important;border-left-color:#fff!important}
[data-testid="stSidebar"] .stRadio label p {font-family:'Bebas Neue',Impact,sans-serif!important;font-size:16px!important;color:#737373!important;letter-spacing:3px!important}
[data-testid="stSidebar"] .stRadio label:hover p {color:#d4d4d4!important}
[data-testid="stSidebar"] .stRadio label:has(input:checked) p {color:#fff!important}

/* Sidebar brand */
.sb-brand {padding:48px 32px 32px;border-bottom:1px solid #262626}
.sb-name {font-family:'Bebas Neue',sans-serif;font-size:22px;color:#fff;margin:0 0 4px;letter-spacing:3px}
.sb-title {font-family:'Inter',sans-serif;font-size:12px;color:#a3a3a3;margin:0 0 20px}
.sb-status {display:inline-flex;align-items:center;gap:8px;background:#262626;padding:6px 14px;font-family:'JetBrains Mono',monospace;font-size:11px;color:#4ade80;letter-spacing:1px}
.sb-status::before {content:'';width:6px;height:6px;background:#4ade80;border-radius:50%}
.sb-footer {position:fixed;bottom:0;left:0;width:280px;padding:20px 32px;border-top:1px solid #262626;background:#0a0a0a}
.sb-dl {display:block;background:#fff;color:#0a0a0a;font-family:'Bebas Neue',sans-serif;font-size:13px;letter-spacing:2px;text-align:center;text-decoration:none;padding:10px}

/* Dark section blocks */
.dark-section {background:#0a0a0a;color:#fff;padding:48px;border-radius:0;margin:0 0 4px 0}
.dark-section h2 {font-family:'Bebas Neue',sans-serif;color:#fff!important;letter-spacing:2px;margin:0 0 8px}
.dark-section p {color:#a3a3a3}
.dark-section .meta {font-family:'JetBrains Mono',monospace;font-size:13px;color:#737373}

/* Accent section */
.accent-section {background:#f5f5f5;padding:32px;border-left:4px solid #0a0a0a;border-radius:0;margin:24px 0}

/* Gold accent */
.gold-border {border-left:3px solid #ca8a04;padding-left:16px;margin-bottom:24px}

/* Case result cards */
.result-card {background:#0a0a0a;padding:24px;text-align:center;border-radius:0;margin:0 2px}
.result-val {font-family:'Bebas Neue',sans-serif;font-size:36px;color:#ca8a04!important}
.result-label {font-family:'Inter',sans-serif;font-size:11px;color:#a3a3a3;text-transform:uppercase;letter-spacing:1px;margin-top:4px}

/* Belief cards */
.belief {font-family:'Inter',sans-serif;font-size:15px;color:#d4d4d4;line-height:1.8;margin-bottom:16px;padding-left:20px;border-left:2px solid #ca8a04}

/* Tags */
.tag {display:inline-block;font-family:'JetBrains Mono',monospace;font-size:12px;padding:6px 12px;margin:2px;border:1px solid #e5e5e5;background:#f5f5f5;color:#0a0a0a}
.tag-dark {border-color:#333;background:#262626;color:#a3a3a3}

/* Headings override */
h1 {font-family:'Bebas Neue',sans-serif!important;letter-spacing:2px!important;color:#0a0a0a!important}
h2 {font-family:'Bebas Neue',sans-serif!important;letter-spacing:2px!important;color:#0a0a0a!important}
h3 {font-family:'Bebas Neue',sans-serif!important;letter-spacing:1px!important;color:#0a0a0a!important}

/* Image frames */
[data-testid="stImage"] {border:1px solid #e5e5e5;border-radius:2px}

/* Tab styling - make tabs visible */
.stTabs [data-baseweb="tab-list"] {background:#f5f5f5;padding:4px;border-radius:4px;gap:4px}
.stTabs [data-baseweb="tab"] {background:#fff;border:1px solid #e5e5e5;border-radius:4px;padding:8px 20px;font-family:'Inter',sans-serif;font-size:14px;font-weight:500;color:#404040}
.stTabs [data-baseweb="tab"]:hover {background:#0a0a0a;color:#fff;border-color:#0a0a0a}
.stTabs [aria-selected="true"] {background:#0a0a0a!important;color:#fff!important;border-color:#0a0a0a!important}
.stTabs [data-baseweb="tab-highlight"] {background:#0a0a0a!important}
.stTabs [data-baseweb="tab-border"] {display:none}
</style>
"""

# =============================================================================
# DATA
# =============================================================================
@st.cache_data
def load_data():
    import os
    csv_path = DATA / "profitability_data.csv"
    if not csv_path.exists():
        st.error(f"Data file not found: {csv_path}")
        st.write("Current working directory:", os.getcwd())
        st.write("Files in root:", os.listdir("."))
        if os.path.exists("data"):
            st.write("Files in data/:", os.listdir("data"))
        else:
            st.write("data/ folder does NOT exist")
        return pd.DataFrame()
    return pd.read_csv(csv_path)

# =============================================================================
# HELPERS
# =============================================================================
def dark_section(content):
    st.markdown(f'<div class="dark-section">{content}</div>', unsafe_allow_html=True)

def result_cards(metrics):
    """metrics = list of (value, label) tuples"""
    cols = st.columns(len(metrics))
    for col, (val, label) in zip(cols, metrics):
        col.markdown(f'<div class="result-card"><div class="result-val">{val}</div><div class="result-label">{label}</div></div>', unsafe_allow_html=True)

def tags(items, dark=False):
    cls = "tag-dark" if dark else "tag"
    html = " ".join(f'<span class="{cls}">{t}</span>' for t in items)
    st.markdown(html, unsafe_allow_html=True)

def show_image(name, caption, width=0.75):
    """Show image with configurable width and fallback if missing"""
    path = ASSETS / name
    if path.exists():
        pad = (1 - width) / 2
        col1, col2, col3 = st.columns([pad, width, pad])
        with col2:
            st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.info(f"Dashboard screenshot: {caption}")

def section_header(title):
    st.markdown(f'<div class="gold-border"><h3>{title}</h3></div>', unsafe_allow_html=True)

# =============================================================================
# MAIN
# =============================================================================
def main():
    st.set_page_config(
        layout="wide",
        page_title="Jason C. Chang | Senior BI & Analytics Manager",
        page_icon="📊",
        initial_sidebar_state="expanded"
    )
    st.markdown(CSS, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown('<div class="sb-brand"><p class="sb-name">JASON C. CHANG</p><p class="sb-title">Senior BI & Analytics Manager</p><div class="sb-status">Open to Opportunities</div></div>', unsafe_allow_html=True)
        page = st.radio("Nav", ["Home", "Work", "About", "Live Demo", "Code & Method", "Connect"], label_visibility="collapsed")
        st.markdown(f'<div class="sb-footer"><a href="{RESUME_URL}" target="_blank" class="sb-dl">DOWNLOAD RESUME</a></div>', unsafe_allow_html=True)

    pages = {
        "Home": render_home,
        "Work": render_work,
        "About": render_about,
        "Live Demo": render_explorer,
        "Code & Method": render_code,
        "Connect": render_connect
    }
    pages[page]()

# =============================================================================
# HOME
# =============================================================================
def render_home():
    st.markdown("##### Senior BI & Analytics Manager — 8+ Years")
    st.markdown("# I WALK INTO DATA CHAOS AND BUILD SYSTEMS EXECUTIVES TRUST")
    st.markdown("Companies hire me when the data exists but nobody believes it. I fix the trust gap between raw data and executive decisions — through platform architecture, metric alignment, and reporting systems that 200+ stakeholders actually use.")
    st.write("")
    tags(["SQL", "Python", "Power BI", "Snowflake", "DAX", "BigQuery"])

    st.divider()

    # Proof bar
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Data Sources Unified", "99+")
    c2.metric("Fewer KPI Conflicts", "70%")
    c3.metric("Reporting Cycle", "5→1 day")
    c4.metric("Stakeholders Served", "250+")

    st.divider()

    # Social proof above the fold
    st.markdown('*"His out of the box thinking provided solutions that others simply would not conceive."* — **Brenton Harlow**, Direct Manager at Advantage Solutions')

    st.divider()

    # Flagship
    dark_section("""
        <p style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#a3a3a3;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px">FLAGSHIP — ADVANTAGE SOLUTIONS</p>
        <h2 style="font-size:36px;line-height:1.1;margin:0 0 12px">FIVE SALES SYSTEMS. FIVE REVENUE NUMBERS. ONE BOARD MEETING.</h2>
        <p class="meta">6 weeks &nbsp;|&nbsp; Post-merger unification &nbsp;|&nbsp; 250 users</p>
        <br>
        <p style="color:#d4d4d4;font-size:16px;line-height:1.8">Five regional sales systems, five definitions of revenue, and a CFO who couldn't trust any of them. I had 6 weeks before Q3 close to build a single source of truth — starting with getting five VPs to agree on what the numbers should mean. Full story under <strong style="color:#ca8a04">Work</strong>.</p>
    """)

    result_cards([
        ("$55M", "Royalty Processing Automated"),
        ("350→2 hrs", "Quarterly Analyst-Hours"),
        ("47→0", "Shadow Excel Trackers"),
        ("70%", "Fewer KPI Conflicts")
    ])

    st.write("")
    tags(["Snowflake", "Power BI", "DAX", "Python", "SQL"], dark=False)

    st.write("")
    st.write("")

    # Project cards
    st.markdown("## SELECTED PROJECTS")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### MODERN HOME STATION")
        st.markdown("### MARKETING WAS SPENDING BLIND")
        st.markdown("No attribution. Same promo to everyone. Data scattered across Facebook, Shopify, GA4. Built cross-channel attribution framework, A/B testing program, and 4-phase ad scaling system from scratch.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Conversion", "+33%")
        m2.metric("CPA", "-18%")
        m3.metric("YoY Revenue", "+85%")

    with col2:
        st.markdown("##### ADVANTAGE SOLUTIONS")
        st.markdown("### SALES PIPELINE — FROM LEADS TO REVENUE")
        st.markdown("Built end-to-end sales conversion analytics tracking 1,489 leads through opportunity, proposal, and close stages. Enabled real-time visibility into rep-level conversion rates across regions and programs.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Win Rate", "24.1%")
        m2.metric("Leads Tracked", "1,489")
        m3.metric("Wins", "360")

    # Dashboard previews — full width so details are readable
    img1, img2 = st.columns(2)
    with img1:
        show_image("mhs_engagement.png", "Answers: Which campaign segments are cost-efficient? Clusters separate high-engagement targets from spend traps by CPC and page interaction.")
    with img2:
        show_image("advantage_program.png", "Answers: Which reps need coaching? Full funnel tracking across 1,489 leads with real-time converter ranking.")

    st.write("")
    st.divider()

    # POV
    st.markdown('<div class="accent-section"><p style="font-family:\'Bebas Neue\',sans-serif;font-size:18px;letter-spacing:2px;margin-bottom:12px;color:#0a0a0a">WHAT I BELIEVE</p><p style="font-size:17px;line-height:1.8;font-style:italic;color:#404040">Most BI teams start with the dashboard. I start with the decision. If you cannot name the specific decision a report changes, you are decorating, not analyzing. The hardest part of my job is never the SQL — it is getting five VPs to agree on what revenue means.</p></div>', unsafe_allow_html=True)

    # Testimonial
    st.write("")
    st.markdown("> *\"Jason is a masterful practitioner of data tools and management. His out of the box thinking provided solutions that others simply would not conceive. His attitude equally matches his aptitude — a positive influence on those around him with the ability to shine in the toughest of situations.\"*")
    st.markdown("**Brenton Harlow** — Executive Leader, CPG Sales & Operations — Direct Manager at Advantage Solutions")


# =============================================================================
# WORK
# =============================================================================
def render_work():
    dark_section("""
        <h2 style="font-size:44px;letter-spacing:4px;margin:0 0 8px">CASE STUDIES</h2>
        <p>Deep dives into organizational data problems I have solved</p>
    """)

    # ─── CASE 01 ─────────────────────────────────────────────────────────
    st.write("")
    st.markdown("`CASE 01 — ADVANTAGE SOLUTIONS`")
    st.markdown("# FIVE REVENUE NUMBERS IN ONE BOARD MEETING")
    st.markdown("*Post-merger data unification — 6 weeks — Snowflake, Power BI, DAX, Python*")

    result_cards([("70%", "Fewer KPI Conflicts"), ("5→1 day", "Reporting Cycle"), ("9%", "Quarterly Revenue Growth")])

    st.write("")
    section_header("THE SITUATION")
    st.markdown("""
After the merger, I inherited 5 sales systems that did not talk to each other. Each region defined revenue differently. The CFO was getting 5 different numbers in every board meeting. Field teams had lost trust in central reporting and created 47 shadow Excel trackers.

- 5 sales systems with incompatible metric definitions
- 47 shadow Excel trackers maintained by field teams
- I inherited the project mid-cycle after the previous lead departed
- 6 weeks until Q3 close deadline
""")

    section_header("WHY THIS WAS HARD")
    st.markdown("This was not a technical problem — it was political. Each regional VP had built metrics to make their team look good. Standardizing meant someone's numbers would go down. Getting alignment required trust-building before any code was written.")

    section_header("MY APPROACH")
    st.markdown("""
**Week 1–2:** Interviewed 12 stakeholders. Asked each one: "What decision are you trying to make with this data?" Mapped every metric definition across all 5 systems.

**Week 3:** Facilitated an alignment session. Got 5 VPs to agree on 12 golden metrics with documented definitions. This was the hardest week.

**Week 4–5:** Built unified Snowflake schema. Wrote 40+ DAX measures. Designed Power BI dashboards with drill-through from executive summary to regional detail.

**Week 6:** Trained 250 users. Deprecated 47 legacy reports. Established a formal data governance process — any metric change required a written change request reviewed by the metric owner and one cross-functional stakeholder before deployment. This prevented the "quiet definition drift" that caused the original mess.

Separately, built a weekly office hours cadence with the 7 regional analytics managers — structured around a shared query library and a rotating "metric of the week" deep dive. Within 3 months, regional teams were self-serving 80% of ad hoc requests instead of routing everything through central BI.

**ETL Automation — Replacing 47 Shadow Trackers**

Replaced the 47 Excel macros that one analyst maintained for 99 vendor data sources with automated Python + SQL pipelines. Sat with the analyst for a full week reverse-engineering undocumented business logic — custom GL code mappings, vendor exception rules. Built dynamic column mapping in Python that handles vendor format changes without code updates. Significantly reduced error rates and eliminated 160 hours of manual processing per quarter.
""")

    section_header("WHAT WENT WRONG")
    st.markdown("APAC had an undocumented custom field that their entire commission structure depended on. Their numbers broke on Day 1 of launch. I deployed an emergency fix to the data model while the regional VP was on a call with the CEO. Lesson: always audit edge-case dependencies before deprecating legacy systems.")

    # Architecture diagram
    st.write("")
    section_header("PLATFORM ARCHITECTURE")
    st.markdown("""
<div style="max-width:600px;margin:0 auto;font-family:'Inter',sans-serif;font-size:14px;line-height:1.6">
<div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:12px">
<span style="background:#f5f5f5;border:1px solid #e5e5e5;padding:6px 14px;font-size:13px">99+ Vendor Sources</span>
<span style="background:#f5f5f5;border:1px solid #e5e5e5;padding:6px 14px;font-size:13px">POS Systems</span>
<span style="background:#f5f5f5;border:1px solid #e5e5e5;padding:6px 14px;font-size:13px">Field & Compliance Data</span>
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#0a0a0a;color:#fff;padding:16px 24px;text-align:center;margin:4px 0">
<div style="font-family:'Bebas Neue',sans-serif;font-size:16px;letter-spacing:2px;color:#ca8a04">PYTHON ETL PIPELINES</div>
<div style="font-size:12px;color:#a3a3a3;margin-top:4px">Dynamic column mapping · GL code logic · QA validation</div>
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#0a0a0a;color:#fff;padding:16px 24px;text-align:center;margin:4px 0">
<div style="font-family:'Bebas Neue',sans-serif;font-size:16px;letter-spacing:2px;color:#ca8a04">SNOWFLAKE WAREHOUSE</div>
<div style="font-size:12px;color:#a3a3a3;margin-top:4px">Unified schema · 12 golden metrics · Single source of truth</div>
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#0a0a0a;color:#fff;padding:16px 24px;text-align:center;margin:4px 0">
<div style="font-family:'Bebas Neue',sans-serif;font-size:16px;letter-spacing:2px;color:#ca8a04">SQL SEMANTIC LAYER</div>
<div style="font-size:12px;color:#a3a3a3;margin-top:4px">40+ DAX measures · Drill-through logic</div>
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#0a0a0a;color:#fff;padding:16px 24px;text-align:center;margin:4px 0">
<div style="font-family:'Bebas Neue',sans-serif;font-size:16px;letter-spacing:2px;color:#ca8a04">POWER BI DASHBOARDS</div>
<div style="font-size:12px;color:#a3a3a3;margin-top:4px">Executive → Regional → Individual views</div>
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="text-align:center;font-family:'Bebas Neue',sans-serif;font-size:18px;letter-spacing:2px;color:#0a0a0a;padding:8px 0">250+ STAKEHOLDERS</div>
</div>
""", unsafe_allow_html=True)
    st.caption("Platform still in production serving 250+ users. Data governance process I established continues to manage metric change requests.")

    # Images
    st.write("")
    st.markdown("##### DASHBOARD VIEWS")
    tab1, tab2, tab3 = st.tabs(["Is the business on track?", "Where are we making vs losing money?", "How is this rep performing?"])
    with tab1:
        show_image("advantage_executive.png", "Answers: Is the business on track this quarter? Enables CFO to compare all 83 customers against budget in one view — by region, by product, with GM% trend.")
    with tab2:
        show_image("advantage_margin.png", "Answers: Where are we making vs losing money? Maps revenue variance against gross margin by business unit and industry — surfaces which programs to scale vs restructure.")
    with tab3:
        show_image("advantage_sales.png", "Answers: How is this rep performing? Individual scorecard showing 16 customers, monthly revenue with budget variance — used in weekly 1:1s between managers and reps.", width=0.50)

    st.divider()

    # ─── CASE 02 ─────────────────────────────────────────────────────────
    st.write("")
    st.markdown("`CASE 02 — MODERN HOME STATION`")
    st.markdown("# SCALING REVENUE WITHOUT SCALING WASTE")
    st.markdown("*Cross-channel attribution, A/B testing & ad spend optimization — GA4, Shopify, Meta, Klaviyo*")

    result_cards([
        ("+33%", "Conversion Rate"),
        ("-18%", "CPA Reduction"),
        ("+85%", "YoY Revenue (FY20)")
    ])

    st.write("")
    section_header("THE SITUATION")
    st.markdown("""
The company was growing — $65K+/month in revenue, 780 units moving. But profitable scaling was the bottleneck. Ad spend was increasing linearly with revenue because there was no systematic framework connecting unit economics to campaign decisions. The marketing team had the tools — Meta Ads, Shopify, GA4, Klaviyo — but each operated in isolation. Budget allocation was reactive: scale what looked good yesterday, kill what didn't. No one had modeled the relationship between COGS ($32.09/unit), platform fees (4%), and the actual breakeven threshold per funnel stage.
""")

    section_header("WHY THIS WAS HARD")
    st.markdown("Three problems compounded each other. First, attribution — every platform claimed credit for the same conversion, so reported ROAS was inflated. Second, no unit economics baseline — without knowing that breakeven CPP was $47.48 and target CPP at 20% margin was $30.91, there was no objective basis for pause/scale decisions. Third, scaling required a framework, not just more budget.")

    section_header("MY APPROACH")
    st.markdown("**Foundation — Unit Economics Model**")
    st.markdown("Built the financial layer first. Mapped AOV, COGS, and platform fees to derive breakeven and target thresholds at every funnel stage:")

    econ_data = {
        "Metric": ["Cost per Purchase", "Cost per Initiate Checkout", "Cost per Add to Cart", "ROAS"],
        "Breakeven": ["$47.48", "$28.49", "$55.14", "1.75x"],
        "20% Margin": ["$30.91", "$18.54", "$35.89", "2.68x"],
        "10% Margin": ["$39.20", "$23.52", "$45.52", "2.11x"]
    }
    st.table(pd.DataFrame(econ_data).set_index("Metric"))

    st.markdown("""
**4-Phase Scaling Framework**

Designed a 4-phase system that took campaigns from discovery to scale with clear gates at each stage. Phase 1 tested 10 interest audiences at $5/adset with strict kill rules (CPC >$2, CTR <1% = pause). Phase 2 introduced lookalike audiences and creative retargeting at controlled budgets. Phase 3 scaled winners vertically (50–100% budget increases on 30–40% net profit adsets) while cutting underperformers. Phase 4 operated at $1K–3K campaign budgets with bid caps, gated by 400+ purchases and consistent 2x breakeven ROAS. Max daily spend capped at $508.

The framework's value was that every pause/scale decision was tied to the unit economics thresholds above — not gut feel, not platform-reported ROAS.

**Cross-Channel Attribution:** Built unified attribution across GA4, Shopify, Meta, Klaviyo. Applied K-Means clustering (4 clusters by CPC vs engagement) to identify high-value campaign segments. Led A/B testing across 12 creative combinations.

**Demand Forecasting:** Implemented demand forecasting dashboards that aligned marketing, warehouse, purchasing, and customer service data — so before any promotion launched, the team could see projected demand against inventory levels and CS staffing. Shortened cross-team feedback loops by 40%.
""")

    section_header("WHAT WENT WRONG")
    st.markdown("""
During Phase 2, three adsets showed 2x ROAS individually but were targeting overlapping audiences, cannibalizing each other. Combined spend was high but incremental conversions were flat. Had to build negative audience exclusions and restructure campaign hierarchy.

Separately: spike in video views with zero page views. Days debugging analytics — turned out mobile videos were autoplaying without sound, users scrolling past. Fixed creative direction, not the data pipeline.
""")

    st.write("")
    st.markdown("##### DASHBOARD VIEWS")
    tab1, tab2, tab3 = st.tabs(["K-Means Clustering", "Customer Journey", "Email Analytics"])
    with tab1:
        show_image("mhs_engagement.png", "Answers: Which campaigns are worth scaling? K-Means clustering separates high-CPC/high-engagement winners from spend traps — used to set Phase 2 budget allocation.")
    with tab2:
        show_image("mhs_customer_journey.png", "Answers: Where do leads drop off? Maps 86 contacts across 17 email journeys — identifies which touchpoints convert vs which get ignored.")
    with tab3:
        show_image("mhs_email_analysis.png", "Answers: What interactions precede a purchase? Ranks all CRM touchpoints by frequency — WebsiteVisited (162) and EmailOpened (86) were the most common pre-purchase interactions.")

    st.caption("Attribution framework and scaling playbook adopted as standard operating process. Unit economics model used for all subsequent campaign launches through FY21.")

    st.divider()

    # ─── CASE 03 ─────────────────────────────────────────────────────────
    st.write("")
    st.markdown("`CASE 03 — ADVANTAGE SOLUTIONS`")
    st.markdown("# FROM LEADS TO REVENUE — BUILDING PIPELINE VISIBILITY")
    st.markdown("*Sales conversion analytics — Power BI, SQL, ZoomCharts*")

    result_cards([
        ("24.1%", "Lead-to-Win Conversion"),
        ("1,489", "Leads Tracked"),
        ("34.09%", "Opportunity-to-Win Ratio")
    ])

    st.write("")
    section_header("THE SITUATION")
    st.markdown("Sales leadership had no real-time visibility into pipeline health. Conversion rates varied wildly by region and program (CSTORE BDR at 40% vs BB BDR at 18.9%) but nobody could see it until quarterly reviews. Individual rep performance was tracked manually in spreadsheets.")

    section_header("WHY THIS WAS HARD")
    st.markdown("Data lived across multiple CRM systems and field reporting tools. Defining consistent funnel stages (Lead → Opportunity → Proposal → Win) across programs required aligning sales ops, regional managers, and field marketing managers on shared definitions — the same political alignment challenge as the metric unification project.")

    section_header("MY APPROACH")
    st.markdown("""
Built end-to-end sales conversion dashboard tracking the full funnel: 1,489 Leads → 1,056 Opportunities → 738 Proposals → 360 Wins. Included period-over-period comparisons, threshold lines for target conversion rates, and drill-down to individual rep performance with sparkline trends. Enabled managers to identify top and bottom converters in real-time instead of quarterly.

Additionally built a program-level view breaking conversion by region (Midwest 26.6%, West 25.1%, South 19.3%) and by program type, with geographic mapping of field marketing manager performance across 92 BDRs managing 519 accounts at 20.9% overall conversion.
""")

    section_header("WHAT WENT WRONG")
    st.markdown("Initial rollout showed inflated win rates because one region was counting verbal commitments as 'wins' while others required signed contracts. Took two weeks to align on a universal definition of each funnel stage across all programs — same lesson as the metric unification project: agree on definitions before building dashboards.")

    st.write("")
    st.markdown("##### DASHBOARD VIEWS")
    st.markdown("*Two views of the same pipeline system at different scope levels — from full team overview to field program geographic breakdown.*")
    tab1, tab2 = st.tabs(["Full Team (1,489 Leads)", "Field Program (21K Engaged)"])
    with tab1:
        show_image("advantage_program.png", "Answers: Who should we coach and who should we promote? Shows 1,489 leads through the full funnel with top/bottom converter ranking — replaces quarterly guesswork with weekly action.")
    with tab2:
        show_image("conversion_dashboard.jpg", "Answers: Which regions and programs need intervention? Maps 92 BDRs across 519 accounts — Midwest at 26.6% vs South at 19.3% triggers resource reallocation decisions.")

    st.caption("Pipeline dashboard used by sales leadership for weekly pipeline reviews and quarterly business reviews through 2024.")


# =============================================================================
# ABOUT
# =============================================================================
def render_about():
    st.markdown("# I AM JASON CHANG.")
    st.markdown("""
I started in consumer electronics managing $500M product lines and realized every decision was being made on gut feel. Over 14 years across five companies, I have progressed from business analyst to BI leadership — with the last 8+ years focused on building enterprise data platforms, executive reporting systems, and the metric alignment processes that turn instinct into evidence.

Most BI teams build dashboards. I build clarity — the kind where a CEO can walk into a board meeting and actually trust the numbers on the screen.
""")

    st.divider()

    # Experience
    st.markdown("## EXPERIENCE")

    timeline = [
        ("2021 – Present", "LEAD DATA ANALYST", "Advantage Solutions",
         "Built national BI ecosystem from fragmented post-merger data. Unified 99+ vendor sources into Snowflake + Power BI platform serving 250+ stakeholders. Mentored 7 regional analytics managers."),
        ("2017 – 2021", "BI STRATEGY & ANALYTICS MANAGER", "Modern Home Station",
         "Created cross-channel attribution framework and 4-phase ad scaling system that drove +45% (FY19) and +85% (FY20) revenue growth. Led A/B testing program, +33% conversion."),
        ("2016 – 2017", "BI & STRATEGIC DEVELOPMENT MANAGER", "China Unicom America",
         "Architected pricing and demand forecast models delivering $2M+ revenue projections for enterprise sales targeting. Reduced planning cycles 50%."),
        ("2014 – 2016", "BI PROJECT ANALYST", "Marshall Electronics",
         "Managed 50+ international product launches across retail channels, $5M annual sales. Built launch tracking dashboards achieving 95% on-time rate."),
        ("2010 – 2014", "SENIOR BUSINESS ANALYST", "Cadence Acoustic Ltd. / Deccon International Ltd.",
         "Built first BI systems replacing Excel across $500M product portfolio. Managed pricing and inventory forecasting through company relocation and post-merger integration.")
    ]

    for dates, role, company, desc in timeline:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"`{dates}`")
        with col2:
            st.markdown(f"**{role}**")
            st.markdown(f"*{company}*")
            st.markdown(desc)
        st.write("")

    st.divider()

    # Education
    st.markdown("## EDUCATION")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("`2010`")
    with col2:
        st.markdown("**B.S. BUSINESS ADMINISTRATION**")
        st.markdown("*University of California, Riverside*")

    st.divider()

    # Skills
    st.markdown("## SKILLS")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### CORE STACK")
        st.markdown("SQL  \nPower BI / DAX  \nPython  \nSnowflake  \nExcel + VBA")
    with c2:
        st.markdown("### ALSO FLUENT")
        st.markdown("BigQuery  \nGA4  \nLooker  \nQlik Sense  \nPower Query  \nMeta Ads  \nShopify  \nHubSpot  \nKlaviyo")
    with c3:
        st.markdown("### METHODS")
        st.markdown("A/B Testing  \nAttribution Modeling  \nK-Means Clustering  \nCohort Analysis  \nForecasting  \nRegression  \nExperiment Design")

    st.divider()

    # Certifications
    st.markdown("## CERTIFICATIONS")
    cert_list = list(CERTS.items())
    row1 = cert_list[:3]
    row2 = cert_list[3:]
    cert_cols = st.columns(3)
    for col, (name, info) in zip(cert_cols, row1):
        with col:
            st.markdown(f"**{name}**")
            date_str = f" — {info['date']}" if info['date'] else ""
            st.markdown(f"*{info['issuer']}{date_str}*")
            if info['url']:
                st.markdown(f'<a href="{info["url"]}" target="_blank">Verify →</a>', unsafe_allow_html=True)
    if row2:
        cert_cols2 = st.columns(3)
        for i, (name, info) in enumerate(row2):
            with cert_cols2[i]:
                st.markdown(f"**{name}**")
                date_str = f" — {info['date']}" if info['date'] else ""
                st.markdown(f"*{info['issuer']}{date_str}*")

    st.divider()

    # Beliefs
    st.markdown('<div class="accent-section">', unsafe_allow_html=True)
    st.markdown("### WHAT I BELIEVE")
    st.markdown("*I have never seen a BI project fail because of bad SQL. Every one I have seen fail was because two VPs could not agree on what a metric meant.*")
    st.markdown("*Data governance is not a project. It is a culture you build one conversation at a time.*")
    st.markdown("*The best BI managers spend more time listening to stakeholders than writing queries.*")
    st.markdown("*If your reporting cycle is longer than your decision cycle, you are always too late.*")
    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Mentorship
    st.markdown("## HOW I MENTOR")
    st.markdown("""
When I joined Advantage Solutions, the 7 regional analytics managers could run reports but could not build them. I created a structured mentorship program:

**Technical development:** Hands-on training in Power BI development, DAX measure writing, and data governance standards — tied to real dashboards they would own.

**Ownership transfer:** Each manager built and presented their own regional dashboard to their VP within 30 days. This was not a training exercise — it became their production deliverable.

**Self-sufficiency:** Within 6 months, regional teams could independently identify performance gaps, build drill-down views, and troubleshoot data quality issues without escalating to me.

The result was not just skill transfer — it was a culture shift from "request a report" to "build the answer yourself."
""")

    st.divider()

    # Portfolio as project
    st.markdown("## ABOUT THIS PORTFOLIO")
    st.markdown("This site is itself a project — built with **Python, Streamlit, Plotly, and Pandas**, deployed on **Streamlit Cloud**, with anonymized real data from Advantage Solutions. The profitability explorer processes 1,047 rows of shipped sales data across 76 accounts and 9 divisions.")
    st.markdown('<a href="https://github.com/jasonchang0102/Streamlit0102" target="_blank">View source code on GitHub →</a>', unsafe_allow_html=True)


# =============================================================================
# EXPLORER
# =============================================================================
def render_explorer():
    st.markdown("# PROFITABILITY EXPLORER")
    st.markdown("Interactive analysis of **$392M in shipped sales** across **76 accounts** and **9 divisions**. Built from real program data at Advantage Solutions.")
    st.markdown("*This tool demonstrates the type of analysis I build for executive stakeholders — connecting revenue to margin to surface which segments are actually profitable vs just generating volume. Account and division names are anonymized for confidentiality.*")
    st.markdown('<a href="https://github.com/jasonchang0102/Streamlit0102" target="_blank">View source code on GitHub →</a>', unsafe_allow_html=True)

    st.markdown('<div class="accent-section"><p style="font-size:14px;line-height:1.7;color:#404040"><strong>Try this:</strong> In the Division filter below, click the X to clear all selections, then pick just one division. Notice how some divisions generate high revenue but negative margin — that insight changes resource allocation. Then sort the account table by Margin % to find which customers are profitable vs just generating volume.</p></div>', unsafe_allow_html=True)

    st.divider()

    df = load_data()

    # Filters
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        divisions = st.multiselect("Division", sorted(df["Division"].unique()), default=sorted(df["Division"].unique()))
    with col_f2:
        month_range = st.slider("Month Range", 1, 10, (1, 10))
        st.caption("Data covers Jan–Oct (shipped orders only)")
    with col_f3:
        top_n = st.selectbox("Show Top N Accounts", [10, 20, 50, "All"], index=1)

    # Filter
    filtered = df[
        (df["Division"].isin(divisions)) &
        (df["Month"] >= month_range[0]) &
        (df["Month"] <= month_range[1])
    ]

    # KPIs
    total_sales = filtered["Shipped_Sales"].sum()
    total_margin = filtered["Margin_Dollars"].sum()
    margin_pct = (total_margin / total_sales * 100) if total_sales > 0 else 0
    total_accounts = filtered["Account"].nunique()
    total_units = filtered["Units"].sum()

    st.write("")
    k1, k2, k3 = st.columns(3)
    k1.metric("Total Sales", f"${total_sales/1e6:.1f}M")
    k2.metric("Total Margin", f"${total_margin/1e6:.1f}M")
    k3.metric("Margin %", f"{margin_pct:.1f}%")
    k4, k5 = st.columns(2)
    k4.metric("Accounts", f"{total_accounts}")
    k5.metric("Units", f"{total_units/1e6:.1f}M")

    st.divider()

    # Monthly trend
    st.markdown("### MONTHLY TREND")
    monthly = filtered.groupby("Month").agg(
        Sales=("Shipped_Sales", "sum"),
        Margin=("Margin_Dollars", "sum")
    ).reset_index()
    monthly["Margin_Pct"] = monthly.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=monthly["Month"], y=monthly["Sales"], name="Shipped Sales", marker_color="#ca8a04", opacity=0.85))
    fig.add_trace(go.Scatter(x=monthly["Month"], y=monthly["Margin_Pct"], name="Margin %", yaxis="y2", mode="lines+markers", line=dict(color="#0a0a0a", width=2.5), marker=dict(size=7)))
    fig.update_layout(
        yaxis=dict(title="Shipped Sales ($)", tickformat="$,.0f"),
        yaxis2=dict(title="Margin %", overlaying="y", side="right", tickformat=".1f", range=[0, max(monthly["Margin_Pct"].max() * 1.2, 50) if len(monthly) > 0 and not pd.isna(monthly["Margin_Pct"].max()) else 50]),
        xaxis=dict(title="Month", dtick=1),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        height=400, margin=dict(l=60, r=60, t=40, b=40),
        plot_bgcolor="#fff", paper_bgcolor="#fff"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Division bubble chart
    st.markdown("### DIVISION PROFITABILITY MAP")
    st.markdown("*Bubble size = number of accounts. Position reveals the revenue vs margin tradeoff by division.*")

    div_agg = filtered.groupby("Division").agg(
        Sales=("Shipped_Sales", "sum"),
        Margin=("Margin_Dollars", "sum"),
        Accounts=("Account", "nunique")
    ).reset_index()
    div_agg["Margin_Pct"] = div_agg.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)

    fig2 = px.scatter(
        div_agg, x="Margin_Pct", y="Sales", size="Accounts",
        color="Division", text="Division",
        labels={"Margin_Pct": "Margin %", "Sales": "Revenue ($)"},
        height=450, size_max=60
    )
    fig2.update_traces(textposition="top center", textfont_size=10)
    fig2.update_layout(
        yaxis=dict(tickformat="$,.0f"),
        xaxis=dict(tickformat=".0f", title="Margin %"),
        showlegend=False,
        plot_bgcolor="#fff", paper_bgcolor="#fff",
        margin=dict(l=60, r=40, t=20, b=40)
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # Account profitability table
    st.markdown("### ACCOUNT PROFITABILITY")

    acct_agg = filtered.groupby(["Account", "Division"]).agg(
        Sales=("Shipped_Sales", "sum"),
        COGS=("Shipped_COGS", "sum"),
        Margin=("Margin_Dollars", "sum"),
        Units=("Units", "sum")
    ).reset_index()
    acct_agg["Margin_Pct"] = acct_agg.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)
    acct_agg = acct_agg[acct_agg["Sales"] > 0]  # Remove zero-sales accounts
    acct_agg = acct_agg.sort_values("Sales", ascending=False)

    if top_n != "All":
        acct_agg = acct_agg.head(int(top_n))

    # Format for display
    display_df = acct_agg.copy()
    display_df["Sales"] = display_df["Sales"].apply(lambda x: f"${x:,.0f}")
    display_df["COGS"] = display_df["COGS"].apply(lambda x: f"${x:,.0f}")
    display_df["Margin"] = display_df["Margin"].apply(lambda x: f"${x:,.0f}")
    display_df["Units"] = display_df["Units"].apply(lambda x: f"{x:,.0f}")
    display_df["Margin_Pct"] = display_df["Margin_Pct"].apply(lambda x: f"{x:.1f}%")
    display_df.columns = ["Account", "Division", "Sales", "COGS", "Margin $", "Units", "Margin %"]

    st.dataframe(display_df, hide_index=True, use_container_width=True, height=500)
    st.caption("Note: Negative margins reflect closeout pricing, returns, or below-cost promotional commitments — real operational data.")

    st.divider()

    # Dynamic insight
    st.markdown("### KEY INSIGHT")
    top_rev = acct_agg.sort_values("Sales", ascending=False).head(1)
    top_margin = acct_agg.sort_values("Margin_Pct", ascending=False).head(1)

    if len(top_rev) > 0 and len(top_margin) > 0:
        rev_name = top_rev.iloc[0]["Account"]
        rev_sales = top_rev.iloc[0]["Sales"]
        rev_mpct = top_rev.iloc[0]["Margin_Pct"]
        mar_name = top_margin.iloc[0]["Account"]
        mar_mpct = top_margin.iloc[0]["Margin_Pct"]
        mar_sales = top_margin.iloc[0]["Sales"]

        if rev_name == mar_name:
            # Same account is both top revenue and top margin — show runner-up comparison
            second_rev = acct_agg.sort_values("Sales", ascending=False).iloc[1] if len(acct_agg) > 1 else None
            if second_rev is not None:
                st.markdown(f'<div class="accent-section"><p style="font-size:16px;line-height:1.8;color:#404040"><strong>{rev_name}</strong> leads in both revenue (${rev_sales:,.0f}) and margin ({rev_mpct:.1f}%) — a rare combination. The next largest account, <strong>{second_rev["Account"]}</strong>, generates ${second_rev["Sales"]:,.0f} at {second_rev["Margin_Pct"]:.1f}% margin. In practice, this is the analysis that triggers a portfolio review — where leadership decides whether to double down on high-margin accounts or invest in turning volume accounts profitable.</p></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="accent-section"><p style="font-size:16px;line-height:1.8;color:#404040"><strong>{rev_name}</strong> leads in both revenue (${rev_sales:,.0f}) and margin ({rev_mpct:.1f}%).</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="accent-section"><p style="font-size:16px;line-height:1.8;color:#404040"><strong>{rev_name}</strong> leads in revenue (${rev_sales:,.0f}) at {rev_mpct:.1f}% margin, while <strong>{mar_name}</strong> achieves the highest margin at {mar_mpct:.1f}% on ${mar_sales:,.0f} in sales. This is the analysis that triggers a portfolio review — high volume does not equal high value, and the resource allocation decision depends on which metric leadership prioritizes.</p></div>', unsafe_allow_html=True)


# =============================================================================
# CODE & METHODOLOGY
# =============================================================================
def render_code():
    st.markdown("# CODE & METHODOLOGY")
    st.markdown("Real code from production systems I built. Not classroom exercises — these solved business problems at scale.")

    st.divider()

    # Python ETL
    section_header("PYTHON ETL — DYNAMIC COLUMN MAPPING")
    st.markdown("**Problem:** 6 vendor source systems (SQL, Amazon, AW Wholesale, AW Retail, A&F, NTD) each send data with completely different column structures. Manual reconciliation took 2 analysts 3+ weeks per quarter.")
    st.markdown("**Solution:** A column mapping dictionary that lets one function process ANY vendor format without code changes. When a vendor changes their schema, we update the mapping — not the pipeline.")
    st.code("""column_mappings = {
    'SQL':          [1, 7, 5, 9, 11, 12, 13, 14, 15, 16, 18, 25, 23, 26, 24, 27, 21],
    'AMAZON':       [1, 16, 17, 6, 5, 7, 8, 9, 10, 19, 18, 11, 12, 14, 13, 15, 2],
    'AW WHOLESALE': [27, 31, 1, 5, 7, 8, 12, 13, 28, 30, 29, 14, 21, 22, 23, 24, 20],
    'AW RETAIL':    [27, 31, 1, 5, 7, 8, 12, 13, 28, 30, 29, 14, 21, 22, 23, 24, 20],
    'A&F':          [2, 35, 17, 21, 19, 26, 27, 28, 29, 37, 31, 38, 39, 41, 40, 42, 24],
    'NTD':          [2, 6, 8, 21, 19, 26, 27, 28, 29, 37, 31, 38, 39, 41, 40, 42, 24]
}

def process_sheet(source_name, source_sheet, output_sheet, vendor_list):
    mapping = column_mappings[source_name]
    for row in source_sheet.iter_rows(min_row=2):
        vendor_num = row[mapping[-1] - 1].value
        if vendor_num in vendor_list:
            data = []
            for idx in mapping:
                cell = row[idx - 1]
                if cell.value is None:
                    data.append("")
                elif cell.is_date:
                    data.append(cell.value.strftime("%Y-%m-%d"))
                else:
                    data.append(cell.value)
            data.append(source_name)  # track origin
            output_sheet.append(data)""", language="python")
    st.markdown("*This pattern processed $55M in quarterly royalties across 99 vendor contracts. The same function handles all 6 source systems — adding a 7th vendor requires only a new mapping line, not new code.*")

    st.divider()

    # SQL
    section_header("SQL — DATABASE SCHEMA DISCOVERY")
    st.markdown("**Problem:** After a merger, we inherited databases with no documentation. Before building the unified data model, I needed to catalog every table, primary key, foreign key, and column description across all databases.")
    st.markdown("**Solution:** A single query that maps the entire SQL Server estate — used before any schema change to assess downstream impact.")
    st.code("""IF OBJECT_ID('tempdb..##AllTables') IS NULL
BEGIN
    CREATE TABLE ##AllTables (
        DatabaseName sysname,
        SchemaName sysname NULL,
        TableName sysname,
        PrimaryKeyColumn sysname NULL,
        ForeignKeyColumn sysname NULL,
        ColumnName sysname NULL,
        ColumnDescription NVARCHAR(MAX) NULL
    );
END

EXEC sp_MSforeachdb '
    USE [?];
    INSERT INTO ##AllTables
    SELECT DB_NAME(), SCHEMA_NAME(), t.name,
        (SELECT TOP 1 c.name FROM sys.indexes i
         JOIN sys.index_columns ic ON i.object_id = ic.object_id
         JOIN sys.columns c ON c.object_id = t.object_id
            AND c.column_id = ic.column_id
         WHERE i.is_primary_key = 1 AND i.object_id = t.object_id),
        (SELECT TOP 1 c.name FROM sys.foreign_key_columns fkc
         JOIN sys.columns c ON c.object_id = t.object_id
            AND c.column_id = fkc.parent_column_id),
        C.name,
        CONVERT(NVARCHAR(MAX), ep.value)
    FROM sys.tables t
    JOIN sys.columns C ON C.object_id = T.object_id
    LEFT JOIN sys.extended_properties ep
        ON ep.major_id = C.object_id AND ep.minor_id = C.column_id;
'
SELECT * FROM ##AllTables;""", language="sql")
    st.markdown("*This query was run before every schema migration. It mapped the full database estate so we could trace which downstream dashboards would break before making changes — not after.*")

    st.divider()

    # Python in Power BI
    section_header("PYTHON IN POWER BI — HEATMAP VISUAL")
    st.markdown("**Problem:** Standard Power BI visuals cannot show two metrics (shipped sales AND gross margin %) in the same cell of a matrix. Executives needed to see both at a glance — which accounts generate volume vs which actually make money.")
    st.markdown("**Solution:** Python visuals embedded directly in Power BI, using seaborn heatmaps with dual annotations.")
    st.code("""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def format_sales(value):
    if pd.isna(value) or value == 0: return ""
    elif value < 1e6: return f"${value/1e3:.1f}K"
    elif value < 1e9: return f"${value/1e6:.1f}M"
    else: return f"${value/1e9:.1f}B"

# Pivot: rows = accounts, cols = divisions
sales_pivot = dataset.pivot_table(
    index="ACCOUNT2", columns="DIVISION",
    values="SHIPPED SALES", aggfunc='sum')
igm_pivot = dataset.pivot_table(
    index="ACCOUNT2", columns="DIVISION",
    values="IGM%", aggfunc='mean')

# Combine: "$12.5M : 42.3%" in each cell
combined = sales_pivot.applymap(format_sales) + " : " + \\
    (igm_pivot * 100).round(1).astype(str) + "%"

plt.figure(figsize=(20, 8))
sns.heatmap(sales_pivot, mask=sales_pivot.isna(),
    annot=combined, fmt="", cmap="Reds",
    linewidths=.5, annot_kws={"size": 10})
plt.title('Shipped Sales and IGM% by Account and Division')
plt.tight_layout()
plt.show()""", language="python")
    st.markdown("*This visual runs inside Power BI as a Python visual. 7 dashboard pages at Advantage Solutions use this pattern — each combining two metrics that standard Power BI matrices cannot display simultaneously.*")

    st.divider()

    # Data Governance Framework
    section_header("DATA GOVERNANCE — 7-LAYER FRAMEWORK")
    st.markdown("My approach to every analytics project follows a 7-layer methodology. This is not theoretical — it was developed across 5 companies and is currently in production at Advantage Solutions.")
    st.write("")

    layers = [
        ("Layer 1", "Business Requirements & Stakeholder Alignment",
         "RACI matrix, KPI definitions, metric change request process, governance committee structure. Every project starts here — not with a dashboard, but with the question: what decision will this enable?"),
        ("Layer 2", "Data Cleaning & Quality Assurance",
         "Null detection, deduplication, schema validation, row count monitoring against 12-week baselines. Hard-fail gates prevent bad data from reaching dashboards."),
        ("Layer 3", "Exploratory Data Analysis & Distribution",
         "Bivariate and multivariate analysis to understand relationships before building models. Correlation does not imply causation — but it tells you where to look."),
        ("Layer 4", "Hypothesis Testing / A/B Design / Forecasting",
         "Experiment design with statistical significance thresholds. Multivariate testing when single-variable A/B is insufficient. Demand forecasting with seasonal adjustment."),
        ("Layer 5", "Visualization & Standardized Reporting",
         "Star schema data models, DAX measure libraries, row-level security, performance optimization (sub-3-second load targets). Every dashboard answers a named decision."),
        ("Layer 6", "Data-Driven Culture & Change Management",
         "Training, onboarding guides, self-service enablement. The goal is not adoption — it is self-sufficiency. If the team cannot operate without me, I have not finished."),
        ("Layer 7", "Delivery, QA & Long-Term Strategy",
         "Upstream and downstream monitoring, KPI variance alerts (±10% from trend), cross-source parity checks, refresh failure alerting. The system must stay trustworthy after I build it.")
    ]

    for num, title, desc in layers:
        st.markdown(f"**{num}: {title}**")
        st.markdown(f"*{desc}*")
        st.write("")

    st.markdown("*Full framework documentation (42,000 words, 151 items with business impact statements) available on request.*")

    st.divider()

    # Downloadable artifacts
    section_header("DOWNLOADABLE ARTIFACTS")
    st.markdown("These are documents I created for my team at Advantage Solutions:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Regional Analytics Onboarding Guide**")
        st.markdown("6-page guide covering platform access, 12 golden metrics, reporting standards, data quality checks, escalation matrix, and 30-day onboarding plan for new regional analytics managers.")
    with col2:
        st.markdown("**Analytics Standards & Development Guide**")
        st.markdown("Companion document with SQL templates, DAX patterns, Python-in-Power-BI standards, ETL error handling procedures, and naming conventions.")

    st.markdown("*Contact me for copies — these documents contain proprietary references that have been generalized for portfolio purposes.*")


# =============================================================================
# CONNECT
# =============================================================================
def render_connect():
    dark_section("""
        <h2 style="font-size:44px;letter-spacing:4px;margin:0 0 12px">LET'S TALK</h2>
        <p style="font-size:16px">Open to Senior BI & Analytics Manager opportunities across all industries.</p>
    """)

    st.markdown("I'm looking for organizations where the data infrastructure is broken or outgrown — where leadership needs someone to come in, align the metrics, build the platform, and make the numbers trustworthy. If that sounds like your team, I'd like to hear about it.")

    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("💼 **LINKEDIN**")
        st.markdown('<a href="https://linkedin.com/in/jchang0102" target="_blank">linkedin.com/in/jchang0102</a>', unsafe_allow_html=True)
    with c2:
        st.markdown("📧 **EMAIL**")
        st.markdown("jason.chang01022024@gmail.com")
    with c3:
        st.markdown("📱 **PHONE**")
        st.markdown("(626) 203-3319")
    with c4:
        st.markdown("📍 **LOCATION**")
        st.markdown("Hacienda Heights, CA")

    st.write("")
    st.markdown(f"[**DOWNLOAD RESUME →**]({RESUME_URL})")

    st.divider()

    st.markdown("## WHAT MY MANAGER SAID")
    st.markdown("> *\"Jason is a masterful practitioner of data tools and management. He is someone our team relied on for all key performance metrics in a very demanding and often changing environment. His attitude equally matches his aptitude. Jason is a positive influence on those around him and has the ability to shine in the darkest of and toughest of situations. His ideas and creativity were an asset to me personally as well as our team and client. His out of the box thinking provided solutions that others simply would not conceive. I am very glad I was fortunate enough to work with Jason and hope to do so again.\"*")
    st.markdown("**Brenton Harlow** — Executive Leader, CPG Sales, Marketing, Operations & Technology — Direct Manager at Advantage Solutions")


main()
