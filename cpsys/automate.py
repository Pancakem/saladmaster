import datetime 
import time

class StartTime:
	start = 0.0
	def __init__(self):
		start = time.time()

current = 2
def automate(maxi, startobj, timedelta):
	global current
	#timedelta = timedelta 
	now = time.time()
	if (now - startobj.start) <= timedelta:
		if current >= maxi:
			return True

	else:
		current = 0
		return False



if __name__ == "__main__":
	a = StartTime()
	time.sleep(5)
	print(automate(3, a, 10))
	