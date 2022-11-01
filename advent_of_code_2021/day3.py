from util.input import get_input


class BinaryDiagnostic:
    def __init__(self):
        self._input = set(get_input("day3"))
        self._amount_of_0s_in_each_column = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self._amount_of_1s_in_each_column = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self._gamma_rate = 0
        self._epsilon_rate = 0
        self._power_consumption = 0

    def calculate_column_bit_amount(self):
        """
        Calculate the amount of bits in each column in input.
        """
        for diagnostic_report in self._input:

            bit_index = -1
            diagnostic_report = list(diagnostic_report)

            for bit in diagnostic_report:

                bit_index += 1

                if bit == "0":
                    self._amount_of_0s_in_each_column[bit_index] += 1

                if bit == "1":
                    self._amount_of_1s_in_each_column[bit_index] += 1

    def calculate_gamma_rate(self):
        """
        Determines gamma rate based on most common bit in each column.
        """
        gamma_rate = []

        for amount in self._amount_of_0s_in_each_column:

            index = self._amount_of_0s_in_each_column.index(amount)

            if amount > self._amount_of_1s_in_each_column[index]:
                gamma_rate.append("0")
                continue

            gamma_rate.append("1")

        self._gamma_rate = gamma_rate

    def calculate_epsilon_rate(self):
        """
        Calculates epsilon rate based on the gamma rate.
        """
        epsilon_rate = []
        
        for bit in self._gamma_rate:

            if bit == "0":
                epsilon_rate.append("1")
                continue

            epsilon_rate.append("0")

        self._epsilon_rate = epsilon_rate

    def calculate_power_consumption(self):
        """
        Calculate power consumption by multiplying the
        decimal representation of gamma_rate with the decimal 
        representation of epsilon_rate
        """
        gamma_rate_number = "".join(self._gamma_rate)
        gamma_rate_number = int(gamma_rate_number, 2)

        epsilon_rate_number = "".join(self._epsilon_rate)
        epsilon_rate_number = int(epsilon_rate_number, 2)

        self._power_consumption = gamma_rate_number * epsilon_rate_number


def main():
    bd = BinaryDiagnostic()

    bd.calculate_column_bit_amount()
    bd.calculate_gamma_rate()
    bd.calculate_epsilon_rate()
    bd.calculate_power_consumption()

    print(bd._power_consumption)


if __name__ == "__main__":
    main()
