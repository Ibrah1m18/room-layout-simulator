class Room:
    def __init__(self, width, depth, door_position, window_position):
        self.width = width
        self.depth = depth
        self.door_position = door_position
        self.window_position = window_position
        self.furniture = []
        print(f"Room width {width}m depth {depth}m, Door position {door_position}, Window position {window_position}")

    def add_furniture(self, Furniture_obj):
        if self.check_design(Furniture_obj):
            self.furniture.append(Furniture_obj)
            print(f"{Furniture_obj.name} added at ({Furniture_obj.x}, {Furniture_obj.y})")
        else:
            Furniture_obj.rotate()
            # Adjust position after rotation in case out of the room 
            if Furniture_obj.x + Furniture_obj.width > self.width:
                Furniture_obj.x = self.width - Furniture_obj.width
            if Furniture_obj.y + Furniture_obj.depth > self.depth:
                Furniture_obj.y = self.depth - Furniture_obj.depth

            print(f"Trying again with {Furniture_obj.name} rotated and adjusted...")
            if self.check_design(Furniture_obj):
                self.furniture.append(Furniture_obj)
                print(f"{Furniture_obj.name} added at ({Furniture_obj.x}, {Furniture_obj.y}) after rotation")
            else:
                print(f"{Furniture_obj.name} still can't be placed even after rotation.")

        self.show_furniture()

    def check_design(self, Furniture_obj):
        left = Furniture_obj.x
        top = Furniture_obj.y
        right = Furniture_obj.x + Furniture_obj.width
        bottom = Furniture_obj.y + Furniture_obj.depth
        dx, dy = self.door_position
        wx, wy = self.window_position

        # boundaries
        if left < 0 or top < 0 or right > self.width or bottom > self.depth:
            print("Error: Out of the room")
            return False

        # door/window rules
        if (left <= dx < right and top <= dy < bottom) or (left <= wx < right and top <= wy < bottom):
            print("Can't put in front of the door or window.")
            return False

        # no overlap
        for old in self.furniture:
            old_left = old.x
            old_top = old.y
            old_right = old.x + old.width
            old_bottom = old.y + old.depth

            if not (right <= old_left or left >= old_right or bottom <= old_top or top >= old_bottom):
                print("Overlap detected with", old.name)
                return False

        return True

    def show_furniture(self):
        if not self.furniture:
            print("The room is empty.")
        else:
            print("Furniture in the room:")
            for item in self.furniture:
                print(f"- {item}")

    # simple ASCII map
    def show_map(self):
        grid = [["." for _ in range(self.width)] for _ in range(self.depth)]
        dx, dy = self.door_position
        wx, wy = self.window_position
        if 0 <= dy < self.depth and 0 <= dx < self.width:
            grid[dy][dx] = "D"
        if 0 <= wy < self.depth and 0 <= wx < self.width:
            grid[wy][wx] = "W"
        for f in self.furniture:
            for i in range(f.depth):
                for j in range(f.width):
                    y = f.y + i
                    x = f.x + j
                    if 0 <= y < self.depth and 0 <= x < self.width:
                        grid[y][x] = f.name[0].upper()
        print("Room Map:")
        for row in grid:
            print("".join(row))


class Furniture:
    def __init__(self, name, width, depth, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.depth = depth

    def rotate(self):
        self.width, self.depth = self.depth, self.width
        print(f"{self.name} rotated: new size {self.width}x{self.depth}")

    def __str__(self):
        return f"{self.name} at ({self.x}, {self.y}), size: {self.width}x{self.depth}"


# Example
if __name__ == "__main__":
    room = Room(10, 8, door_position=(2, 0), window_position=(8, 4))
    big_table = Furniture("BigTable", 7, 5, 3, 1)
    chair = Furniture("Chair", 2, 2, 0, 0)
    sofa = Furniture("Sofa", 3, 3, 7, 0)

    room.add_furniture(big_table)
    room.add_furniture(chair)
    room.add_furniture(sofa)

    room.show_map()
