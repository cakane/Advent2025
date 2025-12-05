class Door:
    def __init__(self, starting_pos=50, numbers=100):
        self.pos = starting_pos
        self.cross_zero_count = 0

    def rot_right(self, distance):
        for i in range(distance):
            self.pos += 1
            if self.pos > 99:
                self.pos = 0

            # Track 0 crossing here
            if self.pos == 0:
                self.cross_zero_count += 1

    def rot_left(self, distance):
        for i in range(distance):
            self.pos -= 1
            if self.pos < 0:
                self.pos = 99
            
            # Track 0 crossing here
            if self.pos == 0:
                self.cross_zero_count += 1


if __name__ == "__main__":
    door = Door(50, 100)
    door.rot_right(10)
    door.rot_left(80)
    print(door.cross_zero_count)
