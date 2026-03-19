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
        st.markdown('<div class="sb-brand"><p class="sb-name">JASON C. CHANG</p><p class="sb-title">Senior BI & Analytics Manager</p><div class="sb-status">Available for Senior BI Roles</div></div>', unsafe_allow_html=True)
        page = st.radio("Nav", ["Home", "Work", "Live Demo", "Connect"], label_visibility="collapsed")
        st.markdown(f'<div class="sb-footer"><a href="{RESUME_URL}" target="_blank" class="sb-dl">DOWNLOAD RESUME</a></div>', unsafe_allow_html=True)

    pages = {
        "Home": render_home,
        "Work": render_work,
        "Live Demo": render_explorer,
        "Connect": render_connect
    }
    pages[page]()

# =============================================================================
# HOME
# =============================================================================
def render_home():
    st.markdown("##### Senior BI & Analytics Manager — 8+ Years")
    st.markdown("# YOUR DATA EXISTS. YOUR EXECUTIVES DON'T TRUST IT.")
    st.markdown("Companies hire me when five VPs show up to a board meeting with five different revenue numbers. I make it one number that everyone trusts.")

    # Result cards — FIRST thing after headline (Direction 2)
    st.write("")
    st.markdown("**What changed at my current company:**")
    result_cards([
        ("$55M", "Royalty Processing Automated"),
        ("350→2 hrs", "Quarterly Analyst-Hours"),
        ("47→0", "Shadow Excel Trackers"),
        ("70%", "Fewer KPI Conflicts")
    ])

    st.write("")
    tags(["SQL", "Python", "Power BI", "Snowflake", "DAX", "BigQuery"])

    st.divider()

    # Proof bar — includes MHS metric (Direction 14)
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Data Sources", "99+")
    c2.metric("KPI Conflicts", "-70%")
    c3.metric("Reporting Cycle", "5→1 day")
    c4.metric("Stakeholders", "250+")
    c5.metric("ROAS Improvement", "2x")

    st.divider()

    # Social proof — one line only
    st.markdown('*"His out of the box thinking provided solutions that others simply would not conceive."* — **Brenton Harlow**, Direct Manager at Advantage Solutions')

    st.divider()

    # Project cards — problem→result format (Direction 5)
    st.markdown("## SELECTED PROJECTS")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### MODERN HOME STATION")
        st.markdown("**Four platforms. Zero attribution. Spending blind.**")
        st.markdown("Built data infrastructure from zero for a DTC startup — unified Facebook, Shopify, GA4, Klaviyo into one framework. Multivariate testing, K-Means segmentation, carrier analysis.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Conversion", "+33%")
        m2.metric("CPA", "-18%")
        m3.metric("YoY Revenue", "+85%")

    with col2:
        st.markdown("##### ADVANTAGE SOLUTIONS")
        st.markdown("**Five systems. Five revenue numbers. Nobody trusted any of them.**")
        st.markdown("Post-merger unification across a $1.68B enterprise — Snowflake + Power BI ecosystem, data governance framework, royalty automation pipeline.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Sources", "99+")
        m2.metric("Users", "250+")
        m3.metric("Cycle", "5→1 day")

    # Direction 7: Industry hook
    st.write("")
    st.markdown('*Whether your problem is fragmented reporting, broken attribution, or manual processes eating analyst time — I have solved each one.*')


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

    result_cards([("70%", "Fewer KPI Conflicts"), ("5→1 day", "Reporting Cycle"), ("$3M", "Misallocated Spend Found")])

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
    st.markdown("APAC had an undocumented custom field that their entire commission structure depended on. Their numbers broke on Day 1 of launch. I deployed an emergency fix to the data model while the regional VP was on a call with the CEO. Lesson: always audit edge-case dependencies before deprecating legacy systems. After the fix, APAC became the highest-adoption group on the platform — because they saw firsthand that the team could respond in real-time.")

    section_header("BUSINESS IMPACT")
    st.markdown("Once the unified platform was live, same-week budget visibility revealed that $3M in trade spend had been allocated to campaigns with negative ROI across regions. Previously invisible because each region reported separately. Leadership reallocated within one reporting cycle, improving ROI by 12%.")

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
        show_image("advantage_sales.png", "Answers: How is this rep performing? Individual scorecard showing 16 customers, monthly revenue with budget variance — used in weekly 1:1s between managers and reps.", width=0.30)

    st.divider()

    st.markdown('*"His out of the box thinking provided solutions that others simply would not conceive."* — **Brenton Harlow**, Direct Manager')

    st.divider()

    # ─── CASE 02 ─────────────────────────────────────────────────────────
    st.write("")
    st.markdown("`CASE 02 — MODERN HOME STATION`")
    st.markdown("# FOUR PLATFORMS. ZERO ATTRIBUTION. SPENDING BLIND.")
    st.markdown("*Cross-channel analytics, multivariate testing, customer segmentation & operations optimization — GA4, Shopify, Meta, Klaviyo*")

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
    st.markdown("Before spending a dollar on ads, we needed to know exactly what 'profitable' meant at every stage of the funnel. Built the financial layer first:")

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

