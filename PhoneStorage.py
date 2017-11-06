class phone():
    def __init__(self, parent, val):
        self.value = val
        self.counter = 0
        self.children = [None] * 10 
        self.parent = parent

    def addChild(self, num):
        if (len(num)) == 0:
            self.counter += 1
            return

        val = int(num[0])
        if not self.children[val]:
            self.children[val] = phone(self, val)

        self.children[val].addChild(num[1:])
            

    def __str__(self):
        return str(self.value)

phone_root = phone(None, None)

phone_root.addChild("4152935130")
phone_root.addChild("4152935126")
phone_root.addChild("2065551123")
phone_root.addChild("2065551111")
phone_root.addChild("206543")


def printNumbers(node, start):
    if node.value != None:
        start += str(node.value)

    for i in range(0, node.counter):
        print(start)

    for child in node.children:
        if child != None:
            printNumbers(child, start)


printNumbers(phone_root, "")
