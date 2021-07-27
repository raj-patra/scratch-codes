__author__ = "github.com/raj-patra"

import pyautogui as pg
import time

def no_sleep():
    (X, Y) = pg.position(pg.size()[0]/2, pg.size()[1]/2)

    pg.moveTo(X, Y)

    while True:
        pg.moveTo(X+50, Y, duration=1)
        pg.click()
        time.sleep(30)

        pg.moveTo(X-50, Y, duration=1)
        pg.click()
        time.sleep(30)

if __name__ == '__main__':
    time.sleep(1)
    no_sleep()
