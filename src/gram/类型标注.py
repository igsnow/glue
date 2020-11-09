class Robot(object):
    def __int__(self):
        self.name = 'Cruse'

    def walk(self):
        print(' I am work')


def run_a_robot(robot_object: Robot):
    robot_object.walk()


run_a_robot(Robot())
