class X:

    def __init__(self, nama):
        self.nama = nama


x = X('x')
y = X('y')
mp = {}

mp[x] = 15
mp[y] = 1

print(mp[x])

for ob in mp.keys():
    print(ob.nama)


a = [1,2,3]

for i in a:
    print(i)