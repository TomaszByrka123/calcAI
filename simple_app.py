import streamlit as st
from streamlit_supabase_auth import login_form, logout_button

session = login_form(
    url="https://qgvdmudlnfpspdbzopxh.supabase.co",
    apiKey="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFndmRtdWRsbmZwc3BkYnpvcHhoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxMTM5NzY3NSwiZXhwIjoyMDI2OTczNjc1fQ.DrLdEt_hHptoC2iYCSRacIqd_ELFLeoCC34XhOLiG9k",
    providers=["apple", "facebook", "github", "google"],
)
def main():
    st.title("Component Gallery")
    st.header("Login with Supabase Auth")
    st.write(session)
    if not session:
        return
    st.experimental_set_query_params(page=["success"])
    with st.sidebar:
        st.write(f"Welcome {session['user']['email']}")
        logout_button()


if __name__ == "__main__":
    main()