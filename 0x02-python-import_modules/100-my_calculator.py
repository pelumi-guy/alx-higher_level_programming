#!/usr/bin/python3
from ast import operator
from xml.etree.ElementInclude import include
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operands = ['+', '-', '*', '/']
    functions = [add, sub, mul, div]
    opr = argv[2]

    if opr not in operands:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        for i in range(len(operands)):
            if operands[i] == opr:
                a = int(argv[1])
                b = int(argv[3])
                res = functions[i](a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, opr, b, res))
        exit(0)
