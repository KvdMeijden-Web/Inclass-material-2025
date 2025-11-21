class Calculator:
    def __init__(self, num_list):
        self.numbers = num_list

    def sum(self):
        total = 0
        for n in self.numbers:
            total += n
        return total

    def average(self):
        return self.sum() / len(self.numbers)

    def max(self):
        m = self.numbers[0]
        for n in self.numbers:
            if n > m:
                m = n
        return m
