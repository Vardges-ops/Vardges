import pathlib
from pathlib import Path
from datetime import datetime

err = 0
info = 0
result = 0
inp = input("Input the operation and number separated by whitespace : ")
now = datetime.now()
dtime = now.strftime("%m/%d/%Y, %H:%M:%S")
if inp:
    info += 1
    print(f"Expression: {inp}")
    try:
        oper, x1, x2 = inp.split(" ", 3)
        if (type(x1) == float or int) and (type(x2) == float or int):
            if oper == '+':
                result = float(x1) + float(x2)
            elif oper == '-':
                result = float(x1) - float(x2)
            elif oper == '*':
                result = float(x1) * float(x2)
            elif oper == '/':
                result = float(x1) / float(x2)
            else:
                err += 1
        if err == 0:
            if type(result) != float:
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
        else:
            print("ERROR : Invalid expression")
        print(f"Report: INFO-{info} ERROR-{err}")
    except:
        err += 1
        print("ERROR : Invalid expression")
        print(f"Report: INFO-{info} ERROR-{err}")
else:
    noinfo = "Expression: Not given"
    print(noinfo)
    print(f"Report: INFO-{info} ERROR-{err}")

path = Path.cwd() / 'memory_data'
errwrite = "{{{}}} :: ERROR :: Invalid expression :: {{{}}}".format(dtime, inp)
infwrite = "{{{}}} :: INFO :: {{{}}} :: {{{}}}".format(dtime, inp, result)

try:
    path.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    pass
pathtofile = pathlib.PurePath(path, "memorydata.txt")
with open(pathtofile, "a") as pf:
    if err == 1:
        pf.write(errwrite)
        pf.write('\n')
    else:
        pf.write(infwrite)
        pf.write('\n')
