import streamlit as st
from twilio.rest import Client


st.title("SMS Sender")

account_sid = "ACcb2dd042df686a03ed1507464a43cbc3"
auth_token = "62db30d3466492cf4af4094a8707f2da"
from_number = '+12053016406'
to_number = st.text_input("Recipient Phone Number")
message_body = st.text_area("Message Body")

if st.button("Send SMS"):
    # Create a Twilio client instance
    client = Client(account_sid, auth_token)

    # Send the SMS
    message = client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )

    # Display the message SID
    st.success("SMS sent successfully! Message SID: {}".format(message.sid))
