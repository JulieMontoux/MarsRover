class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def deplacer(self, dx, dy, planete):
        new_x = (self._x + dx) % planete[0]
        new_y = (self._y + dy) % planete[1]
        return Position(new_x, new_y)

    def get_coords(self):
        return self._x, self._y

    def __repr__(self):
        return f"Position(x={self._x}, y={self._y})"