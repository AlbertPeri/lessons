# names = ["Вин Дизель" , "Д Младший" , "Том Харви"]
# names = iter(names)
# print(names)
# print(next(names))
# print(next(names))
# print(next(names))
# print(next(names))
# while True:
	# try:
	# 	print(next(names))
	# except StopIteration:
	# 	break
# names2 = ["Вин Дизель" , "Д Младший" , "Том Харви"]
# for name in names2:
# 	print(name)


# numbers = [6, 7 ,-9, -16, 5]
# print(len(numbers),
#       sum(numbers),
#       min(numbers),
#       max(numbers),
#       all(numbers),
#       any(numbers))

# liers = ["", False, [], 0, 0, 0.0, 5 < 2]
# print(any(liers))

# good_men = ["ты", "я", "мани"]
# bad_men = ["Саид", "Андрей"]
# for good , bad in zip(good_men, bad_men):
# 	print(good, bad)

# for i, good in enumerate(good_men):
# 	print(i, good)

# numbers = []
# for i in range(1, 17):
# 	if i != 5:
# 		numbers.append(i)
# print(numbers)

# numbers2 = [(i, i) for i in range(1, 17) if i != 5]
# print(numbers2)

# print(range(1, 5))
import random

def giv_number_random(minX, maxX, count):
	i = 0
	while  i < count:
		yield random.randint(minX, maxX)
		i += 1

print(giv_number_random(2, 17, 3))

for i in giv_number_random(2, 17, 100000000):
	print(i)

