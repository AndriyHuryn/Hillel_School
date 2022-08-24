"""
Закончить приклад з уроку.
Зробити так, щоб 2 ракети запускались паралельно"""

from random import randint, random
from time import sleep
from threading import Thread


def get_random_delay():
    """
    Just return radom value from 0 to 2.
    Represents seconds of delay.
    """
    return random() * randint(1, 2)


def get_random_countdown():
    """Just return integer in range 1 <= N <= 5."""
    return randint(3, 7)


class Rocket:
    """
    This class is responsible for running rockets.
    Every rocket has its own delay and countdown.
    """

    def __init__(self, name) -> None:
        self.delay = get_random_delay()
        self.countdown = get_random_countdown()
        self.name = name

    def _countdown(self):
        """Human-base countdown."""

        for i in range(self.countdown + 1, 0, -1):
            print(f"{i}...")
            sleep(1)

    def _delay(self):
        print(f"🕐 Delay for {self.delay} seconds...")
        sleep(self.delay)

    def run(self):
        # Do the countdown before start the rocket
        print(f"\nPrepare the {self.name} ✅")
        self._countdown()

        # Check the delay
        self._delay()

        # Show success message
        print("🚀 Rocket go to the moon...")


def main():
    r1 = Rocket(name="Apollo 1")
    r2 = Rocket(name="Apollo 2")

    t1 = Thread(target=r1.run)
    t2 = Thread(target=r2.run)

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()

