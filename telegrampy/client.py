import json
import requests
from multiprocessing.dummy import Pool

from telegrampy.conf import TELEGRAM_API_DOMAIN, TELEGRAM_API_METHODS, EMOJIS
from telegrampy.utils import get_telegram_bot_token, get_telegram_chat_id


class TelegramClient(object):

    def __init__(self, *args, **kwargs):
        self.token = get_telegram_bot_token()
        self.chat_id = get_telegram_chat_id()
        self.bot = "bot%s" % self.token
        self.pool = Pool(processes=1)

    def _make_request(self, method, endpoint, payload={}):
        headers = {'Content-Type': 'application/json'}
        response = getattr(requests, method)(
            endpoint,
            headers=headers,
            data=json.dumps(payload),
        )
        return response

    def _build_telegram_url(self, action):
        method = TELEGRAM_API_METHODS[action]
        return "{domain}/{bot}/{method}".format(
            domain=TELEGRAM_API_DOMAIN, bot=self.bot, method=method)

    def notify(self, text):
        """
        Post a message using sendMessage method to telegram api. It executes
        http request in a thread.
        """
        url = self._build_telegram_url("send_message")
        payload = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True,
            "disable_notification": False,
        }
        self.pool.apply_async(self._make_request, ["post", url, payload])

    def info(self, text):
        # Append info emoji to text message
        self.notify("%s %s" % (EMOJIS["info"], text))

    def success(self, text):
        # Append success emoji to text message
        self.notify("%s %s" % (EMOJIS["success"], text))

    def warning(self, text):
        # Append warning emoji to text message
        self.notify("%s %s" % (EMOJIS["warning"], text))

    def error(self, text):
        # Append info emoji to text message
        self.notify("%s %s" % (EMOJIS["error"], text))
