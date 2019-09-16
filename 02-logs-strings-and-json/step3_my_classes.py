class Hitting:
    hits = 0
    outs = 0
    total = 0

    def add_hit(self):
        self.hits += 1
        self.total += 1

    def add_out(self):
        self.outs += 1
        self.total += 1

    def __str__(self):
        return f'{self.hits} {self.outs} {self.total}'

    def bat_avg(self):
        return float(self.hits) / float(self.total)
