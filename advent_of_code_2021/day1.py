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

    def find_triple_measurement_increases(self):
        """
        Finds the amount of times the sum of 3 consecutive measurements
        increases from a previous sum of 3 consecutive measurements.
        """

        measurement_increase_count = 0
        triple_measurement = []
        previous_triple_measurement_sum = 0

        for measurement in self.input:

            measurement = int(measurement)
            triple_measurement.append(measurement)
                
            if len(triple_measurement) >= 3:

                if sum(triple_measurement) > previous_triple_measurement_sum and previous_triple_measurement_sum != 0:
                    measurement_increase_count += 1

                previous_triple_measurement_sum = sum(triple_measurement)
                triple_measurement.remove(triple_measurement[0])

        self.increase_count = measurement_increase_count

    def results(self):
        """
        Prints the total amount of increases in the sonar sweepers depth measurements.
        """

        print(f"Total increases in depth measurements: {self.increase_count}")


def main():

    """Part 1"""
    # ss = SonarSweeper()
    # ss.get_input()
    # ss.find_measurement_increases()
    # ss.results()

    """Part 2"""
    ss = SonarSweeper()
    ss.get_input()
    ss.find_triple_measurement_increases()
    ss.results()


if __name__ == "__main__":
    main()
