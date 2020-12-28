from line_chatbot_api import *
from urllib.parse import parse_qsl
import datetime

def appointment_event(event):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/vgFbdDK.jpg',
                    title='網聚',
                    text='請選擇要參加哪一場網聚',
                    actions=[
                        PostbackAction(
                            label='2020/3/18(星期三晚上)',
                            display_text='我要參加網聚：2020/3/18(星期三晚上)的時段',
                            data='action=step2&service=meetup&date=2020/3/18'
                        ),
                        PostbackAction(
                            label='2020/6/17(星期三晚上)',
                            display_text='我要參加網聚：2020/6/17(星期三晚上)的時段',
                            data='action=step2&service=meetup&date=2020/6/17'
                        ),
                        PostbackAction(
                            label='2020/9/16(星期三晚上)',
                            display_text='我要參加2020/9/16(星期三晚上)的時段',
                            data='action=step2&service=meetup&date=2020/9/16'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/SYP9lpm.jpg',
                    title='線上家教',
                    text='請選擇要解決哪一類問題',
                    actions=[
                        PostbackAction(
                            label='LabVIEW虛擬儀器',
                            display_text='LabVIEW虛擬儀器',
                            data='action=step2&service=tutor&kind=labview'
                        ),
                        PostbackAction(
                            label='馬達運動控制',
                            display_text='馬達運動控制',
                            data='action=step2&service=tutor&kind=motion'
                        ),
                        PostbackAction(
                            label='機器視覺',
                            display_text='機器視覺',
                            data='action=step2&service=tutor&kind=vision'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages = [TextSendMessage(text='想參加哪一個活動?'),
                    carousel_template_message]
    )

def appointment_meetup_drink_event(event):
    data = dict(parse_qsl(event.postback.data))
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/w1JM4f5.jpg',
            title='要喝什麼飲料',
            text='請問要喝咖啡還是喝茶呢?',
            actions=[
                PostbackAction(
                    label='咖啡',
                    display_text='喝咖啡',
                    data=f"action=step3&service={data.get('service')}&date={data.get('date')}&drink=coffee"
                ),
                PostbackAction(
                    label='茶',
                    display_text='喝茶',
                    data=f"action=step3&service={data.get('service')}&date={data.get('date')}&drink=tea"
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages = [buttons_template_message]
    )

def appointment_meetup_completed_event(event):
    appointment_service = dict(parse_qsl(event.postback.data)).get('service')
    appointment_date = dict(parse_qsl(event.postback.data)).get('date')
    appointment_drink = dict(parse_qsl(event.postback.data)).get('drink').lower()
    profile_name = line_bot_api.get_profile(event.source.user_id).display_name
    print(appointment_service)
    print(appointment_drink)
    print(profile_name)
    # do something
    appointment_meetup_done_text = f'謝謝{profile_name}，已幫你登記網聚，日期為{appointment_date}'
    appointment_meetup_done_drink_text = f"現場會為你準備{'咖啡' if appointment_drink=='coffee' else '茶'}"
    
    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages = [TextSendMessage(text=appointment_meetup_done_text),
                    TextSendMessage(text=appointment_meetup_done_drink_text)]
    )

def appointment_tutor_datetime_event(event):
    data = dict(parse_qsl(event.postback.data))
    now = datetime.datetime.now()
    min_now = now + datetime.timedelta(days=2)
    max_now = now + datetime.timedelta(days=9)


    image_carousel_template_message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/L3mU9My.jpg',
                    action=DatetimePickerAction(
                            label="預約日期時間",
                            data=f"action=step3&service={data.get('service')}",
                            mode="datetime",
                            initial=f'{min_now:%Y-%m-%dT00:00}',
                            min=f'{min_now:%Y-%m-%dT00:00}',
                            max=f'{max_now:%Y-%m-%dT23:59}'
                        )
                    )
                # ,
                # ImageCarouselColumn(
                #     image_url='https://example.com/item2.jpg',
                #     action=PostbackAction(
                #         label='postback2',
                #         display_text='postback text2',
                #         data='action=buy&itemid=2'
                #     )
                # )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages = [image_carousel_template_message]
    )


def appointment_tutor_completed_event(event):
    appointment_service = dict(parse_qsl(event.postback.data)).get('service')
    appointment_datetime = datetime.datetime.strptime(event.postback.params.get('datetime'), '%Y-%m-%dT%H:%M')
    profile_name = line_bot_api.get_profile(event.source.user_id).display_name
    print(appointment_service)
    print(appointment_datetime)
    print(profile_name)
    # do something
    appointment_tutor_done_text = f'謝謝{profile_name}，你的線上家教預約已完成'
    appointment_tutor_done_datetime_text = f'你預約的日期為{appointment_datetime:%Y-%m-%d}，時間是{appointment_datetime:%H:%M}'
    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages = [TextSendMessage(text=appointment_tutor_done_text),
                    TextSendMessage(text=appointment_tutor_done_datetime_text)]
    )


