
class LexicalClass:
    def lexical_min(self, str):
        temp = sorted(str)
        ch1 = '$'
        ch2 = '$'
        flag = False

        for i in range(len(str)):
            k = str.index(temp[i])

            for j in range(k):
                if str[j] > temp[i]:
                    ch1 = str[j]
                    ch2 = temp[i]
                    flag = True
                    break

                if flag == True:
                    break

        res = ""
        for char in str:
            if char == ch1:
                res += ch2
            elif char == ch2:
                res += ch1
            else:
                res += char

        return res


# ------------------------------------- RUN CODE -----------------------------------------
obj = LexicalClass()
data = obj.lexical_min('accd')
print(data)
