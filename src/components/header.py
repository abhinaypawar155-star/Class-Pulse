
import streamlit as st
import base64
from pathlib import Path

def header_home():
    logo_path = Path(__file__).resolve().parents[2] / "assets" / "logo.png"

    with open(logo_path, "rb") as image:
        logo_base64 = base64.b64encode(image.read()).decode("utf-8")

    logo_url = f"data:image/png;base64,{logo_base64}"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;margin-bottom:30px; margin-top:30px">
            <img src="{logo_url}"style="height:100px; width=auto:"/>
            <h1 style='text-align:center; color:#E0E3FF'>CLASS<br/>PULSE</h1>
        </div>
    
    
                """
                ,unsafe_allow_html=True)

def header_dashboard():
    logo_path = Path(__file__).resolve().parents[2] / "assets" / "logo.png"

    with open(logo_path, "rb") as image:
        logo_base64 = base64.b64encode(image.read()).decode("utf-8")

    logo_url = f"data:image/png;base64,{logo_base64}"
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:12px; margin:20px 0;">
            <img src="{logo_url}" style="height:64px; width:64px; object-fit:contain;" />
            <div style="font-family:'Climate Crisis',sans-serif; color:#5865F2; font-size:2rem; line-height:1.1; white-space:nowrap;">
                CLASS<br/>PULSE
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

