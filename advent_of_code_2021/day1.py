import os


class SonarSweeper:

    def get_input(self):
        """
        Reads text file and converts inputs to a list of inputs.
        """

        input_ = open("advent_of_code_2021/inputs/day1.txt", "r")
        input_ = input_.read().strip().split("\n")

        self.input = input_

    def find_measurement_increases(self):
        """
        Finds the number of times the depth increases from
        a previous measurement.
        """

        measurement_increase_count = 0
        previous_measurement = 0

        for measurement in self.input:
            
            if self.input.index(measurement) > 0:
                measurement = int(measurement)

                if measurement > previous_measurement:
                    measurement_increase_count += 1

            previous_measurement = int(measurement)

        self.increase_count = measurement_increase_count

    def results(self):
        """
        Prints the total amount of increases in the sonar sweepers depth measurements.
        """

        print(f"Total increases in depth measurements: {self.increase_count}")


def main():
    ss = SonarSweeper()
    ss.get_input()
    ss.find_measurement_increases()
    ss.results()


if __name__ == "__main__":
    main()