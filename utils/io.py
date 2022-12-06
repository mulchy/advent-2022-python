import fileinput

def read(filename=None):
    return "".join(fileinput.input(files=filename))