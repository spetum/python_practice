import os
def main():
    f=os.popen("dir")
    print(f.read())

main()
