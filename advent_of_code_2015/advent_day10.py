# part 1
def run1(input_: list, new_list: list) -> list:
    for i in range(40):
        index_ = 0
        amount = 1

        if i != 0:
            input_ = new_list
            new_list = []

        for number in input_:
            index_ += 1
            if index_ == len(input_):
                new_list.append(amount)
                new_list.append(number)
                continue
            if number == input_[index_]:
                amount += 1
                continue

            new_list.append(amount)
            new_list.append(number)
            amount = 1

    return new_list


# part 2
def run2(input_: list, new_list: list) -> list:
    for i in range(50):
        index_ = 0
        amount = 1

        if i != 0:
            input_ = new_list
            new_list = []

        for number in input_:
            index_ += 1
            if index_ == len(input_):
                new_list.append(amount)
                new_list.append(number)
                continue
            if number == input_[index_]:
                amount += 1
                continue

            new_list.append(amount)
            new_list.append(number)
            amount = 1

    return new_list


def main() -> None:
    input_ = [1, 3, 2, 1, 1, 3, 1, 1, 1, 2]
    new_list = []
    # number_list = run1(input_, new_list)
    number_list = run2(input_, new_list)
    print(len(number_list))


if __name__ == "__main__":
    main()
