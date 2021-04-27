"""
    Zype is a easy-to-use, easy-to-read and easy-to-write Programming Language & a replacement of JSON.
"""
import os, json

def Open(Filename):
    """
        You can open/read a Zype File with Open() function.
        Usage: Open(Filename)
        Filename is the Zype File's Name.
    """
    if os.path.isfile(Filename):
        with open(Filename) as Zype:
            content = Zype.read()
        content = '{\n' + content
        content = content + '\n}'
        content = content.replace('<', '  "')
        content = content.replace('>', '":')
        content = content.replace(';', ',')
        content = content.replace('(', '{')
        content = content.replace(')', '  }')
        return json.loads(content)