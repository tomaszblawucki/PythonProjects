#!/usr/bin/env python3

class ImageContent(object):
    def __init__(self):
        self.rows = []
        self.greyScale = []
        self.chars = [
                        ' ', '.', '\'', '"', '^',
                        '-', '~', '*', ':', ';',
                        '!', '|', '?', '+', '=',
                        '§', '%', '&', '#', '@',
                     ]
        self.chars.reverse()

    def printContent(self):
        print("RGB")
        for row in self.rows:
            print(row)

    def printGreyScale(self):
        print("GREYSCALE")
        for row in self.greyScale:
            print(row)

    def convertToGreyScale(self):
        self.greyScale = self.rows
        for rowIdx in range(0, len(self.greyScale)):
            length = len(self.greyScale[rowIdx])
            for colIdx in range(0, length ):
                self.greyScale[rowIdx][colIdx].sort()
                self.greyScale[rowIdx][colIdx].reverse()
                self.greyScale[rowIdx][colIdx] = self.greyScale[rowIdx][colIdx][0]//13
    def renderImage(self):
        image = []
        for row in self.greyScale:
            lineToRender = ""
            for value in row:
                lineToRender += self.chars[value]*2
            print(lineToRender)


    def initializeContent(self, content):
        rowsCount = content[22]
        collsCount = content[18]
        pixels = content[54:]
        row = []
        self.rows = []
        self.delimitersCount = collsCount%4
        self.rowLength = 3 * collsCount + self.delimitersCount
        for rowNumber in range(0, rowsCount):
            row = pixels[rowNumber*self.rowLength : (rowNumber+1)*self.rowLength ]
            row = [int(row[i]) for i in range(0, len(row) - self.delimitersCount) ]
            row  = [ row[i*3:(i+1)*3] for i in range(collsCount) ]
            self.rows.append(row)
        self.rows.reverse()
        self.convertToGreyScale()
        self.renderImage()


def main():
    testImage = open("Jan_Sikora.bmp", 'rb').read()
    imageObject = ImageContent()
    imageObject.initializeContent(testImage)

if __name__ == "__main__":
    main()
