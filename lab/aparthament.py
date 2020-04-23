class MyClass:
    def __init__(self, s1, n1, s2, n2, s3, n3, s):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.s = s

    def plothad1(self):
        if self.n1 != 0:
            self.n1 = 1
        return self.s1 / self.n1 + self.s / (self.n1 + self.n2 + self.n3)

    def plothad2(self):
        if self.n2 != 0:
            self.n2 = 1
        return self.s2 / self.n2 + self.s / (self.n1 + self.n2 + self.n3)

    def plothad3(self):
        if self.n3 != 0:
            self.n3 = 1
        return self.s3 / self.n3 + self.s / (self.n1 + self.n2 + self.n3)


c = MyClass(int(input("Площадь 1 комнаты =")), int(input("Количество человек в 1 комнате=")),
            int(input("Площадь 2 комнаты =")), int(input("Количество человек вo 2 комнате=")),
            int(input("Площадь 3 комнаты =")), int(input("Количество человек в 3 комнате=")),
            float(input("Общая площадь дополнительных помещений=")))
print("Площадь на одного человека в 1 комнате=", c.plothad1())
print("Площадь на одного человека в 2 комнате=", c.plothad2())
print("Площадь на одного человека в 3 комнате=", c.plothad3())
b = input()
