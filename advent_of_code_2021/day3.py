from util.input import get_input

class BinaryDiagnostic:
    def __init__(self):
        self._input = set(get_input("day3"))
        self._gamma_rate = 0
        self._epsilon_rate = 0
        self._power_consumption = 0

if __name__ == "__main__":
    print(BinaryDiagnostic()._input)