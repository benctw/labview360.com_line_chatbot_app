from flask import Flask, request, abort
from urllib.parse import parse_qsl
from line_chatbot_api import *
from lib.emailfromsendgrid import sendemailaction
from event.aboutus import aboutus_event
from event.location import location_event
from event.contact import contact_event
from event.appointment import appointment_event, appointment_tutor_datetime_event, appointment_tutor_completed_event, appointment_meetup_drink_event, appointment_meetup_completed_event

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text.lower()
    return_text = message_text
    sendemailaction(event)
    if message_text == '@關於我們':
        aboutus_event(event)
    elif message_text == '@網聚地點':
        location_event(event)
    elif message_text == '@聯絡我們':
        contact_event(event)
    elif message_text == '@我要參加labview360活動':
        appointment_event(event)
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=return_text)
            )

@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))
    # print(data)
    # print(data.get('action'))
    # print(data.get('service'))
    # print(data.get('date'))
    if data.get('action')=='step2':
        if data.get('service')=='tutor':
            appointment_tutor_datetime_event(event)
        elif data.get('service')=='meetup':
            appointment_meetup_drink_event(event)

    if data.get('action')=='step3' and data.get('service')=='tutor':
        appointment_tutor_completed_event(event)
    elif data.get('action')=='step3' and data.get('service')=='meetup':
        appointment_meetup_completed_event(event)


if __name__ == "__main__":
    app.debug = True
    app.run()