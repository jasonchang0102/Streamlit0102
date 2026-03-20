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
.dark-section h2 {font-family:'Bebas Neue',sans-serif;color:#fff!important;letter-spacing:2px;margin:0 0 8px;font-size:2.4rem!important}
.dark-section p {color:#a3a3a3}
.dark-section .meta {font-family:'JetBrains Mono',monospace;font-size:13px;color:#737373}

/* Accent section */
.accent-section {background:#f5f5f5;padding:32px;border-left:4px solid #0a0a0a;border-radius:0;margin:24px 0}

/* Gold accent — section headers */
.gold-border {border-left:3px solid #ca8a04;padding-left:16px;margin-bottom:24px}
.gold-border h3 {font-size:1.65rem!important}

/* Case result cards */
.result-card {background:#0a0a0a;padding:28px;text-align:center;border-radius:0;margin:0 2px}
.result-val {font-family:'Bebas Neue',sans-serif;font-size:42px;color:#ca8a04!important}
.result-label {font-family:'Inter',sans-serif;font-size:12px;color:#a3a3a3;text-transform:uppercase;letter-spacing:1px;margin-top:6px}

/* Tags */
.tag {display:inline-block;font-family:'JetBrains Mono',monospace;font-size:12px;padding:6px 12px;margin:2px;border:1px solid #e5e5e5;background:#f5f5f5;color:#0a0a0a}
.tag-dark {border-color:#333;background:#262626;color:#a3a3a3}

/* Headings override — 10% larger */
h1 {font-family:'Bebas Neue',sans-serif!important;letter-spacing:2px!important;color:#0a0a0a!important;font-size:2.75rem!important}
h2 {font-family:'Bebas Neue',sans-serif!important;letter-spacing:2px!important;color:#0a0a0a!important;font-size:2.0rem!important}
h3 {font-family:'Bebas Neue',sans-serif!important;letter-spacing:1px!important;color:#0a0a0a!important;font-size:1.5rem!important}
h5 {font-size:1.1rem!important}

/* Metric deltas — all gold, no red/green, no arrows */
[data-testid="stMetricDelta"] {color:#ca8a04!important}
[data-testid="stMetricDelta"] svg {display:none!important}
[data-testid="stMetricValue"] {font-size:1.8rem!important}

/* Image frames */
[data-testid="stImage"] {border:1px solid #e5e5e5;border-radius:2px}

/* Tab styling — larger, dark bg, gold active, clearly interactive */
.stTabs [data-baseweb="tab-list"] {background:#1a1a1a;padding:8px;border-radius:8px;gap:8px}
.stTabs [data-baseweb="tab"] {background:#333;border:2px solid #555;border-radius:8px;padding:14px 32px;font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:#d4d4d4;min-height:52px}
.stTabs [data-baseweb="tab"]:hover {background:#ca8a04;color:#fff;border-color:#ca8a04}
.stTabs [aria-selected="true"] {background:#ca8a04!important;color:#fff!important;border-color:#ca8a04!important}
.stTabs [data-baseweb="tab-highlight"] {background:#ca8a04!important}
.stTabs [data-baseweb="tab-border"] {display:none}

/* Content padding — inset from edges */
.block-container {padding-left:80px!important;padding-right:80px!important}
</style>"""

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
def scroll_to_top():
    """Reset scroll position on page switch — multiple fallbacks for reliability"""
    st.markdown("""
        <script>
            // Try all known Streamlit scroll containers
            try { window.parent.document.querySelector('[data-testid="stAppViewContainer"]').scrollTo(0, 0); } catch(e) {}
            try { window.parent.document.querySelector('section.main').scrollTo(0, 0); } catch(e) {}
            try { window.parent.document.querySelector('.main').scrollTo(0, 0); } catch(e) {}
            try { window.scrollTo(0, 0); } catch(e) {}
        </script>
    """, unsafe_allow_html=True)

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
        page = st.radio("Nav", [
            "Home",
            "Advantage Solutions",
            "Modern Home Station",
            "Live Demo",
            "Connect"
        ], label_visibility="collapsed")
        st.markdown(f'<div class="sb-footer"><a href="{RESUME_URL}" target="_blank" class="sb-dl">DOWNLOAD RESUME</a></div>', unsafe_allow_html=True)

    pages = {
        "Home": render_home,
        "Advantage Solutions": render_advantage,
        "Modern Home Station": render_mhs,
        "Live Demo": render_explorer,
        "Connect": render_connect
    }
    pages[page]()

# =============================================================================
# HOME
# =============================================================================
def render_home():
    scroll_to_top()
    st.markdown("##### Senior BI & Analytics Manager — 8+ Years")
    st.markdown("# FROM STAR SCHEMA TO MULTIVARIATE TESTING — THE ANALYTICAL FRAMEWORK BEHIND TRUSTED DATA")
    st.markdown("Most organizations have the data. What they lack is the analytical framework — star schema design, statistical testing, governance processes — that turns conflicting numbers into a single trusted view. Over 14 years and 5 organizations, I have developed a methodology that connects data architecture to business decisions. The platforms I build are still in production. The teams I mentor are self-sufficient.")

    # Result cards — FIRST thing after headline (Direction 2)
    st.write("")
    st.markdown("**Impact delivered at Advantage Solutions:**")
    result_cards([
        ("$55M", "Royalty Processing Automated"),
        ("350→2 hrs", "Quarterly Analyst-Hours"),
        ("47→0", "Shadow Excel Trackers"),
        ("$3M", "Misallocated Spend Found")
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
    st.markdown('*"His out of the box thinking provided solutions that others simply would not conceive."* — **Brenton Harlow**, Executive Leader, Advantage Solutions')

    st.divider()

    # Project cards — problem→result format (Direction 5)
    st.markdown("## SELECTED PROJECTS")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### MODERN HOME STATION")
        st.markdown("**Cross-channel attribution from scratch**")
        st.markdown("DTC startup with no analytics infrastructure. Built single attribution framework across GA4, Shopify, Meta, and Klaviyo. Designed 12-group multivariate testing program, used K-Means clustering (page view sequences, visit depth, engagement patterns) to surface 4 distinct behavioral segments, and surfaced shipping cost inefficiencies through carrier-by-country analysis.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Conversion", "+33%")
        m2.metric("CPA", "-18%")
        m3.metric("YoY Revenue", "+85%")

    with col2:
        st.markdown("##### ADVANTAGE SOLUTIONS")
        st.markdown("**Post-merger data unification across $1.68B enterprise**")
        st.markdown("Post-merger unification across a $1.68B enterprise — Snowflake + Power BI ecosystem, data governance framework, royalty automation pipeline.")
        m1, m2, m3 = st.columns(3)
        m1.metric("Sources", "99+")
        m2.metric("Users", "250+")
        m3.metric("Cycle", "5→1 day")

    # Dashboard previews
    st.write("")
    img1, img2 = st.columns(2)
    with img1:
        show_image("mhs_engagement.png", "K-Means clustering: which campaigns are worth scaling vs spend traps")
    with img2:
        show_image("advantage_executive.png", "Executive dashboard: 83 customers against budget in one view")

    st.markdown("*Full case studies with dashboard walkthroughs on the **Work** page →*")

    # Live Demo CTA (Gap 1)
    st.write("")
    dark_section("""
        <p style="font-size:18px;text-align:center;margin:0;color:#d4d4d4"><strong style="color:#ca8a04">Live Demo</strong> — explore profitability, concentration risk, and margin trend analysis across $387M in real operational data.</p>
    """)

    # Industry hook
    st.write("")
    st.markdown('*From statistical testing and customer segmentation to ETL automation and governance design — platforms still in production, teams self-serving, years after initial deployment.*')


# =============================================================================
# ADVANTAGE SOLUTIONS
# =============================================================================
def render_advantage():
    scroll_to_top()
    dark_section("""
        <h2 style="font-size:40px;letter-spacing:3px;margin:0 0 8px">ADVANTAGE SOLUTIONS</h2>
        <p style="font-size:16px;color:#a3a3a3">$1.68B Enterprise · Post-Merger · 250+ Stakeholders · 99 Vendor Sources</p>
    """)

    # Key results — above fold
    result_cards([
        ("70%", "Fewer KPI Conflicts"),
        ("$3M", "Misallocated Spend Surfaced"),
        ("350→2 hrs", "Quarterly Processing"),
        ("80%", "Team Self-Service Rate")
    ])

    st.write("")

    # ─── SECTION 1: THE ENVIRONMENT I INHERITED ──────────────────────────
    section_header("THE STARTING POINT")
    st.markdown("""
Following the merger, Advantage Solutions operated five separate regional sales systems — each with its own metric definitions, data sources, and reporting cadence. The CFO received five different revenue numbers in board meetings. Field teams, lacking confidence in centralized reporting, had created 47 independent Excel trackers across regions. Two senior financial analysts spent three full weeks every quarter manually processing $55M in royalty calculations across 99 vendor contracts from 6 different source systems.

The opportunity was clear: unify the data infrastructure, establish governance, automate the manual processes, and develop the regional analytics team to sustain it independently.
""")

    # Before → After metrics
    ba1, ba2, ba3, ba4 = st.columns(4)
    ba1.metric("Revenue Definitions", "1", "4 consolidated", delta_color="normal")
    ba2.metric("Shadow Trackers", "0", "47 eliminated", delta_color="normal")
    ba3.metric("Reporting Cycle", "24 hrs", "4 days faster", delta_color="normal")
    ba4.metric("Governance", "Bi-weekly", "VP committee est.", delta_color="normal")

    st.divider()

    # ─── SECTION 2: WHAT I BUILT — TECHNICAL ─────────────────────────────
    section_header("WHAT I BUILT")

    st.markdown("**Platform Unification (6 weeks to Q3 close)**")
    st.markdown("""
I was brought in mid-cycle after the previous lead departed — with 6 weeks to Q3 close. The approach followed a structured sequence:

**Weeks 1–2:** Interviewed 12 stakeholders. Asked each one: "What decision are you trying to make with this data?" Mapped every metric definition across all 5 systems.

**Week 3:** Facilitated a cross-regional alignment session. Five VPs collaboratively defined 12 golden metrics with documented business rules. This was the most critical week.

**Weeks 4–5:** Built unified Snowflake schema. Wrote 40+ DAX measures. Designed Power BI dashboards with drill-through from executive summary to regional detail.

**Week 6:** Trained 250 users. Deprecated 47 legacy reports. Established a formal data governance process — any metric change required a written change request reviewed by the metric owner and one cross-functional stakeholder before deployment.
""")

    # Timeline
    t1, t2, t3, t4 = st.columns(4)
    t1.markdown("**Week 1-2**  \nStakeholder interviews  \nMetric mapping")
    t2.markdown("**Week 3**  \nVP alignment session  \n12 golden metrics")
    t3.markdown("**Week 4-5**  \nSnowflake schema  \n40+ DAX measures")
    t4.markdown("**Week 6**  \n250 users trained  \nGovernance launched")

    st.write("")
    st.markdown("**Royalty Automation ($55M across 99 vendors)**")
    st.markdown("""
The lead finance analyst had been processing royalty calculations manually for 3 years. During our week together reverse-engineering her process, undocumented rules surfaced that only existed in her head — vendor exception codes, seasonal rate adjustments, GL mappings that changed quarterly but were never written down. She had developed deep expertise over three years — knowledge that had never been documented because it never needed to be. Automating this required more than coding. It required structured knowledge transfer, making every implicit decision rule explicit and testable.

The solution: a Python ETL pipeline with dynamic column mapping across all 6 source systems, VBA-generated vendor statements matching each licensor's requirements (Disney, Columbia, Warner Bros), and automated email distribution. Adding a new source system requires one new mapping line, not new code. The pipeline reduced quarterly processing from 350+ analyst-hours to 2 hours, freeing two senior financial analysts to focus on strategic analysis.
""")

    st.divider()

    # ─── SECTION 3: DATA ARCHITECTURE ────────────────────────────────────
    section_header("DATA ARCHITECTURE")
    st.markdown("""
I redesigned the data architecture as a star schema — fact tables for sales, compliance, and campaign performance, dimension tables for time, store, product, vendor, and campaign metadata.

**Normalization → Denormalization:** Source data arrived normalized across 6 systems. I normalized further in staging (deduplication, key standardization, referential integrity checks), then denormalized into the star schema for reporting performance. This two-step process ensured data quality upstream while enabling sub-3-second dashboard loads downstream.

**Type 1 Warehouse Mitigation:** The source systems used Type 1 slowly-changing dimensions — meaning historical values were overwritten. I implemented weekly Snowflake snapshots to preserve historical state, then built reconstruction logic for any point-in-time view. This gave leadership the ability to compare current performance against true historical baselines.

**Performance:** Pre-aggregated fact tables at multiple grain levels. Row-level security filtering at the Snowflake level, not Power BI level. Dashboard load target: under 3 seconds. Full refresh cycle: under 15 minutes. Refresh errors reduced 80%.
""")

    # Architecture diagram
    st.markdown("""
<div style="max-width:600px;margin:0 auto;font-family:'Inter',sans-serif;font-size:14px;line-height:1.6">
<div style="background:#f5f5f5;border:1px solid #e5e5e5;padding:12px 20px;text-align:center;margin:4px 0">
<strong>RAW</strong> — Unmodified vendor ingestion (read-only)
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#f5f5f5;border:1px solid #e5e5e5;padding:12px 20px;text-align:center;margin:4px 0">
<strong>STAGING</strong> — Cleaned, deduped, normalized, schema-validated
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#0a0a0a;color:#fff;padding:12px 20px;text-align:center;margin:4px 0">
<strong style="color:#ca8a04">ANALYTICS</strong> — Star schema: fct_sales, fct_compliance, fct_campaign + dim_time, dim_store, dim_product, dim_vendor
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#0a0a0a;color:#fff;padding:12px 20px;text-align:center;margin:4px 0">
<strong style="color:#ca8a04">SEMANTIC LAYER</strong> — 40+ DAX measures, row-level security, drill-through logic
</div>
<div style="text-align:center;color:#a3a3a3;font-size:18px;margin:4px 0">▼</div>
<div style="background:#f5f5f5;border:1px solid #e5e5e5;padding:12px 20px;text-align:center;margin:4px 0">
<strong>PRESENTATION</strong> — Executive → Regional → Individual dashboards (250+ users)
</div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ─── SECTION 4: HOW I LED ────────────────────────────────────────────
    section_header("EXECUTIVE ALIGNMENT & GOVERNANCE")
    st.markdown("""
The unification required alignment before architecture. Each regional VP had built metrics around their team's strengths. Standardizing meant some numbers would shift. Building consensus required trust and transparency before any code was written.

The governance framework I established includes: a formal metric change request process, QA validation gates (row count monitoring, null detection, KPI variance ±10% from trend), and a bi-weekly governance committee with VP Finance, VP Sales, and VP Operations. This framework is still in production and serves as the standard for cross-program reporting.

Once unified, the platform's same-week budget visibility surfaced $3M in trade spend allocated to campaigns with negative ROI — an insight that only became visible once all regions reported from a unified data source. Leadership reallocated within one reporting cycle, improving ROI by 12%.
""")

    st.markdown("**Analytical Methodology**")
    st.markdown("Every project I lead follows a 7-layer methodology refined across 5 organizations over 14 years:")
    approach = [
        "**1. Requirements & Alignment** — What decision will this enable? RACI, KPI definitions, governance.",
        "**2. Data Quality** — Null detection, deduplication, schema validation, row count baselines. Hard-fail gates.",
        "**3. Exploratory Analysis** — Understand relationships before building. Identify patterns before modeling.",
        "**4. Hypothesis & Testing** — A/B, multivariate, forecasting. Statistical significance, not assumptions.",
        "**5. Visualization & Reporting** — Star schema, DAX measures, RLS, sub-3-second load targets.",
        "**6. Culture & Change** — Training, mentorship, onboarding, self-service enablement. The goal is team self-sufficiency.",
        "**7. Delivery & QA** — KPI variance alerts, cross-source parity, refresh monitoring. Trust must persist."
    ]
    for line in approach:
        st.markdown(line)

    st.divider()

    # ─── SECTION 5: TEAM DEVELOPMENT ─────────────────────────────────────
    section_header("TEAM DEVELOPMENT")
    st.markdown("""
When I joined, the 7 regional analytics managers could run pre-built reports but could not build their own. Every ad hoc request escalated to me — consuming 60% of my time.

**Phase 1 — Foundation (Weeks 1-4):** Hands-on training in Power BI development, DAX measure writing, and data governance standards. Each session tied to a real dashboard they would own. I paired each manager with a specific business question their VP had been asking, and we built the answer together.

**Phase 2 — Ownership Transfer (Weeks 5-8):** Each manager built and presented their own regional dashboard to their VP. I reviewed the data model and DAX logic before presentation but did not build it for them.

**Phase 3 — Self-Sufficiency (Months 3-6):** Established a shared query library, rotating "metric of the week" deep dives, and peer review process. Within 6 months, 80% of ad hoc analytical requests were resolved at the regional level without escalation.
""")

    # Team before→after
    ta1, ta2, ta3, ta4 = st.columns(4)
    ta1.metric("Ad Hoc Escalations", "20%", "80% now self-served", delta_color="normal")
    ta2.metric("Managers Building", "7 of 7", "From 0", delta_color="normal")
    ta3.metric("My Time on Strategy", "80%", "60% shifted from Q&A", delta_color="normal")
    ta4.metric("Peer Reviews", "Active", "Culture established", delta_color="normal")

    st.divider()

    # ─── SECTION 6: DASHBOARDS ───────────────────────────────────────────
    section_header("DASHBOARD VIEWS")
    show_image("advantage_executive.png", "Executive view: 83 customers against budget — revenue, margin, GM% trend.")
    dtab1, dtab2 = st.tabs(["Margin Analysis", "Rep Scorecard"])
    with dtab1:
        show_image("advantage_margin.png", "Revenue variance vs gross margin by business unit.")
    with dtab2:
        show_image("advantage_sales.png", "Rep scorecard: 16 customers, monthly revenue.", width=0.30)

    st.divider()

    # ─── SECTION 7: WHAT WENT WRONG + DURABILITY ─────────────────────────
    section_header("CHALLENGES & DURABILITY")
    st.markdown("APAC had an undocumented custom field that their entire commission structure depended on. Their numbers shifted on Day 1 of launch. The team deployed an emergency data model fix within hours while the regional VP was on a call with the CEO. After the resolution, APAC became the highest-adoption group on the platform — because they experienced firsthand that the team could respond in real-time.")
    st.markdown("The first royalty automation run produced incorrect rates for one vendor group — a tiered rate structure that the analyst handled mentally but had never documented. Built a rate lookup table with threshold logic to handle this and any future tiered contracts.")
    st.caption("Platform still in production serving 250+ users. Royalty pipeline has processed 4+ quarters without manual intervention. Mentorship structure has onboarded 3 additional managers since established.")

    st.divider()
    st.markdown("*More case studies in the sidebar. Contact details on the **Connect** page.*")


# =============================================================================
# MODERN HOME STATION
# =============================================================================
def render_mhs():
    scroll_to_top()
    dark_section("""
        <h2 style="font-size:40px;letter-spacing:3px;margin:0 0 8px">MODERN HOME STATION</h2>
        <p style="font-size:16px;color:#a3a3a3">DTC eCommerce Startup · Built Analytics from Zero · 4 Platforms Unified</p>
    """)

    # Key results — above fold
    result_cards([
        ("+85%", "YoY Revenue (FY20)"),
        ("2x", "ROAS Improvement"),
        ("-75%", "Unmet Delivery Expectations"),
        ("-18%", "Shipping Costs")
    ])

    st.write("")

    # ─── SECTION 1: THE ENVIRONMENT ──────────────────────────────────────
    section_header("THE STARTING POINT")
    st.markdown("""
DTC startup, $65K+/month revenue, 780 units moving. Four ad platforms operating independently — GA4, Shopify, Meta, Klaviyo. Each platform attributed the same conversions to itself, making accurate breakeven analysis impractical without a unified framework.

When I joined, the founder was making budget decisions based on platform-reported ROAS — numbers that overstated performance because Facebook, Google, and Shopify each attributed the same conversions independently. The marketing team was scaling what appeared profitable, but the fundamental question had not yet been addressed: what does a profitable order actually cost after COGS, shipping, and platform fees? The first time I walked the team through the unit economics — showing that breakeven CPP was $47.48 — significantly higher than the working assumption of $20. This insight required a fundamental rethinking of the ad scaling strategy.
""")

    st.divider()

    # ─── SECTION 2: UNIT ECONOMICS & TESTING ─────────────────────────────
    section_header("ANALYTICAL FRAMEWORK")

    st.markdown("**Unit Economics Model** — Before allocating budget, the team needed a shared definition of 'profitable' at every funnel stage:")

    econ_data = {
        "Metric": ["Cost per Purchase", "Cost per Initiate Checkout", "Cost per Add to Cart", "ROAS"],
        "Breakeven": ["$47.48", "$28.49", "$55.14", "1.75x"],
        "20% Margin": ["$30.91", "$18.54", "$35.89", "2.68x"],
        "10% Margin": ["$39.20", "$23.52", "$45.52", "2.11x"]
    }
    st.table(pd.DataFrame(econ_data).set_index("Metric"))

    st.markdown("""
**4-Phase Scaling Framework:**

Phase 1: Discovery — 10 audiences at $5/adset, strict kill rules (CPC >$2 or CTR <1% = pause)
Phase 2: Controlled — Lookalike audiences, creative retargeting at capped budgets
Phase 3: Scale — 50-100% increases on profitable adsets, cut underperformers
Phase 4: Bid Cap — $1K-3K campaigns, gated by 400+ purchases and 2x breakeven ROAS

**Multivariate Testing (12 Groups)** — Designed a 3×2×2 test matrix: 3 creative types × 2 CTAs × 2 interaction formats. The winning combination (instructional creative + Learn More CTA + comment prompt) achieved the highest CTR at the lowest CPM — confirming that engagement-driven strategies outperformed direct-response for this product category.

**K-Means Clustering** — Customer segmentation by page view sequences, visit depth, and engagement patterns. The analysis surfaced 4 distinct clusters by CPC vs engagement, revealing which segments warranted further investment.

**Demand Forecasting** — Unified marketing, warehouse, purchasing, and customer service data into a shared operational view. Enabled cross-team decision-making with 40% shorter feedback cycles.
""")

    # Results
    r1, r2, r3, r4 = st.columns(4)
    r1.metric("Conversion", "+33%")
    r2.metric("CPA", "-18%")
    r3.metric("CPM", "-36%")
    r4.metric("ROAS", "2x")

    st.divider()

    # ─── SECTION 3: OPERATIONS INTELLIGENCE ──────────────────────────────
    section_header("OPERATIONS: AD SPEND → CUSTOMER SERVICE")
    st.markdown("""
As the DTC business scaled internationally, customer inquiries about shipping timelines increased — but the data to understand the root causes was distributed across multiple systems. Ad budgets were approved by country without visibility into downstream impact: how many orders each campaign would generate, which carriers would handle them, expected delay rates, and how many Zendesk tickets that would create.

This was not a single-department problem. The chain was: ad budget → order volume → shipping carrier selection → delivery timeline → customer expectation → support ticket volume → CS staffing. These steps had not yet been connected across teams. Each team optimized within their domain — marketing for ROAS, fulfillment for cost, customer service for response time — without visibility into the upstream and downstream effects.
""")

    st.markdown("""
The first step was mapping the full chain that had not yet been connected across teams. For each of 18 countries: shipping cost per unit, carrier assignment, average delay days, delay rate, and the downstream ticket generation rate (~1.8 Zendesk tickets per delayed order).

The data immediately surfaced a pattern: YanWen (燕文专线) corridors had a 44% average delay rate across 6 countries (Brazil, Russia, Italy, Poland, Switzerland, New Zealand) vs 12% for direct postal carriers.

Downstream, each delayed order generated ~1.8 support tickets (initial inquiry + follow-up). At 1,797 delayed orders per quarter, that was ~3,200 Zendesk tickets requiring ~800 CS hours — equivalent to a half-time CS hire that had not been budgeted because the connection between shipping delays and staffing demand had not been quantified.

For corridors where carrier switches were not cost-effective, the solution was expectation management — an automated notification system that set delivery expectations at the point of purchase by country. This reduced "where is my order?" inquiries by 75%.

The model ultimately became the backbone for ad budget approval. Before scaling spend into a new country, leadership could see the full cost: ad spend + shipping + expected delays + CS ticket volume + staffing implications.
""")

    # Interactive shipping demo
    st.write("")
    st.markdown("**Interactive: Country-Level Operations Model**")

    ship_df = pd.read_csv(DATA / "shipping_ops_data.csv")

    sk1, sk2, sk3, sk4 = st.columns(4)
    sk1.metric("Countries", f"{len(ship_df)}")
    sk2.metric("Quarterly Orders", f"{ship_df['orders_quarterly'].sum():,}")
    sk3.metric("Delayed Orders", f"{ship_df['delayed_orders'].sum():,}", f"{ship_df['delayed_orders'].sum()/ship_df['orders_quarterly'].sum()*100:.0f}%")
    sk4.metric("Est. CS Tickets", f"{ship_df['cs_tickets_est'].sum():,}")

    carriers = st.multiselect("Filter by Carrier", sorted(ship_df["carrier"].unique()), default=sorted(ship_df["carrier"].unique()), key="ship_carrier")
    ship_filtered = ship_df[ship_df["carrier"].isin(carriers)]

    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown("**Delay Rate by Country**")
        fig_delay = px.bar(
            ship_filtered.sort_values("delay_rate", ascending=True),
            x="delay_rate", y="country", orientation="h",
            color="carrier",
            labels={"delay_rate": "Delay Rate", "country": ""},
            height=450
        )
        fig_delay.update_layout(
            xaxis=dict(tickformat=".0%"),
            margin=dict(l=120, r=30, t=20, b=30),
            plot_bgcolor="#fff", paper_bgcolor="#fff",
            legend=dict(orientation="h", yanchor="bottom", y=1.02)
        )
        st.plotly_chart(fig_delay, use_container_width=True)

    with sc2:
        st.markdown("**Shipping Cost vs Delay Rate**")
        fig_cost = px.scatter(
            ship_filtered, x="ship_cost", y="delay_rate",
            size="orders_quarterly", color="carrier",
            hover_name="country",
            labels={"ship_cost": "Shipping Cost ($)", "delay_rate": "Delay Rate"},
            height=450, size_max=50
        )
        fig_cost.update_layout(
            yaxis=dict(tickformat=".0%"),
            margin=dict(l=50, r=30, t=20, b=30),
            plot_bgcolor="#fff", paper_bgcolor="#fff",
            legend=dict(orientation="h", yanchor="bottom", y=1.02)
        )
        st.plotly_chart(fig_cost, use_container_width=True)

    st.divider()

    # ─── SECTION 4: DASHBOARDS ───────────────────────────────────────────
    section_header("DASHBOARD VIEWS")
    show_image("mhs_engagement.png", "K-Means clustering: campaign segments by CPC vs engagement.")
    dtab1, dtab2 = st.tabs(["Customer Journey", "Email Analytics"])
    with dtab1:
        show_image("mhs_customer_journey.png", "86 contacts across 17 email journeys — which touchpoints convert?")
    with dtab2:
        show_image("mhs_email_analysis.png", "CRM touchpoint ranking: WebsiteVisited (162) and EmailOpened (86) led pre-purchase.")

    st.divider()

    # ─── SECTION 5: CHALLENGES & DURABILITY ──────────────────────────────
    section_header("CHALLENGES & DURABILITY")
    st.markdown("Three adsets cannibalizing each other due to overlapping audiences — built negative exclusions and restructured campaign hierarchy. Separately: silent autoplay videos inflating view counts — implemented a pre-launch QA checklist for all creative (audio, thumbnail, CTA rendering, platform-specific format).")
    st.markdown("Initial carrier switch recommendation for Brazil (YanWen → DHL) was cost-prohibitive. Found a middle path: regional carrier at $36/unit with 22% delay rate (down from 45%). Operational optimization is always constrained by unit economics.")
    st.caption("Attribution framework, scaling playbook, and operational model adopted as standard processes. Unit economics model used for all subsequent campaign launches through FY21.")

    st.divider()
    st.markdown("*More case studies in the sidebar. Contact details on the **Connect** page.*")


# =============================================================================
# EXPLORER
# =============================================================================
def render_explorer():
    scroll_to_top()
    st.markdown("# LIVE DEMOS")
    st.markdown("Interactive analyses built from **real operational data** — $387M in shipped sales across **75 accounts** and **9 divisions**. Profitability analysis, heatmap visualization, concentration risk, and trend detection — the same analytical methods I apply at Advantage Solutions, rebuilt with Plotly, Pandas, and Streamlit.")
    st.markdown('<a href="https://github.com/jasonchang0102/Streamlit0102/tree/main/code_samples" target="_blank">View code samples on GitHub →</a>', unsafe_allow_html=True)

    st.divider()

    df = load_data()

    # Summary metrics at top (Gap 3) — visible regardless of which tab is active
    total_sales = df["Shipped_Sales"].sum()
    total_margin = df["Margin_Dollars"].sum()
    overall_margin_pct = (total_margin / total_sales * 100) if total_sales > 0 else 0
    total_accounts = df["Account"].nunique()
    top3_pct = df.groupby("Account")["Shipped_Sales"].sum().nlargest(3).sum() / total_sales * 100

    sk1, sk2, sk3, sk4, sk5 = st.columns(5)
    sk1.metric("Total Sales", f"${total_sales/1e6:.0f}M")
    sk2.metric("Margin", f"{overall_margin_pct:.1f}%")
    sk3.metric("Accounts", f"{total_accounts}")
    sk4.metric("Top 3 Concentration", f"{top3_pct:.0f}%")
    sk5.metric("Divisions", f"{df['Division'].nunique()}")

    st.divider()

    demo_tab1, demo_tab2, demo_tab3, demo_tab4, demo_tab5, demo_tab6 = st.tabs([
        "📊 Profitability Explorer",
        "🔥 Revenue × Margin Heatmap",
        "📈 Division Deep Dive",
        "🎯 Customer Concentration",
        "📉 Month-over-Month Trend",
        "🧪 Multivariate Testing"
    ])

    # ─── DEMO 1: PROFITABILITY EXPLORER ──────────────────────────────────
    with demo_tab1:
        st.markdown("### PROFITABILITY EXPLORER")
        st.markdown("*If Division X has 40% of revenue but low margin, do you invest to fix it or reallocate to Division Y?*")

        col_f1, col_f2, col_f3 = st.columns(3)
        with col_f1:
            default_divisions = ["Division D - Core/Licensed", "Division F - Specialty"]
            divisions = st.multiselect("Division", sorted(df["Division"].unique()), default=default_divisions, key="demo1_div")
        with col_f2:
            month_range = st.slider("Month Range", 1, 10, (1, 10), key="demo1_month")
            st.caption("Data covers Jan–Oct (shipped orders only)")
        with col_f3:
            top_n = st.selectbox("Show Top N Accounts", [10, 20, 50, "All"], index=1, key="demo1_topn")

        filtered = df[
            (df["Division"].isin(divisions)) &
            (df["Month"] >= month_range[0]) &
            (df["Month"] <= month_range[1])
        ]

        total_sales = filtered["Shipped_Sales"].sum()
        total_margin = filtered["Margin_Dollars"].sum()
        margin_pct = (total_margin / total_sales * 100) if total_sales > 0 else 0
        total_accounts = filtered["Account"].nunique()
        total_units = filtered["Units"].sum()

        st.write("")
        k1, k2, k3, k4, k5 = st.columns(5)
        k1.metric("Sales", f"${total_sales/1e6:.1f}M")
        k2.metric("Margin $", f"${total_margin/1e6:.1f}M")
        k3.metric("Margin %", f"{margin_pct:.1f}%")
        k4.metric("Accounts", f"{total_accounts}")
        k5.metric("Units", f"{total_units/1e6:.1f}M")

        st.divider()

        # Monthly trend + bubble chart side by side
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown("**Monthly Trend**")
            monthly = filtered.groupby("Month").agg(
                Sales=("Shipped_Sales", "sum"),
                Margin=("Margin_Dollars", "sum")
            ).reset_index()
            monthly["Margin_Pct"] = monthly.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)

            fig = go.Figure()
            fig.add_trace(go.Bar(x=monthly["Month"], y=monthly["Sales"], name="Shipped Sales", marker_color="#ca8a04", opacity=0.85))
            fig.add_trace(go.Scatter(x=monthly["Month"], y=monthly["Margin_Pct"], name="Margin %", yaxis="y2", mode="lines+markers", line=dict(color="#0a0a0a", width=2.5), marker=dict(size=7)))
            fig.update_layout(
                yaxis=dict(title="Sales ($)", tickformat="$,.0f"),
                yaxis2=dict(title="Margin %", overlaying="y", side="right", tickformat=".1f", range=[0, max(monthly["Margin_Pct"].max() * 1.2, 50) if len(monthly) > 0 and not pd.isna(monthly["Margin_Pct"].max()) else 50]),
                xaxis=dict(title="Month", dtick=1),
                legend=dict(orientation="h", yanchor="bottom", y=1.02),
                height=350, margin=dict(l=50, r=50, t=30, b=30),
                plot_bgcolor="#fff", paper_bgcolor="#fff"
            )
            st.plotly_chart(fig, use_container_width=True)

        with chart_col2:
            st.markdown("**Division Profitability Map**")
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
                height=350, size_max=55
            )
            fig2.update_traces(textposition="top center", textfont_size=9)
            fig2.update_layout(
                yaxis=dict(tickformat="$,.0f"),
                xaxis=dict(tickformat=".0f", title="Margin %"),
                showlegend=False,
                plot_bgcolor="#fff", paper_bgcolor="#fff",
                margin=dict(l=50, r=30, t=20, b=30)
            )
            st.plotly_chart(fig2, use_container_width=True)

        st.divider()

        # Account table
        st.markdown("**Account Profitability**")
        acct_agg = filtered.groupby(["Account", "Division"]).agg(
            Sales=("Shipped_Sales", "sum"),
            COGS=("Shipped_COGS", "sum"),
            Margin=("Margin_Dollars", "sum"),
            Units=("Units", "sum")
        ).reset_index()
        acct_agg["Margin_Pct"] = acct_agg.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)
        acct_agg = acct_agg[acct_agg["Sales"] > 0]
        acct_agg = acct_agg.sort_values("Sales", ascending=False)

        if top_n != "All":
            acct_agg = acct_agg.head(int(top_n))

        display_df = acct_agg.copy()
        display_df["Sales"] = display_df["Sales"].apply(lambda x: f"${x:,.0f}")
        display_df["COGS"] = display_df["COGS"].apply(lambda x: f"${x:,.0f}")
        display_df["Margin"] = display_df["Margin"].apply(lambda x: f"${x:,.0f}")
        display_df["Units"] = display_df["Units"].apply(lambda x: f"{x:,.0f}")
        display_df["Margin_Pct"] = display_df["Margin_Pct"].apply(lambda x: f"{x:.1f}%")
        display_df.columns = ["Account", "Division", "Sales", "COGS", "Margin $", "Units", "Margin %"]

        st.dataframe(display_df, hide_index=True, use_container_width=True, height=400)

    # ─── DEMO 2: HEATMAP ────────────────────────────────────────────────
    with demo_tab2:
        st.markdown("### REVENUE × MARGIN HEATMAP")
        st.markdown("*I developed this dual-metric heatmap technique to solve a Power BI limitation — standard matrices cannot display two measures per cell. Running in production at Advantage Solutions using Python embedded in Power BI. Rebuilt here in Plotly for interactivity.*")

        # Build heatmap: accounts (rows) x divisions (cols)
        heatmap_data = df.groupby(["Account", "Division"]).agg(
            Sales=("Shipped_Sales", "sum"),
            Margin_Pct=("Margin_Pct", "mean")
        ).reset_index()

        # Get top 20 accounts by total sales
        top_accounts = df.groupby("Account")["Shipped_Sales"].sum().nlargest(20).index.tolist()
        heatmap_filtered = heatmap_data[heatmap_data["Account"].isin(top_accounts)]

        sales_pivot = heatmap_filtered.pivot_table(index="Account", columns="Division", values="Sales", aggfunc="sum").fillna(0)
        margin_pivot = heatmap_filtered.pivot_table(index="Account", columns="Division", values="Margin_Pct", aggfunc="mean").fillna(0)

        # Sort by total sales
        sales_pivot = sales_pivot.loc[sales_pivot.sum(axis=1).sort_values(ascending=True).index]

        # Build annotations: "$12.5M : 28.9%"
        import numpy as np
        annotations = []
        for i, acct in enumerate(sales_pivot.index):
            for j, div in enumerate(sales_pivot.columns):
                val = sales_pivot.iloc[i, j]
                mpct = margin_pivot.loc[acct, div] if acct in margin_pivot.index and div in margin_pivot.columns else 0
                if val > 0:
                    if val >= 1e6:
                        text = f"${val/1e6:.1f}M : {mpct:.0f}%"
                    elif val >= 1e3:
                        text = f"${val/1e3:.0f}K : {mpct:.0f}%"
                    else:
                        text = f"${val:.0f}"
                else:
                    text = ""
                annotations.append(dict(
                    x=div, y=acct, text=text,
                    font=dict(size=9, color="white" if val > sales_pivot.values.max() * 0.4 else "black"),
                    showarrow=False
                ))

        fig3 = go.Figure(data=go.Heatmap(
            z=sales_pivot.values,
            x=[d.split(" - ")[0] for d in sales_pivot.columns],
            y=sales_pivot.index,
            colorscale="Reds",
            showscale=True,
            colorbar=dict(title="Sales ($)", tickformat="$,.0f")
        ))
        fig3.update_layout(
            annotations=[dict(x=a["x"].split(" - ")[0] if " - " in str(a["x"]) else a["x"],
                              y=a["y"], text=a["text"], font=a["font"], showarrow=False) for a in annotations],
            height=600,
            xaxis=dict(title="Division", tickangle=45),
            yaxis=dict(title=""),
            margin=dict(l=150, r=40, t=20, b=80),
            plot_bgcolor="#fff", paper_bgcolor="#fff"
        )
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("*Top 20 accounts by total sales. Each cell: revenue and margin %. Red intensity = higher sales. This dual-metric view is what standard Power BI matrices cannot do — I solve it with Python visuals embedded in Power BI.*")

    # ─── DEMO 3: DIVISION DEEP DIVE ─────────────────────────────────────
    with demo_tab3:
        st.markdown("### DIVISION DEEP DIVE")
        st.markdown("*The drill-down view used in weekly regional reviews. I designed this to surface margin erosion at the account level — select a division to see which accounts are growing, which are declining, and where intervention is needed.*")

        selected_div = st.selectbox("Select Division", sorted(df["Division"].unique()), key="demo3_div")
        div_df = df[df["Division"] == selected_div]

        # KPIs for selected division
        div_sales = div_df["Shipped_Sales"].sum()
        div_margin = div_df["Margin_Dollars"].sum()
        div_mpct = (div_margin / div_sales * 100) if div_sales > 0 else 0
        div_accts = div_df["Account"].nunique()

        d1, d2, d3, d4 = st.columns(4)
        d1.metric("Division Sales", f"${div_sales/1e6:.1f}M")
        d2.metric("Margin $", f"${div_margin/1e6:.1f}M")
        d3.metric("Margin %", f"{div_mpct:.1f}%")
        d4.metric("Accounts", f"{div_accts}")

        st.divider()

        deep_col1, deep_col2 = st.columns(2)

        with deep_col1:
            st.markdown("**Monthly Trajectory**")
            div_monthly = div_df.groupby("Month").agg(
                Sales=("Shipped_Sales", "sum"),
                Margin=("Margin_Dollars", "sum")
            ).reset_index()
            div_monthly["Margin_Pct"] = div_monthly.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)

            fig4 = go.Figure()
            fig4.add_trace(go.Scatter(x=div_monthly["Month"], y=div_monthly["Sales"], mode="lines+markers", name="Sales", line=dict(color="#ca8a04", width=3), marker=dict(size=8)))
            fig4.update_layout(
                yaxis=dict(tickformat="$,.0f"),
                xaxis=dict(title="Month", dtick=1),
                height=300, margin=dict(l=50, r=30, t=20, b=30),
                plot_bgcolor="#fff", paper_bgcolor="#fff"
            )
            st.plotly_chart(fig4, use_container_width=True)

        with deep_col2:
            st.markdown("**Account Margin Distribution**")
            div_acct = div_df.groupby("Account").agg(
                Sales=("Shipped_Sales", "sum"),
                Margin_Pct=("Margin_Pct", "mean")
            ).reset_index()
            div_acct = div_acct[div_acct["Sales"] > 0].sort_values("Sales", ascending=False)

            fig5 = px.bar(
                div_acct.head(15), x="Margin_Pct", y="Account", orientation="h",
                color="Margin_Pct",
                color_continuous_scale=["#dc2626", "#f59e0b", "#16a34a"],
                labels={"Margin_Pct": "Margin %"},
                height=300
            )
            fig5.update_layout(
                showlegend=False,
                xaxis=dict(title="Margin %"),
                yaxis=dict(title=""),
                margin=dict(l=120, r=30, t=20, b=30),
                plot_bgcolor="#fff", paper_bgcolor="#fff"
            )
            st.plotly_chart(fig5, use_container_width=True)

        # Top accounts table for this division
        st.markdown("**Top Accounts**")
        div_table = div_df.groupby("Account").agg(
            Sales=("Shipped_Sales", "sum"),
            Margin=("Margin_Dollars", "sum"),
            Units=("Units", "sum")
        ).reset_index()
        div_table["Margin_Pct"] = div_table.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)
        div_table = div_table[div_table["Sales"] > 0].sort_values("Sales", ascending=False)

        div_display = div_table.copy()
        div_display["Sales"] = div_display["Sales"].apply(lambda x: f"${x:,.0f}")
        div_display["Margin"] = div_display["Margin"].apply(lambda x: f"${x:,.0f}")
        div_display["Units"] = div_display["Units"].apply(lambda x: f"{x:,.0f}")
        div_display["Margin_Pct"] = div_display["Margin_Pct"].apply(lambda x: f"{x:.1f}%")
        div_display.columns = ["Account", "Sales", "Margin $", "Units", "Margin %"]

        st.dataframe(div_display, hide_index=True, use_container_width=True, height=300)

    # ─── DEMO 4: CUSTOMER CONCENTRATION ──────────────────────────────────
    with demo_tab4:
        st.markdown("### CUSTOMER CONCENTRATION RISK")
        st.markdown("*How dependent is the business on its top accounts? If your top 3 customers represent 60%+ of revenue, one lost contract changes everything.*")

        # Pareto / concentration analysis
        acct_total = df.groupby("Account").agg(
            Sales=("Shipped_Sales", "sum"),
            Margin=("Margin_Dollars", "sum")
        ).reset_index().sort_values("Sales", ascending=False)
        acct_total["Margin_Pct"] = acct_total.apply(lambda r: round(r["Margin"] / r["Sales"] * 100, 1) if r["Sales"] > 0 else 0, axis=1)
        acct_total["Cumulative_Sales"] = acct_total["Sales"].cumsum()
        acct_total["Cumulative_Pct"] = (acct_total["Cumulative_Sales"] / acct_total["Sales"].sum() * 100).round(1)
        acct_total["Rank"] = range(1, len(acct_total) + 1)

        # KPIs
        top3_pct = acct_total.head(3)["Sales"].sum() / acct_total["Sales"].sum() * 100
        top10_pct = acct_total.head(10)["Sales"].sum() / acct_total["Sales"].sum() * 100
        accounts_for_80 = acct_total[acct_total["Cumulative_Pct"] <= 80].shape[0] + 1

        c1, c2, c3 = st.columns(3)
        c1.metric("Top 3 Accounts", f"{top3_pct:.1f}% of Revenue")
        c2.metric("Top 10 Accounts", f"{top10_pct:.1f}% of Revenue")
        c3.metric("Accounts for 80% Revenue", f"{accounts_for_80}")

        st.divider()

        # Pareto chart
        fig_pareto = go.Figure()
        fig_pareto.add_trace(go.Bar(
            x=acct_total.head(20)["Account"],
            y=acct_total.head(20)["Sales"],
            name="Revenue",
            marker_color="#ca8a04",
            opacity=0.85
        ))
        fig_pareto.add_trace(go.Scatter(
            x=acct_total.head(20)["Account"],
            y=acct_total.head(20)["Cumulative_Pct"],
            name="Cumulative %",
            yaxis="y2",
            mode="lines+markers",
            line=dict(color="#0a0a0a", width=2.5),
            marker=dict(size=6)
        ))
        fig_pareto.add_hline(y=80, yref="y2", line_dash="dash", line_color="#dc2626", annotation_text="80% threshold")
        fig_pareto.update_layout(
            yaxis=dict(title="Revenue ($)", tickformat="$,.0f"),
            yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0, 105]),
            xaxis=dict(tickangle=45),
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
            height=400, margin=dict(l=60, r=60, t=40, b=120),
            plot_bgcolor="#fff", paper_bgcolor="#fff"
        )
        st.plotly_chart(fig_pareto, use_container_width=True)

        st.markdown("*This is the analysis that triggers a customer diversification discussion in a quarterly business review. If one account churns, what happens to the P&L?*")
        st.markdown("*I present this analysis quarterly to leadership. The actionable question it drives: which of our top 5 accounts has the weakest renewal position, and what is the contingency if we lose them?*")

        # Top 10 table with margin
        st.markdown("**Top 10 Accounts — Revenue & Margin**")
        top10_display = acct_total.head(10).copy()
        top10_display["Sales"] = top10_display["Sales"].apply(lambda x: f"${x:,.0f}")
        top10_display["Margin"] = top10_display["Margin"].apply(lambda x: f"${x:,.0f}")
        top10_display["Cumulative_Pct"] = top10_display["Cumulative_Pct"].apply(lambda x: f"{x:.1f}%")
        top10_display["Margin_Pct"] = top10_display["Margin_Pct"].apply(lambda x: f"{x:.1f}%")
        top10_display = top10_display[["Rank", "Account", "Sales", "Margin", "Margin_Pct", "Cumulative_Pct"]]
        top10_display.columns = ["#", "Account", "Sales", "Margin $", "Margin %", "Cumulative %"]
        st.dataframe(top10_display, hide_index=True, use_container_width=True)

    # ─── DEMO 5: MONTH-OVER-MONTH TREND ─────────────────────────────────
    with demo_tab5:
        st.markdown("### MONTH-OVER-MONTH ANALYSIS")
        st.markdown("*Trend analysis for early signal detection. I built this monitoring approach after a 3-month margin decline across two regions surfaced $3M in misallocated spend — the kind of pattern that only becomes visible with unified, consistent data.*")

        # Overall monthly trend with MoM change
        monthly_all = df.groupby("Month").agg(
            Sales=("Shipped_Sales", "sum"),
            COGS=("Shipped_COGS", "sum"),
            Margin=("Margin_Dollars", "sum"),
            Units=("Units", "sum"),
            Transactions=("Transactions", "sum")
        ).reset_index()
        monthly_all["Margin_Pct"] = (monthly_all["Margin"] / monthly_all["Sales"] * 100).round(1)
        monthly_all["Sales_MoM"] = monthly_all["Sales"].pct_change() * 100
        monthly_all["Margin_MoM"] = monthly_all["Margin_Pct"].diff()
        monthly_all["Avg_Order"] = (monthly_all["Sales"] / monthly_all["Transactions"]).round(0)

        # KPIs — latest month vs first month
        latest = monthly_all.iloc[-1]
        first = monthly_all.iloc[0]
        sales_change = ((latest["Sales"] - first["Sales"]) / first["Sales"] * 100)
        margin_change = latest["Margin_Pct"] - first["Margin_Pct"]

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Latest Month Sales", f"${latest['Sales']/1e6:.1f}M", f"{sales_change:+.1f}% vs M1")
        c2.metric("Latest Margin %", f"{latest['Margin_Pct']:.1f}%", f"{margin_change:+.1f}pp vs M1")
        c3.metric("Avg Order Value", f"${latest['Avg_Order']:,.0f}")
        c4.metric("Monthly Transactions", f"{latest['Transactions']:,.0f}")

        st.divider()

        # Dual chart: Sales bars + Margin % line + MoM % change
        trend_col1, trend_col2 = st.columns(2)

        with trend_col1:
            st.markdown("**Sales & Margin Trend**")
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Bar(x=monthly_all["Month"], y=monthly_all["Sales"], name="Sales", marker_color="#ca8a04", opacity=0.85))
            fig_trend.add_trace(go.Scatter(x=monthly_all["Month"], y=monthly_all["Margin_Pct"], name="Margin %", yaxis="y2", mode="lines+markers", line=dict(color="#0a0a0a", width=2.5), marker=dict(size=7)))
            fig_trend.update_layout(
                yaxis=dict(title="Sales ($)", tickformat="$,.0f"),
                yaxis2=dict(title="Margin %", overlaying="y", side="right", tickformat=".1f", range=[0, max(monthly_all["Margin_Pct"].max() * 1.3, 40)]),
                xaxis=dict(title="Month", dtick=1),
                legend=dict(orientation="h", yanchor="bottom", y=1.02),
                height=350, margin=dict(l=50, r=50, t=30, b=30),
                plot_bgcolor="#fff", paper_bgcolor="#fff"
            )
            st.plotly_chart(fig_trend, use_container_width=True)

        with trend_col2:
            st.markdown("**Month-over-Month Sales Change %**")
            colors = ["#16a34a" if v >= 0 else "#dc2626" for v in monthly_all["Sales_MoM"].fillna(0)]
            fig_mom = go.Figure()
            fig_mom.add_trace(go.Bar(
                x=monthly_all["Month"],
                y=monthly_all["Sales_MoM"].fillna(0),
                marker_color=colors
            ))
            fig_mom.add_hline(y=0, line_color="#a3a3a3", line_width=1)
            fig_mom.update_layout(
                yaxis=dict(title="MoM Change %", tickformat=".1f"),
                xaxis=dict(title="Month", dtick=1),
                height=350, margin=dict(l=50, r=30, t=30, b=30),
                plot_bgcolor="#fff", paper_bgcolor="#fff"
            )
            st.plotly_chart(fig_mom, use_container_width=True)

        # Monthly detail table
        st.markdown("**Monthly Detail**")
        monthly_display = monthly_all.copy()
        monthly_display["Sales"] = monthly_display["Sales"].apply(lambda x: f"${x:,.0f}")
        monthly_display["COGS"] = monthly_display["COGS"].apply(lambda x: f"${x:,.0f}")
        monthly_display["Margin"] = monthly_display["Margin"].apply(lambda x: f"${x:,.0f}")
        monthly_display["Units"] = monthly_display["Units"].apply(lambda x: f"{x:,.0f}")
        monthly_display["Margin_Pct"] = monthly_display["Margin_Pct"].apply(lambda x: f"{x:.1f}%")
        monthly_display["Sales_MoM"] = monthly_display["Sales_MoM"].apply(lambda x: f"{x:+.1f}%" if pd.notna(x) else "—")
        monthly_display["Avg_Order"] = monthly_display["Avg_Order"].apply(lambda x: f"${x:,.0f}")
        monthly_display = monthly_display[["Month", "Sales", "COGS", "Margin", "Margin_Pct", "Units", "Sales_MoM", "Avg_Order"]]
        monthly_display.columns = ["Month", "Sales", "COGS", "Margin $", "Margin %", "Units", "MoM %", "Avg Order"]
        st.dataframe(monthly_display, hide_index=True, use_container_width=True)

    # ─── DEMO 6: MULTIVARIATE TESTING ──────────────────────────────────
    with demo_tab6:
        st.markdown("### MULTIVARIATE TEST DESIGN & RESULTS")
        st.markdown("*At Modern Home Station, I designed a 12-group multivariate test (3 creatives × 2 CTAs × 2 interaction types) to optimize ad performance. This interactive demo shows the test matrix and simulated results based on the actual patterns we observed.*")

        st.divider()

        # MVT test matrix
        st.markdown("**Test Matrix: 3 × 2 × 2 = 12 Groups**")
        import numpy as np
        np.random.seed(42)

        creatives = ["Meme A — Lifestyle", "Meme B — Instructional", "Meme C — Testimonial"]
        ctas = ["Shop Now", "Learn More"]
        interactions = ["Like/React", "Comment Prompt"]

        mvt_data = []
        # Based on actual MHS patterns: Meme B + Learn More + Comment was winner
        base_ctr = {"Meme A — Lifestyle": 2.0, "Meme B — Instructional": 2.6, "Meme C — Testimonial": 1.8}
        cta_mult = {"Shop Now": 1.0, "Learn More": 1.15}
        interact_mult = {"Like/React": 1.0, "Comment Prompt": 1.10}

        for cr in creatives:
            for ct in ctas:
                for inter in interactions:
                    ctr = base_ctr[cr] * cta_mult[ct] * interact_mult[inter] * (1 + np.random.normal(0, 0.05))
                    cpm = 7.80 / (ctr / 2.1) * (1 + np.random.normal(0, 0.08))
                    conv = 3.8 * (ctr / 2.1) * (1 + np.random.normal(0, 0.06))
                    engage = 5.1 * (ctr / 2.1) * interact_mult[inter] * (1 + np.random.normal(0, 0.07))
                    mvt_data.append({
                        "Creative": cr,
                        "CTA": ct,
                        "Interaction": inter,
                        "CTR %": round(ctr, 2),
                        "CPM ($)": round(cpm, 2),
                        "Conv %": round(conv, 2),
                        "Engage %": round(engage, 2)
                    })

        mvt_df = pd.DataFrame(mvt_data)
        mvt_df["Group"] = range(1, 13)
        mvt_df["Performance Score"] = ((mvt_df["CTR %"] / mvt_df["CTR %"].max()) * 0.3 +
                                        (1 - mvt_df["CPM ($)"] / mvt_df["CPM ($)"].max()) * 0.3 +
                                        (mvt_df["Conv %"] / mvt_df["Conv %"].max()) * 0.4).round(3)

        # Filters
        f1, f2 = st.columns(2)
        with f1:
            selected_creative = st.multiselect("Filter by Creative", creatives, default=creatives, key="mvt_cr")
        with f2:
            sort_by = st.selectbox("Sort by", ["Performance Score", "CTR %", "CPM ($)", "Conv %", "Engage %"], key="mvt_sort")

        filtered_mvt = mvt_df[mvt_df["Creative"].isin(selected_creative)].sort_values(sort_by, ascending=(sort_by == "CPM ($)"))

        # Winner highlight
        winner = mvt_df.sort_values("Performance Score", ascending=False).iloc[0]
        w1, w2, w3, w4 = st.columns(4)
        w1.metric("Winning Group", f"#{int(winner['Group'])}")
        w2.metric("Best CTR", f"{winner['CTR %']:.1f}%")
        w3.metric("Lowest CPM", f"${mvt_df['CPM ($)'].min():.2f}")
        w4.metric("Best Conv", f"{mvt_df['Conv %'].max():.1f}%")

        st.divider()

        # Heatmap: Creative × CTA with CTR as values
        mvt_col1, mvt_col2 = st.columns(2)

        with mvt_col1:
            st.markdown("**CTR by Creative × CTA**")
            ctr_pivot = mvt_df.groupby(["Creative", "CTA"])["CTR %"].mean().reset_index()
            ctr_matrix = ctr_pivot.pivot(index="Creative", columns="CTA", values="CTR %")

            fig_mvt1 = go.Figure(data=go.Heatmap(
                z=ctr_matrix.values,
                x=ctr_matrix.columns.tolist(),
                y=ctr_matrix.index.tolist(),
                colorscale="Greens",
                text=ctr_matrix.values.round(2),
                texttemplate="%{text}%",
                showscale=True,
                colorbar=dict(title="CTR %")
            ))
            fig_mvt1.update_layout(height=250, margin=dict(l=150, r=30, t=20, b=40), plot_bgcolor="#fff", paper_bgcolor="#fff")
            st.plotly_chart(fig_mvt1, use_container_width=True)

        with mvt_col2:
            st.markdown("**CPM by Creative × Interaction**")
            cpm_pivot = mvt_df.groupby(["Creative", "Interaction"])["CPM ($)"].mean().reset_index()
            cpm_matrix = cpm_pivot.pivot(index="Creative", columns="Interaction", values="CPM ($)")

            fig_mvt2 = go.Figure(data=go.Heatmap(
                z=cpm_matrix.values,
                x=cpm_matrix.columns.tolist(),
                y=cpm_matrix.index.tolist(),
                colorscale="Reds_r",
                text=cpm_matrix.values.round(2),
                texttemplate="$%{text}",
                showscale=True,
                colorbar=dict(title="CPM ($)")
            ))
            fig_mvt2.update_layout(height=250, margin=dict(l=150, r=30, t=20, b=40), plot_bgcolor="#fff", paper_bgcolor="#fff")
            st.plotly_chart(fig_mvt2, use_container_width=True)

        # Full results table
        st.markdown("**All 12 Groups — Full Results**")
        display_mvt = filtered_mvt[["Group", "Creative", "CTA", "Interaction", "CTR %", "CPM ($)", "Conv %", "Engage %", "Performance Score"]].copy()
        st.dataframe(display_mvt, hide_index=True, use_container_width=True, height=350)

        st.markdown(f"**Winner: Group #{int(winner['Group'])}** — {winner['Creative']} + {winner['CTA']} + {winner['Interaction']}")
        st.markdown("*The winning combination (instructional creative + Learn More CTA + comment prompt) achieved the highest CTR at the lowest CPM — confirming that engagement-driven strategies outperform direct-response approaches for this product category. This finding informed all subsequent campaign launches through FY21.*")

    st.divider()
    st.caption("All data anonymized. Account and division names replaced for confidentiality. Underlying data is real operational data from Advantage Solutions.")
    st.markdown("**Ready to talk?** Navigate to **Connect** or reach me at [linkedin.com/in/jchang0102](https://linkedin.com/in/jchang0102).")


# =============================================================================
# CONNECT
# =============================================================================
def render_connect():
    scroll_to_top()
    dark_section("""
        <h2 style="font-size:44px;letter-spacing:4px;margin:0 0 12px">LET'S TALK</h2>
        <p style="font-size:16px">Open to Senior BI & Analytics Manager roles. Best reached via LinkedIn.</p>
    """)

    st.markdown("I'm looking for organizations where the right analytical framework, data platform, and team mentorship can turn fragmented data into confident decisions. I have built trusted platforms and developed analytics capabilities at four organizations — a $1.68B enterprise, a DTC startup, a B2B telecom company, and a consumer electronics manufacturer. The methodology scales regardless of industry.")

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
        ("How do you handle metric disagreements between VPs?", "Bring the source data into the room, not the dashboards. Most disagreements dissolve when everyone is looking at the same raw numbers. Define the metric first, then build the visualization."),
        ("What's the hardest part of post-merger data work?", "Not the schemas — the politics of whose numbers go down when you standardize."),
        ("How do you know a dashboard is successful?", "When stakeholders stop requesting ad hoc reports and start discovering insights on their own. Self-service is the goal — 80% of analytical questions answered without escalation."),
        ("How do you build trust with non-technical stakeholders?", "I start with the decision, not the data. Once stakeholders articulate the decision they need to make, the data requirements become clear.")
    ]
    for q, a in faq:
        st.markdown(f"**{q}**")
        st.markdown(f"*{a}*")
        st.write("")

    st.divider()

    # Direction 29: Trimmed Brenton quote
    st.markdown("## LEADERSHIP TESTIMONIAL")
    st.markdown("> *\"He is someone our team relied on for all key performance metrics in a very demanding and often changing environment. His out of the box thinking provided solutions that others simply would not conceive.\"*")
    st.markdown("**Brenton Harlow** — Executive Leader, CPG Sales, Marketing, Operations & Technology — Direct Manager at Advantage Solutions")

    st.divider()

    st.markdown("*This portfolio was built with Python, Streamlit, Plotly, and Pandas — deployed on Streamlit Cloud with anonymized real data.*")
    st.markdown('<a href="https://github.com/jasonchang0102/Streamlit0102/tree/main/code_samples" target="_blank">View code samples on GitHub →</a>', unsafe_allow_html=True)


main()
