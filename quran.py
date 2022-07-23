from telegram import *
from telegram.ext import *

s_10="Suralar: 1-10, 114 dan\n\n1. Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)\n2. Al-Baqara (سُورَةُ البَقَرَةِ)\n3. Aal-i-Imraan (سُورَةُ آلِ عِمۡرَانَ)\n4. An-Nisaa (سُورَةُ النِّسَاءِ)\n5. Al-Maaida (سُورَةُ المَائـِدَةِ)\n6. Al-An'aam (سُورَةُ الأَنۡعَامِ)\n7. Al-A'raaf (سُورَةُ الأَعۡرَافِ)\n8. Al-Anfaal (سُورَةُ الأَنفَالِ)\n9. At-Tawba (سُورَةُ التَّوۡبَةِ)\n10. Yunus (سُورَةُ يُونُسَ)"
s_20="Suralar: 11-20, 114 dan\n\n11. Hud (سُورَةُ هُودٍ)\n12. Yusuf (سُورَةُ يُوسُفَ)\n13. Ar-Ra'd (سُورَةُ الرَّعۡدِ)\n14. Ibrahim (سُورَةُ إِبۡرَاهِيمَ)\n15. Al-Hijr (سُورَةُ الحِجۡرِ)\n16. An-Nahl (سُورَةُ النَّحۡلِ)\n17. Al-Israa (سُورَةُ الإِسۡرَاءِ)\n18. Al-Kahf (سُورَةُ الكَهۡفِ)\n19. Maryam (سُورَةُ مَرۡيَمَ)\n20. Taa-Haa (سُورَةُ طه)"
s_30="Suralar: 21-30, 114 dan\n\n21. Al-Anbiyaa (سُورَةُ الأَنبِيَاءِ)\n22. Al-Hajj (سُورَةُ الحَجِّ)\n23. Al-Muminoon (سُورَةُ المُؤۡمِنُونَ)\n24. An-Noor (سُورَةُ النُّورِ)\n25. Al-Furqaan (سُورَةُ الفُرۡقَانِ)\n26. Ash-Shu'araa (سُورَةُ الشُّعَرَاءِ)\n27. An-Naml (سُورَةُ النَّمۡلِ)\n28. Al-Qasas (سُورَةُ القَصَصِ)\n29. Al-Ankaboot (سُورَةُ العَنكَبُوتِ)\n30. Ar-Room (سُورَةُ الرُّومِ)"
s_40="Suralar: 31-40, 114 dan\n\n31. Luqman (سُورَةُ لُقۡمَانَ)\n32. As-Sajda (سُورَةُ السَّجۡدَةِ)\n33. Al-Ahzaab (سُورَةُ الأَحۡزَابِ)\n34. Saba (سُورَةُ سَبَإٍ)\n35. Faatir (سُورَةُ فَاطِرٍ)\n36. Yaseen (سُورَةُ يسٓ)\n37. As-Saaffaat (سُورَةُ الصَّافَّاتِ)\n38. Saad (سُورَةُ صٓ)\n39. Az-Zumar (سُورَةُ الزُّمَرِ)\n40. Ghafir (سُورَةُ غَافِرٍ)"
s_50="Suralar: 41-50, 114 dan\n\n41. Fussilat (سُورَةُ فُصِّلَتۡ)\n42. Ash-Shura (سُورَةُ الشُّورَىٰ)\n43. Az-Zukhruf (سُورَةُ الزُّخۡرُفِ)\n44. Ad-Dukhaan (سُورَةُ الدُّخَانِ)\n45. Al-Jaathiya (سُورَةُ الجَاثِيَةِ)\n46. Al-Ahqaf (سُورَةُ الأَحۡقَافِ)\n47. Muhammad (سُورَةُ مُحَمَّدٍ)\n48. Al-Fath (سُورَةُ الفَتۡحِ)\n49. Al-Hujuraat (سُورَةُ الحُجُرَاتِ)\n50. Qaaf (سُورَةُ قٓ)"
s_60="Suralar: 51-60, 114 dan\n\n51. Adh-Dhaariyat (سُورَةُ الذَّارِيَاتِ)\n52. At-Tur (سُورَةُ الطُّورِ)\n53. An-Najm (سُورَةُ النَّجۡمِ)\n54. Al-Qamar (سُورَةُ القَمَرِ)\n55. Ar-Rahmaan (سُورَةُ الرَّحۡمَٰن)\n56. Al-Waaqia (سُورَةُ الوَاقِعَةِ)\n57. Al-Hadid (سُورَةُ الحَدِيدِ)\n58. Al-Mujaadila (سُورَةُ المُجَادلَةِ)\n59. Al-Hashr (سُورَةُ الحَشۡرِ)\n60. Al-Mumtahana (سُورَةُ المُمۡتَحنَةِ)"
s_70="Suralar: 61-70, 114 dan\n\n61. As-Saff (سُورَةُ الصَّفِّ)\n62. Al-Jumu'a (سُورَةُ الجُمُعَةِ)\n63. Al-Munaafiqoon (سُورَةُ المُنَافِقُونَ)\n64. At-Taghaabun (سُورَةُ التَّغَابُنِ)\n65. At-Talaaq (سُورَةُ الطَّلَاقِ)\n66. At-Tahrim (سُورَةُ التَّحۡرِيمِ)\n67. Al-Mulk (سُورَةُ المُلۡكِ)\n68. Al-Qalam (سُورَةُ القَلَمِ)\n69. Al-Haaqqa (سُورَةُ الحَاقَّةِ)\n70. Al-Ma'aarij (سُورَةُ المَعَارِجِ)"
s_80="Suralar: 71-80, 114 dan\n\n71. Nooh (سُورَةُ نُوحٍ)\n72. Al-Jinn (سُورَةُ الجِنِّ)\n73. Al-Muzzammil (سُورَةُ المُزَّمِّلِ)\n74. Al-Muddaththir (سُورَةُ المُدَّثِّرِ)\n75. Al-Qiyaama (سُورَةُ القِيَامَةِ)\n76. Al-Insaan (سُورَةُ الإِنسَانِ)\n77. Al-Mursalaat (سُورَةُ المُرۡسَلَاتِ)\n78. An-Naba (سُورَةُ النَّبَإِ)\n79. An-Naazi'aat (سُورَةُ النَّازِعَاتِ)\n80. Abasa (سُورَةُ عَبَسَ)"
s_90="Suralar: 81-90, 114 dan\n\n81. At-Takwir (سُورَةُ التَّكۡوِيرِ)\n82. Al-Infitaar (سُورَةُ الانفِطَارِ)\n83. Al-Mutaffifin (سُورَةُ المُطَفِّفِينَ)\n84. Al-Inshiqaaq (سُورَةُ الانشِقَاقِ)\n85. Al-Burooj (سُورَةُ البُرُوجِ)\n86. At-Taariq (سُورَةُ الطَّارِقِ)\n87. Al-A'laa (سُورَةُ الأَعۡلَىٰ)\n88. Al-Ghaashiya (سُورَةُ الغَاشِيَةِ)\n89. Al-Fajr (سُورَةُ الفَجۡرِ)\n90. Al-Balad (سُورَةُ البَلَدِ)"
s_100="Suralar: 91-100, 114 dan\n\n91. Ash-Shams (سُورَةُ الشَّمۡسِ)\n92. Al-Lail (سُورَةُ اللَّيۡلِ)\n93. Ad-Dhuhaa (سُورَةُ الضُّحَىٰ)\n94. Ash-Sharh (سُورَةُ الشَّرۡحِ)\n95. At-Tin (سُورَةُ التِّينِ)\n96. Al-Alaq (سُورَةُ العَلَقِ)\n97. Al-Qadr (سُورَةُ القَدۡرِ)\n98. Al-Bayyina (سُورَةُ البَيِّنَةِ)\n99. Az-Zalzala (سُورَةُ الزَّلۡزَلَةِ)\n100. Al-Aadiyaat (سُورَةُ العَادِيَاتِ)"
s_110="Suralar: 101-110, 114 dan\n\n101. Al-Qaari'a (سُورَةُ القَارِعَةِ)\n102. At-Takaathur (سُورَةُ التَّكَاثُرِ)\n103. Al-Asr (سُورَةُ العَصۡرِ)\n104. Al-Humaza (سُورَةُ الهُمَزَةِ)\n105. Al-Fil (سُورَةُ الفِيلِ)\n106. Quraish (سُورَةُ قُرَيۡشٍ)\n107. Al-Maa'un (سُورَةُ المَاعُونِ)\n108. Al-Kawthar (سُورَةُ الكَوۡثَرِ)\n109. Al-Kaafiroon (سُورَةُ الكَافِرُونَ)\n110. An-Nasr (سُورَةُ النَّصۡرِ)"
s_114="Suralar: 111-114, 114 dan\n\n111. Al-Masad (سُورَةُ المَسَدِ)\n112. Al-Ikhlaas (سُورَةُ الإِخۡلَاصِ)\n113. Al-Falaq (سُورَةُ الفَلَقِ)\n114. An-Naas (سُورَةُ النَّاسِ)"
sb_10=InlineKeyboardMarkup([[
    InlineKeyboardButton("1",callback_data="1"),
    InlineKeyboardButton("2",callback_data="2"),
    InlineKeyboardButton("3",callback_data="3"),
    InlineKeyboardButton("4",callback_data="4"),
    InlineKeyboardButton("5",callback_data="5"),
    ],[
    InlineKeyboardButton("6",callback_data="6"),
    InlineKeyboardButton("7",callback_data="7"),
    InlineKeyboardButton("8",callback_data="8"),
    InlineKeyboardButton("9",callback_data="9"),
    InlineKeyboardButton("10",callback_data="10"),
    ],[
    InlineKeyboardButton("Keyingi >>",callback_data="su20")
    ]
])
sb_20=InlineKeyboardMarkup([[
    InlineKeyboardButton("11",callback_data="11"),
    InlineKeyboardButton("12",callback_data="12"),
    InlineKeyboardButton("13",callback_data="13"),
    InlineKeyboardButton("14",callback_data="14"),
    InlineKeyboardButton("15",callback_data="15"),
    ],[
    InlineKeyboardButton("16",callback_data="16"),
    InlineKeyboardButton("17",callback_data="17"),
    InlineKeyboardButton("18",callback_data="18"),
    InlineKeyboardButton("19",callback_data="19"),
    InlineKeyboardButton("20",callback_data="20"),
    ]
])
sb_30=InlineKeyboardMarkup([[
    InlineKeyboardButton("21",callback_data="21"),
    InlineKeyboardButton("22",callback_data="22"),
    InlineKeyboardButton("23",callback_data="23"),
    InlineKeyboardButton("24",callback_data="24"),
    InlineKeyboardButton("25",callback_data="25"),
    ],[
    InlineKeyboardButton("26",callback_data="26"),
    InlineKeyboardButton("27",callback_data="27"),
    InlineKeyboardButton("28",callback_data="28"),
    InlineKeyboardButton("29",callback_data="29"),
    InlineKeyboardButton("30",callback_data="30"),
    ]
])
sb_40=InlineKeyboardMarkup([[
    InlineKeyboardButton("31",callback_data="31"),
    InlineKeyboardButton("32",callback_data="32"),
    InlineKeyboardButton("33",callback_data="33"),
    InlineKeyboardButton("34",callback_data="34"),
    InlineKeyboardButton("35",callback_data="35"),
    ],[
    InlineKeyboardButton("36",callback_data="36"),
    InlineKeyboardButton("37",callback_data="37"),
    InlineKeyboardButton("38",callback_data="38"),
    InlineKeyboardButton("39",callback_data="39"),
    InlineKeyboardButton("40",callback_data="40"),
    ]
])
sb_50=InlineKeyboardMarkup([[
    InlineKeyboardButton("41",callback_data="41"),
    InlineKeyboardButton("42",callback_data="42"),
    InlineKeyboardButton("43",callback_data="43"),
    InlineKeyboardButton("44",callback_data="44"),
    InlineKeyboardButton("45",callback_data="45"),
    ],[
    InlineKeyboardButton("46",callback_data="46"),
    InlineKeyboardButton("47",callback_data="47"),
    InlineKeyboardButton("48",callback_data="48"),
    InlineKeyboardButton("49",callback_data="49"),
    InlineKeyboardButton("50",callback_data="50"),
    ]
])
sb_60=InlineKeyboardMarkup([[
    InlineKeyboardButton("51",callback_data="51"),
    InlineKeyboardButton("52",callback_data="52"),
    InlineKeyboardButton("53",callback_data="53"),
    InlineKeyboardButton("54",callback_data="54"),
    InlineKeyboardButton("55",callback_data="55"),
    ],[
    InlineKeyboardButton("56",callback_data="56"),
    InlineKeyboardButton("57",callback_data="57"),
    InlineKeyboardButton("58",callback_data="58"),
    InlineKeyboardButton("59",callback_data="59"),
    InlineKeyboardButton("60",callback_data="60"),
    ]
])
sb_70=InlineKeyboardMarkup([[
    InlineKeyboardButton("61",callback_data="61"),
    InlineKeyboardButton("62",callback_data="62"),
    InlineKeyboardButton("63",callback_data="63"),
    InlineKeyboardButton("64",callback_data="64"),
    InlineKeyboardButton("65",callback_data="65"),
    ],[
    InlineKeyboardButton("66",callback_data="66"),
    InlineKeyboardButton("67",callback_data="67"),
    InlineKeyboardButton("68",callback_data="68"),
    InlineKeyboardButton("69",callback_data="69"),
    InlineKeyboardButton("70",callback_data="70"),
    ]
])
sb_80=InlineKeyboardMarkup([[
    InlineKeyboardButton("71",callback_data="71"),
    InlineKeyboardButton("72",callback_data="72"),
    InlineKeyboardButton("73",callback_data="73"),
    InlineKeyboardButton("74",callback_data="74"),
    InlineKeyboardButton("75",callback_data="75"),
    ],[
    InlineKeyboardButton("76",callback_data="76"),
    InlineKeyboardButton("77",callback_data="77"),
    InlineKeyboardButton("78",callback_data="78"),
    InlineKeyboardButton("79",callback_data="79"),
    InlineKeyboardButton("80",callback_data="80"),
    ]
])
sb_90=InlineKeyboardMarkup([[
    InlineKeyboardButton("81",callback_data="81"),
    InlineKeyboardButton("82",callback_data="82"),
    InlineKeyboardButton("83",callback_data="83"),
    InlineKeyboardButton("84",callback_data="84"),
    InlineKeyboardButton("85",callback_data="85"),
    ],[
    InlineKeyboardButton("86",callback_data="86"),
    InlineKeyboardButton("87",callback_data="87"),
    InlineKeyboardButton("88",callback_data="88"),
    InlineKeyboardButton("89",callback_data="89"),
    InlineKeyboardButton("90",callback_data="90"),
    ]
])
sb_100=InlineKeyboardMarkup([[
    InlineKeyboardButton("91",callback_data="91"),
    InlineKeyboardButton("92",callback_data="92"),
    InlineKeyboardButton("93",callback_data="93"),
    InlineKeyboardButton("94",callback_data="94"),
    InlineKeyboardButton("95",callback_data="95"),
    ],[
    InlineKeyboardButton("96",callback_data="96"),
    InlineKeyboardButton("97",callback_data="97"),
    InlineKeyboardButton("98",callback_data="98"),
    InlineKeyboardButton("99",callback_data="99"),
    InlineKeyboardButton("100",callback_data="100"),
    ]
])
sb_110=InlineKeyboardMarkup([[
    InlineKeyboardButton("101",callback_data="101"),
    InlineKeyboardButton("102",callback_data="102"),
    InlineKeyboardButton("103",callback_data="103"),
    InlineKeyboardButton("104",callback_data="104"),
    InlineKeyboardButton("105",callback_data="105"),
    ],[
    InlineKeyboardButton("106",callback_data="106"),
    InlineKeyboardButton("107",callback_data="107"),
    InlineKeyboardButton("108",callback_data="108"),
    InlineKeyboardButton("109",callback_data="109"),
    InlineKeyboardButton("110",callback_data="110"),
    ]
])
sb_114=InlineKeyboardMarkup([[
    InlineKeyboardButton("111",callback_data="111"),
    InlineKeyboardButton("112",callback_data="112"),
    InlineKeyboardButton("113",callback_data="113"),
    InlineKeyboardButton("114",callback_data="114"),
    ]
])

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
    update.message.reply_text(s_10,reply_markup=sb_10)

