import string
from src.core.job.mapper import Mapper

class WordCountMapper(Mapper):
    def map(self, record, emit):
        # Набір голосних для 3-го завдання
        vowels = set("aeiouyаеєиіїоуюя")
        
        # Видаляємо пунктуацію
        translator = str.maketrans('', '', string.punctuation)
        clean_record = str(record).translate(translator)

        for token in clean_record.split():
            clean_token = token.lower()
            if not clean_token:
                continue
            
            # Завдання 1: Порахувати всі слова без розділових знаків
            emit(f"Task1_{clean_token}", 1)

            # Завдання 2: Порахувати слова довжиною > 5 символів
            if len(clean_token) > 5:
                emit(f"Task2_{clean_token}", 1)

            # Завдання 3: Підрахунок голосних/приголосних за довжиною слова
            v_count = 0
            c_count = 0
            for char in clean_token:
                if char.isalpha():
                    if char in vowels:
                        v_count += 1
                    else:
                        c_count += 1
            
            if v_count > 0 or c_count > 0:
                length = len(clean_token)
                emit(f"Task3_{length}", (v_count, c_count))