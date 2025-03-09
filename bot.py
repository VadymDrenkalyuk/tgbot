from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler

# Твой токен бота от BotFather
TOKEN = "7925748933:AAEW70GhZ_ubQhiiRDbY3LGWss0-Vun17-E"

# ID твоего канала (можно указать @username канала или числовой ID)
CHANNEL_ID = "@dnipro_alerts"

# Ключевые слова для фильтрации
KEYWORDS = ["Дніпро", "Дніпра", "Ігрень" "Ігрені" "Павлоград" "Павлограду" "Павлограда"]  # Можно добавить свои

# Создание бота
app = Application.builder().token(TOKEN).build()

async def filter_messages(update: Update, context):
    """Обрабатывает новые сообщения и пересылает только нужные"""
    text = update.message.text.lower()
    
    if any(keyword in text for keyword in KEYWORDS):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"📢 Фильтр: {update.message.text}")

# Добавляем обработчик сообщений
app.add_handler(MessageHandler(filters.TEXT & filters.Chat(CHANNEL_ID), filter_messages))

print("Бот запущен!")
app.run_polling()
