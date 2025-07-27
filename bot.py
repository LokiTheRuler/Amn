from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")  # Secure way to handle token
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # e.g., -1001234567890

FOOTER_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("🎥 Subscribe", url="https://t.me/YourChannelUsername")],
    [InlineKeyboardButton("🤖 Join Bot", url="https://t.me/YourBotUsername")],
    [InlineKeyboardButton("🌐 Visit Website", url="https://yourwebsite.com")]
])

def add_footer_buttons(update: Update, context: CallbackContext):
    if update.effective_chat.id == CHANNEL_ID:
        try:
            context.bot.send_message(
                chat_id=CHANNEL_ID,
                text="👇 Useful Links 👇",
                reply_markup=FOOTER_BUTTONS,
                reply_to_message_id=update.message.message_id
            )
            print("✅ Footer added.")
        except Exception as e:
            print("❌ Error:", e)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.update.channel_posts, add_footer_buttons))
    print("🤖 Bot running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