def help_command(update,context):
    update.message.reply_text("Buyruqlar:\n/start - Qayta boshlash\n/about - Qur'on haqida\n/surah - Suralar\nMurojaat uchun: @aziz2004official")

def buttons(update,context):
    q=update.callback_query.data
    if "surah"==q:
        update.effective_message.edit_text(s_10,reply_markup=sb_10)
    if "help"==q:
        update.effective_message.edit_text("Buyruqlar:\n/start - Qayta boshlash\n/about - Qur'on haqida\n/surah - Suralar\nMurojaat uchun: @aziz2004official")
    if "su10"==q:
        update.effective_message.edit_text(s_10,reply_markup=sb_10)
    if "su20"==q:
        update.effective_message.edit_text(s_20,reply_markup=sb_20)
    if "su30"==q:
        update.effective_message.edit_text(s_30,reply_markup=sb_30)
    if "su40"==q:
        update.effective_message.edit_text(s_40,reply_markup=sb_40)
    if "su50"==q:
        update.effective_message.edit_text(s_50,reply_markup=sb_50)
    if "su60"==q:
        update.effective_message.edit_text(s_60,reply_markup=sb_60)
    if "su70"==q:
        update.effective_message.edit_text(s_70,reply_markup=sb_70)
    if "su80"==q:
        update.effective_message.edit_text(s_80,reply_markup=sb_80)
    if "su90"==q:
        update.effective_message.edit_text(s_90,reply_markup=sb_90)
    if "su100"==q:
        update.effective_message.edit_text(s_100,reply_markup=sb_100)
    if "su110"==q:
        update.effective_message.edit_text(s_110,reply_markup=sb_110)
    if "su114"==q:
        update.effective_message.edit_text(s_114,reply_markup=sb_114)
    if "1"==q:
        image=("https://t.me/quron_suralar_qiroat/3")
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id,media=[InputMediaAudio(image,caption="")])

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