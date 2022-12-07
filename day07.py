from __future__ import annotations

from utils.io import read

input = read()

class File():
    def __init__(self, name: str, size: int, parent: Directory) -> None:
        self.name = name
        self.size = size
        self.parent = parent

class Directory():
    def __init__(self, name: str, parent: Directory | None) -> None:
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def add_child(self, node: Directory | File):
        if isinstance(node, File):
            ptr = self
            while ptr is not None:
                ptr.size += node.size
                ptr = ptr.parent

        self.children.append(node)

    def child_with_name(self, name: str):
        return next(child for child in self.children if child.name == name)

    def __str__(self) -> str:
        return f"name:{self.name}, size:{self.size}"

    def __repr__(self) -> str:
        return self.__str__()


root = Directory(name="/", parent=None)
cwd = root
directories = [root]

for line in input.splitlines():
    match line.split():
        case ["$", "cd", directory]:
            if directory == "/":
                cwd = root
            elif directory == "..":
                cwd = cwd.parent
            else:
                cwd = cwd.child_with_name(directory)
        case ["$", "ls"]:
            pass
        case ["dir", filename]:
            dir = Directory(name=filename, parent=cwd)
            cwd.add_child(dir)
            directories.append(dir)
        case [size, filename] if size.isdigit():
            cwd.add_child(File(name=filename, parent=cwd, size=int(size)))
        case _:
            print(f"Unable to parse command {line}")

print(sum(dir.size for dir in directories if dir.size <= 100000))

filesystem_size = 70000000
free = filesystem_size - root.size
needed = 30000000 - free

candidates = sorted([dir for dir in directories if dir.size >= needed], key=lambda d: d.size)

print(candidates[0])