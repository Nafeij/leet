import string


class Solution:
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
