import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")


# =====================================================
# GLOBAL STYLING
# =====================================================
def set_background_color_and_right_space():
    st.markdown("""
        <style>
        body {
            background-color: #F2F9FF !important;
        }
        .reportview-container .main {
            background-color: #F2F9FF !important;
        }
        .reportview-container .main .block-container{
            padding-right: 16.666% !important;
        }
        </style>
    """, unsafe_allow_html=True)


set_background_color_and_right_space()


st.markdown("""
<link href='https://fonts.googleapis.com/css?family=Bebas+Neue|Lato&display=swap' rel='stylesheet'>
<style>
.big-font { font-family:'Bebas Neue'; font-size:94px !important; color:#3e4047; margin-top:-40px;}
.big2-font { font-family:'Bebas Neue'; font-size:60px !important; color:#3e4047; margin-top:20px;}
.med2-font { font-family:'Bebas Neue'; font-size:26px !important; color:#D09E55;}
.medium-font { font-family:'Bebas Neue'; font-size:38px !important; color:#D09E55;}
.small-font { font-family:'Lato'; font-size:30px !important; color:#282D33;}
.streamlit-container p, li { font-family:'Lato' !important; font-size:30px !important; color:#282D33;}
.sidebar .sidebar-content { background-color:#1D262F; color:white; }
</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)

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
# ✅ NEW STREAMLIT CACHE (NO WARNING)
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


data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)


# =====================================================
# PAGES
# =====================================================

# -------------------------
# WELCOME
# -------------------------
if page == "WELCOME":

    st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
    st.markdown('<p class="big2-font">PORTFOLIO</p><hr>', unsafe_allow_html=True)
    st.markdown('<p class="med2-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)

    st.markdown("""
    As a Senior Data Analyst focused on analytics strategy, data engineering, and monetization,
    I convert complex datasets into measurable business outcomes and scalable systems.
    """)


# -------------------------
# DATA ANALYTICS
# -------------------------
elif page == "DATA ANALYTICS / ENGAGEMENT & MONETIZATION":

    st.header("DATA ANALYTICS / ENGAGEMENT & MONETIZATION")

    heatmap_data = (
        data.groupby(["region", "platform"])["dollars_spent"]
        .mean()
        .unstack()
    )

    fig1 = plt.figure(figsize=(7, 5))
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f")
    st.pyplot(fig1)

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


# -------------------------
# OTHER PAGES
# -------------------------
elif page == "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS":
    st.header("DASHBOARD / EXECUTIVE BUSINESS INSIGHTS")
    st.write("Executive reporting + Power BI + schema redesign.")


elif page == "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION":
    st.header("WAREHOUSE & GL ACCOUNT OPTIMIZATION")
    st.write("Cost analysis + process improvement + savings.")


elif page == "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT":
    st.header("PROCESS AUTOMATION")
    st.write("Python + VBA automation reduced 1 month → 2 hours.")


elif page == "SCOPE OF SKILLS":
    st.header("SKILLS")
    st.write("Python • SQL • Snowflake • Power BI • ETL • Modeling • Analytics Strategy")


elif page == "CERTIFICATIONS":
    st.header("CERTIFICATIONS")
    st.write("ML • Deep Learning • Power BI • AWS • SQL")


elif page == "LET'S CONNECT":
    st.header("LET'S CONNECT")
    st.write("LinkedIn: linkedin.com/in/jchang0102")
