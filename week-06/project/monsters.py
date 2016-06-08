class monster(object):
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.skeleton_image = PhotoImage(file='skeleton.png')
        self.key = False
        self.boss = False
        self.x = x
        self.y = y
        self.max_hp = 2 * random.randint(1, 6)
        self.hp = self.max_hp
        self.dp = 0.5 * random.randint(1, 6)
        self.sp = random.randint(1, 6)
        self.stat = 'Monster HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)

    def draw(self):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = self.skeleton_image, anchor = NW)


class boss(object):
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.boss_image = PhotoImage(file='boss.png')
        self.key = False
        self.boss = True
        self.x = x
        self.y = y
        self.max_hp = 2 * random.randint(1, 6) + random.randint(1, 6)
        self.hp = self.max_hp
        self.dp = 0.5 * random.randint(1, 6) + random.randint(1, 6)/2
        self.sp = random.randint(1, 6)
        self.stat = 'Monster HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)

    def draw(self):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = self.boss_image, anchor = NW)

    def create_monsters(self):
        self.monsters = []
        self.monsters.append(boss(10, 10, self.canvas))
        self.map[0].enemy = True
        for i in range(3):
            j = True
            while j == True:
                ran_x = random.randint(2, 10)
                ran_y = random.randint(2, 10)
                for each in self.map:
                    if each.x == ran_x and each.y == ran_y and each.type == 'floor' and each.enemy == False:
                        self.monsters.append(monster(ran_x, ran_y, self.canvas))
                        each.enemy = True
                        j = False
