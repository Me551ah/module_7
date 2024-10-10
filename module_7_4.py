name_team1 = 'Мастера кода'
name_team2 = "Волшебники Данных"
team1_num, team2_num = 5, 6
score_1, score_2 = 40, 42
team1_time, team2_time = 1552.512, 2153.31451

# Использование %
print('В команде Мастера кода участников: %d!' % team1_num)
print('В команде Мастера кода участников: %d!' % team2_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))
print()

# Использование format()
print('Команда {} решила задач: {} !'.format(name_team1, score_1))
print('{} решили задачи за {:.1f} с!'.format(name_team1, team1_time))
print('Команда {} решила задач: {} !'.format(name_team2, score_2))
print('{} решили задачи за {:.1f} с!'.format(name_team2, team2_time))
print()

# Использование f-строк
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
challenge_result = ('Пока мы не знаем какая команда победила, но сейчас мы её определим при помощи условных операторов.'
                    'Для этого напишем функцию, которая не будет принимать никаких аргументов,'
                    'но будет возвращать строку с условным названием команды победителя.')


def win() -> str:
    if team1_time / score_1 / team1_num < team2_time / score_2 / team2_num:
        result = f'Победа команды {name_team1}!'
    elif team1_time / score_1 / team1_num > team2_time / score_2 / team2_num:
        result = f'Победа команды {name_team2}!'
    else:
        result = 'Ничья!'
    return result


print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {win()}')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg:.1f} секунды на задачу!.')

