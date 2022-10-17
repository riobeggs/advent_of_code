class Password_Maker:
    _original_password = None
    _password_letters = None
    _alphabet = None

    def __init__(self):
        self._original_password = "hxbxwxba"
        self._password_letters = []
        self._alphabet = "abcdefghijklmnopqrstuvwxyz"

    def get_password_letters(self):
        """
        Returns a list containing all letters in the current password.
        """
        for letter in self._original_password:
            self._password_letters.append(letter)

    


def main():
    pm = Password_Maker()


if __name__ == "__main__":
    main()
