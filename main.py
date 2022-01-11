# problem 2. a random walking path
import random as rn
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from statistics import median
from math import sin,cos

walkersnumber = 100000  # commented out since my computer didnt like running that many instances, but you can re-run with it.
b = 10
viable_paths = []


def pathmaker(steps, xpos, ypos, phi, sigma,
              clossness_radius):  # N, initial position, initial bearing φ0, and the standard distribution 𝜎
    phi = (2 * np.pi) / 360  # transference of phi to rads
    xpositions = [xpos]
    ypositions = [ypos]
    foundhome = False
    for k in range(1, steps):
        if foundhome == False:
            ypositions.append(ypositions[-1] + 1 * sin(phi))  # up down
            ypositions[-1] = round(ypositions[-1], 1)
            xpositions.append(xpositions[-1] + 1 * cos(phi))  # left right
            xpositions[-1] = round(xpositions[-1], 1)

            phi = ((phi * 360 / (2 * np.pi) + round((rn.randint(-17, 17)), 3)) * (2 * np.pi) / 360)
            if ((xpositions[-1] - (b)) ** 2) <= clossness_radius ** 2 and (
            ypositions[-1]) ** 2 <= clossness_radius ** 2:
                # print("the walker reached B on step number",k)   #only returns 10 for some reason

                foundhome = True
                plt.plot(xpositions, ypositions)
                return [xpositions, ypositions]

            else:
                pass

    if foundhome == False:
        pass
        # print("they did not find their way home within",maxitterations,"steps" )


for count in range(1, walkersnumber + 1):
    viable_paths.append(pathmaker(40, 0, 0, 110, 17, .1))

plt.plot(0, 0, '*')
plt.show()