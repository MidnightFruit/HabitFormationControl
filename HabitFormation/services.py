from celery.worker.state import requests

from config import settings


def send_tg_message(text, chat_id):
    params = {
        'text': text,
        'chat_id': chat_id,
    }

    response = requests.get(f'{settings.TELEGRAM_URL}/sendMessage', params=params)
    return response