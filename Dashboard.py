import streamlit as st
import pandas as pd

from src.agent import WaterAgent
from src.database import log_intake, get_intake_history



if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False



if not st.session_state.tracker_started:

    st.title("💧 Welcome to AI Water Tracker")

    st.markdown("""
    Track your daily hydration with the help of AI.

    • Log water intake  
    • Get hydration feedback  
    • View intake history  
    """)

    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()



else:

    st.title("💧 AI Water Tracker Dashboard")

    st.sidebar.header("Log Water Intake")

    user_id = st.sidebar.text_input(
        "User ID",
        value="aditya"
    )

    intake_ml = st.sidebar.number_input(
        "Water Intake (mL)",
        min_value=0,
        step=100
    )

    if st.sidebar.button("Submit Intake"):

        if user_id and intake_ml > 0:

            # Save to DB
            log_intake(user_id, intake_ml)

            st.success(
                f"✅ Logged {intake_ml} mL for {user_id}"
            )

            # AI Feedback
            agent = WaterAgent()

            feedback = agent.analyse_and_intake(
                intake_ml
            )

            st.info(feedback)

        else:
            st.warning(
                "Please enter a valid intake amount."
            )

    

    history = get_intake_history(user_id)

    if history:

        st.subheader("📊 Intake History")

        history_rows = []
        for row in history:
            if len(row) == 4:
                history_rows.append(row)
            elif len(row) == 2:
                history_rows.append((None, user_id, row[0], row[1]))

        df = pd.DataFrame(
            history_rows,
            columns=[
                "ID",
                "User ID",
                "Intake (mL)",
                "Date"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.info("No intake history found.")
