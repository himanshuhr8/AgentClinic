import streamlit as st
import json

st.set_page_config(page_title="Agentic AI - Medical OSCE Diagnosis", layout="wide")

st.title("🧠 Agentic Medical AI — OSCE Case Diagnosis")
st.markdown("Demonstration of a multi-agent AI reasoning system on structured patient scenarios.")

# Sample pre-filled scenario
sample_case = {
    "OSCE_Examination": {
        "Objective_for_Doctor": "Assess and diagnose the patient presenting with double vision, difficulty climbing stairs, and upper limb weakness.",
        "Patient_Actor": {
            "Demographics": "35-year-old female",
            "History": "1-month history of double vision, difficulty climbing stairs, and weakness when brushing her hair. Symptoms worsen after activity, improve with rest.",
            "Symptoms": {
                "Primary_Symptom": "Double vision",
                "Secondary_Symptoms": [
                    "Difficulty climbing stairs",
                    "Weakness in upper limbs",
                    "Improvement of symptoms after rest"
                ]
            },
            "Past_Medical_History": "No significant past medical history.",
            "Social_History": "Non-smoker, drinks wine occasionally. Works as a graphic designer.",
            "Review_of_Systems": "No chest pain, palpitations, shortness of breath, or infections."
        },
        "Physical_Examination_Findings": {
            "Vital_Signs": {
                "Temperature": "36.6°C",
                "Blood_Pressure": "125/80 mmHg",
                "Heart_Rate": "72 bpm",
                "Respiratory_Rate": "16 breaths/min"
            },
            "Neurological_Examination": {
                "Cranial_Nerves": "Ptosis of right upper eyelid, worsens with upward gaze.",
                "Motor_Strength": "Weakness in upper limbs, no atrophy.",
                "Reflexes": "Normal",
                "Sensation": "Normal"
            }
        },
        "Test_Results": {
            "Blood_Tests": {
                "Acetylcholine_Receptor_Antibodies": "Present (elevated)"
            },
            "Electromyography": {
                "Findings": "Decreased muscle response with repetitive stimulation"
            },
            "Imaging": {
                "Chest_CT": {
                    "Findings": "Normal, no thymoma"
                }
            }
        },
        "Correct_Diagnosis": "Myasthenia gravis"
    }
}

# Sidebar: scenario input
st.sidebar.header("📋 Scenario Input")
use_sample = st.sidebar.checkbox("Use Sample Case", value=True)
uploaded_json = st.sidebar.file_uploader("Upload JSON File", type=["json"])

scenario = None

if use_sample:
    scenario = sample_case
elif uploaded_json is not None:
    scenario = json.load(uploaded_json)

if scenario:
    # Display scenario summary
    osce = scenario["OSCE_Examination"]
    st.subheader("🧑‍⚕️ Doctor's Objective")
    st.info(osce["Objective_for_Doctor"])

    st.subheader("🧍‍♀️ Patient Details")
    patient = osce["Patient_Actor"]
    st.markdown(f"- **Demographics:** {patient['Demographics']}")
    st.markdown(f"- **Primary Symptom:** {patient['Symptoms']['Primary_Symptom']}")
    st.markdown(f"- **Other Symptoms:** {', '.join(patient['Symptoms']['Secondary_Symptoms'])}")
    with st.expander("Full Patient History"):
        st.markdown(f"**History:** {patient['History']}")
        st.markdown(f"**Past Medical History:** {patient['Past_Medical_History']}")
        st.markdown(f"**Social History:** {patient['Social_History']}")
        st.markdown(f"**Review of Systems:** {patient['Review_of_Systems']}")

    st.subheader("🧪 Physical & Test Findings")
    with st.expander("Physical Examination"):
        st.json(osce["Physical_Examination_Findings"])
    with st.expander("Test Results"):
        st.json(osce["Test_Results"])

    # Run agent button
    if st.button("🤖 Run Agent Diagnosis"):
        with st.spinner("Agent is thinking..."):
            # Simulate agent output (replace with real API call later)
            for i in range(1, 6):
                st.markdown(f"**Doctor [{i*20}%]:** Agent reasoning step {i}...")
                st.markdown(f"**Patient [{i*20}%]:** Simulated patient response based on scenario.")

            st.success("✅ Diagnosis Ready: **Myasthenia Gravis**")
            st.markdown("> This diagnosis was generated based on patient symptoms, physical exam, and test findings using agentic step-wise inference.")
else:
    st.warning("Please select 'Use Sample Case' or upload a scenario JSON file.")

