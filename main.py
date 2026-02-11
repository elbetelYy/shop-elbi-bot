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

# MAIN MENU
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍 Shop Now", callback_data="shop")],
        [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/shopelbii?igsh=cjZuZWN1cm5mYTgw&utm_source=qr")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "✨ Welcome to Shop Elbi ✨\n\nYour cute fashion assistant 💕",
        reply_markup=reply_markup
    )

# BUTTON HANDLER
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # PRODUCT MENU
    if query.data == "shop":
        keyboard = [
            [InlineKeyboardButton("🧕 Bonnet", callback_data="bonnet")],
            [InlineKeyboardButton("🎀 Scrunchies", callback_data="scrunchies")],
            [InlineKeyboardButton("🦋 Claw Clips", callback_data="claw")],
            [InlineKeyboardButton("👑 Headbands", callback_data="headband")],
            [InlineKeyboardButton("🧶 Crochets", callback_data="crochet")],
            [InlineKeyboardButton("🎁 Package Sets", callback_data="package")],
            [InlineKeyboardButton("⬅ Back", callback_data="back_main")]
        ]

        await query.edit_message_text(
            "🛍 Choose a category below:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # PRODUCT DETAILS
    elif query.data == "bonnet":
        await query.edit_message_text(
            "🧕 Bonnet Collection\n\nPremium silk bonnets\nPrice: 350 birr 💕",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅ Back", callback_data="shop")]]
            )
        )

    elif query.data == "scrunchies":
        await query.edit_message_text(
            "🎀 Scrunchies Collection\n\nSoft & stylish scrunchies\nPrice: 120 birr 💕",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅ Back", callback_data="shop")]]
            )
        )

    elif query.data == "claw":
        await query.edit_message_text(
            "🦋 Claw Clips\n\nTrendy claw clips\nPrice: 200 birr 💕",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅ Back", callback_data="shop")]]
            )
        )

    elif query.data == "headband":
        await query.edit_message_text(
            "👑 Headbands\n\nCute & comfy headbands\nPrice: 180 birr 💕",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅ Back", callback_data="shop")]]
            )
        )

    elif query.data == "crochet":
        await query.edit_message_text(
            "🧶 Crochets\n\nHandmade crochet pieces\nPrice: 400 birr 💕",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅ Back", callback_data="shop")]]
            )
        )

    elif query.data == "package":
        await query.edit_message_text(
            "🎁 Package Sets\n\nBundle & save deals\nPrice: Starting 900 birr 💕",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅ Back", callback_data="shop")]]
            )
        )

    elif query.data == "back_main":
        await query.edit_message_text(
            "✨ Welcome back to Shop Elbi ✨",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🛍 Shop Now", callback_data="shop")],
                [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/shopelbii?igsh=cjZuZWN1cm5mYTgw&utm_source=qr")]
            ])
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
