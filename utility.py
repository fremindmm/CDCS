# -*- coding:utf-8 -*-
import json
import codecs 
from pprint import pprint 

def addSolutionInfo(id):
    """
    Add one solution of a competition
    """
    with codecs.open('solutions.json', 'r', encoding='utf-8') as f:
        solutions = json.load(f)
    if str(id) in solutions.keys():
        print("ID exsited, please try again")
        return 
    algo = input("Enter algorithm: ")
    code = input("Enter code: ")
    s = {"algorithm": algo, "code":code}
    solutions[id] = s
    with codecs.open("solutions.json", 'w', encoding='utf-8') as f:
        json.dump(solutions, f, indent=4)

def addCompe():
    """
    Add a competition
    """
    with codecs.open('competitions.json', 'r', encoding='utf-8') as f:
        coms = json.load(f)
    with codecs.open('solutions.json', 'r', encoding='utf-8') as f:
        solutions = json.load(f)
    cid = max([int(i) for i in solutions.keys()]) + 1
    newCom = {}
    for i in ["name", "link", "type", "platform", "pic", "hosts", "ddl"]:
        newCom[i] = input("Enter %s: "%(i))
    newCom["pic"] = "https://github.com/geekinglcq/CDCS/blob/master/img/%s?raw=true"%(newCom["pic"])
    solution = []
    num = input("How many solutins you find?  ")
    for i in range(int(num)):
        rank = input("Rank: ")
        print("The id of this solutions is %d"%(cid))
        addSolutionInfo(cid)
        solution.append({"rank":rank, "id":cid})
        cid += 1
        
    newCom["solutions"] = solution
    coms.append(newCom)
    with codecs.open("competitions.json", "w", encoding='utf-8') as f:
        json.dump(coms, f, indent=4)

def renderToMK():
    data = codecs.open("header.md", 'r', 'utf-8').readlines()
    f = codecs.open("ReadMe.md", 'w', 'utf-8')
    coms = json.load(codecs.open('competitions.json'))
    solutions = json.load(codecs.open('solutions.json'))
    for line in data:
        f.write(line)
    f.write("||名称|类型|截止日期|解决方案|平台|主办方|  \n")
    f.write("|--|--|--|--|--|--|--|  \n")
    for com in coms:
        f.write("|![](http://p0qqn3m6c.bkt.clouddn.com/%s?imageView2/2/w/100/h/100/q/75)|[%s](%s)|%s|%s|"%( \
             com['pic'][51:-9], com['name'], com['link'], com['type'], com['ddl']))
        soStrings = []
        print(com['name'])
        for solution in com['solutions']:
            st = "第%s名 "%(solution['rank'])
            so = solutions[str(solution['id'])]
            if so['algorithm'] != "null":
                st = "%s [算法](%s)"%(st, so['algorithm'])
            if so['code'] != "null":
                st = "%s [代码](%s)"%(st, so['code'])
            soStrings.append(st)
        f.write('<br>'.join(soStrings))
        f.write("|%s|%s|  \n"%(com['platform'], com['hosts']))
    
    f.close()
        
