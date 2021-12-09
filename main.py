def mean(numbers):
    total = 0
    for i in numbers:
        total += int(i)
    return total / len(numbers)


def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        index_1 = (len(numbers) / 2) + 1
        index_2 = ((len(numbers) + 1) / 2) + 1
        return int(numbers[index_1]) + int(numbers[index_2]) / 2
    else:
        index = ((len(numbers) + 1) / 2) + 1
        return int(numbers[index])


def mode(numbers):
    max = [0, 0]
    for i in numbers:
        amount = numbers.count(i)
        if amount > max[0]:
            max = [amount, i]
    return int(max[1])


while True:
    input_value = input("Please state what operation you would like to use |Mean| |Median| |Mode|\n").lower()

    if input_value == "quit":
        break

    numbers = input("Enter your numbers (Separate with blank spaces)\n").split(" ")

    if input_value == "mean":
        print(mean(numbers))
    elif input_value == "median":
        print(median(numbers))
    elif input_value == "mode":
        print(mode(numbers))

