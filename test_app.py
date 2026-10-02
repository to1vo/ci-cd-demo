from app import add, subtract, describe_temperature


def test_add() -> None:
	assert add(2, 3) == 5

def test_subtract() -> None:
	assert subtract(2, 1) = 1

def test_temperature_boundaries() -> None:
	assert describe_temperature(-1) == "freezing"
	assert describe_temperature(0) == "cool"
	assert describe_temperature(15.9) == "cool"
	assert describe_temperature(16) == "warm"
