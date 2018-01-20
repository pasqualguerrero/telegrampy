import os

from telegrampy.exceptions import MissingTelegramBotToken, MissingTelegramChatId


def get_telegram_bot_token():
    """
    Return a string with bot token. Tries to load it from environment variables
    and if not from django.conf module.
    """
    token = ""
    try:
        token = os.environ["TELEGRAM_BOT_TOKEN"]
    except KeyError:
        pass

    try:
        from django.conf import settings
        token = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
    except ImportError:
        pass

    if not token:
        raise MissingTelegramBotToken("Couldn't get telegram bot token")
    return token


def get_telegram_chat_id():
    """
    Return a string with telegram chat id. Tries to load it from environment
    variables and if not from django.conf module.
    """
    chat_id = ""
    try:
        chat_id = os.environ["TELEGRAM_CHAT_ID"]
    except KeyError:
        pass

    try:
        from django.conf import settings
        chat_id = getattr(settings, "TELEGRAM_CHAT_ID", None)
    except ImportError:
        pass

    if not chat_id:
        raise MissingTelegramChatId("Couldn't get telegram chat id")
    return chat_id
