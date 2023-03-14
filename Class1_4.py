import random
from Class2_3 import Triangle, Rect, Circle
rec = []
tri = []
cir = []

#Bai1
def generateRec(f):
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    if a > b:
        c = a
        a = b
        b = c
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Rect\n")
    f.write("{} {}\n".format(a, b))
    f.write("{} {}\n".format(x, y))


def generateCir(f):
    bk = random.randint(0, 10)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Circle\n")
    f.write("{}\n".format(bk))
    f.write("{} {}\n".format(x, y))


def generateTri(f):
    a, b, c = 0, 0, 0
    while a + b <= c or a + c <= b or \
            b + c <= a:
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        c = random.randint(0, a + b)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    f.write("#Triangle\n")
    f.write("{} {} {}\n".format(a, b, c))
    f.write("{} {}\n".format(x, y))


def createfile(filename="input.txt", amount=1000):
    try:
        with open(filename, "w") as f:
            for i in range(amount):
                generateRec(f)
                generateCir(f)
                generateTri(f)
        return True
    except:
        return False

#Bai4a
def readfile(filename):
    global rec
    global cir
    global tri
    try:
        with open(filename) as file:
            line = file.readline()
            while line != '':
                if line == "#Rect\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = [int(x) for x in data.split(" ")]
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    rect = Rect(info[0], info[1], info2[0], info2[1])
                    rec.append(rect)
                if line == "#Circle\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = int(data.strip())
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    circle = Circle(info, info2[0], info2[1])
                    cir.append(circle)
                if line == "#Triangle\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = [int(x) for x in data.split(" ")]
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    triangle = Triangle(info[0], info[1], info[2], info2[0], info2[1])
                    tri.append(triangle)
                line = file.readline()
        return True
    except:
        return False

#Bai4b
def checkmax():
    maxCV = 0
    maxDT = 0
    for i in rec:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    for i in cir:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    for i in tri:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    print("Hình có chu vi lớn nhất với chu vi là {}:".format(maxCV))
    cv.printinfo()
    print("-"*30)
    print("Hình có diện tích lớn nhất với diện tích là {}:".format(maxDT))
    dt.printinfo()


def getinfo(e):
    if e == 1:
        print("_"*100)
        print("Danh sách thông tin hình vuông:")
        for i in range(0, len(rec)):
            print("{}. ".format(i+1), end="")
            rec[i].printinfo()
            print()
    if e == 2:
        print("_" * 100)
        print("Danh sách thông tin hình tròn:")
        for i in range(0, len(cir)):
            print("{}. ".format(i+1), end="")
            cir[i].printinfo()
            print()
    if e == 3:
        print("_" * 100)
        print("Danh sách thông tin hình tam giác:")
        for i in range(0, len(rec)):
            print("{}. ".format(i+1), end="")
            rec[i].printinfo()
            print()


def maxcollide():

    return None
