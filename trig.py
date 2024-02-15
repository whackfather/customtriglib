# Trigonometry
# v1.0

def pi():
	return 3.141592653589793

def fact(x):
	factorial = 1
	for i in range(1, x + 1):
		factorial = factorial * i
	return factorial

def rsin(x):
	if x == 0 or x == pi():
		return 0
	elif x == pi() / 2:
		return 1
	elif x == -pi() / 2:
		return -1
	else:
		x_sign = x / abs(x)
		while True:
			if -pi() <= x <= pi():
				break
			elif x_sign == 1:
				x -= 2 * pi()
			elif x_sign == -1:
				x += 2 * pi()
		sine = x - ((x ** 3) / (fact(3))) + ((x ** 5) / (fact(5))) - ((x ** 7) / (fact(7))) + ((x ** 9) / (fact(9))) - ((x ** 11) / (fact(11)))
		return round(sine, 6)

def rcos(x):
	if x == pi() / 2 or x == -pi() / 2:
		return 0
	elif x == pi():
		return 1
	elif x == -pi():
		return -1
	else:
		x_sign = x / abs(x)
		while True:
			if -pi() <= x <= pi():
				break
			elif x_sign == 1:
				x -= 2 * pi()
			elif x_sign == -1:
				x += 2 * pi()
		cosine = 1 - ((x ** 2) / (fact(2))) + ((x ** 4) / (fact(4))) - ((x ** 6) / (fact(6))) + ((x ** 8) / (fact(8))) - ((x ** 10) / (fact(10))) + ((x ** 12) / (fact(12)))
		return round(cosine, 6)

def rtan(x):
	return rsin(x) / rcos(x)

def rcsc(x):
	return 1 / rsin(x)

def rsec(x):
	return 1 / rcos(x)

def rcot(x):
	return 1 / rtan(x)

def dsin(x):
	x *= (pi() / 180)
	if x == 0 or x == pi():
		return 0
	elif x == pi() / 2:
		return 1
	elif x == -pi() / 2:
		return -1
	else:
		x_sign = x / abs(x)
		while True:
			if -pi() <= x <= pi():
				break
			elif x_sign == 1:
				x -= 2 * pi()
			elif x_sign == -1:
				x += 2 * pi()
		sine = x - ((x ** 3) / (fact(3))) + ((x ** 5) / (fact(5))) - ((x ** 7) / (fact(7))) + ((x ** 9) / (fact(9))) - ((x ** 11) / (fact(11)))
		return round(sine, 6)

def dcos(x):
	x *= (pi() / 180)
	if x == pi() / 2 or x == -pi() / 2:
		return 0
	elif x == pi():
		return 1
	elif x == -pi():
		return -1
	else:
		x_sign = x / abs(x)
		while True:
			if -pi() <= x <= pi():
				break
			elif x_sign == 1:
				x -= 2 * pi()
			elif x_sign == -1:
				x += 2 * pi()
		cosine = 1 - ((x ** 2) / (fact(2))) + ((x ** 4) / (fact(4))) - ((x ** 6) / (fact(6))) + ((x ** 8) / (fact(8))) - ((x ** 10) / (fact(10))) + ((x ** 12) / (fact(12)))
		return round(cosine, 6)

def dtan(x):
	return dsin(x) / dcos(x)

def dcsc(x):
	return 1 / dsin(x)

def dsec(x):
	return 1 / dcos(x)

def dcot(x):
	return 1 / dtan(x)
