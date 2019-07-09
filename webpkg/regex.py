import re

def findMatchstr(regex, str):
    p = re.compile(regex)
    m = p.match(str)
    return m

def findSearchstr(regex, str):
    p = re.compile(regex)
    s = p.search(str)
    return s

def htmlOnetag(tagname, str):
    p = re.compile("\<" + tagname + " [a-zA-Z]+[^>]+[" + tagname + "\>]")
    s = p.search(str)
    return s