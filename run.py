import sys
from tkpyro import run

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print "I....uhhh....need a file. :)"
        sys.exit()

    run(filename)
