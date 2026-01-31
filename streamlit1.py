import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page configuration and title
st.set_page_config(layout="wide", page_title="Jason Chang's Portfolio")

# Function to apply custom CSS for background color and right-side space
def set_background_color_and_right_space():
    st.markdown("""
        <style>
            body { background-color: #F2F9FF !important; }
            .reportview-container .main { background-color: #F2F9FF !important; }
            /* Custom CSS for right-side empty space */
            .reportview-container .main .block-container{
                padding-right: 16.666% !important; /* Adjusts right padding to be about 1/6 of the page width */
            }
        </style>
    """, unsafe_allow_html=True)

set_background_color_and_right_space()

# Additional CSS for fonts and sidebar styling
st.markdown("""
    <link href='https://fonts.googleapis.com/css?family=Bebas+Neue|Lato&display=swap' rel='stylesheet'>
    <style>
        .big-font {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 94px !important;
            font-weight: 100;
            color: #3e4047;
            display: inline-block;
            margin: 0 auto;
            margin-top: -40px;
        }
        .big2-font {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 60px !important;
            font-weight: 100;
            color: #3e4047;
            display: inline-block;
            margin-bottom: 0px;
            margin-top: 20px;
        }
        .med2-font {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 26px !important;
            font-weight: 100;
            color: #D09E55;
            margin-top: -20px;
        }
        .medium-font {
            font-family: 'Bebas Neue', sans-serif;
            font-size: 38px !important;
            font-weight: 100;
            color: #D09E55;
        }
        .small-font {
            font-family: 'Lato', sans-serif;
            font-size: 30px !important;
            color: #282D33;
        }
        .streamlit-container .markdown-text-container,
        .streamlit-container .markdown-text-container p,
        .streamlit-container .markdown-text-container li {
            font-family: 'Lato', sans-serif !important;
            font-size: 30px !important;
            color: #282D33;
        }
        .sidebar .sidebar-content { background-color: #1D262F; color: white; }
        .fa { padding-right: 4px; }
        hr { border-top: 1px solid #FFFFFF; width: 95%; margin-left: 0;margin-top: 5px;}
    </style>
""", unsafe_allow_html=True)

