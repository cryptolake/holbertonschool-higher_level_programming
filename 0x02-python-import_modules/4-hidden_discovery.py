#!/usr/bin/python3
import hidden_4


def main():
    modules = dir(hidden_4)
    for module in modules:
        if module[0:2] != "__":
            print(module)


if __name__ == "__main__":
    main()
