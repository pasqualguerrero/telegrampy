import os
from unittest import TestCase

from telegrampy import utils
from telegrampy.exceptions import MissingTelegramBotToken, MissingTelegramChatId

class TestUtils(TestCase):

    def test_get_telegram_bot_token(self):

        with self.assertRaises(MissingTelegramBotToken):
            utils.get_telegram_bot_token()

        os.environ["TELEGRAM_BOT_TOKEN"] = "foo_token"

        token = utils.get_telegram_bot_token()
        self.assertEqual(token, "foo_token")

    def test_get_telegram_chat_id(self):

        with self.assertRaises(MissingTelegramChatId):
            utils.get_telegram_chat_id()

        os.environ["TELEGRAM_CHAT_ID"] = "foo_chat_id"

        chat_id = utils.get_telegram_chat_id()
        self.assertEqual(chat_id, "foo_chat_id")

