from telegrampy.client import TelegramClient


def notify(text):
    return TelegramClient().notify(text)

def notify_info(text):
    return TelegramClient().info(text)

def notify_success(text):
    return TelegramClient().success(text)

def notify_warning(text):
    return TelegramClient().warning(text)

def notify_error(text):
    return TelegramClient().error(text)
