from googletrans import Translator


def Process(text):
    transaltion = Translator()
    print(transaltion.translate(text,dest='en').text)