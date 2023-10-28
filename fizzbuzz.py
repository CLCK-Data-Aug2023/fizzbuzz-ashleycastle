for num in range(1,101):
    if num % 3 == 0:
        print("fizz")
    if num % 5 == 0:
        print("buzz")
    if num % 5 == 0 and num % 3 == 0:
        print("fizzbuzz")
    if num % 5 != 0 and num % 3 != 0:
        print(num)
