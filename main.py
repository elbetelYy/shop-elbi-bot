import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛍 Shop Now",
                url="https://t.me/shopelbibot"
            )
        ],
        [
            InlineKeyboardButton(
                "📸 Instagram",
                url="https://www.instagram.com/shopelbii?igsh=cjZuZWN1cm5mYTgw&utm_source=qr"
            ),
            InlineKeyboardButton(
                "💬 Contact Us",
                callback_data="contact"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🛍 Welcome to Shop Elbi!\n"
        "✨ Cute accessories, thoughtfully made ✨\n\n"
        "🎀 Scrunchies • 👜 Tote Bags • 💖 Everyday essentials\n\n"
        "Tap below to get started 💫",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Run the bot
app.run_polling()
