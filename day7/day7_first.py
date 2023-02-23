class Direktory:
    name = ""
    content = []
    size = 0

    def __init__(self, name):
        self.name = name
        self.content = []
        self.size = 0

    def calcSize(self):
        self.size = 0
        for i in self.content:
            if isinstance(i, Direktory):
                self.size += i.calcSize()
            else:
                self.size += int(i.split(" ")[0])
        return self.size

    def addContent(self, content):
        self.content.append(content)

    def getSize(self):
        self.calcSize()
        return self.size

    def moveIn(self, name):
        for i in self.content:
            if isinstance(i, Direktory):
                if i.name == name:
                    return i
        return None


def main():
    instructions = []

    home = Direktory("/")
    pointer = ""
    path = []
    allDirektorys: list(Direktory) = [home]
    final = 0

    with open("Day7\input.txt") as my_file:
        instructions = my_file.read().split("\n")

    instructions.reverse()

    while len(instructions) > 0:
        instruction = instructions.pop()

        if instruction.startswith("$"):
            if instruction[2:4] == "cd":
                if instruction[5:] == "/":
                    path = [home]
                    pointer = home
                elif instruction[5:] == "..":
                    pointer = path.pop()
                else:
                    path.append(pointer)
                    newPointer = pointer.moveIn(instruction[5:])
                    pointer = newPointer

            elif instruction[2:4] == "ls":
                pass
        else:
            if instruction.startswith("dir"):
                newDir = Direktory(instruction[4:])
                pointer.addContent(newDir)
                allDirektorys.append(newDir)
            else:
                pointer.addContent(instruction)

    for i in allDirektorys:
        if i.getSize() <= 100000:
            final += i.getSize()

    print(final)


if __name__ == "__main__":
    main()
