import time
from threading import *


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        count_warrior = 100
        day = 0
        print(f'Sir {self.name}, на нас напали!')
        while count_warrior:
            time.sleep(1)
            day += 1
            count_warrior -= self.skill
            print(f'Sir {self.name}, сражается {day} день(дня)..., осталось {count_warrior} воинов.')
        print(f'Sir {self.name} одержал победу спустя {day} дней!')
