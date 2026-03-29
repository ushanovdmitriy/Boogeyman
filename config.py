"""
Конфигурация проекта.

Читает переменные окружения из файла .env через python-dotenv.
Все обязательные переменные валидируются при импорте модуля.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def _require(name: str, cast=str):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Обязательная переменная окружения не задана: {name}")
    try:
        return cast(value)
    except (ValueError, TypeError) as e:
        raise RuntimeError(f"Неверное значение переменной {name}: {e}") from e


TELEGRAM_BOT_TOKEN: str = _require("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_ID: int = _require("TELEGRAM_API_ID", int)
TELEGRAM_API_HASH: str = _require("TELEGRAM_API_HASH")
ANTHROPIC_API_KEY: str = _require("ANTHROPIC_API_KEY")
CHAT_ID: int = _require("CHAT_ID", int)
TELETHON_SESSION_NAME: str = os.getenv("TELETHON_SESSION_NAME", "bot_session")
