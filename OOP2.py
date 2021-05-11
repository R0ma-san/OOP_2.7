class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
	    print('I am climbing the tree') 

a = Monkey()
b = Monkey()

print(a.max_age, a.loves_bananas)
a.climb()

print(b.max_age, b.loves_bananas)
b.climb()