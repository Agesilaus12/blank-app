import streamlit as st
from core.config import CSS
from core.state_manager import init_session_state
from pages.load_list import render_load_list
from pages.manifest import render_manifest
from pages.bermuda import render_bermuda

st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

init_session_state()

advanced_mode = st.sidebar.checkbox("Show Advanced Features", value=False)
st.session_state.show_advanced = advanced_mode

tab1, tab2, tab3 = st.tabs(["📦 Load List", "🚛 Musket Manifest", "🇧🇲 Bermuda Manifest"])

with tab1:
    render_load_list()

with tab2:
    render_manifest()

with tab3:
    render_bermuda()