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
RESUME_URL = "https://github.com/jasonchang0102/Streamlit0102/raw/main/--Jason_Chang_Sr_BI_Analytics_Manager_Resume--03-17-26.pdf"
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
    }
}

# =============================================================================
# CSS - minimal, only what Streamlit can't do natively
# =============================================================================
CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>

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
.result-card {background:#0a0a0a;padding:24px;text-align:center;border-radius:0;margin-top:0}
.result-val {font-family:'Bebas Neue',sans-serif;font-size:36px;color:#fff!important}
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

def show_image(name, caption):
    """Show image with fallback if missing"""
    path = ASSETS / name
    if path.exists():
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
        page = st.radio("Nav", ["Home", "Work", "About", "Live Demo", "Connect"], label_visibility="collapsed")
        st.markdown(f'<div class="sb-footer"><a href="{RESUME_URL}" target="_blank" class="sb-dl">DOWNLOAD RESUME</a></div>', unsafe_allow_html=True)

    pages = {
        "Home": render_home,
        "Work": render_work,
        "About": render_about,
        "Live Demo": render_explorer,
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
    c1.metric("Stakeholders Served", "250+")
    c2.metric("Data Sources Unified", "99+")
    c3.metric("Fewer KPI Conflicts", "70%")
    c4.metric("Reporting Cycle", "5→1 day")

    st.divider()

    # Flagship
    dark_section("""
        <p style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#a3a3a3;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px">FLAGSHIP — ADVANTAGE SOLUTIONS</p>
        <h2 style="font-size:36px;line-height:1.1;margin:0 0 12px">FIVE SALES SYSTEMS. FIVE REVENUE NUMBERS. ONE BOARD MEETING.</h2>
        <p class="meta">6 weeks &nbsp;|&nbsp; Post-merger unification &nbsp;|&nbsp; 250 users</p>
        <br>
        <p style="color:#d4d4d4;font-size:16px;line-height:1.8">Five regional sales systems, five definitions of revenue, and a CFO who couldn't trust any of them. I had 6 weeks before Q3 close to build a single source of truth — starting with getting five VPs to agree on what the numbers should mean. Read the full story under <strong style="color:#ca8a04">Work</strong> in the sidebar.</p>
    """)

    result_cards([
        ("70%", "Fewer KPI Conflicts"),
        ("5→1 day", "Reporting Cycle"),
        ("9%", "Quarterly Revenue Growth"),
        ("250", "Users on Platform")
    ])

    st.write("")
    tags(["Snowflake", "Power BI", "DAX", "Python", "SQL"], dark=False)

    st.write("")
    st.write("")

    # Project cards
    st.markdown("## MORE WORK")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### MODERN HOME STATION")
        st.markdown("### MARKETING WAS SPENDING BLIND")
        st.markdown("No attribution. Same promo to everyone. Data scattered across Facebook, Shopify, GA4. Built cross-channel attribution framework, A/B testing program, and 4-phase ad scaling system from scratch.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Conversion", "+33%")
        m2.metric("CPA", "-18%")
        m3.metric("YoY Revenue", "+85%")
        show_image("mhs_engagement.png", "K-Means clustering: CPC vs Page Engagement across 4 campaign segments")

    with col2:
        st.markdown("##### ADVANTAGE SOLUTIONS")
        st.markdown("### SALES PIPELINE — FROM LEADS TO REVENUE")
        st.markdown("Built end-to-end sales conversion analytics tracking 1,489 leads through opportunity, proposal, and close stages. Enabled real-time visibility into rep-level conversion rates across regions and programs.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Win Rate", "24.1%")
        m2.metric("Leads Tracked", "1,489")
        m3.metric("Wins", "360")
        show_image("advantage_program.png", "Sales Conversion: 1,489 leads, 24.1% win rate, period-over-period tracking")

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
- Previous BI lead quit mid-project
- 6 weeks until Q3 close deadline
""")

    section_header("WHY THIS WAS HARD")
    st.markdown("This was not a technical problem — it was political. Each regional VP had built metrics to make their team look good. Standardizing meant someone's numbers would go down. Getting alignment required trust-building before any code was written.")

    section_header("MY APPROACH")
    st.markdown("""
**Week 1–2:** Interviewed 12 stakeholders. Asked each one: "What decision are you trying to make with this data?" Mapped every metric definition across all 5 systems.

**Week 3:** Facilitated an alignment session. Got 5 VPs to agree on 12 golden metrics with documented definitions. This was the hardest week.

**Week 4–5:** Built unified Snowflake schema. Wrote 40+ DAX measures. Designed Power BI dashboards with drill-through from executive summary to regional detail.

**Week 6:** Trained 250 users. Deprecated 47 legacy reports. Set up data governance process for future metric changes.

Additionally, replaced the 47 Excel macros that one analyst maintained for 99 vendor data sources with automated Python + SQL pipelines. Sat with the analyst for a full week reverse-engineering undocumented business logic — custom GL code mappings, vendor exception rules. Built dynamic column mapping in Python that handles vendor format changes without code updates. Significantly reduced error rates and eliminated 160 hours of manual processing per quarter.
""")

    section_header("WHAT WENT WRONG")
    st.markdown("APAC had an undocumented custom field that their entire commission structure depended on. Their numbers broke on Day 1 of launch. I had to patch the data model live while the regional VP was on a call with the CEO. Lesson: always audit edge-case dependencies before deprecating legacy systems.")

    # Images
    st.write("")
    st.markdown("##### DASHBOARD VIEWS")
    tab1, tab2, tab3 = st.tabs(["Executive Dashboard", "Margin Analysis", "Scorecard"])
    with tab1:
        show_image("advantage_executive.png", "Team Scorecard: 83 customers, 7 products, 42.5% GM%, revenue variance to budget by month, revenue by region (North/East/South/Central/West)")
    with tab2:
        show_image("advantage_margin.png", "Program Margin Analysis: RevenueTY and GM% by business unit, bubble chart of Revenue Var % to Budget vs GM% by industry, product-level treemap (Primus/Gladius/Sova), GM% trend by month")
    with tab3:
        show_image("advantage_sales.png", "Individual Scorecard: 16 customers, RevenueTY by month with budget variance line, revenue by region")

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
    st.dataframe(pd.DataFrame(econ_data), hide_index=True, use_container_width=True)

    st.markdown("""
**4-Phase Scaling Framework**

**Phase 1 — Discovery (Week 1–4):** 10 interest audiences at $5/adset, horizontal testing only. Kill rules: CPC >$2, CTR <1%, CPM >$15 by day 2 = pause. Zero purchases by day 4 = kill. Goal: 5 proven adsets with 10+ purchases each.

**Phase 2 — Controlled Scaling (Week 4–8):** Add lookalike audiences, creative retargeting. Budget: 50% LAA, 40% new interests, 10% retarget. Duplicate proven adsets at 50% higher budget. One variable change at a time, every 3 days.

**Phase 3 — H+V Scale (Week 8–11):** $10–50/adset, introduce bid cap. Vertical scaling on winners (50–100% budget increase on 30–40% net profit adsets). Decrease underperformers 20–33% every 2 days. Value-based audience layering.

**Phase 4 — Bid Cap at Scale (Week 11+):** $1K–3K campaign budgets, Super LAA. Gate: 400+ purchases, consistent 2x breakeven ROAS. Winner identification every 12 hours. Max daily spend: $508.

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
        show_image("mhs_engagement.png", "K-Means clustering: 4 clusters by CPC vs page engagement. 162K sales, 104K sessions. Campaign-level cluster assignment.")
    with tab2:
        show_image("mhs_customer_journey.png", "Customer Journey: 86 contacts across 17 journeys. Email delivery, open, click, and submission tracking with dispatch timeline.")
    with tab3:
        show_image("mhs_email_analysis.png", "CRM interaction analysis: Ranked by file count — ActivityContactDispatched (99), WebsiteVisited (162), EmailOpened (86), EmailSent (63), FormVisited (82), FormSubmitted (47). Full interaction funnel visibility.")

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
    st.markdown("*Three views of the same pipeline system at different scope levels — from full team to individual agent to field program.*")
    tab1, tab2, tab3 = st.tabs(["Full Team (1,489 Leads)", "Single Agent Filter (354 Leads)", "Field Program (21K Engaged)"])
    with tab1:
        show_image("advantage_program.png", "Sales Conversion — Multiple Agents: 1,489 leads, 24.1% win rate, top/bottom converter identification with sparklines")
    with tab2:
        show_image("lead_to_win.png", "Lead-to-Win Dashboard (development view): 354 leads → 67 wins (18.93%). Converted leads over time with threshold tracking. Lead-to-Opp 69.77%, Opp-to-Win 27.13%.")
    with tab3:
        show_image("conversion_dashboard.jpg", "Field Conversion: 21K engaged → 14K sampled → 20.9% conversion. By region, FMM, and program with geographic mapping.")


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
        st.markdown("SQL (8+ years)  \nPower BI / DAX  \nPython  \nSnowflake  \nExcel + VBA")
    with c2:
        st.markdown("### ALSO FLUENT")
        st.markdown("BigQuery  \nGA4  \nLooker  \nQlik Sense  \nPower Query  \nMeta Ads  \nShopify  \nHubSpot  \nKlaviyo")
    with c3:
        st.markdown("### METHODS")
        st.markdown("A/B Testing  \nAttribution Modeling  \nK-Means Clustering  \nCohort Analysis  \nForecasting  \nRegression  \nExperiment Design")

    st.divider()

    # Certifications
    st.markdown("## CERTIFICATIONS")
    cert_cols = st.columns(len(CERTS))
    for col, (name, info) in zip(cert_cols, CERTS.items()):
        with col:
            st.markdown(f"**{name}**")
            date_str = f" — {info['date']}" if info['date'] else ""
            st.markdown(f"*{info['issuer']}{date_str}*")
            st.markdown(f"[Verify →]({info['url']})")

    st.divider()

    # Beliefs
    dark_section("""
        <h2 style="font-size:28px;letter-spacing:3px;margin:0 0 24px">WHAT I BELIEVE</h2>
        <p class="belief">A dashboard nobody uses is worse than no dashboard — it consumed resources and created false confidence.</p>
        <p class="belief">Data governance is not a project. It is a culture you build one conversation at a time.</p>
        <p class="belief">The best BI managers spend more time listening to stakeholders than writing queries.</p>
        <p class="belief">If your reporting cycle is longer than your decision cycle, you are always too late.</p>
    """)


# =============================================================================
# EXPLORER
# =============================================================================
def render_explorer():
    st.markdown("# PROFITABILITY EXPLORER")
    st.markdown("Interactive analysis of **~$392M in shipped sales** across **76 accounts** and **9 divisions**. Built from real program data at Advantage Solutions.")
    st.markdown("*This tool demonstrates the type of analysis I build for executive stakeholders — connecting revenue to margin to surface which segments are actually profitable vs just generating volume. Account and division names are anonymized for confidentiality.*")

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
    fig.add_trace(go.Bar(x=monthly["Month"], y=monthly["Sales"], name="Shipped Sales", marker_color="#0d9488", opacity=0.85))
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
                st.markdown(f'<div class="accent-section"><p style="font-size:16px;line-height:1.8;color:#404040"><strong>{rev_name}</strong> leads in both revenue (${rev_sales:,.0f}) and margin ({rev_mpct:.1f}%) — a rare combination. The next largest account, <strong>{second_rev["Account"]}</strong>, generates ${second_rev["Sales"]:,.0f} at {second_rev["Margin_Pct"]:.1f}% margin. Understanding which accounts combine volume with profitability is how you prioritize sales resources.</p></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="accent-section"><p style="font-size:16px;line-height:1.8;color:#404040"><strong>{rev_name}</strong> leads in both revenue (${rev_sales:,.0f}) and margin ({rev_mpct:.1f}%).</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="accent-section"><p style="font-size:16px;line-height:1.8;color:#404040"><strong>{rev_name}</strong> leads in revenue (${rev_sales:,.0f}) at {rev_mpct:.1f}% margin, while <strong>{mar_name}</strong> achieves the highest margin at {mar_mpct:.1f}% on ${mar_sales:,.0f} in sales. This is the type of tradeoff analysis that changes how a company allocates sales resources — volume does not automatically equal profitability.</p></div>', unsafe_allow_html=True)


# =============================================================================
# CONNECT
# =============================================================================
def render_connect():
    dark_section("""
        <h2 style="font-size:44px;letter-spacing:4px;margin:0 0 12px">LET'S TALK</h2>
        <p style="font-size:16px">Open to Senior BI & Analytics Manager opportunities. Best way to reach me is email.</p>
    """)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("📧 **EMAIL**")
        st.markdown("jason.chang01022024@gmail.com")
    with c2:
        st.markdown("💼 **LINKEDIN**")
        st.markdown("[linkedin.com/in/jchang0102](https://linkedin.com/in/jchang0102)")
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
