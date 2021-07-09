from functools import cmp_to_key


class LargestValue:
    def compare(self, a, b):
        c = a * len(b)
        d = b * len(a)
        if c > d:
            return 1
        elif c < d:
            return -1
        else:
            return 0

    def largest(self, arr):
        l = [str(x) for x in arr]
        l.sort(key=cmp_to_key(self.compare), reverse=True)
        return ''.join(l)


# ------------------------------------- RUN CODE -----------------------------------------
lst = [3, 30, 34, 5, 9]
lst = [54, 546, 548, 60]

obj = LargestValue()
data = obj.largest(lst)

print(data)
