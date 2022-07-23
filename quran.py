from telegram import *
from telegram.ext import *

print("Bot started...")

def start_command(update,context):
    text="Salom! "
    text+=update.message.chat.first_name
    text+=" "
    text+=update.message.chat.last_name
    text+="\nBuyruqlar:\n/about - Qur'on haqida\n/surah - Suralar\n/help - Yordam"
    update.message.reply_text(text)

def about_command(update,context):
    update.message.reply_text("Qurʼon (arabcha: القرآن oʻqimoq, qiroat qilmoq) — musulmonlarning asosiy muqaddas kitobi. Islom eʼtiqodiga koʻra, Qurʼon vahiy orqali Muhammad Mustafo Sallollohu alayhi vasallamga 610—632 yillar davomida nozil qilingan Allohning kalomi (Kalomulloh). Qurʼon „Kitob“ (yozuv), „Furqon“ (haq bilan botilning orasini ayiruvchi), „Zikr“ (eslatma), „Tanzil“ (nozil qilingan) kabi nomlar bilan atalib, „Nur“ (yorugʻlik), „Hudo“ (hidoyat), „Muborak“ (barakotli), „Mubin“ (ochiq-ravshan), „Bushro“ (xushxabar), „Aziz“ (eʼzozlanuvchi), „Majid“ (ulugʻ), „Bashir“ (bashorat beruvchi), „Nazir“ (ogohlantiruvchi) kabi soʻzlar bilan sifatlangan. Islom olamida Qurʼon musʼhaf nomi bilan ham mashhur. Islom ulamolari Qurʼonning 30 xil nom va sifatlarini sanab oʻtganlar.",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Suralar", callback_data="surah"),InlineKeyboardButton("Yordam",callback_data="help")]]))

def surah_command(update,context):
    image=("https://t.me/quron_suralar_qiroat/3")
    context.bot.sendMediaGroup(chat_id=update.effective_chat.id,media=[InputMediaAudio(image,caption="Fotiha surasi")])

def help_command(update,context):
    update.message.reply_text("Buyruqlar:\n/start - Qayta boshlash\n/about - Qur'on haqida\n/surah - Suralar\nMurojaat uchun: @aziz2004official")

def buttons(update,context):
    pass

def error(update,context):
    print(f"Yangilash: {update} Xatolik: {context.error}")

def main():
    updater=Updater("5480920558:AAHkXEPFFrDIObibLhocMNCeXOLLmwsDo7c",use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("about",about_command))
    dp.add_handler(CommandHandler("surah",surah_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CallbackQueryHandler(buttons))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()