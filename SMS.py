import requests
import streamlit as st

# Nexmo API credentials
NEXMO_API_KEY = 'a477b9ce'
NEXMO_API_SECRET = 'tS32uKc1ZdKQ5hZF'
NEXMO_PHONE_NUMBER = '21627692361'

# Streamlit UI
st.title("Send SMS")
recipient = st.text_input("Recipient Phone Number")
message = st.text_area("Message")
submit = st.button("Send")

# Function to send SMS
def send_sms(api_key, api_secret, phone_number, recipient, message):
    url = f'https://rest.nexmo.com/sms/json?api_key={api_key}&api_secret={api_secret}&from={phone_number}&to={recipient}&text={message}'
    response = requests.get(url)
    data = response.json()
    return data

# Handle form submission
if submit:
    if not recipient or not message:
        st.warning("Please enter recipient phone number and message.")
    else:
        result = send_sms(NEXMO_API_KEY, NEXMO_API_SECRET, NEXMO_PHONE_NUMBER, recipient, message)
        if 'messages' in result and result['messages'][0]['status'] == '0':
            st.success("SMS sent successfully.")
        else:
            st.error("Failed to send SMS.")

