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

# Category keyboard (reusable)
def category_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎀 Bonnets", callback_data="bonnets")],
        [InlineKeyboardButton("💖 Scrunchies", callback_data="scrunchies")],
        [InlineKeyboardButton("🖇 Claw Clips", callback_data="claw_clips")],
        [InlineKeyboardButton("🎗 Headbands", callback_data="headbands")],
        [InlineKeyboardButton("🧶 Crochets", callback_data="crochets")],
        [InlineKeyboardButton("🎁 Package Sets", callback_data="packages")],
    ])

# Back button
def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Categories", callback_data="browse")]
    ])

# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "browse":
        await query.message.reply_text(
            "🛍 Choose a category:",
            reply_markup=category_keyboard()
        )

    elif query.data == "bonnets":
        await query.message.reply_photo(
            photo="https://via.placeholder.com/600x600.png?text=Bonnets",
            caption=(
                "🎀 *Bonnets*\n\n"
                "• Satin Bonnets — from *300 ETB*\n"
                "• Double-layer Bonnets — from *350 ETB*\n\n"
                "✨ Multiple colors available\n"
                "💬 Message us to order"
            ),
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    elif query.data == "scrunchies":
        await query.message.reply_photo(
            photo="https://via.placeholder.com/600x600.png?text=Scrunchies",
            caption=(
                "💖 *Scrunchies*\n\n"
                "• Satin — *150 ETB*\n"
                "• Velvet — *180 ETB*\n"
                "• Mini — *120 ETB*\n\n"
                "🎀 Bundle discounts available\n"
                "💬 Message us to order"
            ),
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    elif query.data == "claw_clips":
        await query.message.reply_photo(
            photo="https://via.placeholder.com/600x600.png?text=Claw+Clips",
            caption=(
                "🖇 *Claw Clips*\n\n"
                "• Small — *200 ETB*\n"
                "• Medium — *250 ETB*\n"
                "• Large — *300 ETB*\n\n"
                "✨ Strong & trendy\n"
                "💬 Message us to order"
            ),
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    elif query.data == "headbands":
        await query.message.reply_photo(
            photo="https://via.placeholder.com/600x600.png?text=Headbands",
            caption=(
                "🎗 *Headbands*\n\n"
                "• Fabric — *200 ETB*\n"
                "• Knotted — *250 ETB*\n\n"
                "✨ Comfortable & stylish\n"
                "💬 Message us to order"
            ),
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    elif query.data == "crochets":
        await query.message.reply_photo(
            photo="https://via.placeholder.com/600x600.png?text=Crochets",
            caption=(
                "🧶 *Crochets*\n\n"
                "• Handmade — from *400 ETB*\n\n"
                "✨ Custom colors available\n"
                "💬 Message us to order"
            ),
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    elif query.data == "packages":
        await query.message.reply_photo(
            photo="https://via.placeholder.com/600x600.png?text=Package+Sets",
            caption=(
                "🎁 *Package Sets*\n\n"
                "• Starter — *700 ETB*\n"
                "• Gift — *900 ETB*\n"
                "• Deluxe — *1200 ETB*\n\n"
                "🎀 Perfect for gifts\n"
                "💬 Message us to order"
            ),
            parse_mode="Markdown",
            reply_markup=back_button()
        )

# App setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# Run the bot
app.run_polling()
