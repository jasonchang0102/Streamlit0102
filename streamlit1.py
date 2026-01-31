import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# Set the page configuration
st.set_page_config(layout="wide", page_title="Jason Chang | Analytics Leader", page_icon="📈")

# Scroll to top function
def scroll_to_top():
    components.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )

# Professional CSS styling
st.markdown("""
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lexend:wght@400;500;600;700&display=swap' rel='stylesheet'>
    <style>
        /* Main background & Global Font */
        .stApp {
            background: #0f172a;
            font-family: 'Inter', sans-serif;
        }
        
        /* Typography Scale */
        .hero-name {
            font-family: 'Lexend', sans-serif;
            font-size: 52px;
            font-weight: 700;
            color: #f8fafc;
            letter-spacing: -1px;
            margin-bottom: 0;
            line-height: 1;
        }
        
        .hero-title {
            font-family: 'Lexend', sans-serif;
            font-size: 20px;
            font-weight: 400;
            color: #3b82f6;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-top: 8px;
        }

        .section-header {
            font-family: 'Lexend', sans-serif;
            font-size: 32px;
            font-weight: 600;
            color: #f8fafc;
            margin-bottom: 24px;
            border-left: 5px solid #3b82f6;
            padding-left: 15px;
        }
        
        .subsection-header {
            font-family: 'Lexend', sans-serif;
            font-size: 14px;
            font-weight: 700;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-top: 30px;
            margin-bottom: 10px;
        }

        /* Component Cards */
        .info-card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 24px;
            transition: transform 0.2s ease;
        }
        .info-card:hover {
            border-color: #3b82f6;
        }

        .metric-value {
            font-family: 'Lexend', sans-serif;
            font-size: 36px;
            font-weight: 700;
            color: #3b82f6;
            line-height: 1;
        }
        
        .metric-label {
            font-size: 14px;
            color: #94a3b8;
            margin-top: 5px;
            font-weight: 500;
        }

        /* List Items */
        .bullet-point {
            display: flex;
            align-items: flex-start;
            margin-bottom: 12px;
            color: #cbd5e1;
            font-size: 15px;
            line-height: 1.6;
        }
        .bullet-point::before {
            content: "▹";
            color: #3b82f6;
            font-weight: bold;
            margin-right: 12px;
        }

        /* Navigation Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #020617 !important;
        }
        
        /* Hide Default Decorations */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<p style="color: #64748b; font-weight: 700; font-size: 12px; letter-spacing: 2px; margin-bottom: 20px;">NAVIGATION</p>', unsafe_allow_html=True)
    page = st.radio(
        "",
        [
            "Profile Summary",
            "Monetization Strategy",
            "BI & Data Governance",
            "Supply Chain Analytics",
            "Workflow Engineering",
            "Tech Stack",
            "Certifications",
            "Contact"
        ],
        label_visibility="collapsed"
    )

scroll_to_top()

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)

# ==================== PROFILE SUMMARY ====================
if page == "Profile Summary":
    st.markdown('<p class="hero-name">JASON CHANG</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">Strategic Analytics Leader</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style="color: #cbd5e1; font-size: 18px; line-height: 1.8; max-width: 850px;">
    Business Intelligence professional with 10+ years of experience leading national revenue growth and process optimization. 
    Expert in bridging the gap between <strong>complex data engineering (Snowflake, SQL)</strong> and <strong>executive decision-making (Power BI, Python)</strong>. 
    Proven track record in automating legacy systems to drive 85% efficiency gains and identifying multi-million dollar revenue opportunities.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    metrics = [
        ("10+", "Years of Experience"),
        ("85%", "Automation Efficiency"),
        ("21%", "Revenue Growth Impact")
    ]
    
    for col, (val, lab) in zip([col1, col2, col3], metrics):
        with col:
            st.markdown(f"""
            <div class="info-card" style="text-align: center;">
                <div class="metric-value">{val}</div>
                <div class="metric-label">{lab}</div>
            </div>
            """, unsafe_allow_html=True)

# ==================== MONETIZATION STRATEGY ====================
elif page == "Monetization Strategy":
    st.markdown('<p class="section-header">Player Engagement & Monetization</p>', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 1.2])
    with col_a:
        st.markdown('<p class="subsection-header">Situation & Objective</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="bullet-point">Analyze player behavior across two major Warcraft in-game events.</div>
        <div class="bullet-point">Identify high-value segments for targeted monetization.</div>
        <div class="bullet-point">Address regional and platform-specific spending friction.</div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown('<p class="subsection-header">Technical Action</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="bullet-point"><strong>Clustering:</strong> Applied K-Means to segment users by engagement depth.</div>
        <div class="bullet-point"><strong>EDA:</strong> Built Python-driven heatmaps to cross-reference region vs. spend.</div>
        <div class="bullet-point"><strong>Comparative Analysis:</strong> KDE density plots to track skill-level shifts between events.</div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Visualization Section
    heatmap_data = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    fig1.patch.set_facecolor('#0f172a')
    ax1.set_facecolor('#0f172a')
    sns.heatmap(heatmap_data, annot=True, cmap="Blues", fmt=".2f", ax=ax1, cbar_kws={'label': 'Avg Spend'})
    ax1.set_title("Revenue Concentration: Region vs Platform", color='white', pad=20)
    ax1.tick_params(colors='white')
    st.pyplot(fig1)

    st.markdown('<p class="subsection-header">Business Impact</p>', unsafe_allow_html=True)
    res1, res2 = st.columns(2)
    res1.success("**+21% Engagement:** Validated high-value segments for Q3 promotions.")
    res2.info("**-15% Churn Risk:** Identified underperforming regions for retention intervention.")

# ==================== BI & DATA GOVERNANCE ====================
elif page == "BI & Data Governance":
    st.markdown('<p class="section-header">Executive Dashboard & Data Infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <p style="color: #3b82f6; font-weight: 600; font-size: 18px; margin-bottom: 10px;">Post-Merger System Integration</p>
        <p style="color: #94a3b8; line-height: 1.6;">
        Developed a centralized reporting hub for Finance leadership to unify data from fragmented legacy systems. 
        Engineered a SQL-based ETL pipeline to ensure <strong>single-source-of-truth</strong> accuracy across corporate KPIs.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Architecture Components</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.code("EXTRACT\nSnowflake / SQL Server\nDeduplication Logic", language="sql")
    c2.code("TRANSFORM\nNormalization\nStar Schema Design", language="sql")
    c3.code("LOAD\nPower BI Dashboards\nAutomated Refreshes", language="sql")

# ==================== SUPPLY CHAIN ANALYTICS ====================
elif page == "Supply Chain Analytics":
    st.markdown('<p class="section-header">Warehouse & GL Cost Optimization</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Operational Audit</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="bullet-point">Audited 3PL Logistics and SKYLAB divisions to reduce escalating overhead.</div>
    <div class="bullet-point">Mapped General Ledger (GL) accounts to physical cost drivers.</div>
    <div class="bullet-point">Resulted in streamlined vendor contracts and optimized resource allocation.</div>
    """, unsafe_allow_html=True)

