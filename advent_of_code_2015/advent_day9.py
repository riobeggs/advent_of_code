def input_list() -> list:
    inputs = open("/Users/riobeggs/Downloads/day9.txt", "r")
    inputs = inputs.read().split("\n")
    inputs = inputs[:-1]
    return inputs


def location_list(inputs) -> list:
    locations = []
    for location in inputs:
        location = location.split(" ")
        if location[0] not in locations:
            locations.append(location[0])
        if location[2] not in locations:
            locations.append(location[2])
    return locations


def visited_locations() -> bool:
    visited = []
    
    



def main() -> None:
    inputs = input_list()
    locations = location_list(inputs)


if __name__ == "__main__":
    main()