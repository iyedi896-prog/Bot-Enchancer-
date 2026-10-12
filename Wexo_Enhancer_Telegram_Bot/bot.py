import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

BOT_TOKEN = os.getenv("8662091341:AAGgY7WGz8u-Q0eo0Wwvh0E-k7Y2V7ntfhQ")

WELCOME_TEXT = (
    "Welcome to Wexo Enhancer!\n\n"
    "Enhance your experience with Wexo. Let's get you registered.\n\n"
    "Are you the person who wants to register for Wexo Enhancer?"
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    keyboard = [
        [InlineKeyboardButton("🟢 Yes, it's me", callback_data="confirm_yes")],
        [InlineKeyboardButton("🔴 No, it's not me", callback_data="confirm_no")],
    ]
    await update.effective_message.reply_text(
        WELCOME_TEXT,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def handle_choice(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "confirm_yes":
        await query.edit_message_text(
            "Great! Let's continue with your Wexo Enhancer registration."
        )
    elif query.data == "confirm_no":
        await query.edit_message_text(
            "No problem. Registration has been cancelled."
        )


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "Missing TELEGRAM_BOT_TOKEN. Set it as an environment variable "
            "before starting the bot."
        )

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        CallbackQueryHandler(handle_choice, pattern=r"^confirm_(yes|no)$")
    )

    logging.info("Wexo Enhancer bot is starting.")
    app.run_polling()


if __name__ == "__main__":
    main()
