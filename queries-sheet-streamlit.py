import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- Google Sheets Setup ---
# Define scope
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# Load credentials from your service account JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet (use name or URL)
sheet = client.open("StreamlitEntries").sheet1

# --- Streamlit UI ---
st.title("Streamlit → Google Sheets Demo")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
feedback = st.text_area("Your feedback")

if st.button("Submit"):
    # Append entry to Google Sheet
    sheet.append_row([name, email, feedback])
    st.success("Your entry has been saved to Google Sheets!")
