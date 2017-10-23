import scipy.stats as stats

class AbscissRange:
    min = 0
    max = 0

    def __init__(self, min, max):
        self.min = min
        self.max = max

class Uniform:
    loc = 0
    scale = 1

    def __init__(self, loc, scale):
        self.loc = loc
        self.scale = scale

    def pdf(self):
        return lambda x : stats.uniform.pdf(x, self.loc, self.scale)

    def absciss_range(self):
        return AbscissRange(self.loc, self.loc + self.scale);

class Param:

    def __init__(self, ids, values):
        assert(len(ids) == len(values)), "Parameter ids and values should have same lenght"
        self.__ids = ids
        self.__values = values
        self.__dim = len(self.__ids)

    def dimension(self):
        return self.__dim;

    def dimensions_ids(self):
        return self.__ids;

    def value(self, id):
        return self.__values[self.__ids.index(id)];
