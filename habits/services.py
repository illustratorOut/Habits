import requests
from django.conf import settings


class MyBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKKEN

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': '785281914',
                'text': text,
            }
        )
