class Home:
    def __init__(self):
        pass

    def room1(self):
        width = 100
        breadth = 100
        print('area of room1', width*breadth)

    def kitchen(self):
        width = 422
        breadth = 488
        print('area of kitchen', width*breadth)

    def room2(self):
        width = 150
        breadth = 150
        print('area of room2', width*breadth)

    def living_room(self):

        width = 330
        breadth = 230
        print('area of living room', width*breadth)


class FirstHome(Home):

    def study_room(self):

        width = 220
        breadth = 230
        print('area of study room', width*breadth)


class SecondHome(Home):
    def work_area(self):
        width = 120
        breadth = 130
        print('area of work area', width*breadth)


if __name__ == '__main__':
    obj1 = FirstHome()
    obj2 = SecondHome()
    print("First Home")
    obj1.room1()
    obj1.room2()
    obj1.study_room()
    obj1.living_room()
    obj1.kitchen()
    print("Second Home")
    obj2.room1()
    obj2.room2()
    obj2.living_room()
    obj2.kitchen()
    obj2.work_area()
