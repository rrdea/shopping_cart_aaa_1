class X:

    name = 'hehe'

x = X()
mp = {}

mp[x] = 2
print(mp[x])

for ob in mp.keys():
    print(ob.name)
