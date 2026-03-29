# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Boogeyman is a Telegram bot for reading and sending messages in a private channel, built with `python-telegram-bot` (v21+, async API).

## Setup & Running

```bash
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN="<token from @BotFather>"
export TELEGRAM_CHANNEL_ID="<channel id, e.g. -1001234567890>"
python bot.py
```

## Architecture

Single-file bot (`bot.py`) using `python-telegram-bot`'s async `Application` builder pattern with long-polling (`app.run_polling()`).

- **Config**: `BOT_TOKEN` and `CHANNEL_ID` from env vars (`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHANNEL_ID`)
- **Handlers**: `/start` command + `MessageHandler` filtered to the configured channel ID
- **Stubs**: `handle_channel_message` (process incoming) and `send_message_to_channel` (post to channel) — not yet implemented

All handler functions are `async` and use `ContextTypes.DEFAULT_TYPE`. The library is v21+ which uses the async API exclusively — do not use the deprecated synchronous patterns.
