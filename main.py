from random import randint


class Screen:
    """
    S -> Score
    D -> T-REX
    C -> Cactus
    B -> Bird
    _ -> Floor1
    - -> Floor2
    """
    def __init__(self):
        # Define the size of the scenario
        self.X_ = 20
        self.Y_ = 4

        # Define the initial position
        self.T_Rex_ = TRex()
        self.Score_Position = [[0, self.X_-1], [0, self.X_-2], [0, self.X_-3]]

        # Define the minimum squares between two cactus
        self.distance_cactus_ = 5
        self.count_cactus_distance = 0

        # Create the scenario
        self.scenario_ = self.create_scenario()
        self.set_fixed_elements()

        # Define the frame
        self.frame = 0

    def create_scenario(self):
        scenario = []
        for y in range(0, self.Y_):
            line = []
            for x in range(0, self.X_):
                if y == self.Y_-1:
                    line.append('_')
                else:
                    line.append(' ')
            scenario.append(line)

        return scenario

    def set_fixed_elements(self):
        # Add the dinosaur position
        if self.T_Rex_.doing == 'DUCK':
            self.scenario_[self.T_Rex_.position[0]][self.T_Rex_.position[1]] = 'D'
            self.scenario_[self.T_Rex_.position[0]][self.T_Rex_.position[1]+1] = 'D'
        else:
            self.scenario_[self.T_Rex_.position[0]][self.T_Rex_.position[1]] = 'D'
            self.scenario_[self.T_Rex_.position[0]-1][self.T_Rex_.position[1]] = 'D'
        # Add the score position
        for place in self.Score_Position:
            self.scenario_[place[0]][place[1]] = 'S'

    def generate_cactus(self, chance):
        if randint(0, chance) == 1 and self.count_cactus_distance > 5:
            self.scenario_[2][self.X_-1] = 'C'
            self.count_cactus_distance = 0
            print(self.count_cactus_distance)
        else:
            self.count_cactus_distance += 1
            print(self.count_cactus_distance)

    def actualize(self):
        for y in range(0, self.Y_-2):
            self.scenario_[y+1].append(' ')
            self.scenario_[y+1].pop(0)
            self.scenario_[y][0] = ' '
            self.scenario_[y+1][0] = ' '

        self.T_Rex_.counter += 1
        if self.T_Rex_.counter == self.T_Rex_.time_actions+1:
            if self.T_Rex_.doing == 'JUMP':
                self.scenario_[0][self.T_Rex_.init_position_[1]] = ' '
                self.T_Rex_.doing = 'NOTHING'
            elif self.T_Rex_.doing == 'DUCK':
                self.scenario_[self.T_Rex_.init_position_[0]][self.T_Rex_.init_position_[1]+1] = ' '
                self.T_Rex_.doing = 'NOTHING'
            self.T_Rex_.position = self.T_Rex_.init_position_

        self.frame += 1
        self.set_fixed_elements()


class TRex:
    def __init__(self):
        self.init_position_ = [2, 1]
        self.position = [2, 1]

        self.time_actions = 5
        self.counter = 0
        self.doing = 'NOTHING'

    def jump(self):
        self.doing = 'JUMP'
        self.position = [1, 1]
        self.counter = 0

    def duck(self):
        self.doing = 'DUCK'
        self.counter = 0


screen = Screen()

for i in range(0, 50):
    screen.generate_cactus(8)
    for line in screen.scenario_:
        print(line)

    if i == 10:
        screen.T_Rex_.duck()

    screen.actualize()

