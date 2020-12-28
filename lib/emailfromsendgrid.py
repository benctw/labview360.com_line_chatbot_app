import os
from line_chatbot_api import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendemailaction(event):
    profile_user_id = event.source.user_id
    profile_name = line_bot_api.get_profile(event.source.user_id).display_name
    # print(profile_user_id)
    message = Mail(
        from_email='linechatbot@labview360.com',
        to_emails='benctw@gmail.com',
        subject=f'Line Chatbot;{profile_name}',
        html_content=f'<strong>有人使用Line Chatbot</strong><br>{profile_name}<br>{profile_user_id}')
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)

    except Exception as e:
        print(e)