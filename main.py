from googletrans import Translator

translator = Translator()

name = "PDF merge"
shortdesc = "Easy to use PDF merge and opener app"
fulldesc= "Easy to use PDF merge and opener app \nWith the help of this app, you can create a pdf by merging different kind of files like PDF, image, web page. Moreover, the app provides you to share, archive the created PDF files. \nAnother great advantage of the app is to open the merged pdfs which means it is NOT needed to install any other software to open the files. However, it is also possible to open the file with different applications too. \nYou can create PDF from text or scanning a document too.\nYou are able to rearrange files.\nHere is the main functionalities:\n1. Merge PDFs\n2. Create PDF from image\n3. Open PDF inside the app\n4. Rearrange the files\n5. Compress files\n6. Encrypt created PDF documents."
strings_tranlate1 = ["af", "sq", "am", "hy", "az", "ca", "zh-tw", "zh-cn", "hr", "cs", "da", "nl", "et", "fi", "fr",
                     "gl", "ka", "de", "el", "gu", "iw", "hi", "hu", "is", "id", "it", "ja", "kn", "kk", "km", "ko",
                     "ky", "lo", "lv"]
strings_playconsole1 = ["af", "sq", "am", "hy-AM", "az-AZ", "ca", "zh-TW", "zh-CN", "hr", "cs-CZ", "da-DK", "nl-NL",
                        "et", "fi-FI", "fr-FR", "gl-ES", "ka-GE", "de-DE", "el-GR", "gu", "iw-IL", "hi-IN", "hu-HU",
                        "is-IS", "id", "it-IT", "ja-JP", "kn-IN", "kk", "km-KH", "ko-KR", "ky-KG", "lo-LA", "lv"]
print(len(strings_playconsole1))
print(len(strings_tranlate1))
for i in range(34):
    name_trans1 = translator.translate(name, strings_tranlate1[i]).text
    shortdesc_trans1 = translator.translate(shortdesc, strings_tranlate1[i]).text
    fulldesc_trans1 = translator.translate(fulldesc,strings_tranlate1[i]).text
    if len(name_trans1) <= 30 and len(shortdesc_trans1) <= 80:
      print("{`\"1`\":`\""+strings_playconsole1[i]+"`\",`\"3`\":`\""+name_trans1+"`\",`\"4`\":`\""+fulldesc_trans1+"`\",`\"5`\":`\""+shortdesc_trans1+"`\"},",end="")

strings_tranlate2 = ["sr", "si", "sk", "sl", "es", "sw", "sv", "ta", "th", "tr", "uk", "ur", "vi", "zu", "ru"]
strings_playconsole2 = ["sr", "si-LK", "sk", "sl", "es-ES", "sw", "sv-SE", "ta-IN", "th", "tr-TR", "uk", "ur", "vi","zu", "ru-RU"]
for i in range(15):
    name_trans2 = translator.translate(name, strings_tranlate2[i]).text
    shortdesc_trans2 = translator.translate(shortdesc, strings_tranlate2[i]).text
    fulldesc_trans2 = translator.translate(fulldesc,strings_tranlate2[i]).text
    if len(name_trans2) <= 30 and len(shortdesc_trans2) <= 80:
     print("{`\"1`\":`\""+strings_playconsole2[i]+"`\",`\"3`\":`\""+name_trans2+"`\",`\"4`\":`\""+fulldesc_trans2+"`\",`\"5`\":`\""+shortdesc_trans2+"`\"},",end="")

strings_tranlate3 = ["ms", "ml", "mr", "mn", "ne", "no", "pl", "pt"]
strings_playconsole3 = ["ms", "ml-IN", "mr-IN", "mn-MN", "ne-NP", "no-NO", "pl-PL", "pt-BR"]

for i in range(10):
    name_trans3 = translator.translate(name, strings_tranlate3[i]).text
    shortdesc_trans3 = translator.translate(shortdesc, strings_tranlate3[i]).text
    fulldesc_trans3 = translator.translate(fulldesc, strings_tranlate3[i]).text
    if len(name_trans3) <= 30 and len(shortdesc_trans3) <= 80:
        print("{`\"1`\":`\"" + strings_playconsole3[i] + "`\",`\"3`\":`\"" + name_trans3 + "`\",`\"4`\":`\"" + fulldesc_trans3 + "`\",`\"5`\":`\"" + shortdesc_trans3 + "`\"},")
