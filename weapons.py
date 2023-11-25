class Weapons:
    def __init__(self, weapons_array):
        self.name = weapons_array[0]
        self.price = weapons_array[1]
        self.min_range = weapons_array[2]
        self.max_range = weapons_array[3]
        self.weight = weapons_array[4]
        self.dmg_type = weapons_array[5]
        self.property = weapons_array[6]
        self.hit_die_num = weapons_array[7]
        self.hit_die_type = weapons_array[8]
        self.v_die_num = weapons_array[9]
        self.v_die_type = weapons_array[10]
