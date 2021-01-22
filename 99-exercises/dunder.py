class adder:

    # magiic method
    def __init__(self, number):
        self.number = number

    def __add__(self, num):
        return self.number + num

if __name__ == '__main__':
    add = adder(3)
    result = add + 5;
    print(result)