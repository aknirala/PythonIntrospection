import re
'''
given object it should output it's attribute etc:
Object type:
'''
def dummyFun():
    print('I am dummy')
def AnalyzeObj(obj, exclRgEx=["__doc__", "__builtins__"]):
    q = input('Press Enter, help would be displayed (q to Quit the help, b4 it appears)')
    if q != 'q' and q != 'Q':
        help(obj)
    print('Type of object passed: ')
    print(type(obj))
    print('It has : '+str(len(dir(obj)))+' number of attributes/function etc')
    cnt = 1
    objDir = dir(obj)
    objs = {}
    patterns = list()
    for exR in exclRgEx:
        patterns.append(re.compile(exR))
    for o in objDir:
        toBExcluded = False
        for p in patterns:
            if p.match(o):
                toBExcluded = True
                print(str(cnt)+'> Excluding: '+o)
                cnt += 1
                break
        if toBExcluded:
            continue
        objs[o] = False;
        
    attDic = {}
    for l in dir(obj):
        if type(getattr(obj,l)) not in attDic:
            attDic[type(getattr(obj,l))] = list()
        attDic[type(getattr(obj,l))].append(l)

    simpleType = [bool, str, float, int]
    dictType = [dict, list]
    functionType = [type(dummyFun), ]
    moduleType = [type(re), ]

    alltypes = [simpleType, dictType, functionType, moduleType]
    for tp in [tp for types in alltypes for tp in types]:
        firstFound = False
        for o in [o for o in objs.keys() if not objs[o]]:
            if type(getattr(obj, o)) == tp:
                objs[o] = True
                if not firstFound:
                    firstFound = True
                    print('\n For Type: ')
                    print(tp)
                print(cnt)
                cnt += 1
                print(o)
                if type(getattr(obj, o)) in simpleType:
                    print('Its value: '+str(getattr(obj,o)))
                if type(getattr(obj, o)) == list:
                    print('Its list value: ')
                    print(getattr(obj,o))
                if type(getattr(obj, o)) == dict:
                    objDV = getattr(obj, o)
                    print('Its Dict has values: ')
                    for k in objDV.keys():
                        print("->")
                        print(k)
                        print(objDV[k])
    print('Attributes not mapped')
    for o in [o for o in objs.keys() if not objs[o]]:
        print("("+o+", "+type(getattr(obj,o)).__name__+")")
