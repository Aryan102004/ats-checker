import streamlit as st
import matplotlib.pyplot as plt

from src.parser import extract_resume_text
from src.keyword_matcher import find_skill_gap
from src.section_scorer import calculate_section_wise_score
from src.report_generator import generate_pdf

from src.ats_simulator import simulate_ats_score
from src.learning_path import generate_learning_path
from src.project_suggester import suggest_projects
from src.bullet_generator import generate_resume_bullets
from src.role_roadmap import get_role_based_roadmap

from src.gemini_advisor import gemini_ai_advisor
from src.gemini_chatbot import resume_chatbot


# ---------------- Page Config ----------------
st.set_page_config(
    page_title="ATS Resume Checker AI",
    page_icon="📄",
    layout="wide"
)


# ---------------- Load CSS ----------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


# ======================================================
# HERO HEADER
# ======================================================
st.markdown("<div class='hero-title'>ATS Resume Score Checker</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>AI Resume Analyzer with ATS Simulator + Gemini Assistant</div>",
    unsafe_allow_html=True
)

st.write("")


# ======================================================
# MAIN CORE INPUTS (MAIN PAGE)
# ======================================================
st.markdown(
    """
    <div class="main-card">
        <h2>📌 Upload Resume & Job Description</h2>
        <p class="card-subtext">
            Upload your resume and paste job description to instantly get ATS score,
            missing skills, and AI recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume (PDF or DOCX)",
        type=["pdf", "docx"]
    )

with col2:
    job_description = st.text_area(
        "📝 Paste Job Description",
        height=200
    )


# ======================================================
# SIDEBAR EXTRA FEATURES
# ======================================================
st.sidebar.title("⚙ Advanced Settings")

target_role = st.sidebar.selectbox(
    "🎯 Select Target Role",
    ["Data Scientist", "Web Developer", "DevOps Engineer", "AI Engineer"]
)

ats_mode = st.sidebar.radio(
    "📊 ATS Simulation Mode",
    ["Basic ATS", "Skill-Weighted ATS", "Experience-Boosted ATS"]
)

enable_ai = st.sidebar.checkbox("🤖 Enable Gemini AI Advisor", value=True)
enable_chat = st.sidebar.checkbox("💬 Enable Resume Chatbot", value=True)


st.write("")
analyze_btn = st.button("🚀 Analyze Resume")


# ======================================================
# MAIN ANALYSIS
# ======================================================
if analyze_btn:

    if resume_file is None:
        st.error("❌ Please upload your resume first.")
        st.stop()

    if job_description.strip() == "":
        st.error("❌ Please paste job description first.")
        st.stop()

    with st.spinner("Running ATS + AI Analysis... ⏳"):

        resume_text = extract_resume_text(resume_file)

        matched, missing = find_skill_gap(resume_text, job_description)

        score = simulate_ats_score(resume_text, job_description, matched, ats_mode)

        skills_score, exp_score, edu_score, overall_score = calculate_section_wise_score(
            resume_text, job_description
        )

        st.session_state.analysis_data = {
            "resume_text": resume_text,
            "job_description": job_description,
            "matched": matched,
            "missing": missing,
            "score": score,
            "skills_score": skills_score,
            "exp_score": exp_score,
            "edu_score": edu_score,
            "target_role": target_role,
            "ats_mode": ats_mode
        }

    st.success("✅ Resume Analysis Completed Successfully!")


if "analysis_data" in st.session_state:
    data = st.session_state.analysis_data

    # ======================================================
    # DASHBOARD RESULTS (MAIN PAGE)
    # ======================================================
    tab1, tab2, tab3 = st.tabs(
        ["📊 Dashboard", "🤖 AI Advisor", "💬 Chatbot"]
    )

    # ---------------- TAB 1 Dashboard ----------------
    with tab1:

        left, right = st.columns([1, 1])

        with left:
            st.subheader("⭐ ATS Match Score")

            st.markdown(
                f"""
                <div class="score-circle">
                    <div class="score-value">{data['score']}%</div>
                    <div class="score-label">ATS Score</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(min(data['score'] / 100, 1.0))

            st.write(f"**Target Role:** {data['target_role']}")
            st.write(f"**ATS Mode:** {data['ats_mode']}")

        with right:
            st.subheader("📄 Resume Preview")

            preview_text = data['resume_text'][:1500] + "..."
            st.text_area("Extracted Resume Text", preview_text, height=260)

        st.write("---")

        st.subheader("📊 Section Breakdown")

        categories = ["Skills", "Experience", "Education"]
        values = [data['skills_score'], data['exp_score'], data['edu_score']]

        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_ylim(0, 100)
        st.pyplot(fig)

        st.subheader("✅ Skill Gap Insights")

        st.markdown("### Matched Skills")
        for s in data['matched'][:10]:
            st.markdown(f"<span class='chip good'>{s}</span>", unsafe_allow_html=True)

        st.markdown("### Missing Skills")
        for s in data['missing'][:10]:
            st.markdown(f"<span class='chip bad'>{s}</span>", unsafe_allow_html=True)

        st.subheader("📄 Download ATS Report")

        pdf_file = generate_pdf(data['score'], data['matched'], data['missing'])

        with open(pdf_file, "rb") as f:
            st.download_button(
                "⬇️ Download Report (PDF)",
                data=f,
                file_name="ATS_Report.pdf",
                mime="application/pdf"
            )

    # ---------------- TAB 2 AI Advisor ----------------
    with tab2:

        if not enable_ai:
            st.warning("⚠ AI Advisor is disabled from sidebar.")
        else:
            st.subheader("📚 Personalized Learning Path")
            for skill, link in generate_learning_path(data['missing']):
                st.write(f"✅ {skill} → {link}")

            st.subheader("💡 Recommended Projects")
            for p in suggest_projects(data['missing']):
                st.write("🚀", p)

            st.subheader("📝 Resume Bullet Improvements")
            for b in generate_resume_bullets(data['missing']):
                st.write("•", b)

            st.subheader("🚀 Role Roadmap")
            for step in get_role_based_roadmap(data['target_role']):
                st.write("➡️", step)

            st.subheader("🤖 Gemini AI Career Advisor")

            if st.button("Generate AI Suggestions ✨"):
                ai_text = gemini_ai_advisor(data['score'], data['matched'], data['missing'], data['target_role'])
                st.write(ai_text)

    # ---------------- TAB 3 Chatbot ----------------
    with tab3:

        if not enable_chat:
            st.warning("⚠ Chatbot is disabled from sidebar.")
        else:
            st.subheader("💬 Resume Assistant Chatbot")

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

            user_prompt = st.chat_input("Ask something about your resume...")

            if user_prompt:

                st.session_state.messages.append(
                    {"role": "user", "content": user_prompt}
                )

                with st.chat_message("user"):
                    st.markdown(user_prompt)

                reply = resume_chatbot(
                    user_prompt,
                    data['resume_text'][:2000],
                    data['job_description'][:2000]
                )

                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )

                with st.chat_message("assistant"):
                    st.markdown(reply)


else:
    st.info("📌 Upload resume + job description above, then click Analyze.")


# ======================================================
# FOOTER
# ======================================================
st.markdown(
    "<div class='footer'>Built with Streamlit + Gemini AI | MCA Final Year Project</div>",
    unsafe_allow_html=True
)