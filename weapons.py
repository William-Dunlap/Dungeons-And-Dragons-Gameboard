class Weapons:
    def __init__(self, weapons_arr):
        self.price = weapons_arr[0]
        self.min_range = weapons_arr[1]
        self.max_range = weapons_arr[2]
        self.weight = weapons_arr[3]
        self.dmg_type = weapons_arr[4]
        self.property = weapons_arr[5]
        self.hit_die_num = weapons_arr[6]
        self.hit_die_type = weapons_arr[7]
        self.v_die_num = weapons_arr[8]
        self.v_die_type = weapons_arr[9]
