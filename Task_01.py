#2) Морской бой.

from random import randint

pole_warships = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

for i in pole_warships:
    print(i)

pole_warships[randint(0, 2)][randint(0, 2)] = 2

def hit(fire_x, fire_y):
    if 0 <= fire_x and fire_y <= 2:
        if hit == 2:
            return 'Попадание'
        else:
            return 'Промах'
    else:
        return 'Таких координат не существует, попробуйте ещё!'

fire_x = int(input('Введите координату по оси X от 0 до 2: '))
fire_y = int(input('Введите координату по оси Y от 0 до 2: '))

hit = pole_warships[fire_x] [fire_y]

print(hit)
