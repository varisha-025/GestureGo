import googletrans
from googletrans import Translator


class GoogleTranslate:

    def __init__(self):
        self.translator = Translator()
        self.languages= googletrans.LANGUAGES

    def get_language_code(self,language):
        for key, value in self.languages.items():
            if value.lower() == language.lower():
                return key

    def detect_language(self,text):
        lang_code = self.translator.detect(text).lang
        return self.languages[lang_code]

    def translate_to_en(self,text, dest='en'):
        return self.translator.translate(text, dest=dest).text

    def translate_to_lang(self,text, lang):
        dest = self.get_language_code(lang)
        return self.translator.translate(text, dest=dest).text
