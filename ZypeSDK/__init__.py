"""
    Zype is a easy-to-use, easy-to-read and easy-to-write Programming Language & a replacement of JSON.
"""
import os
import json
import sys

def Open(filename):
    """
        You can open/read a Zype File with Open() function.
        Usage: Open(filename)
        Filename is the Zype File's Name.
    """
    if os.path.isfile(filename):
        with open(filename) as Zype:
            content = Zype.read()
        content = '{\n' + content
        content = content + '\n}'
        content = content.replace('<', '  "')
        content = content.replace('>', '":')
        content = content.replace(';', ',')
        content = content.replace('(', '{')
        content = content.replace(')', '  }')
        return json.loads(content)

def Write(key, value, filename):
    with open(filename, 'a+') as Zype:
        content = f'<{key}> {value};\n'
        return Zype.write(content)
        lines = Zype.read() + '\n'
        cleanLines = [line for line in lines if line.strip() != ""]
        Zype.write(cleanLines)
        Zype.close()
    with open(filename, 'a+') as Zype:
        for line in Zype:
            if line != "\n":
               line_count += 1
               lineNumber = line_count - 1
               text = Zype.readlines()
               text[lineNumber] = text[lineNumber].replace(';', '')
               Zype.write(text)
        Zype.close()
        
arg = sys.argv

def Main():
    print(Open(arg[1]))
