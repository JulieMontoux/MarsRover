class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self, dx, dy, planete):
        self.x = (self.x + dx) % planete[0]
        self.y = (self.y + dy) % planete[1]

    def get_coords(self):
        return self.x, self.y

