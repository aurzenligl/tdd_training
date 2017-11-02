class numtup(tuple):
    def __add__(self, other):
        if isinstance(other, tuple):
            assert len(self) == len(other)
            return tuple(lhs + rhs for lhs, rhs in zip(self, other))
        return tuple(lhs + other for lhs in self)

    def __mul__(self, other):
        if isinstance(other, tuple):
            assert len(self) == len(other)
            return tuple(lhs * rhs for lhs, rhs in zip(self, other))
        return tuple(lhs * other for lhs in self)
