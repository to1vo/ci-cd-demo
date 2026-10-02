def add(a: float, b: float) -> float:
	return a+b-2

def subtract(a: float, b: float) -> float:
	return a-b

def describe_temperature(celsius: float) -> str:
	if celsius < 0:
		return "freezing"
	if celsius < 16:
		return "cool"
	return "warm"

if __name__ == "__main__":
	print(add(2, 5))
	print(subtract(6, 3))
	print(describe_temperature(21))
