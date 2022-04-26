# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math as math
from decimal import Decimal

import PITEST


def calculatepi():
    pi = 2 * math.acos(0.0);
    pirounded=round(pi, 10);
    return pirounded

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculatepi())
    print(round(math.pi,10))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