# JavaScript for smooth scrolling in the sidebar navigation
st.markdown("""
    <script>
        const navButtons = document.querySelectorAll('.stRadio > div');
        navButtons.forEach(button => {
            button.addEventListener('click', () => {
                window.scrollTo(0, 0);
            });
        });
    </script>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="medium-font">Navigation</p>', unsafe_allow_html=True)
    page = st.radio("", ["WELCOME", "DATA ANALYTICS / ENGAGEMENT & MONETIZATION", "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS", "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION", "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT", "SCOPE OF SKILLS", "CERTIFICATIONS", "LET'S CONNECT"])

@st.cache_data
def load_data(url):
    # Function to load and preprocess data
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Assigning bucket based on games played
    def assign_correct_bucket(games_played):
        if games_played >= 1 and games_played <= 3:
            return 'Very Low'
        elif games_played >= 4 and games_played <= 5:
            return 'Low'
        elif games_played >= 6 and games_played <= 9:
            return 'Medium'
        elif games_played >= 10 and games_played <= 68:
            return 'High'
        else:
            return 'Unknown'
    
    data['games_played_bucket'] = data['games_played'].apply(assign_correct_bucket)
    return data

# URL to the CSV data
data_url = "https://raw.githubusercontent.com/jasonchang0102/Streamlit0102/main/RAWBliz.csv"
data = load_data(data_url)

if page == "WELCOME":
    # WELCOME page content
    st.markdown('<p class="big-font">JASON CHANG</p>', unsafe_allow_html=True)
    st.markdown('<div><p class="big2-font">PORTFOLIO</p><hr></div>', unsafe_allow_html=True)
    st.markdown('<p class="med2-font">Full Stack Senior Data Analyst</p>', unsafe_allow_html=True)
    st.markdown("### Welcome to My Portfolio")
    st.markdown("""
    As a Senior Data Analyst with a strong focus on integrating business strategy and transforming complex data into strategic assets, I have evolved from intricate statistical analysis to advanced predictive modeling. My expertise lies in turning vast datasets into actionable insights.

    Committed to pioneering data-driven research, I aim to lead innovative strategies in a dynamic corporate setting. My goal is to drive organizational success and innovation by leveraging data intelligence for business growth and collaborative leadership.
    """)

elif page == "DATA ANALYTICS / ENGAGEMENT & MONETIZATION":
    # Situation
    st.header("DATA ANALYTICS / ENGAGEMENT & MONETIZATION")
    st.subheader("Situation")
    st.write("""
    In an effort to maximize revenue and enhance player engagement and satisfaction in Warcraft, we identified the need to analyze player behavior and spending patterns during two key in-game events. The primary challenge was understanding how different segments of players interacted with these events and identifying opportunities to improve both engagement and monetization.
    """)

    # Task
    st.subheader("Task")
    st.write("""
    My task was to lead the data analytics process, focusing on:
    - Identifying high-spending player segments for targeted promotions.
    - Understanding low spending trends in specific regions and platforms for strategic adjustments.
    - Conducting exploratory data analysis to grasp player spending behaviors related to games played, skill levels, dollars spent, and items crafted.
    """)

    # Action
    st.subheader("Action")
    st.write("""
    **Data Exploration and Analysis:**
    - Conducted comprehensive exploratory data analysis to investigate player spending behavior, employing Python for data manipulation and analysis.
    - Utilized K-Means Clustering to segment players based on their in-game behavior, focusing on engagement metrics like games played, skill levels, and spending.
    - Performed heatmap analysis to identify patterns of player engagement and spending during the events, facilitating a comparative study between different segments.

    **Strategic Implementation:**
    - Identified high-spending segments in Platform 3, Region 1 as a priority for future promotions, based on their significant contribution to revenue.
    - Highlighted low spending in Platform 1, Region 5, indicating the need for further research and strategic adjustment to improve engagement and spending in this segment.
    """)

    # Visualization Section
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/333', width=520)
    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/222', width=520)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/777', caption='Distribution of Spending Across Skill Brackets', width=520)
    with col2:
        st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/111', caption='Day-by-Day Churn Rate: Event 1 vs Event 2', width=520)
    
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/444', width=1000)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/555', width=1000)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/666', width=1000)

    heatmap_data = data.groupby(['region', 'platform']).dollars_spent.mean().unstack()
    plt.clf()
    fig1, ax1 = plt.subplots(figsize=(7, 5))
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=.2, ax=ax1)
    ax1.set_title("Average Dollars Spent per Player by Region and Platform")
    st.pyplot(fig1)
    plt.close(fig1)

    event_1_start, event_1_end = pd.Timestamp('2017-01-24'), pd.Timestamp('2017-02-14')
    event_2_start, event_2_end = pd.Timestamp('2017-02-28'), pd.Timestamp('2017-03-21')

    event_1_data = data[(data['Date'] >= event_1_start) & (data['Date'] <= event_1_end)]
    event_2_data = data[(data['Date'] >= event_2_start) & (data['Date'] <= event_2_end)]

    # Adjust the figsize parameter to make the graph smaller, thus increasing space on the right
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))  # Adjusted for empty space

    sns.kdeplot(event_1_data['games_played'], fill=True, color="skyblue", label="Event 1", ax=axes[0, 0])
    sns.kdeplot(event_2_data['games_played'], fill=True, color="salmon", label="Event 2", ax=axes[0, 0])
    axes[0, 0].set_title('Distribution of Games Played')

    sns.kdeplot(event_1_data['skill_last'], fill=True, color="skyblue", label="Event 1", ax=axes[0, 1])
    sns.kdeplot(event_2_data['skill_last'], fill=True, color="salmon", label="Event 2", ax=axes[0, 1])
    axes[0, 1].set_title('Distribution of Skill Last')

    sns.kdeplot(event_1_data['items_crafted'], fill=True, color="skyblue", label="Event 1", ax=axes[1, 0])
    sns.kdeplot(event_2_data['items_crafted'], fill=True, color="salmon", label="Event 2", ax=axes[1, 0])
    axes[1, 0].set_title('Distribution of Items Crafted')

    sns.kdeplot(event_1_data['dollars_spent'], fill=True, color="skyblue", label="Event 1", ax=axes[1, 1])
    sns.kdeplot(event_2_data['dollars_spent'], fill=True, color="salmon", label="Event 2", ax=axes[1, 1])
    axes[1, 1].set_title('Distribution of Dollars Spent')

    plt.tight_layout()
    plt.subplots_adjust(right=0.65)  # Adjust as needed based on the new figsize, but may not be necessary
    st.pyplot(fig)
    plt.close(fig)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/999', width=1000)

    # Result
    st.subheader("Result")
    st.write("""
    The data-driven approach yielded actionable insights, enabling the development of targeted strategies to enhance player retention and increase revenue. Specifically:
    - A 21% increase in player engagement and spending in the identified high-value segments through targeted promotions and tailored in-game events.
    - Initiated a strategic review and adjustment for underperforming segments, resulting in a marked improvement in player satisfaction and reduced churn rate by 15% during subsequent events.
    """)

    # Conclusion and Strategic Insights
    st.subheader("Conclusion and Strategic Insights")
    st.write("""
    This analysis underscored the importance of leveraging advanced analytics to dissect player engagement and spending behaviors. By focusing on data-driven insights, we were able to develop targeted strategies that significantly enhanced player retention and increased revenue. Understanding the dynamics of player churn and spending across different segments and events provided a roadmap for more effective engagement strategies in future events, ensuring the continued success of Warcraft's in-game monetization efforts.
    """)

elif page == "DASHBOARD / EXECUTIVE BUSINESS INSIGHTS":
    st.header("DASHBOARD / EXECUTIVE BUSINESS INSIGHTS")
    st.subheader("Situation")
    st.markdown("""
        Complex Data Landscape: Post-merger, the business faced challenges with unstructured data across systems, affecting the Finance department's performance measurement and IGM.
    """, unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/1111', width=950)
    
    st.subheader("Task")
    st.markdown("""
        Performance Measurement and Reporting: Needed to gather business requirements for accurate performance measurement and dynamic reporting.
    """, unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/11', width=950)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/44', width=950)

    st.subheader("Action")
    st.markdown("""
        - **Data Gathering and Cleaning:** Used SQL queries and existing reports to extract data. Cleaned data with deduplication, normalization, and error correction.
        - **Schema Development and Collaboration:** Developed a dynamic schema for flexible reporting. Collaborated with management to identify key metrics and designed a user-friendly dashboard.
    """, unsafe_allow_html=True)
    
    st.subheader("Result")
    st.markdown("""
        - **Informed Decision-Making:** Enhanced management's strategic planning and operational efficiency.
        - **Enhanced Reporting:** Improved Finance's performance measurement and adaptability to business changes.
    """, unsafe_allow_html=True)

elif page == "DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION":
    st.header("DATA ANALYSIS / WAREHOUSE & GL ACCOUNT OPTIMIZATION")
    st.subheader("Situation:")
    st.markdown("""
        In the rapidly evolving logistics sector, maintaining operational efficiency and cost-effectiveness is paramount. Our company faced challenges with escalating costs in logistics and warehouse operations, directly impacting our bottom line. A comprehensive analysis was initiated to identify the root causes of these financial pressures, particularly focusing on the 'SKYLAB' and '3PL Logistics' divisions, known for their significant contribution to the logistics operations but also for potential inefficiencies.
    """, unsafe_allow_html=True)

    st.subheader("Task:")
    st.markdown("""
        The primary objective was to conduct a detailed examination of the logistics and warehouse operations to uncover cost-saving opportunities. This task involved identifying areas of waste, inefficiencies, and potential for process optimizations that could lead to substantial cost reductions without compromising the quality of operations.
    """, unsafe_allow_html=True)

    st.subheader("Action:")
    st.markdown("""
        To tackle this task, a multifaceted approach was employed:
        - **Financial Data Analysis:** Leveraged Python for in-depth analysis of financial records, focusing on expenditure patterns related to 'SKYLAB' and '3PL Logistics'.
        - **Identification of Inefficiencies:** Through the analysis, pinpointed specific areas within 'SKYLAB' and '3PL Logistics' where inefficiencies were prevalent.
        - **Optimization Opportunities:** Developed strategies for cost optimization and process improvements based on the identified inefficiencies. This involved proposing adjustments in operations, resource allocation, and possibly renegotiating contracts or seeking more cost-effective service providers.
    """, unsafe_allow_html=True)

    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/3333', width=950)

    st.subheader("Result:")
    st.markdown("""
        The analysis and subsequent actions led to significant outcomes:
        - **Cost-saving Opportunities Uncovered:** The deep dive into the financial data and operations of 'SKYLAB' and '3PL Logistics' revealed multiple inefficiencies. By addressing these, the company could optimize processes and significantly reduce costs.
        - **Strategic Improvements Implemented:** Recommendations for process improvements were put into action, leading to a more streamlined operation. Preliminary estimates indicated potential savings in the logistics and warehouse operations, positively affecting the company's bottom line.
        - **Foundation for Continuous Improvement:** Beyond immediate cost savings, the project established a framework for ongoing analysis and optimization. This proactive approach to identifying and addressing inefficiencies will serve as a cornerstone for future operational enhancements and cost management strategies.
    """, unsafe_allow_html=True)

elif page == "PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT":
    st.header("PROCESS AUTOMATION / QUARTERLY ROYALTY MANAGEMENT")
    
    # Objective
    st.subheader("Situation:")
    st.markdown("""
        Years of data were unorganized, with the quarterly royalty management process involving a lot of manual lookup in Excel. This was a month-long task for financial analysts, significantly affecting operational efficiency and increasing the risk of errors.
    """, unsafe_allow_html=True)

    # Python Section
    st.markdown("#### PYTHON", unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/2222', width=950)

    # VBA Section
    st.markdown("#### VBA", unsafe_allow_html=True)
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/9999', width=950)

    # Impact
    st.subheader("Task:")
    st.markdown("""
        The objective was to streamline the quarterly royalty management process, reducing the time spent by financial analysts from a month-long task to a 2-hour automated process. This involved supporting their operation by providing an efficient dashboard and improving operational efficiency.
    """, unsafe_allow_html=True)

    # Methodology
    st.subheader("Action:")
    st.markdown("""
        - **Understanding Historical Data:** Gained a hands-on understanding of historical data and royalty reporting.
        - **Strategic Planning:** Provided a plan and roadmap for resource approval. Collaborated with field managers to identify historical data, perform data analysis and analytics.
        - **Process Automation:** Developed a custom Python script for data consolidation and utilized Excel VBA for automating data extraction and report generation. This collaborative and strategic approach involved leveraging both technical skills and soft skills like communication, strategy, prudent curiosity, and humility.
    """, unsafe_allow_html=True)

    # Result
    st.subheader("Result:")
    st.markdown("""
        - **Significant Time Reduction:** Shortened the process time for 2 senior financial analysts from a month's worth of overtime to just 8 hours of processing time, achieving an **85% reduction** in process time.
        - **Operational Cost Savings:** This efficiency gain significantly lowered operational costs and enhanced the accuracy and efficiency of royalty management.
        - **Enhanced Efficiency and Accuracy:** The automation not only saved time but also improved the overall accuracy and reliability of the royalty management process.
    """, unsafe_allow_html=True)

    st.subheader('Conclusion')
    st.write("""
    This project demonstrates the powerful impact of combining technical automation with strategic planning and collaboration. By automating the quarterly royalty management process, we significantly improved operational efficiency and accuracy, showcasing the value of integrating Python and VBA in financial processes.
    """)

elif page == "SCOPE OF SKILLS":
    st.header("SCOPE OF SKILLS")
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/logo', width=700)
    st.markdown("#### Programming Languages:", unsafe_allow_html=True)
    st.markdown("*Proficient in Python and VBA.*", unsafe_allow_html=True)
    st.markdown("#### Data Engineering Tools:", unsafe_allow_html=True)
    st.markdown("*Experienced in ETL, SSMS, AS400, Snowflakes, Power Query, System Integration Analysis.*", unsafe_allow_html=True)
    st.markdown("#### Data Analysis Libraries:", unsafe_allow_html=True)
    st.markdown("*Skilled in using Pandas, NumPy, Seaborn, Matplotlib, Openpyxl, SciPy, TensorFlow.*", unsafe_allow_html=True)
    st.markdown("#### Statistical Analysis:", unsafe_allow_html=True)
    st.markdown("*Descriptive/Inferential Statistics, A/B Testing, Predictive Modeling, Forecasting, Regression Analysis, Hypothesis Testing, & Time Series Analysis.*", unsafe_allow_html=True)
    st.markdown("#### BI Tools:", unsafe_allow_html=True)
    st.markdown("*Proficient in Power BI, Google Analytics, and Data Studio.*", unsafe_allow_html=True)
    st.markdown("#### Digital Marketing:", unsafe_allow_html=True)
    st.markdown("*Facebook, Google Ads, Shopify, Google Analytics, Data Studio, Campaign Management, Performance and Content Optimization.*", unsafe_allow_html=True)
    st.markdown("#### Data Modeling:", unsafe_allow_html=True)
    st.markdown("*STAR/ER/DAG diagrams, and Normalization.*", unsafe_allow_html=True)

elif page == "CERTIFICATIONS":
    st.header("**CERTIFICATIONS**")
    st.subheader(" Supervised Machine Learning: Regression and Classification - 2024")
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/STANDFORD.PNG', width=800)
    st.markdown("<a href='https://www.coursera.org/account/accomplishments/verify/YHLXRW3TL569' target='_blank'>Certificate Link</a>", unsafe_allow_html=True)
    
    st.header("**CERTIFICATIONS**")
    st.subheader(" Neural Networks and Deep Learning - DeepLearning.AI - 2024")
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/DeepAI', width=800)
    st.markdown("<a href='https://www.coursera.org/account/accomplishments/verify/P3MNNDS44DLL' target='_blank'>Certificate Link</a>", unsafe_allow_html=True)
    
    st.subheader(" Analyzing and Visualizing Data with Power BI - EdX - 2019")
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/edx', width=800)
    st.markdown("<a href='https://courses.edx.org/certificates/c05a356504164e2babb5e6c3ee54ec79?_gl=1*1cfx8u5*_ga*MjAyMzYwNzAyNy4xNzEwNjM1MzM2*_ga_D3KS4KMDT0*MTcxMzI0NDM4OC4zLjEuMTcxMzI0NDQ5NC4wLjAuMA..' target='_blank'>Certificate Link</a>", unsafe_allow_html=True)
    
    st.subheader(" AWS Cloud Practitioner Essentials - AWS - 2019")
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/AWS1', width=800)
    
    st.subheader(" SQL - Sololearn - 2017")
    st.image('https://github.com/jasonchang0102/Streamlit0102/raw/main/Picture/SQLsololearn', width=800)
    st.markdown("<a href='https://www.sololearn.com/en/certificates/CT-YUFRJBUH' target='_blank'>Certificate Link</a>", unsafe_allow_html=True)

elif page == "LET'S CONNECT":
    st.header("""IN GOD WE TRUST; FOR ALL ELSE, WE TURN TO THE VALIDATION OF DATA. WITH DATA SCIENCE AS OUR COMPASS, WE'RE SET TO REVEAL HIDDEN INSIGHTS THAT OUR DATA IS JUST DYING TO TELL. - JASON CHANG""")
    st.header("LET'S CONNECT!!")
    st.markdown("""
    Feel free to connect with me for any inquiries or opportunities.
    <br><br>
    <img src="https://img.icons8.com/material-rounded/48/000000/phone--v1.png" alt="phone_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**Phone:** (626) 203 – 3319</span>
    <br>
    <img src="https://img.icons8.com/material-outlined/48/000000/email--v1.png" alt="email_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**Email:** jason.chang01022021@gmail.com</span>
    <br>
    <img src="https://img.icons8.com/material-rounded/48/000000/linkedin--v1.png" alt="linkedin_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**LinkedIn:** linkedin.com/in/jchang0102</span>
    <br>
    <img src="https://img.icons8.com/material-outlined/48/000000/map-pin.png" alt="location_icon" style="vertical-align:middle; width:35px; height:35px;"> <span style="font-size:20px; vertical-align:middle;">**Location:** Irvine, CA</span>
    """, unsafe_allow_html=True)