# ==================== WORKFLOW ENGINEERING ====================
elif page == "Workflow Engineering":
    st.markdown('<p class="section-header">Quarterly Royalty Automation</p>', unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 1])
    with col_left:
        st.markdown('<p class="subsection-header">The Problem</p>', unsafe_allow_html=True)
        st.error("1 Month / Quarter manual Excel lookups. High risk of human error.")
    
    with col_right:
        st.markdown('<p class="subsection-header">The Solution</p>', unsafe_allow_html=True)
        st.success("8 Hours / Quarter automated Python/VBA pipeline. 100% data integrity.")

    st.markdown("""
    <div class="info-card" style="margin-top: 20px;">
        <p style="color: #f8fafc; font-weight: 600;">Technical Stack:</p>
        <p style="color: #94a3b8;">Python (Pandas/Openpyxl) for data consolidation + VBA for dynamic report formatting.</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TECH STACK ====================
elif page == "Tech Stack":
    st.markdown('<p class="section-header">Technical Expertise</p>', unsafe_allow_html=True)
    
    categories = {
        "Data Engineering": "Snowflake, SQL (T-SQL/PostgreSQL), ETL Pipelines, SSMS, AS400",
        "Data Science": "Python, Pandas, NumPy, Scikit-learn, TensorFlow, Statistical Modeling",
        "Visualization": "Power BI, Looker Studio, Seaborn, Matplotlib, Streamlit",
        "Business Systems": "VBA, Excel Expert, Google Analytics, ERP Integration"
    }
    
    for cat, tools in categories.items():
        st.markdown(f"""
        <div class="info-card" style="margin-bottom: 15px;">
            <span style="color: #3b82f6; font-weight: 700; font-size: 16px;">{cat}:</span>
            <span style="color: #cbd5e1; margin-left: 10px;">{tools}</span>
        </div>
        """, unsafe_allow_html=True)

# ==================== CERTIFICATIONS ====================
elif page == "Certifications":
    st.markdown('<p class="section-header">Professional Development</p>', unsafe_allow_html=True)
    
    certs = [
        ("Machine Learning Specialization", "Stanford University / DeepLearning.AI"),
        ("AWS Cloud Practitioner", "Amazon Web Services"),
        ("Data Visualization Professional", "EdX / Microsoft"),
        ("Advanced SQL Certification", "Sololearn")
    ]
    
    for title, org in certs:
        st.markdown(f"""
        <div class="info-card" style="margin-bottom: 10px; padding: 15px;">
            <div style="color: #f8fafc; font-weight: 600;">{title}</div>
            <div style="color: #64748b; font-size: 13px;">{org}</div>
        </div>
        """, unsafe_allow_html=True)

# ==================== CONTACT ====================
elif page == "Contact":
    st.markdown('<p class="section-header">Contact & Inquiries</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card" style="max-width: 600px;">
        <p style="color: #94a3b8; font-size: 14px; text-transform: uppercase; margin-bottom: 20px;">Irvine, CA | Open to Relocation</p>
        <p style="font-size: 18px; color: #f8fafc; margin-bottom: 10px;">📧 jason.chang01022021@gmail.com</p>
        <p style="font-size: 18px; color: #f8fafc; margin-bottom: 10px;">📱 (626) 203-3319</p>
        <p style="font-size: 18px; color: #f8fafc;">🔗 <a href="https://linkedin.com/in/jchang0102" style="color: #3b82f6; text-decoration: none;">linkedin.com/in/jchang0102</a></p>
    </div>
    """, unsafe_allow_html=True)
