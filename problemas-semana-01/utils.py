#!/usr/bin/env python

def file_to_list(filepath, ignore_blanks=False):
    """ Reads a file line by line into a list """
    result = file(filepath).read()
    result = result.split('\n')
    if ignore_blanks:
        aux = result
        result = []
        for element in aux:
            if len(element)>0:
                result.append(element)
    return result
 
def clear_screen():
    """ Clears the screen. Works in UNIX. """
    import os, sys
    sys.stdout.write(os.popen('clear').read())
    
def wait(seconds):
    """ Pauses the program for a given number of seconds """
    import time
    time.sleep(seconds)
 
if __name__ == '__main__':
    try:
        print file_to_list("prueba.txt", True)
        wait(1)
        clear_screen()
        print file_to_list("prueba.txt", True)
    except:
        pass
