from util.input import get_input


class Dive1:
    def __init__(self):
        self._input = get_input("day2")
        self._horizontal_position = 0
        self._vertical_position = 0
        self._coverage = None

    def find_positions(self):
        """
        Finds positions after all moves in self._input.
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
        print(f"Coverage: {self._coverage}")


class Dive2:
    def __init__(self):
        self._input = get_input("day2")
        self._horizontal_position = 0
        self._vertical_position = 0
        self._aim = 0
        self._coverage = None

    def find_positions(self):
        """
        Finds positions after all moves in self._input.
        """
        for move in self._input:

            if "forward" in move:
                amount = move.split(" ")
                self._horizontal_position += int(amount[1])
                self._vertical_position += self._aim * int(amount[1])

            elif "up" in move:
                amount = move.split(" ")
                self._aim -= int(amount[1])

            elif "down" in move:
                amount = move.split(" ")
                self._aim += int(amount[1])

    def find_coverage(self):
        """
        Total coverage by multiplying the final vertical and horizontal positions.
        """
        self._coverage = self._horizontal_position * self._vertical_position

    def run(self):
        self.find_positions()
        self.find_coverage()
        print(f"Coverage: {self._coverage}")


def main():
    """Part 1"""
    # dive1 = Dive1()
    # dive1.run()

    """Part 2"""
    dive2 = Dive2()
    dive2.run()

if __name__ == "__main__":
    main()
