from line_chatbot_api import *

def aboutus_event(event):
    image_url='https://i.imgur.com/tNq5hgd.jpg'
    image_url_preview = 'https://i.imgur.com/9NpUGfy.jpg'
    return_text = 'LabVIEW360 Community是個以華文LabVIEW使用者為主的非官方LabVIEW愛用者技術研討社群，我們在這裡討論NI LabVIEW軟體、NI硬體、與其他可能的第三方儀器連結應用的相關技術，希望透過知識交流討論，協助使用者在使用LabVIEW軟體上更加得心應手。LabVIEW360 Community上的網友都相當熱情與善良，我希望透過良性的互動，讓不管是新手老手，都可以在這裡得到LabVIEW技術能量。'
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=return_text),
        ImageSendMessage(original_content_url=image_url,
                            preview_image_url=image_url_preview),
        StickerSendMessage(
                package_id='11537',
                sticker_id='52002734'
                )]
        )