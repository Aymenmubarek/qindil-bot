import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import openai
import os

# ==============================
# 🔑 Use Railway environment variables
# ==============================
TELEGRAM_TOKEN = os.environ.get("8375212961:AAGSutZ3vt5DVln-4OeovW0XgNnivVwrN9E")
OPENAI_API_KEY = os.environ.get("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")

openai.api_key = OPENAI_API_KEY

# ==============================
# ChatGPT group reply
# ==============================
async def chat_with_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text

    if update.message.reply_to_message or f"@{context.bot.username}" in message_text:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message_text}]
            )
            answer = response["choices"][0]["message"]["content"]
            await update.message.reply_text(answer)
        except Exception as e:
            await update.message.reply_text("⚠️ Error: " + str(e))

# ==============================
# Run the bot
# ==============================
app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_ai))

async def main():
    print("🤖 Bot is running in the group...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
