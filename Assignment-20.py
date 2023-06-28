from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def mul(self):
        pass

    @abstractmethod
    def div(self):
        pass


class Phone_Calculator(Calculator):

    def add(self, a, b):

        self.a = a

        self.b = b

        print(f"Sum is {self.a+self.b}")

    def sub(self, a, b):

        self.a = a

        self.b = b

        print(f"Diffrence is {self.a-self.b}")

    def mul(self, a, b):

        self.a = a

        self.b = b
        print(f"Product is {self.a*self.b}")

    def div(self, a, b):

        self.a = a

        self.b = b
        print(f"Quotient is {self.a/self.b}")


if __name__ == '__main__':
    a = int(input("Number 1 "))
    b = int(input("Number 2 "))
    obj = Phone_Calculator()
    obj.add(a, b)
    obj.sub(a, b)
    obj.mul(a, b)
    obj.div(a, b)
