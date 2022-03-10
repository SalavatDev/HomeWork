# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, a=0, ib=0):
        self.a = a
        self.ib = ib

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.ib + other.ib)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.ib * other.ib, self.a * other.ib + self.ib * other.a)

    def __str__(self):
        if self.ib < 0:
            return f'{self.a}{self.ib}*i'
        else:
            return f'{self.a} + {self.ib}*i'


z1 = ComplexNumber(7, 2)
z2 = ComplexNumber(3, -4)

print(z1 + z2)
print(z1 * z2)
