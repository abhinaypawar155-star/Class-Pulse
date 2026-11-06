import streamlit as st
import segno
import io
from src.database.db import create_subject

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "http://localhost:8501"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col ,col2 = st.columns(2)

    with col:
        st.markdown("### Copy Link")
        st.code(join_url,language="text")
        st.code(subject_code,language="text")
        st.info("Share this link on Whatsapp or Email")

    with col2:
        st.markdown("### Scan Code to Join") 
        st.image(out.getvalue(),caption="Use QR Code for class join") 


