from translate import Translator

trans = Translator(to_lang="ja")
with open("C:/Users/foxhe/OneDrive/Desktop/Frog Detective.txt", mode="r") as my_file:
    text = my_file.read()
    res = trans.translate(text)


with open("files/translated.txt", mode="a", encoding="utf-8") as my_file:
    my_file.write(res)
