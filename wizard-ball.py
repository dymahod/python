import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как Вас зовут? ')
print('Привет,', name)

again = 'д'

while again.lower() == 'д':
    question = input('Задай мне свой вопрос: ')
    if question == '':
        print('Введите вопрос!')
    else:   
        print(random.choice(answers))
        again = input('Задать еще один вопрос? (д = да, н = нет): ')
    
        if not again.lower() == 'д':
            print('Возвращайся, если возникнут вопросы!')