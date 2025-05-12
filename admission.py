import streamlit as st

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/pegasflight/student-predictor/refs/heads/main/his.png" alt="University Logo" width="150"/>
        <h1>HIS University Admission Eligibility Checker</h1>
    </div>
    """,
    unsafe_allow_html=True
)
# Dropdowns and inputs
bac_year = st.selectbox("Year of BAC", options=list(range(2005, 2025)))
high_school_major = st.selectbox("High School Major", options=["M", "MT", "S", "ECO", "LET"])
bac_average = st.sidebar.slider("BAC General Average (/20)", 0.0, 20.0, 12.0, 0.1)
math_grade = st.sidebar.slider("BAC Math Grade (/20)", 0.0, 20.0, 12.0, 0.1)
faculty_choice = st.selectbox("Faculty to Apply To", options=["MI", "SEGC", "SHS", "DSP"])

decision = ""
weighted_average = None

# Logic
if bac_year < 2005:
    decision = "❌ Rejected - BAC year too old"
else:
    if faculty_choice == "MI":
        if high_school_major in ["M", "MT", "S"]:
            weighted_average = round(((bac_average * 2) + math_grade) / 3, 2)
            st.write(f"📊 Weighted Average (MI): **{weighted_average}**")
            if weighted_average >= 12:
                decision = "✅ Accepted"
            else:
                decision = "ℹ️ Suggested for Preparatory Cycle"
        else:
            decision = "❌ Rejected - Major not accepted for MI"

    elif faculty_choice == "SEGC":
        if high_school_major in ["M", "MT", "S", "ECO", "LET"]:
            if high_school_major == "LET":
                if bac_average >= 10 and math_grade >= 12:
                    decision = "✅ Accepted"
                else:
                    decision = "ℹ️ Suggested for Preparatory Cycle"
            else:
                if bac_average >= 10 and math_grade >= 10:
                    decision = "✅ Accepted"
                else:
                    decision = "ℹ️ Suggested for Preparatory Cycle"
        else:
            decision = "❌ Rejected - Major not accepted for SEGC"

    elif faculty_choice in ["SHS", "DSP"]:
        decision = "✅ Accepted"

# Display final decision
if decision:
    st.subheader("📝 Admission Decision")
    st.info(decision)
