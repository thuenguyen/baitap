import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    
    def read(self):
        try:
            tmp = input('Nhap vao lan luot toa do x va y (cach nhau boi dau cach): ')
            coords = tmp.split()
            if len(coords) != 2:
                raise ValueError("Phai nhap dung 2 gia tri")
            self.__x = int(coords[0])
            self.__y = int(coords[1])
        except ValueError as e:
            print(f"Loi: {e}. Su dung toa do mac dinh (0,1)")
            self.__x = 0
            self.__y = 1

    def __str__(self):
        return f"({self.__x},{self.__y})"

    def move(self, dx=0, dy=0):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self, *args):
        if len(args) == 0:
            return math.sqrt(self.__x**2 + self.__y**2)
        if len(args) == 1 and isinstance(args[0], Point): 
            return math.sqrt((self.__x - args[0].__x)**2 + (self.__y - args[0].__y)**2)

class PointTest:
    def main(self):
        p2 = Point()
        print("Toa do diem p2:", p2)
        p3 = Point()
        p3.read()
        print("Toa do diem p3:", p3)
        print("Khoang cach tu diem p3 den goc toa do:", p3.distance())
        print("Khoang cach giua 2 diem p2 va p3:", p2.distance(p3))

PointTest().main()
