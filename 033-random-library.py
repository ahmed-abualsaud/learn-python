import random as rand

print("Random number between 0  and 1:", rand.random())

print("Random number between 1 and 10:", rand.uniform(1, 10))

print("Random integer between 0 and 100:", rand.randrange(100))

print("Random integer between 10 and 100:", rand.randint(10, 100))

print("Random integer from the even number between 50 and 100:", rand.randrange(50, 100, 2))

print("Random integer between 50 and 100 that is a multiple of 5:", rand.randrange(50, 100, 5))


print('\n')


countries = ['Egypt', 'Saudi Arabia', 'Sudan', 'Lybia', 'Jordan', 'Syria']

print("Countries:", countries)

print("Random choice from the countirs list is:", rand.choice(countries) )


print('\n')


population = range(100)

sample = rand.sample(population, 10)

print("Integers Population:", list(population))
print('\n')
print("Sample of 10 elements from the population is:", sample)


print('\n')


population = [rand.uniform(0, 100) for i in range(100)] # get 100 numbers (not just integers) between 0 and 100

sample = rand.sample(population, 10)

print("Numbers Population:", list(population))
print('\n')
print("Sample of 10 elements from the population is:", sample)


print('\n')

rand.shuffle(sample)

print("Shuffle the sample: ", sample)