#!/usr/bin/python3

import sys

def parseObj():
    print("parsing")
    output = ""
    v   = "v" #vertices vector
    vi  = "vi" #vertices indices for faces
    vti = "vti" #vertices texture indices for faces
    vni = "vni" #vertices normal indices for faces
    obj = open(sys.argv[1])# .obj file handle for read only
    for line in obj:
        if "".join(line.strip()[:2]) == "v ": #vertice line
            v += " "+line.strip()[2:]
        elif line.strip()[0] == "f": #face attributes line
            (X, Y, Z, *ER) = line.strip().split(" ")[1:]
            if ER :
                print("Model form concluded in file is not supported by OpenGL ES.\nPlease triangulate faces before proceeding")
                obj.close()
                quit()            
            X = X.split("/")
            Y = Y.split("/")
            Z = Z.split("/")
            vi  += " {0} {1} {2}".format(X[0], Y[0], Z[0])
            vti += " {0} {1} {2}".format(X[1], Y[1], Z[1])
            vni += " {0} {1} {2}".format(X[2], Y[2], Z[2])
    v   += "\n"
    vi  += "\n"
    vti += "\n"
    vni += "\n"         
    obj.close()
    outputFile = open("parsed_"+sys.argv[1], "w") #new file created
    outputFile.write(v)
    outputFile.write(vi)
    outputFile.write(vti)
    outputFile.write(vni)
    outputFile.close()
    
def main():
    if len(sys.argv) > 1 and sys.argv[1].split('.')[-1] == 'obj':
        parseObj()
    else:
        print("No file loaded, or file format not supported.\n Required .obj files")
        quit()

if __name__ == "__main__":
    main()
