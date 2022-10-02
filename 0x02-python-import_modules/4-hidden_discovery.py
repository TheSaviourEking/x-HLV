#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    def disp_names():
        name = dir(hidden_4)
        for i in name:
            if i[:2] != "__":
                print("{:s}".format(i))

disp_names()
