import re


def non_raw_list() -> list:
    non_raw = open("/Users/riobeggs/Downloads/day8.txt", "r")
    non_raw = non_raw.read()
    non_raw = non_raw. replace("\\\"", "\"") # replaces \" with " 
    non_raw = non_raw.replace("\\\\", "|") # replaces \\ with |
    non_raw = re.sub("\\\\x.{2}", "?", non_raw) # replaces \\x** with ?
    non_raw = non_raw.strip()
    non_raw = non_raw.split("\n") 
    return non_raw


def raw_string() -> str:
    raw = open("/Users/riobeggs/Downloads/day8.txt", "r")
    raw = raw.read()
    raw = raw.replace("\n", "")
    raw = raw.replace("\\", "/")
    return(raw)


def character_counter(non_raw: list) -> int:
    characters = 0
    for string in non_raw:
        index_ = 0
        for character in string:
            index_ += 1
            if index_ == 1:
                continue
            if index_ == len(string):
                continue
            characters += 1
    return characters


def code_counter(raw: str) -> int:
    code = len(raw)
    return code    


def total(characters: int, code: int) -> None:
    total = code - characters

    print("\ncode =", code)
    print("characters =", characters)
    print("total =", total)
    print()


def main() -> None:
    non_raw = non_raw_list()
    raw = raw_string()
    # for i in non_raw:
    #     print(i)
    #     length = int(len(i))
    #     print(length - 2)
    #     print()
    characters = character_counter(non_raw)
    code = code_counter(raw)
    total(characters, code)


if __name__ == "__main__":
    main()