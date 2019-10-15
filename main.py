import sys
from community import Community

def main():  
    coms = []
    for i in range(4):
        coms.append(Community(2, i + 1, 2))
        for m in coms[i].getMembers():
            print(m.getWords())    


if __name__ == "__main__":
    main()