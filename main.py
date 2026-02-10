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

    await update.message.reply_text(
        "🛍 Welcome to Shop Elbi!\n"
        "✨ Cute accessories, thoughtfully made ✨\n\n"
        "Tap below to explore our products 💫",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Category menu
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

    # Products + prices
    elif query.data == "bonnets":
        await query.message.reply_text(
            "🎀 *Bonnets*\n\n"
            "• Satin Bonnets — from *300 ETB*\n"
            "• Double-layer Bonnets — from *350 ETB*\n\n"
            "✨ Multiple colors available\n"
            "💬 Message us to order",
            parse_mode="Markdown"
        )

    elif query.data == "scrunchies":
        await query.message.reply_text(
            "💖 *Scrunchies*\n\n"
            "• Satin Scrunchies — *150 ETB*\n"
            "• Velvet Scrunchies — *180 ETB*\n"
            "• Mini Scrunchies — *120 ETB*\n\n"
            "🎀 Bundle discounts available\n"
            "💬 Message us to order",
            parse_mode="Markdown"
        )

    elif query.data == "claw_clips":
        await query.message.reply_text(
            "🖇 *Claw Clips*\n\n"
            "• Small Size — *200 ETB*\n"
            "• Medium Size — *250 ETB*\n"
            "• Large Size — *300 ETB*\n\n"
            "✨ Trendy & strong grip\n"
            "💬 Message us to order",
            parse_mode="Markdown"
        )

    elif query.data == "headbands":
        await query.message.reply_text(
            "🎗 *Headbands*\n\n"
            "• Fabric Headbands — *200 ETB*\n"
            "• Knotted Headbands — *250 ETB*\n\n"
            "✨ Comfortable & stylish\n"
            "💬 Message us to order",
            parse_mode="Markdown"
        )

    elif query.data == "crochets":
        await query.message.reply_text(
            "🧶 *Crochets*\n\n"
            "• Handmade Crochets — from *400 ETB*\n\n"
            "✨ Custom colors available\n"
            "💬 Message us to order",
            parse_mode="Markdown"
        )

    elif query.data == "packages":
        await query.message.reply_text(
            "🎁 *Package Sets*\n\n"
            "• Starter Set — *700 ETB*\n"
            "• Gift Set — *900 ETB*\n"
            "• Deluxe Set — *1200 ETB*\n\n"
            "🎀 Perfect for gifts\n"
            "💬 Message us to order",
            parse_mode="Markdown"
        )

# App setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# Run the bot
app.run_polling()
