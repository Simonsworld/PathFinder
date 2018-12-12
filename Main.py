# hier kommt die GUI rein
from tkinter import *
from Search import Graph


# Erstellung des Roots
root = Tk()
# Größe der Felder
w = 400/20
h = 400/20
# Erstellen des Starts und des Ziels
start = (2,2)
end = (18, 13)

# Erstellen des Spielfelds
## google, wie 2 Dim. Arrays verwaltet werden
# 0 = nichts
# 1 = wall
# 2 = start
# 3 = end
# 4 = Weg von Start zum Ziel

a = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]




# GUI für Algorithmus erstellen
field = Canvas(root, width=400, height=400)
field.pack(side=LEFT)



# Aufteilung der Oberfläche in 2 Bereiche links und Rechts
rightframe = Frame(root)
rightframe.pack(side=RIGHT)



# Methode für den Knopf, um zu reagieren
def startSearch():
    type = optionReturn()

    if type == "A-Star":
        aStar()

    elif type == "test1":
        print("test1")


# A-Star Algorithmus aufrufen
def aStar():
    search = Graph()
    path = search.astar(a, start, end)

    for i in range(0, len(path)):
        x = path[i][0]
        y = path[i][1]
        print(x)
        print(y)
        addWay(x,y)

    drawCanvas()
    print(path)


# Button hinzufügen
b1 = Button(rightframe, text="Search", fg="Black", command=startSearch)

# Dja
b1.pack()

# Drop Down hinzufügen
choices = StringVar(root)
choices.set("A-Star")

d1 = OptionMenu(rightframe, choices, "A-Star", "test1", "test2")

# Methode, um die aktuelle Auswahl zu erhalten
def optionReturn():
    type = "A-Star"
    return type


d1.pack()


# Maus hinzufügen
def leftClick(event):
    print("Left")
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))
    manageWall(x,y)

    # update der GUI
    field.update()
    drawCanvas()

def middleClick(event):
    print("Middle")


def rightClick(event):
    print("Right")

# callback für Aktionen
def callback(event):
    print("mousecursor at" + event.x + " / " + event.y)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))


# Einfügefunktion im Array
def manageWall(x,y):
    x = int(x / 20)
    y = int(y / 20)

    if a[x][y] == 0:
        a[x][y] = 1
    elif a[x][y] == 1:
        a[x][y] = 0

    output()


# Überprüfung der Änderung durch eine Ausgabe
def output():
    for i in range(0, 19):
        l = ""
        for j in range(0, 19):
            erg = a[i][j]
            l += str(erg)
        print(l)


# Löschfunktion im Array
def delete(x,y):
    x = x / 20
    y = y / 20

# Zeichnen der Canvas
def drawCanvas():

    for x in range(0, 20):
        for y in range(0, 20):
            if a[x][y] == 4:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="lime")
            if a[x][y] == 3:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")
            if a[x][y] == 2:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="green")
            if a[x][y] == 1:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="black")
            if a[x][y] == 0:
                field.create_rectangle(w * x, h * y, w * x + 20, h * y + 20, fill="grey")

# Update a

# Add a way
def addWay(x,y):

    a[x][y] = 4




field.bind("<Button-1>", leftClick)
field.bind("<Button-2>", middleClick)
field.bind("<Button-3>", rightClick)

#field.bind("<Motion>", motion)

drawCanvas()
root.mainloop()