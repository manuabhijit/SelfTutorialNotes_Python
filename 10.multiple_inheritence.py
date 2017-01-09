class Mario():
    def move(self):
        print("mario is moving")

class Shroom():
    def eat(self):
        print("i am big")

class Flower():
    def fire(self):
        print("i am police")

class BigMario(Mario,Shroom,Flower):
    pass

bm = BigMario()
bm.move()
bm.eat()
bm.fire()


