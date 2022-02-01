from sprites.Ammunition.Ammunition import *


class Helmet1(Ammunition):
    def __init__(self):
        super().__init__(texture='оружие_43.png', slot='head')


class Helmet2(Ammunition):
    def __init__(self):
        super().__init__(texture='оружие_44.png', slot='head')


class Helmet3(Ammunition):
    def __init__(self):
        super().__init__(texture='оружие_45.png', slot='head')


class Bib1(Ammunition):
    def __init__(self):
        super().__init__(texture='оружие_42.png', slot='chest')


class Bib2(Ammunition):
    def __init__(self):
        super().__init__(texture='оружие_41.png', slot='chest')
