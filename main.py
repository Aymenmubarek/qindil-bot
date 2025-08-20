from telegram.ext import Updater, CommandHandler
import os

# Bot token will come from Render environment variable
TOKEN = os.getenv("8330109086:AAF-rFVWVB19h0ZQUupQuSWUZe2-C9AGjlw")

# /start command
def start(update, context):
    update.message.reply_text("👋 Hello Qindil Team! The bot is running on Render 🚀")

# /help command
def help_command(update, context):
    update.message.reply_text(
        "📌 Available Commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