**Process change after this:** Implemented a pre-launch QA checklist for all ad creative — verifying audio, thumbnail, CTA rendering, and platform-specific format requirements before any budget was allocated.
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

    st.caption("Attribution framework and scaling playbook adopted as standard operating process. Unit economics model used for all subsequent campaign launches through FY21. Shipping delay analysis by country and carrier also led to carrier switch, reducing unmet delivery expectations by 75% and shipping costs by 18%.")

    st.divider()

    # ─── CASE 03 ─────────────────────────────────────────────────────────
    st.write("")
    st.markdown("`CASE 03 — ADVANTAGE SOLUTIONS`")
    st.markdown("# TWO ANALYSTS. THREE WEEKS. EVERY QUARTER. FOR $55M IN ROYALTIES.")
    st.markdown("*End-to-end automation — Python, VBA, Excel, automated email distribution*")

    result_cards([
        ("$55M", "Quarterly Royalties"),
        ("350→2 hrs", "Processing Time"),
        ("99", "Vendor Contracts")
    ])

    st.write("")
    section_header("THE SITUATION")
    st.markdown("Every quarter, two senior financial analysts spent three full weeks manually processing royalty calculations across 99 vendor contracts from 6 different source systems (SQL exports, Amazon, AW Wholesale, AW Retail, A&F, NTD). Each source had a completely different column structure. The analysts manually mapped columns, filtered by vendor lists, formatted statements, and emailed results to each vendor individually. Error rate was high. Any mistake meant incorrect payments to licensors like Disney, Columbia, and Warner Bros.")

    section_header("WHY THIS WAS HARD")
    st.markdown("This was not a simple automation — it was reverse-engineering undocumented business logic. I sat with the finance analyst for a full week mapping every column transformation, GL code mapping, and vendor exception rule. Each of the 6 source systems had different column positions for the same data fields (e.g., 'Net Sales' was column 12 in SQL but column 29 in AW Wholesale). The output had to match exact formatting requirements for each vendor's royalty statement template.")

    section_header("MY APPROACH")
    st.markdown("""
**Dynamic Column Mapping:** Built a Python dictionary that maps each source system's column positions to a standard output format. Adding a new source system requires one new line, not new code.

**Vendor Filtering:** 99 vendors organized into 4 contract groups. Python filters transactions by vendor ID, processes through the column mapping, and outputs clean data per group.

**VBA Statement Generation:** Embedded VBA macros auto-generate formatted royalty statements matching each vendor's contractual template — including headers, currency formatting, date formatting, and summary calculations.

**Automated Distribution:** Final statements emailed to each vendor contact automatically. Finance reviews a QA summary before release.

**Result:** 350+ analyst-hours per quarter reduced to 2 hours. Two senior FAs reassigned to strategic analysis. Error rate dropped to near-zero because the logic is coded, not manual.
""")

    section_header("WHAT WENT WRONG")
    st.markdown("First run produced incorrect royalty rates for one vendor group because their contract had a tiered rate structure (different % above/below a sales threshold) that the original analyst handled mentally but never documented. Built a rate lookup table with threshold logic to handle this and any future tiered contracts.")

    st.caption("Pipeline still in production. Has processed 4+ quarters of royalty calculations without manual intervention.")

    st.divider()

    # Compact methodology section
    st.markdown("## MY APPROACH")
    st.markdown("Every project above followed the same 7-layer methodology — developed across 5 companies over 14 years:")
    approach = [
        "**1. Requirements & Alignment** — What decision will this enable? RACI, KPI definitions, governance.",
        "**2. Data Quality** — Null detection, dedup, schema validation, row count baselines. Hard-fail gates.",
        "**3. Exploratory Analysis** — Understand relationships before building. Correlation tells you where to look.",
        "**4. Hypothesis & Testing** — A/B, multivariate, forecasting. Statistical significance, not gut feel.",
        "**5. Visualization & Reporting** — Star schema, DAX measures, RLS, sub-3-second load targets.",
        "**6. Culture & Change** — Training, onboarding, self-service. If the team can't operate without me, I'm not done.",
        "**7. Delivery & QA** — KPI variance alerts, cross-source parity, refresh monitoring. Trust must persist."
    ]
    for line in approach:
        st.markdown(line)

    st.divider()
    st.markdown("**Ready to talk?** Navigate to **Connect** or reach me at [linkedin.com/in/jchang0102](https://linkedin.com/in/jchang0102).")


