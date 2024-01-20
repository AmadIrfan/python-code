import io as io


class FileHandle:
    name = ""
    path = ""
    a = 0

    def __init__(self, name, path, a):
        self.name = name
        self.path = path
        self.a = a

    def ToFile(self):
        file = open(self.path, mode="w")
        file.write(self.name)

    def fromFile(self):
        file = open(self.path, mode="r")
        a=file.read()
        print(a)



d = FileHandle("Amad Irfan", "this.txt", 6)
d.ToFile()

d.fromFile()