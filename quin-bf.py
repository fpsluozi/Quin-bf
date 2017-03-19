#!/usr/bin/python
# -*- coding: utf-8 -*-
# Quinish Interpreter
# By Lawrence Luo 2017
# Inspired by Sebastian Kaspari 2011

import sys
import getch

def run(filename):
    f = open(filename, "r")
    evaluate(f.read())
    f.close()


def evaluate(code):
    code = cleanup(code)
    bracemap = buildbracemap(code)  
    cells, codeptr, cellptr = [0], 0, 0
    
    while codeptr < len(code):
        command = code[codeptr].decode('utf-8')
        # >
        if command == u"真实":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)
        # <
        if command == u"神秘": 
            cellptr = 0 if cellptr <= 0 else cellptr - 1
        # +
        if command == u"摸": 
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0
        # - 
        if command == u"勃": 
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255
        # [
        if command == u"猛男" and cells[cellptr] == 0: 
            codeptr = bracemap[codeptr]
        # ]
        if command == u"狗屎" and cells[cellptr] != 0: 
            codeptr = bracemap[codeptr]
        # ,
        if command == u"食鸡": 
            cells[cellptr] = ord(getch.getch())
        # .
        if command == u"二五仔": 
            sys.stdout.write(chr(cells[cellptr]))
          
        codeptr += 1


def cleanup(code):
    return filter(lambda x: x in ['食鸡', '二五仔', '猛男', '狗屎', '勃', '摸', '真实', '神秘'], code.strip().split())


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        command = command.decode('utf-8')
        if command == u'狗屎':
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start

        if command == u'猛男': 
            temp_bracestack.append(position)
    
    return bracemap


def main():
    if len(sys.argv) == 2: 
        run(sys.argv[1])
    else: 
        print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__": main()

