points    = [(7, 2), (3, 10), (4, 1), (0, 1)]
# points    = [(8, 3), (5, 2), (0, 2), (2, 5), (6, 6)]
points    = sorted(points)
#* будем считать, что наимаеньшая точка -  почтовое отделение
start     = min(points)

def calc_path(first_point, second_point):
    ''' Функция для вычисления расстояния '''
    return ((second_point[0] - first_point[0]) ** 2
            + (second_point[1] - first_point[1]) ** 2) ** 0.5

def find_shortest():
    '''Перебор и суммирование расстояния'''
    calculated_path = 0
    last_point      = 0
    print(start, end=' -> ')
    for now in range(len(points)-1):
        last_point     = now
        next     = now + 1
        now_path = calc_path(points[now], points[next])
        calculated_path += now_path
        print(f"{points[next]}[{calculated_path}]", end=' -> ')
    finish = calculated_path + calc_path(points[last_point], start)
    print(f'{start}, {finish} = {finish}')

if __name__ == '__main__':
    find_shortest()
