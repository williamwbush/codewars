def next_bigger(n):
    n_digits = [int(n) for n in str(n)]
    i = len(n_digits) - 2
    end_digits = [n_digits[i+1]]

    while i >= 0:
        end_digits.append(n_digits[i])
        if n_digits[i] < n_digits[i+1]:
            next_highest_end_digit = sorted(set(end_digits))[sorted(set(end_digits)).index(n_digits[i]) + 1]
            end_digits.remove(next_highest_end_digit)
            next_b_digits = n_digits[:i] + [next_highest_end_digit] + sorted(end_digits)
            return int("".join(str(d) for d in next_b_digits))
        i -= 1
    return -1

n = 56244232
next_bigger(n)