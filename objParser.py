#!/usr/bin/python3

import sys

def parseObj():
    output = ""
    positions    = []
    faces        = []
    texCoords    = []
    normalCoords = []

    vertices = []
    textures = []
    normals  = []
    
    obj = open(sys.argv[1])

    for line in obj:
        if "".join(line.strip()[:2]) == "v ": #vertice line
            positions.append(line.strip()[2:])
        elif "".join(line.strip()[:2]) == "vn": #normals line
            normalCoords.append(line.strip()[3:])
        elif "".join(line.strip()[:2]) == "vt": #texture line
            texCoords.append(line.strip()[3:])
        elif line.strip()[0] == "f": #face attributes line
            (X, Y, Z, *ER) = line.strip().split(" ")[1:]
            if ER :
                print('''Model form concluded in file is not supported by OpenGL ES.\n
                      Please triangulate faces before proceeding...''')
                obj.close()
                quit()            
            X = X.split("/")
            Y = Y.split("/")
            Z = Z.split("/")
            faces.append((X, Y, Z))       
    obj.close()

    for face in faces:
        for vert in face:
            if positions: vertices.append(positions[int(vert[0])-1])  
            if texCoords: textures.append(texCoords[int(vert[1])-1]) 
            if normalCoords: normals.append(normalCoords[int(vert[2])-1])


    output = [
              "v {0}\n".format(" ".join(vertices)),
              "t {0}\n".format(" ".join(textures)),
              "n {0}\n".format(" ".join(normals)),
              "s {0}\n".format(len(faces))
              ]
    
    outputFile = open("RawData.txt", "w") #new file created
    outputFile.write("".join(output))
    outputFile.close()
    
def main():
    if len(sys.argv) > 1 and sys.argv[1].split('.')[-1] == 'obj':
        parseObj()
    else:
        print("No file loaded, or file format not supported.\n Required .obj files")
        quit()

if __name__ == "__main__":
    main()

