from line_chatbot_api import *

def contact_event(event):
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/jciBSx9.jpg',
            title='Contact',
            text='Please select',
            actions=[
                # PostbackAction(
                #     label='postback',
                #     display_text='postback text',
                #     data='action=buy&itemid=1'
                # ),
                # MessageAction(
                #     label='message',
                #     text='message text'
                # ),
                URIAction(
                    label='寫信給LabVIEW360',
                    uri='mailto:info@labview360.com'
                ),
                URIAction(
                    label='致電LabVIEW360',
                    uri='tel:+886933333252'
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages = [buttons_template_message]
    )