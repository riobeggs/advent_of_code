class Dive:

    def get_input(self):
        """
        Reads text file and converts inputs to a list of inputs.
        """

        input_ = open("advent_of_code_2021/inputs/day2.txt", "r")
        input_ = input_.read().strip().split("\n")
        self.input = input_


def main():
    dive = Dive()
    dive.get_input()


if __name__ == "__main__":
    main()