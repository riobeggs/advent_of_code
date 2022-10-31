def get_input(day: str):
    """
    Reads text file and converts inputs to a list of inputs.
    """

    input_ = open(f"advent_of_code_2021/inputs/{day}.txt", "r")
    input_ = input_.read().strip().split("\n")

    return input_