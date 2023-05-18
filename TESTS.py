class Test:
    _x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


t = Test()

t.x = 10

a = t.x

print(t.x)

t.x = 20

print(a)
