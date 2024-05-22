def MyGenerator(numbers: list[int]):
    for number in numbers:
        yield number * 2

for i in MyGenerator(numbers=[1,2,3]):
    print(i)