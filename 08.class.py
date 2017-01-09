class Enemy:
    life = 05
    type = 'e1'

    def __init__(self, x=3, y="e2"):
        self.type = y
        print('enemy ' + self.type + ' created'),
        self.life = x
        print ('with energy level ' + str(self.life))

    def attack(self, x=1):
        print('ouch')
        self.life -= x

    def check_life(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print (str(self.life) + " life left")

enemy1 = Enemy()
enemy2 = Enemy(7, "e3")

enemy1.attack()
enemy1.check_life()
enemy1.attack(5)
enemy1.check_life()

enemy2.life = 4
enemy2.check_life()

