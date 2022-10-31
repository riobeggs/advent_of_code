from util.input import get_input


class Dive:
    def __init__(self):
        self._input = get_input("day2")
        self._horizontal_position = 0
        self._vertical_position = 0
        self._coverage = None

    def find_positions(self):
        """
        Finds the horizonal position after all forward moves in self._input.
        """
        for move in self._input:

            if "forward" in move:
                amount = move.split(" ")
                self._horizontal_position += int(amount[1])

            elif "up" in move:
                amount = move.split(" ")
                self._vertical_position -= int(amount[1])

            elif "down" in move:
                amount = move.split(" ")
                self._vertical_position += int(amount[1])

    def find_coverage(self):
        """
        Total coverage by multiplying the final vertical and horizontal positions.
        """
        self._coverage = self._horizontal_position * self._vertical_position

    def run(self):
        self.find_positions()
        self.find_coverage()
        print(self._coverage)


def main():
    """Part 1"""
    dive = Dive()
    dive.run()


if __name__ == "__main__":
    main()
