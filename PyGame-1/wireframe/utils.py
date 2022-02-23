import math

def cart_to_polar(cx, cy, x, y):
	d = math.hypot(y - cy, x - cx)
	theta = math.atan2(y - cy, x - cx)
	return (theta, d)
