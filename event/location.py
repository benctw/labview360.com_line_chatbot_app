from line_chatbot_api import *

def location_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title='LabVIEW360的網聚地點',
            address='106台北市大安區復興南路一段390號2樓',
            latitude=25.033725,
            longitude=121.543419
        )
        )