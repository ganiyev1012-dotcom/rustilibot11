import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishga tushdi!")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Yangi Python versiyalari uchun kerak
asyncio.set_event_loop(asyncio.new_event_loop())
app.run_polling()
