import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG (runs instantly)
# =====================================================
st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")


# =====================================================
# GLOBAL STYLE (lightweight only)
# =====================================================
st.markdown("""
<link href='https://fonts.googleapis.com/css?family=Bebas+Neue|Lato&display=swap' rel='stylesheet'>
<style>
body {background-color:#F2F9FF;}
.big-font {font-family:'Bebas Neue'; font-size:94px; color:#3e4047;}
.big2-font {font-family:'Bebas Neue'; font-size:60px; color:#3e4047;}
.med2-font {font-family:'Bebas Neue'; font-size:26px; color:#D09E55;}
.sidebar .sidebar-content {background:#1D262F; color:white;}
</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown("### Navigation")
    page = st.radio("", [
        "WELCOME",
        "DATA ANALYTICS / ENGAGEMENT & MONETIZATION",
        "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS",
        "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION",
        "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT",
        "SCOPE OF SKILLS",
        "CERTIFICATIONS",
        "LET'S CONNECT"
    ])


# =====================================================
# ✅ MODERN CACHE (NO WARNING)
# Only used when needed
# =====================================================
@st.cache_data(show_spinner=False)
def load_data(url: str):
    df = pd.read_csv(url)
    df["Date"] = pd.to_datetime(df["Date"])

    def bucket(x):
        if 1 <= x <= 3:
            return "Very Low"
        elif 4 <= x <= 5:
            return "Low"
        elif 6 <= x <= 9:
            return "Medium"
        elif 10 <= x <= 68:
            return "High"
        return "Unknown"

    df["games_played_bucket"] = df["games_played"].apply(bucket)
    return df


DATA_URL = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"


# =====================================================
# PAGES
# =====================================================

# -----------------------------------------------------
# WELCOME (instant load, no data)
# -----------------------------------------------------
if page == "WELCOME":

    st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
    st.markdown('<p class="big2-font">PORTFOLIO</p>', unsafe_allow_html=True)
    st.markdown('<p class="med2-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)

    st.write("""
    Senior Data Analyst specializing in analytics strategy, data engineering,
    automation, and revenue optimization.
    """)


# -----------------------------------------------------
# DATA ANALYTICS (lazy loads data ONLY here)
# -----------------------------------------------------
elif page == "DATA ANALYTICS / ENGAGEMENT & MONETIZATION":

    st.header("DATA ANALYTICS / ENGAGEMENT & MONETIZATION")

    # ✅ load only when this page is opened
    data = load_data(DATA_URL)

    heatmap_data = (
        data.groupby(["region", "platform"])["dollars_spent"]
        .mean()
        .unstack()
    )

    fig1 = plt.figure(figsize=(7, 5))
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f")
    st.pyplot(fig1)
    plt.close(fig1)

    event_1 = data[(data["Date"] >= "2017-01-24") & (data["Date"] <= "2017-02-14")]
    event_2 = data[(data["Date"] >= "2017-02-28") & (data["Date"] <= "2017-03-21")]

    fig, axes = plt.subplots(2, 2, figsize=(8, 6))

    sns.kdeplot(event_1["games_played"], fill=True, ax=axes[0, 0])
    sns.kdeplot(event_2["games_played"], fill=True, ax=axes[0, 0])

    sns.kdeplot(event_1["skill_last"], fill=True, ax=axes[0, 1])
    sns.kdeplot(event_2["skill_last"], fill=True, ax=axes[0, 1])

    sns.kdeplot(event_1["items_crafted"], fill=True, ax=axes[1, 0])
    sns.kdeplot(event_2["items_crafted"], fill=True, ax=axes[1, 0])

    sns.kdeplot(event_1["dollars_spent"], fill=True, ax=axes[1, 1])
    sns.kdeplot(event_2["dollars_spent"], fill=True, ax=axes[1, 1])

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# -----------------------------------------------------
# LIGHTWEIGHT TEXT PAGES (fast)
# -----------------------------------------------------
elif page == "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS":
    st.header("DASHBOARD / EXECUTIVE BUSINESS INSIGHTS")
    st.write("Executive dashboards, Snowflake modeling, Power BI reporting.")


elif page == "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION":
    st.header("WAREHOUSE & GL ACCOUNT OPTIMIZATION")
    st.write("Cost analysis, process improvement, logistics optimization.")


elif page == "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT":
    st.header("PROCESS AUTOMATION")
    st.write("Python + VBA automation reduced 1 month → 2 hours.")


elif page == "SCOPE OF SKILLS":
    st.header("SKILLS")
    st.write("Python • SQL • Snowflake • Power BI • ETL • Analytics Strategy")


elif page == "CERTIFICATIONS":
    st.header("CERTIFICATIONS")
    st.write("Machine Learning • Deep Learning • Power BI • AWS • SQL")


elif page == "LET'S CONNECT":
    st.header("LET'S CONNECT")
    st.write("linkedin.com/in/jchang0102")
