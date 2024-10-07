# print("привет, " + "мир!")
# print('меня зовут %(name)s, мне %(year)s' % {'name': 'денис', 'year': 14})
# print('Я учусь в {title}{postfix} {title}'.format(title="Урбан", postfix='-university'))
# print(f'{"Urban" * 2} это лучший университет')

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg =  ((team1_time / score_1) + (team2_time / score_2)) / 2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challange_result = result


team1 = 'В команде Мастера кода: %s!' % team1_num
all_teams = 'Итого в командах участников: %s и %s!' % (team1_num, team2_num)
team2_score = 'Команда Волшебники данных решила задач: {}!'.format(score_2)
time_team1 = 'Волшебники данных решили задачи за {}c!'.format(team1_time)

print(team1)
print(all_teams)
print(team2_score)
print(time_team1)
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challange_result}!')
print(f'Сегодня было решено {tasks_total}, в среднем по {time_avg} секунды на задачу')



