# Wexo Enhancer Telegram Bot

A small English-only Telegram bot with a short introduction and two confirmation buttons.

## 1. Create or configure your bot
1. Open [@BotFather](https://t.me/BotFather) in Telegram.
2. Create a bot with `/newbot`, or select your existing bot.
3. If the token you previously shared was real, revoke it in BotFather and use a newly generated token.

## 2. Install Python dependencies
Python 3.10 or newer is recommended.

```bash
python -m pip install -r requirements.txt
```

## 3. Set your bot token securely

Do not paste the token into `bot.py`, publish it, or share it.

### Windows PowerShell
```powershell
$env:TELEGRAM_BOT_TOKEN="PASTE_YOUR_NEW_BOT_TOKEN_HERE"
python bot.py
```

### Windows Command Prompt
```bat
set TELEGRAM_BOT_TOKEN=PASTE_YOUR_NEW_BOT_TOKEN_HERE
python bot.py
```

### macOS / Linux
```bash
export TELEGRAM_BOT_TOKEN="PASTE_YOUR_NEW_BOT_TOKEN_HERE"
python bot.py
```

## 4. Test it
Open your bot in Telegram and send `/start`.

- **🟢 Yes, it's me** shows a registration continuation message.
- **🔴 No, it's not me** cancels the current registration step.

## Notes
- Telegram bot buttons cannot have custom background colors; the green and red emoji communicate the choices.
- This starter version does not yet create accounts or save registrations to a database.
- Keep the bot running while you want it to respond. For continuous operation, deploy it to a trusted server.
