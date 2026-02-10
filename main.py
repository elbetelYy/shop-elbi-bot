import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

BOT_TOKEN = os.environ["BOT_TOKEN"]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍 Browse Products", callback_data="browse")],
        [
            InlineKeyboardButton(
                "📸 Instagram",
                url="https://www.instagram.com/shopelbii?igsh=cjZuZWN1cm5mYTgw&utm_source=qr"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🛍 Welcome to Shop Elbi!\n"
        "✨ Cute accessories, thoughtfully made ✨\n\n"
        "Tap below to explore our products 💫",
        reply_markup=reply_markup
    )

# Handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "browse":
        keyboard = [
            [InlineKeyboardButton("🎀 Bonnets", callback_data="bonnets")],
            [InlineKeyboardButton("💖 Scrunchies", callback_data="scrunchies")],
            [InlineKeyboardButton("🖇 Claw Clips", callback_data="claw_clips")],
            [InlineKeyboardButton("🎗 Headbands", callback_data="headbands")],
            [InlineKeyboardButton("🧶 Crochets", callback_data="crochets")],
            [InlineKeyboardButton("🎁 Package Sets", callback_data="packages")],
        ]

        await query.message.reply_text(
            "🛍 Choose a category:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data in [
        "bonnets",
        "scrunchies",
        "claw_clips",
        "headbands",
        "crochets",
        "packages"
    ]:
        category_names = {
            "bonnets": "🎀 Bonnets",
            "scrunchies": "💖 Scrunchies",
            "claw_clips": "🖇 Claw Clips",
            "headbands": "🎗 Headbands",
            "crochets": "🧶 Crochets",
            "packages": "🎁 Package Sets"
        }

        await query.message.reply_text(
            f"{category_names[query.data]}\n\n"
            "✨ Beautiful styles available\n"
            "📦 Multiple colors & designs\n\n"
            "💬 Send us a message here to order!"
        )

# App setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# Run the bot
app.run_polling()
