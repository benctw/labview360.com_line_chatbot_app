from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, 
    PostbackEvent,
    TextMessage, 
    TextSendMessage, 
    ImageSendMessage, 
    StickerSendMessage, 
    LocationSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
    URIAction,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    DatetimePickerAction
)

line_bot_api = LineBotApi('S1h87/mV9J+K5krM8Kjir1GmT0sdXaBQII5rR2Q8oedBjPEjT5T1DzVyBV1ELHrEKWurTD0aWRqjF1jt2d7VtXm1zguUdlwli6naJ9jtxKtTEz2Bi1/tQ7OfVRw7t1AW80CVlDBW/GUcF5IUeg0mOQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5463d562e7cabacfa70e4f4518f14cc2')