import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# --- Google Sheets Setup ---
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from Streamlit secrets
creds_dict = st.secrets["gcp_service_account"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("StreamlitEntries").sheet1

# --- Streamlit UI ---
st.title("Streamlit → Google Sheets Demo")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
feedback = st.text_area("Your feedback")

if st.button("Submit"):
    sheet.append_row([name, email, feedback])
    st.success("Your entry has been saved to Google Sheets!")
