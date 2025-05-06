import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    
    def read(self):
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y
    
    def print(self):
        print(f"({self.__x}, {self.__y})", end="")
    
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y
    
    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def distanceTo(self, P):
        dx = self.__x - P.getX()
        dy = self.__y - P.getY()
        return math.sqrt(dx**2 + dy**2)

class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
            self.__color = "xanh"
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().__init__(cp.getX(), cp.getY())
            self.__color = cp.__color
        elif len(args) == 3:
            x, y, color = args
            super().__init__(x, y)
            self.__color = color
        else:
            raise ValueError("không hợp lệ")
    
    def read(self):
        parts = input().strip().split()
        x = int(parts[0])
        y = int(parts[1])
        self.setXY(x, y)
        self.__color = ' '.join(parts[2:]) if len(parts) > 2 else "xanh"
    
    def print(self):
        super().print()
        print(f": {self.__color}")
    
    def setColor(self, color):
        self.__color = color

class C002454:
    @staticmethod
    def testCase1():
        A = ColorPoint(5, 10, "trắng")
        A.print()
        print(" PASS")
    
    @staticmethod
    def testCase2():
        print("\nNhập tọa độ và màu cho điểm B (định dạng: x y màu) 33:")
        B = ColorPoint()
        B.read()
        B.move(10, 8)
        B.print()
    
    @staticmethod
    def testCase3():
        print()
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint(C)
        D.print()
        D.setColor("vàng")
        D.print()
        C.print()
        print("\nhamam: PASS")
        print("Set color: PASS")
    
    @staticmethod
    def main():
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()

# To run the test cases
if __name__ == "__main__":
    C002454.main()
