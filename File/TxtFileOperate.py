# This is a sample script to operate a txt file.

class TxtFileOperate(object):

    def __init__(self, fileName):
        self.fileName = fileName
        self.fp = open(fileName, 'w+')

    def OpenFile(self, fileName):
        self.fileName = fileName
        self.fp = open(fileName, 'w+')

    def Close(self):
        self.fp.close()

    def Write(self, size):
        self.fp.write(size)
    
    def Read(self, buf):
        self.fp.read(buf)

test = TxtFileOperate("test.txt")
test.Write("Test")
test.Close()

test = TxtFileOperate("test.txt")
buf = test.Read(100)
print buf;
test.Close()