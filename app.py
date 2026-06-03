import streamlit as st
from modules.pipeline import research_pipeline

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="ResearchPilot",
    page_icon="🔍",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>

/* -----------------------
GLOBAL
------------------------*/

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at top left, #1a1a1a 0%, #070707 40%),
    linear-gradient(135deg,#050816,#0b1020,#121212);
    color: #ffffff;
}

/* Hide Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* -----------------------
HERO
------------------------*/

.hero-top{
    font-family:'DM Mono', monospace;
    letter-spacing:6px;
    text-align:center;
    color:#8B5CF6;
    font-size:13px;
    margin-top:20px;
    text-transform:uppercase;
}

.hero-title{
    font-family:'Syne', sans-serif;
    text-align:center;
    font-size:7rem;
    font-weight:400;
    line-height:1;
    letter-spacing:-4px;
    margin-top:20px;
}

.hero-title span{
    color:#8B5CF6;
}

.hero-subtitle{
    font-family:'DM Sans', sans-serif;
    text-align:center;
    max-width:900px;
    margin:auto;
    margin-top:25px;
    margin-bottom:60px;
    color:#a1a1aa;
    font-size:1.15rem;
    line-height:1.8;
}

/* -----------------------
INPUT
------------------------*/

.stTextInput input{
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.08);
    border-radius:18px;
    height:58px;
    color:white;
    font-family:'DM Sans';
}

/* -----------------------
BUTTON
------------------------*/

.stButton button{
    width:100%;
    height:58px;
    border:none;
    border-radius:18px;
    background:linear-gradient(
        90deg,
        #4F8CFF,
        #8B5CF6
    );

    font-family:'Syne';
    font-weight:700;
    color:white;
    font-size:15px;

    transition:.3s ease;
}

.stButton button:hover{
    transform:translateY(-2px);
    box-shadow:0 0 30px rgba(255,140,66,.35);
}

/* -----------------------
METRICS
------------------------*/

[data-testid="metric-container"]{
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.08);
    border-radius:20px;
    padding:20px;
}

[data-testid="metric-container"] label{
    font-family:'DM Mono';
}

[data-testid="metric-container"] div{
    font-family:'Syne';
}

/* -----------------------
TABS
------------------------*/

.stTabs [data-baseweb="tab"]{
    font-family:'DM Mono';
    font-size:14px;
    font-weight:500;
}

/* -----------------------
HEADINGS
------------------------*/

h1,h2,h3{
    font-family:'Syne';
    font-weight:700;
}

/* -----------------------
REPORTS
------------------------*/

.report-box{
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.08);
    border-radius:20px;
    padding:25px;
}

.report-box p{
    font-family:'DM Sans';
    line-height:1.9;
}

/* -----------------------
URLS
------------------------*/

.url{
    font-family:'DM Mono';
    color:#ffb366;
    font-size:13px;
}

/* -----------------------
EXPANDERS
------------------------*/

.streamlit-expanderHeader{
    font-family:'Syne';
    font-weight:700;
}

/* -----------------------
SCROLLBAR
------------------------*/

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#ff8c42;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="hero-top">
AI AGENT
</div>

<div class="hero-title">
Research<span>Pilot</span>
</div>

<div class="hero-subtitle">
A research intelligence system that combines web search,
content extraction, report generation, review, and revision
into a single automated workflow.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# INPUT
# -----------------------------
topic = st.text_input(
    "Research Topic",
    placeholder="Enter any topic for deep research..."
)

# -----------------------------
# BUTTON
# -----------------------------
if st.button("Start Research"):

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    progress = st.progress(0)

    with st.spinner("Research agents are working..."):

        progress.progress(20)

        result = research_pipeline(topic)

        progress.progress(100)

    st.success("Research Completed")

    st.markdown("---")

    # -----------------------------
    # METRICS
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "URLs Found",
            len(result.get("urls", []))
        )

    with col2:
        st.metric(
            "Sources Scraped",
            len(result.get("sources", []))
        )

    with col3:
        st.metric(
            "Report Length",
            len(result.get("revised_report", ""))
        )

    st.markdown("---")

    # -----------------------------
    # TABS
    # -----------------------------
    tab1, tab2, tab3, tab4 = st.tabs([
        "Sources",
        "Draft Report",
        "Reviewer Feedback",
        "Final Report"
    ])

    # -----------------------------
    # SOURCES TAB
    # -----------------------------
    with tab1:

        st.subheader("URLs Found")

        urls = result.get("urls", [])

        if urls:
            for i, url in enumerate(urls, start=1):
                st.markdown(f"**{i}.** {url}")

        st.markdown("---")

        st.subheader("Scraped Sources")

        sources = result.get("sources", [])

        for i, source in enumerate(sources, start=1):

            with st.expander(f"Source {i}"):

                st.markdown(
                    f"**URL:** {source['url']}"
                )

                st.write(
                    source["content"][:2500]
                )

    # -----------------------------
    # DRAFT REPORT TAB
    # -----------------------------
    with tab2:

        st.subheader("Initial Report")

        st.markdown(
            result.get(
                "report",
                "No report generated."
            )
        )

    # -----------------------------
    # REVIEWER TAB
    # -----------------------------
    with tab3:

        st.subheader("Reviewer Feedback")

        st.markdown(
            result.get(
                "feedback",
                "No feedback available."
            )
        )

    # -----------------------------
    # FINAL REPORT TAB
    # -----------------------------
    with tab4:

        st.subheader("Final Revised Report")

        final_report = result.get(
            "revised_report",
            "No revised report available."
        )

        st.markdown(final_report)

        st.download_button(
            label="Download Report",
            data=final_report,
            file_name=f"{topic}_research_report.txt",
            mime="text/plain"
        )