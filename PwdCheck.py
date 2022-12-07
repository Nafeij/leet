import string


class Solution:
    '''
    A password is considered strong if the below conditions are all met:

    1. It has at least 6 characters and at most 20 characters.
    2. It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
    3. It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).

    In one 'step', you can:

    1. Insert one character to password,
    2. Delete one character from password, or
    3. Replace one character of password with another character.

    Given a string password, return the minimum number of steps required to make password strong.
        If password is already strong, return 0.
    '''
    def strongPasswordChecker(self, password: str) -> int:
        lflag = uflag = dflag = 1
        for c in password:
            if c in string.ascii_lowercase:
                lflag = 0
            elif c in string.ascii_uppercase:
                uflag = 0
            elif c in string.digits:
                dflag = 0

        missing_d = lflag + uflag + dflag
        replace = zero_reps = one_reps = 0
        i = 2
        while i < len(password):
            if password[i - 2] == password[i - 1] == password[i]:
                rep = 2
                while i < len(password) and password[i] == password[i - 1]:
                    rep += 1
                    i += 1
                replace += rep // 3
                if rep % 3 == 0:
                    zero_reps += 1
                elif rep % 3 == 1:
                    one_reps += 1
            else:
                i += 1

        if len(password) < 6:
            return max(missing_d, 6 - len(password))
        elif len(password) < 21:
            return max(missing_d, replace)
        else:
            remove = len(password) - 20

            replace -= min(zero_reps, remove)
            remove = max(remove - zero_reps, 0)

            replace -= min(one_reps, remove // 2)
            remove = max(remove - one_reps * 2, 0)

            replace -= remove // 3

            return len(password) - 20 + max(replace, missing_d)


if __name__ == '__main__':
    print(Solution().strongPasswordChecker('1111111111'))
