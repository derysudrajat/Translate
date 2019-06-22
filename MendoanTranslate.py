from translate import Translator

indoTrans = Translator(to_lang="id")
engTrans = Translator(from_lang="id", to_lang="en")
indoTxt = indoTrans.translate("I have made a new technology company that works in the social field")
engTxt = engTrans.translate(indoTxt)
print("Indo: \n", indoTxt)
print("Eng: \n", engTxt)