# =============================================================================
# EXPLORER
# =============================================================================
def render_explorer():
    st.markdown("# PROFITABILITY EXPLORER")
    st.markdown("A working profitability analyzer processing **$392M in shipped sales** across **76 accounts** and **9 divisions**. Filter by division, sort by margin, and see which accounts make money vs which just generate volume.")
    st.markdown("*If Division X has 40% of revenue but negative margin, do you invest to fix it or reallocate to Division Y? That is what this tool answers.*")
    st.markdown('<a href="https://github.com/jasonchang0102/Streamlit0102/tree/main/code_samples" target="_blank">View code samples on GitHub →</a>', unsafe_allow_html=True)

    st.markdown('<div class="accent-section"><p style="font-size:14px;line-height:1.7;color:#404040"><strong>Try this:</strong> The default view shows Division D and Division F side by side. Division D generates $139M in revenue at 28.9% margin. Division F generates only $6M — but at 34.4% margin. That gap is the resource allocation question: do you scale the profitable niche or double down on volume? Click the X to clear the filter and explore all 9 divisions.</p></div>', unsafe_allow_html=True)

    st.divider()

    df = load_data()

    # Filters — pre-filtered for aha moment (Direction 8)
    default_divisions = ["Division D - Core/Licensed", "Division F - Specialty"]
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        divisions = st.multiselect("Division", sorted(df["Division"].unique()), default=default_divisions)
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
# CONNECT
# =============================================================================
def render_connect():
    dark_section("""
        <h2 style="font-size:44px;letter-spacing:4px;margin:0 0 12px">LET'S TALK</h2>
        <p style="font-size:16px">Currently interviewing for Senior BI & Analytics Manager roles. Best reached via LinkedIn for a quick response.</p>
    """)

    st.markdown("I'm looking for organizations ready to turn their data into a strategic asset — where the right platform and governance can unlock decisions that are currently blocked. If that sounds like your team, I'd like to hear about it.")

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

    # Direction 4: FAQ
    st.markdown("## WHAT HIRING MANAGERS ASK ME")
    faq = [
        ("How do you handle metric disagreements between VPs?", "I get them in a room with the data, not the dashboards. Definitions first, visualizations second."),
        ("What's the hardest part of post-merger data work?", "Not the schemas — the politics of whose numbers go down when you standardize."),
        ("How do you know a dashboard is successful?", "When stakeholders stop requesting ad hoc reports and start making decisions in the same meeting they see the data."),
        ("How do you build trust with non-technical stakeholders?", "I ask them what decision they're trying to make before I ask what data they need.")
    ]
    for q, a in faq:
        st.markdown(f"**{q}**")
        st.markdown(f"*{a}*")
        st.write("")

    st.divider()

    # Direction 29: Trimmed Brenton quote
    st.markdown("## WHAT MY MANAGER SAID")
    st.markdown("> *\"He is someone our team relied on for all key performance metrics in a very demanding and often changing environment. His out of the box thinking provided solutions that others simply would not conceive.\"*")
    st.markdown("**Brenton Harlow** — Executive Leader, CPG Sales, Marketing, Operations & Technology — Direct Manager at Advantage Solutions")

    st.divider()

    st.markdown("*This portfolio was built with Python, Streamlit, Plotly, and Pandas — deployed on Streamlit Cloud with anonymized real data.*")
    st.markdown('<a href="https://github.com/jasonchang0102/Streamlit0102/tree/main/code_samples" target="_blank">View code samples on GitHub →</a>', unsafe_allow_html=True)


main()
