#!/usr/bin/python
#
# Brainfuck Interpreter
# Copyright 2011 Sebastian Kaspari
#
# Usage: ./brainfuck.py [FILE]

import sys
import getch

def execute(filename):
  '''执行文件
  
  Example:
     execute('/code/others/Python-Brainfuck/fil.bf')
  '''
  f = open(filename, "r")
  evaluate(f.read())
  f.close()


def evaluate(code):
  
  #print (code)
  code     = cleanup(list(code)) 
  #print (type(code))  output: str 
  #print (code)


  bracemap = buildbracemap(code)
  #print (bracemap)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "<":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "-":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == ".": sys.stdout.write(chr(cells[cellptr]))
    if command == ",": cells[cellptr] = ord(getch.getch())
      
    codeptr += 1
  print (cells[:], codeptr, cellptr)

def cleanup(code):
  '''清洗数据，删除空格
  Example：
      code: list
            ++++++++++[>+++++++>++++++++++>+++>+<<<<-]
                >++.>+.+++++++..+++.>++.<<+++++++++++++++.
                    >.+++.------.--------.>+.>.
      cleanup(code): list
            ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
  '''
  return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    #print (position,command)
    if command == "[": 
      temp_bracestack.append(position)
      #print(temp_bracestack[:])
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  
  # type(sys.argv[:]) =  ['e:\\code\\others\\Python-Brainfuck\\brainfuck.py']
  sys.argv = ['e:\\code\\others\\Python-Brainfuck\\brainfuck.py','/code/others/Python-Brainfuck/fil.bf']
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()

  
