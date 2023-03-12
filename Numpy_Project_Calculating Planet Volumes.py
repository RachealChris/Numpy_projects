'''In this project, we shall be utilizing NumPy to perform mathematical calculations to get various planet volumes at one time'''

#We start by importing the numpy package into the IDE
import numpy as np

#Calculating the planets volumes: We start by creating a variable that will contain all the radii for the various planets

radii = np.array([2439.7, 6051.8, 3389.7, 69911, 58232, 25362, 24622])
print(radii)

# Creating a variable volume that contains the calculations 
volumes = 4/3 * np.pi * radii**3
print(volumes)

#Bonus: Calculating the volumes of random integers 

numbers = np.random.randint(10, 100, 1000000)
print(numbers)
volume = 4/3 * np.pi * numbers**3
print(volume)

'''We can ideally use loops in python to get similar results, but Numpy is faster and more efficient'''

#Using for loops to calculate the volumes 

radii = [2439.7, 6051.8, 3389.7, 69911, 58232, 25362, 24622]

for i in radii:
    volume = 4/3 * np.pi * i**3
print(i, volume)

#Bonus: Using random numbers
number =  range(1,100,2)
print(number)

for i in number:
    volume = 4/3 * np.pi * i**3
print(volume)