from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)
from dotenv import load_dotenv
import os



# Примитивная база знаний
faq = {
    "справка": "Справку можно получить в деканате.",
    "академ отпуск": "Академический отпуск оформляется через заявление.",
    "расписание": "Расписание доступно на сайте университета или в системе Платонус.",
    "оценки": "Оценки можно посмотреть в Платонусе.",
    "перевод": "Для перевода на другой факультет обратитесь в учебный отдел."
}

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я деканат-бот. Задайте вопрос, например: 'Где взять справку?'"
    )

# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    response = "Извините, не нашёл ответ. Попробуйте другими словами."

    for keyword, answer in faq.items():
        if keyword in user_message:
            response = answer
            break

    await update.message.reply_text(response)

# Запуск бота
def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    print(f"TOKEN: {TOKEN!r}")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
