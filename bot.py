"""
Telegram bot for reading and sending messages in a private channel.

Uses python-telegram-bot library.
Install: pip install python-telegram-bot
"""

import os
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Bot token from @BotFather
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# Private channel ID (e.g. -1001234567890)
CHANNEL_ID = int(os.getenv("TELEGRAM_CHANNEL_ID", "0"))


async def handle_channel_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Called when a new message appears in the private channel.

    TODO: implement message reading/processing logic.
    """
    pass


async def send_message_to_channel(context: ContextTypes.DEFAULT_TYPE, text: str) -> None:
    """Send a text message to the private channel.

    TODO: implement message sending logic.
    """
    pass


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command."""
    await update.message.reply_text("Bot is running.")


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN env variable is not set")
    if CHANNEL_ID == 0:
        raise RuntimeError("TELEGRAM_CHANNEL_ID env variable is not set")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # Listen to messages from the private channel
    app.add_handler(
        MessageHandler(
            filters.Chat(chat_id=CHANNEL_ID) & filters.ALL,
            handle_channel_message,
        )
    )

    logger.info("Bot started, listening for channel %s", CHANNEL_ID)
    app.run_polling()


if __name__ == "__main__":
    main()
