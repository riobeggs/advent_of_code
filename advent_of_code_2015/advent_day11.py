class Password_Maker:
    _original_password = None
    _password_letters = None
    _alphabet = None
    _new_password = None

    def __init__(self):
        self._original_password = "hxbxwxba"
        self._password_letters = []

        # Regular alphabet without "i, o, l"
        self._alphabet = "abcdefghjkmnpqrstuvwxyz"

        self._new_password = None

    def get_password_letters(self):
        """
        Returns a list containing all letters in the current password.
        """
        for letter in self._original_password:
            self._password_letters.append(letter)

    def check_for_non_overlapping_pairs(self):
        """
        Returns True if there are x2 overlapping letter pairs in the current password
        """
        return True

    def check_for_3_consecutive_letters(self):
        "Returns True if the current password has 3 consecutive letters"
        return True

    def change_password(self):
        "Changes the original password to fit requirements of check methods"

    @property
    def new_password(self):
        if not self._new_password:
            self.change_password()

        return self._new_password


def main():
    pm = Password_Maker()
    print(pm._new_password)


if __name__ == "__main__":
    main()
