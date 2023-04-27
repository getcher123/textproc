import os
import json
import openai

import logging



from Morph.stopwords import TextProcessor
from Morph.textproc import text_processing


#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def init():
    global tp
    tp = TextProcessor() # class for removing stopwords from text
    return 'Init complete!'


init()

result = text_processing('{"words": "проверить,случай,слово"}', "Проверяем корректные случаи вхождения определенных слов")
print(result)
