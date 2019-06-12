# Sample Question
a = [1, 2, 5]
a.append(a[1])
print(a)
a.reverse()
print(a)

s, t = "James Brown", ""
for i in range(len(s)):
    t += s[i - len(s)]
    print(t)
