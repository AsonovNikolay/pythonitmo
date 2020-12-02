import random

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, x):
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def remove(self, pos):
        if self.first == None:
            return
        current = self.first
        count = 0
        if pos == 0:
            self.first = self.first.next
            return
        while current != None:
            if count == pos:
                if current.next == None:
                    self.last = current
                old.next = current.next
                break
            old = current
            current = current.next
            count += 1

    def transform(self):
        if self.first == None:
            return self.list
        self.list = []
        current = self.first
        while current != None:
            self.list.append(current.value)
            current = current.next
        return self.list

    def clear(self):
        self.__init__()

class Country:
    def __init__(self, name="No_DATA", capital="NO_DATA", population="NO_DATA", confession="NO_DATA"):
        self.name = name
        self.capital = capital
        self.population = population
        self.confession = confession

    def __str__(self):
        return "Страна " + self.name + " со столицей в городе " + self.capital + " и населением в " + self.population + " человек, которое исповедует " + self.confession


if __name__ == "__main__":

    numbers = MyQueue()
    for i in range(10):
        numbers.add(random.randint(0, 10))
    print(numbers.transform())

    countries = [Country("Russia", "Moscow", "140m"), Country("USA", "Washington"), Country("UK", "London")]
    countrie = MyQueue()
    for i in countries:
        countrie.add(i.__str__())
    for x in countrie.transform():
        print(x)
