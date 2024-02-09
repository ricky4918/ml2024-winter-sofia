class TrackNumber:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        for i in range(n):
            num = int(input("Enter number {}: ".format(i + 1)))
            self.numbers.append(num)

    def find_index(self, x):
        for i, num in enumerate(self.numbers):
            if num == x:
                return i + 1
        return -1


def main():
    n = int(input("Enter the number of elements (N): "))
    tracker = TrackNumber()
    tracker.read_numbers(n)

    x = int(input("Enter the number to search (X): "))

    index = tracker.find_index(x)

    if index == -1:
        print("-1")
    else:
        print("Index of {} is: {}".format(x, index))


if __name__ == "__main__":
    main()
    