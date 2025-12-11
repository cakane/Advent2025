#wtf is this

from pathlib import Path
import time 

class Door:
    def __init__(self, starting_pos=50, numbers=100):
        self.pos = starting_pos
        self.cross_zero_count = 0
        self.click = 0

    def rot_right(self, distance):
        for i in range(distance):
            self.click += 1
            self.pos += 1
            if self.pos > 99:
                self.pos = 0

            # Track 0 crossing here
            if self.pos == 0:
                self.cross_zero_count += 1

    def rot_left(self, distance):
        for i in range(distance):
            self.click += 1
            self.pos -= 1
            if self.pos < 0:
                self.pos = 99
            
            # Track 0 crossing here
            if self.pos == 0:
                self.cross_zero_count += 1

start = time.time()
if __name__ == "__main__":
    door = Door(50, 100)

    for line in Path("./document.txt").read_text().splitlines():
        dr = line[0]
        dt = int(line[1:])
        if dr == 'R':
            door.rot_right(dt)
        elif dr == 'L':
            door.rot_left(dt)

    print(door.cross_zero_count)
    print(door.click)
end = time.time()
print(end - start)
