from src.core.job.reducer import Reducer

class WordCountReducer(Reducer):
    def reduce(self, key, values, emit):
        # Визначаємо, до якого завдання належить поточний ключ
        if key.startswith("Task1_") or key.startswith("Task2_"):
            # Для завдань 1 і 2 логіка незмінна: просто сумуємо входження
            emit(key, sum(values))
            
        elif key.startswith("Task3_"):
            # Для завдання 3 обчислюємо відсотки голосних та приголосних
            total_vowels = 0
            total_consonants = 0
            
            for v, c in values:
                total_vowels += v
                total_consonants += c
                
            total_letters = total_vowels + total_consonants
            
            if total_letters > 0:
                v_percent = (total_vowels / total_letters) * 100
                c_percent = (total_consonants / total_letters) * 100
                
                emit(key, f"{v_percent:.0f}% голосних, {c_percent:.0f}% приголосних")