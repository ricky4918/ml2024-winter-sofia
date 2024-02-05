def find_x_index():
    
    N = int(input("Enter a positive integer N: "))
    numbers = []
    for i in range(N):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    X = int(input("Enter an integer X: "))
    if X in numbers:
        index = numbers.index(X) + 1
        print(f"The index of {X} is: {index}")
    else:
        print("-1")


find_x_index()
