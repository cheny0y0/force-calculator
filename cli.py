# coding=UTF-8

import sys
from os import name as os_name

try :
    raw_input
except NameError :
    pass
else :
    input = raw_input

while 1 :
    try :
        inp = input("Input an expression, or press Ctrl-C to define a function, or press Ctrl-"+["D", "Z plus return"][os_name=="nt"]+" to exit:")
    except KeyboardInterrupt :
        try :
            print("\nDefine a function:(press Ctrl-"+["D", "Z plus return"][os_name=="nt"]+" for done, press Ctrl-C to cancel)")
        except KeyboardInterrupt :
            pass
        else :
            try :
                exec("".join(sys.stdin.readlines()))
            except BaseException as err :
                print("traceback: "+str(err))
    except EOFError :
        break
    else :
        try :
            print(repr(eval(inp)))
        except BaseException as err :
            print("traceback: "+str(err))
