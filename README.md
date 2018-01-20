# Telegrampy
Get notifications from multiple services through telegram

### Installation
```
pip install telegrampy
```

### Usage

#### Settings
Telegrampy can load settings in two ways:

- From environment variables:
    ```sh
    export TELEGRAM_BOT_TOKEN="<bot_token>"
    export TELEGRAM_CHAT_ID="<chat_id>"
    ```

- From django.conf module:
    ```py
    TELEGRAM_BOT_TOKEN = "<bot_token>"
    TELEGRAM_CHAT_ID = "<chat_id>"
    ```
#### Examples
```py
from telegrampy import notify, notify_info, notify_success, notify_warning, notify_error

notify("foo message")
notify_info("foo message")
notify_success("foo message")
notify_warning("foo message")
notify_error("foo message")
```

### Run tests
```
pip install -r requirements-test.txt
tox
```
