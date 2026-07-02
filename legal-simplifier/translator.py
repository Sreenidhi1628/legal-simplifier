from deep_translator import GoogleTranslator

def translate_to_tamil(text):
    try:
        translated = GoogleTranslator(source='en', target='ta').translate(text)
        return translated
    except:
        return text

def translate_to_malayalam(text):
    try:
        translated = GoogleTranslator(source='en', target='ml').translate(text)
        return translated
    except:
        return text