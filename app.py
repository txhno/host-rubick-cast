from base64 import b64encode
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


DOC_PATH = Path(__file__).with_name("cast.html")
DOWNLOAD_PATH = Path(__file__).with_name("rubick_cast_documentation.docx")


st.set_page_config(
    page_title="Rubick CAST Documentation",
    page_icon=":blue_book:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def build_download_pill() -> str:
    encoded_document = b64encode(DOWNLOAD_PATH.read_bytes()).decode("ascii")
    return (
        '<a class="pill" '
        f'href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{encoded_document}" '
        f'download="{DOWNLOAD_PATH.name}">Download DOCX</a>'
    )


def load_document() -> str:
    html = DOC_PATH.read_text(encoding="utf-8")
    if not DOWNLOAD_PATH.exists():
        return html

    old_metadata = """<span class="pill">Last updated: <time datetime="2026-05-21">21 May 2026</time></span>
<a class="pill" download="" href="rubick_cast_documentation.docx">Download DOCX</a>
<span class="pill">Diagrams open in zoom view</span>"""
    new_metadata = f"""<span class="pill">Last updated: <time datetime="2026-05-21">21 May 2026</time></span>
{build_download_pill()}"""
    return html.replace(old_metadata, new_metadata)


if not DOC_PATH.exists():
    st.error("Missing cast.html next to app.py.")
    st.stop()

st.markdown(
    """
    <style>
      html,
      body,
      .stApp,
      [data-testid="stAppViewContainer"],
      [data-testid="stAppViewContainer"] > .main {
        margin: 0;
        padding: 0;
        background: transparent;
      }
      .block-container {
        max-width: none;
        padding: 0 !important;
      }
      header[data-testid="stHeader"],
      div[data-testid="stDecoration"],
      div[data-testid="stToolbar"],
      footer {
        display: none !important;
        height: 0 !important;
      }
      div[data-testid="stVerticalBlock"],
      div[data-testid="stVerticalBlock"] > div {
        gap: 0 !important;
      }
      iframe {
        display: block;
        margin: 0;
        padding: 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if not DOWNLOAD_PATH.exists():
    st.error(f"Missing {DOWNLOAD_PATH.name} next to app.py.")

components.html(load_document(), height=1200, scrolling=True)
