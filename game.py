import random

number = random.randint(1, 101)

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False
    
print('Добро пожаловать в числовую угадайку')
count = 0
while True:
    answer = input('Введите число от 1 до 100: ')
    if not is_valid(answer):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    answer = int(answer)
    
    if answer < number:
        print('Ваше число меньше загаданного, попробуйте еще разок.')
        count +=1
    elif answer > number:
        print('Ваше число больше загаданного, попробуйте еще разок.')
        count +=1
    else:
        print('Вы угадали число за', count, 'попыток, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...') 