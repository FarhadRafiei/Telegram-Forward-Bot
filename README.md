<<<<<<< HEAD
# Telegram-Forward-Bot
ForwardBot is a lightweight Python script that automatically forwards messages from a source Telegram chat or channel to a target group. Easy to set up and run on PC or Raspberry Pi.
=======
# ForwardBot

A simple Python script that automatically forwards messages from one Telegram chat (channel, private, or group) to another group.

## Features
- Forward messages from one chat to another automatically
- Supports text messages (can be extended for photos, files, etc.)
- Easy to set up and run on PC or Raspberry Pi
- Lightweight – based on pyTelegramBotAPI

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/telegram-forward-bot.git
   cd telegram-forward-bot
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux / macOS
   pip install -r requirements.txt
   ```

## Setup
1. Create a Telegram bot with [BotFather](https://t.me/BotFather) and copy your Bot Token.
2. Edit `forwardbot.py`:
   ```python
   BOT_TOKEN = "YOUR_BOT_TOKEN"
   SOURCE_CHAT_ID = -1001234567890
   TARGET_CHAT_ID = -1009876543210
   ```

## Run
```bash
python forwardbot.py
```
- Keep it running with `screen` or `tmux` for 24/7 operation.

## License
MIT License
>>>>>>> a36eb65 (Initial commit: ForwardBot)
