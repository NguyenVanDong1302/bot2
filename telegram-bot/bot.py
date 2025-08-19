from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8442804662:AAG4WDSPEs_y58098EAITysc76uV_9EAzJo"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"👋 Chào mừng {member.full_name} đã tham gia nhóm!")

def main():
    print(">>> Starting bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.run_polling()

if __name__ == "__main__":
    import telegram
    print(">>> Telegram Bot version:", telegram.__version__)
    main()
