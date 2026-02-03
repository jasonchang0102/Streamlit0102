"""
Jason C. Chang | BI Manager Portfolio
=====================================
Built WITH Streamlit's native components, not against them.
"""

import streamlit as st

# =============================================================================
# PAGE CONFIG
# =============================================================================

st.set_page_config(
    page_title="Jason C. Chang | BI Manager",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# MINIMAL CSS
# =============================================================================

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# CONFIG
# =============================================================================

NAME = "Jason C. Chang"
TITLE = "BI Manager"
TAGLINE = "I help executives stop arguing about numbers and start making decisions."
EMAIL = "jason.chang01022024@gmail.com"
PHONE = "(626) 203-3319"
LINKEDIN = "linkedin.com/in/jchang0102"
LOCATION = "Hacienda Heights, CA"

# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.subheader(NAME)
    st.caption(TITLE)
    st.success("🟢 Open to Opportunities")
    
    st.divider()
    
    page = st.radio(
        "Navigation",
        ["Home", "Work", "About", "Connect"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.download_button(
        label="📄 Download Resume",
        data="Resume placeholder",
        file_name="Jason_Chang_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# =============================================================================
# HOME PAGE
# =============================================================================

if page == "Home":
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.caption(f"{TITLE} · 10+ YEARS · ADVANTAGE SOLUTIONS")
        st.title("I turn data chaos into executive clarity")
        st.write(TAGLINE)
        st.write("**Core Skills:** `SQL` `Python` `Power BI` `Snowflake` `DAX`")
    
    with col2:
        st.image("https://via.placeholder.com/200x200?text=Photo", caption="Add your photo")
    
    st.divider()
    
    st.subheader("Impact at a Glance")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Years in BI", "10+")
    c2.metric("Revenue Impact", "$15M+")
    c3.metric("Users Enabled", "250+")
    c4.metric("Faster Decisions", "70%")
    
    st.divider()
    
    st.subheader("🏆 Flagship Project")
    st.markdown("### Unified 5 Conflicting Data Sources Into a Single Source of Truth")
    st.caption("Advantage Solutions · 6 weeks · $12M annual impact · 250 users")
    st.write("""
    After the merger, I found 5 sales systems that didn't talk to each other. 
    Each region defined "revenue" differently. The CFO was getting 5 different 
    numbers in every board meeting. I had 6 weeks to fix it.
    """)
    
    r1, r2, r3, r4 = st.columns(4)
    r1.metric("Revenue Lift", "9%")
    r2.metric("Fewer Conflicts", "70%")
    r3.metric("Decision Cycle", "5→1 days")
    r4.metric("Annual Impact", "$12M")
    
    st.divider()
    
    st.subheader("More Work")
    proj1, proj2 = st.columns(2)
    
    with proj1:
        with st.container(border=True):
            st.caption("MODERN HOME STATION")
            st.write("**+33% Conversion via A/B Testing**")
            st.caption("8 weeks · Cross-channel attribution")
            st.write("Built cross-channel attribution across GA4, Shopify, Meta.")
            m1, m2, m3 = st.columns(3)
            m1.metric("Conversion", "+33%")
            m2.metric("CPA", "-18%")
            m3.metric("ROAS", "2x")
    
    with proj2:
        with st.container(border=True):
            st.caption("OPERATIONS AUTOMATION")
            st.write("**160 Hours Saved Quarterly**")
            st.caption("4 weeks · 99 vendor sources")
            st.write("Replaced 47 Excel macros with Python pipelines.")
            m1, m2, m3 = st.columns(3)
            m1.metric("Saved/Qtr", "160 hrs")
            m2.metric("Error Rate", "0%")
            m3.metric("Vendors", "99")

# =============================================================================
# WORK PAGE
# =============================================================================

elif page == "Work":
    
    st.title("Selected Work")
    st.caption("Deep dives into problems I've solved — the mess, the struggle, what I learned")
    
    st.divider()
    
    # Case Study 1
    st.subheader("🏆 Unified Executive Intelligence")
    st.caption("Advantage Solutions · 6 weeks · $12M impact · 250 users")
    
    r1, r2, r3 = st.columns(3)
    r1.metric("Quarterly Revenue Lift", "9%")
    r2.metric("Fewer KPI Conflicts", "70%")
    r3.metric("Decision Cycle", "5→1 days")
    
    with st.expander("THE MESS — What I inherited", expanded=True):
        st.write("""
        After the merger, I inherited 5 sales systems that didn't talk to each other. 
        Each region defined "revenue" differently — APAC included returns, EMEA didn't. 
        The CFO was getting 5 different numbers in every board meeting.
        """)
        st.write("- CFO getting 5 different revenue numbers at every board meeting")
        st.write("- Field teams created 47 shadow Excel trackers")
        st.write("- Previous BI lead quit mid-project")
        st.write("- Snowflake instance already over capacity")
    
    with st.expander("WHY THIS WAS HARD — The constraint"):
        st.write("""
        This wasn't a technical problem — it was political. Each regional VP had built 
        metrics to make their team look good. Standardizing meant someone's numbers would go down.
        """)
    
    with st.expander("MY APPROACH — Week by week"):
        st.write("**Week 1-2:** Discovery. Asked every stakeholder: What decision are you trying to make? Found 70% of must-have metrics weren't actually used.")
        st.write("**Week 3:** Forced alignment meeting. Locked 5 VPs in a room until we agreed on 12 golden metrics.")
        st.write("**Week 4-5:** Built unified Snowflake schema. Wrote 40+ DAX measures.")
        st.write("**Week 6:** Trained 250 users. Killed old reports. No going back.")
    
    with st.expander("WHAT WENT WRONG — And how I adapted"):
        st.write("""
        APAC had an undocumented custom field that their entire commission structure depended on. 
        Their numbers broke Day 1 of launch. I had to patch the data model live while the regional 
        VP was on a CEO call explaining the discrepancy.
        """)
        st.write("**Lesson:** Undocumented doesn't mean unimportant. I now mandate field audits before any migration.")
    
    st.info("💬 \"For the first time in two years, I walked into a board meeting with confidence in our numbers.\" — CFO")
    
    st.divider()
    
    # Case Study 2
    st.subheader("+33% Conversion Through A/B Testing")
    st.caption("Modern Home Station · 8 weeks · Cross-Channel Analytics")
    
    r1, r2, r3 = st.columns(3)
    r1.metric("Conversion Rate", "+33%")
    r2.metric("CPA Reduction", "-18%")
    r3.metric("ROAS", "2x")
    
    with st.expander("THE MESS"):
        st.write("""
        Marketing was sending the same promotion to everyone. Data scattered across 
        Facebook, Shopify, Google Analytics — no unified customer view. Attribution 
        meant whoever yelled loudest got credit.
        """)
    
    with st.expander("MY APPROACH"):
        st.write("""
        Built cross-channel attribution integrating GA4, Shopify, Meta, Klaviyo. 
        Applied K-Means segmentation to identify 4 distinct customer personas. 
        Led multivariate testing across 12 ad combinations.
        """)
    
    with st.expander("WHAT WENT WRONG"):
        st.write("""
        Saw spike in content views but no page views. Spent days debugging — 
        mobile video sound settings were wrong, causing users to scroll past. 
        The data was right; my interpretation was wrong.
        """)
    
    st.divider()
    
    # Case Study 3
    st.subheader("160 Hours Saved via Automation")
    st.caption("99 Vendor Data Sources · 4 weeks · Python + SQL")
    
    r1, r2, r3 = st.columns(3)
    r1.metric("Saved Quarterly", "160 hrs")
    r2.metric("Error Rate", "15% → 0%")
    r3.metric("Vendors", "99")
    
    with st.expander("THE MESS"):
        st.write("""
        Automation meant 47 Excel macros that one person (who left) understood. 
        Every Monday, 3 analysts spent 4 hours manually processing vendor reports. 
        Error rate: 15%. Finance didn't trust any of it.
        """)
    
    with st.expander("MY APPROACH"):
        st.write("""
        Built dynamic column mapping in Python — no more breaking when vendors changed formats. 
        Created normalization buckets aligned with GL codes. Combined Python + VBA for hybrid 
        automation (some vendors only sent Excel files via email).
        """)
    
    with st.expander("WHAT WENT WRONG"):
        st.write("""
        One vendor only sent PDF reports with inconsistent formatting — spent 2 days building 
        a custom parser. Three vendors reported in different timezones — took a week to standardize.
        """)
    
    st.info("💬 \"Finance finally trusts the automated reports. That hasn't happened in years.\" — VP of Finance")

# =============================================================================
# ABOUT PAGE
# =============================================================================

elif page == "About":
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("https://via.placeholder.com/200x200?text=Photo", caption="Add your photo")
    
    with col2:
        st.title("Hi, I'm Jason.")
        st.write("""
        I've spent the last decade helping companies **stop guessing and start knowing**.
        
        Most BI teams build dashboards. I build clarity — the kind where a CEO can walk 
        into a board meeting and actually trust the numbers.
        
        **What I've learned:** The hard part is never the SQL. It's getting humans to agree on what "revenue" means.
        """)
    
    st.divider()
    
    st.subheader("Experience")
    
    st.write("**BI Manager** · Advantage Solutions · 2021 – Present")
    st.caption("Built national Power BI ecosystem with Snowflake. Unified 5 sales domains. Automated 99+ vendor pipelines.")
    
    st.write("**BI Strategy & Analytics Manager** · Modern Home Station · 2017 – 2021")
    st.caption("Cross-channel attribution (GA4, Shopify, Meta). A/B testing program. Revenue: +45% FY19, +85% FY20.")
    
    st.write("**BI & Strategic Development Manager** · China Unicom America · 2016 – 2017")
    st.caption("GTM pricing models. $2M+ revenue projections. Automated churn reporting.")
    
    st.write("**BI Project Analyst** · Marshall Electronics · 2014 – 2016")
    st.caption("50+ product launches, $5M annual sales. 95% on-time rate.")
    
    st.write("**Senior Business Analyst** · Cadence Acoustic Ltd. · 2010 – 2014")
    st.caption("Migrated Excel to SQL dashboards. Managed $500M product lines.")
    
    st.divider()
    
    st.subheader("Education")
    st.write("**B.S. Business Administration** · University of California, Riverside · 2010")
    
    st.divider()
    
    st.subheader("Skills")
    s1, s2, s3 = st.columns(3)
    
    with s1:
        st.write("**Daily Drivers**")
        st.write("SQL (10+ years)")
        st.write("Power BI / DAX")
        st.write("Python")
        st.write("Snowflake")
        st.write("Excel + VBA")
    
    with s2:
        st.write("**Fluent**")
        st.write("BigQuery")
        st.write("GA4")
        st.write("Looker")
        st.write("Qlik")
        st.write("Power Query")
    
    with s3:
        st.write("**Statistical**")
        st.write("A/B Testing")
        st.write("Regression")
        st.write("K-Means")
        st.write("Cohort Analysis")
        st.write("Forecasting")
    
    st.divider()
    
    st.subheader("Certifications")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.write("**Supervised Machine Learning**")
        st.caption("Stanford Online · 2024")
    
    with c2:
        st.write("**Neural Networks & Deep Learning**")
        st.caption("DeepLearning.AI · 2024")
    
    with c3:
        st.write("**Power BI Data Visualization**")
        st.caption("edX · 2019")

# =============================================================================
# CONNECT PAGE
# =============================================================================

elif page == "Connect":
    
    st.title("Let's Talk")
    st.write("I'm open to Senior BI Manager and Analytics Lead roles. Best way to reach me is email.")
    
    st.divider()
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.write("**📧 Email**")
        st.write(EMAIL)
    
    with c2:
        st.write("**💼 LinkedIn**")
        st.write(LINKEDIN)
    
    with c3:
        st.write("**📱 Phone**")
        st.write(PHONE)
    
    with c4:
        st.write("**📍 Location**")
        st.write(LOCATION)
    
    st.divider()
    
    st.subheader("What Colleagues Say")
    
    t1, t2 = st.columns(2)
    
    with t1:
        with st.container(border=True):
            st.write("*\"For the first time in two years, I walked into a board meeting with confidence in our numbers. Jason didn't just fix our data — he changed how we think about measurement.\"*")
            st.write("**[Name]** · CFO, Advantage Solutions")
        
        with st.container(border=True):
            st.write("*\"Most analysts give you data. Jason gives you decisions. He made our CEO actually look forward to reviewing dashboards.\"*")
            st.write("**[Name]** · Director of Operations")
    
    with t2:
        with st.container(border=True):
            st.write("*\"Jason has a rare ability to translate complex data into stories that executives actually act on. He doesn't just answer questions — he asks better ones.\"*")
            st.write("**[Name]** · VP of Sales")
        
        with st.container(border=True):
            st.write("*\"Finance finally trusts the automated reports. That hasn't happened in years.\"*")
            st.write("**[Name]** · VP of Finance")
