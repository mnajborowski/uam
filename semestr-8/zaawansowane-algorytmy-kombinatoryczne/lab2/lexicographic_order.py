class LexicographicOrder:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def __can_increment(self, string):
        for index, element in list(enumerate(string)):
            if element != self.__max_value_of_element(index):
                return True
            return False

    def __increment(self, string):
        for index, element in reversed(list(enumerate(string))):
            if element < self.__max_value_of_element(index):
                string[index] = element + 1
                for subindex, _ in list(enumerate(string[index:])):
                    try:
                        string[index + subindex + 1] = string[index + subindex] + 1
                    except IndexError:
                        pass
                break

    def __max_value_of_element(self, index):
        return index + self.n - self.k + 1

    def print(self):
        string = [i for i in range(1, self.k + 1)]
        while self.__can_increment(string):
            print(*string, sep=" ")
            self.__increment(string)
        print(*string, sep=" ")


class AntilexicographicOrder:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def __can_increment(self, string):
        for index, element in reversed(list(enumerate(string))):
            if element != self.__max_value_of_element(index):
                return True
            return False

    def __increment_and_reduce_right(self, string, index):
        string[index] = string[index] + 1
        for subindex, _ in list(enumerate(string[index:])):
            try:
                string[index + subindex + 1] = self.__min_value_of_element(index + subindex + 1)
            except IndexError:
                pass

    def __increment_and_print(self, string):
        for index, _ in reversed(list(enumerate(string))):
            if index > 0:
                if string[index] < self.__max_value_of_element(index) and string[index - 1] - string[index] >= 2:
                    self.__increment_and_reduce_right(string, index)
                    break
            else:
                if string[index] < self.__max_value_of_element(index):
                    self.__increment_and_reduce_right(string, index)
                    break

    def __max_value_of_element(self, index):
        return self.n - index

    def __min_value_of_element(self, index):
        return self.k - index

    def print(self):
        string = [i for i in range(self.k, 0, -1)]
        print(*string, sep=" ")
        while self.__can_increment(string):
            self.__increment_and_print(string)
            print(*string, sep=" ")


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    assert 1 <= n <= 10
    assert 1 <= k <= n
    LexicographicOrder(n, k).print()
