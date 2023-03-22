import requests

TOKEN = '6058623152:AAGNlIY67LiEiPIQAQl6S4puvE9mgSPHMjU'
URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_last_update() -> dict:
    '''get last update from telegram server'''
    url = f'{URL}getUpdates'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result'][-1]
    return False

def send_welcome_msg(chat_id: int,User_name1,User_name2) -> None:
    '''send welcome message'''
    url = f'{URL}sendMessage'
    btn1 = {
        'text': '👍'
    }
    btn2 = {
        'text': '👎'
    }
    keyborad = {
        'keyboard': [[btn1, btn2]],
        'resize_keyboard': True
    }

    payload = {
        'chat_id': chat_id,
        'text': f'_*Welcome to our bot {User_name1} {User_name2}*_\n\n_press one of the buttons?_',
        'parse_mode': 'MarkdownV2',
        'reply_markup': keyborad
    }
    response = requests.get(url, json=payload)


def send_like_dislike(chat_id: int, like: int, dislike: int) -> None:
    '''send message to tg user about number of like and dislike'''
    url = f'{URL}sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': f'*like: {like}\ndislike: {dislike}*',
        'parse_mode': 'MarkdownV2'
    }
    response = requests.get(url, params=payload)