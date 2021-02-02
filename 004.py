class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\n {self.name} остановка.'

    def turn(self, direction):
        return f'\n {self.name} поворот на {direction}.'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревышаете! Ваша скорость: {self.speed}'
        else:
            return f'Нормальная скорость: {self.name}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревышаете! Ваша скорость: {self.speed}'
        else:
            return f'Нормальная скорость: {self.name} '


class PoliceCar(Car):
    pass


town = TownCar('VAZ Kalina', 70, 'голубой', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar('Lada Raven', 200, 'красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('лево'), sport.stop())

police = PoliceCar('UAZ', 50, 'зелёный', True)
print('3:\n' + police.go(), police.show_speed(), police.turn('право'), police.turn('право'), police.stop())

work = WorkCar('Ford', 40, 'белый', False)
print('4:\n' + work.go(), work.show_speed(), work.turn('право'), work.stop())
