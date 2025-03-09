from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import CallbackContext

# Твой токен бота от BotFather
TOKEN = "7925748933:AAEW70GhZ_ubQhiiRDbY3LGWss0-Vun17-E"

# ID твоего канала (можно указать @username канала или числовой ID)
CHANNEL_ID = "@dnipro_alerts"

# Ключевые слова для фильтрации
KEYWORDS = ["дніпро", "дніпра", "ігрені", "павлоград", "павлограду", "павлограда"]  # Убедись, что слова в нижнем регистре

# Создание бота
app = Application.builder().token(TOKEN).build()

# Обработчик команды /start
async def start(update: Update, context: CallbackContext):
    # Исправлена строка с кавычками
    await update.message.reply_text('Dnipro Alerts will notify you about "дніпро", "дніпра", "ігрені", "ігрень", "павлоград", "павлограду", "павлограда" only')

# Фильтрация сообщений
async def filter_messages(update: Update, context: CallbackContext):
    """Обрабатывает новые сообщения и пересылает только нужные"""
    text = update.message.text.lower()
    
    if any(keyword in text for keyword in KEYWORDS):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"📢 Фильтр: {update.message.text}")

# Добавляем обработчик команды /start
app.add_handler(CommandHandler("start", start))

# Добавляем обработчик фильтрации сообщений
app.add_handler(MessageHandler(filters.TEXT & filters.Chat(CHANNEL_ID), filter_messages))

# Запуск бота
print("Bot started!")
app.run_polling()
