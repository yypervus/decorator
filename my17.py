import datetime
import time
import os

def logger(log_path):
    def decorator(is_one_away):
        def new_is_one_away(*args, **kwargs):
            date_today = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
            start = time.time()
            result = is_one_away(*args, **kwargs)
            finish = time.time() - start
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'Имя функции - {is_one_away.__name__}' + '\n')
                f.write(f'Дата и время вызова функции - {date_today}' + '\n')
                f.write(f'Аргументы функции - {args}, {kwargs}' + '\n')
                f.write(f'Результат - {result}' + '\n')
                f.write(f'Время работы функции - {finish}' + '\n')
                f.write(f'Путь к логам - {os.path.abspath(log_path)}')
            return result
        return new_is_one_away
    return decorator




@logger('logs.txt')
def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for j in range(len(word1)):
            if word1[j] == word2[j]:
                count += 1
    if count == len(word1) - 1:
        return True
    else:
        return False



txt1 = 'bike'
txt2 = 'hike'


print(is_one_away(txt1, txt2))