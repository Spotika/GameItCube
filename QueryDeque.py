from collections import deque


class QueryDeque:
    """
    самопальная очередь вызовов против рекурсии
    """

    queryDeque = deque()  # самопальный стек вызовов приложений
    """хранит (объект, *args, **kwargs)"""

    @classmethod
    def add(cls, obj, *args, **kwargs):
        """добавляет запрос в очередь принимая аргументы"""
        cls.queryDeque.append((obj, args, kwargs))

    @classmethod
    def do_next(cls):
        """выполняет следующий запрос и передаёт аргументы"""
        currentApp, args, kwargs = cls.queryDeque.pop()
        currentApp.begin(*args, **kwargs)

    @classmethod
    def is_empty(cls):
        return len(cls.queryDeque) == 0
