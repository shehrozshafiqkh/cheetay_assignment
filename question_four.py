class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


def no_of_meeting(l, n):
    ans = []

    l.sort(key=lambda x: x.end)

    ans.append(l[0].pos)

    time_limit = l[0].end

    for i in range(1, n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end

    return len(ans)


# ------------------------------------- RUN CODE -----------------------------------------
s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]

n = len(s)
l = []

for i in range(n):
    l.append(Meeting(s[i], f[i], i))

# function calling
data = no_of_meeting(l, n)
print(data)