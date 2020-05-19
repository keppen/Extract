import sys
import methods as mt
import processing as ps

fp = sys.argv
fp.pop(0)
print (fp)

def sel (path):
    if path[0] == '0':
        path.pop(0)
        for i in mt.inp(path):
            name = i[0].replace('.xyz', '.inp')
            w = open (name, 'w')
            w.write(i[1])
            w.flush

    if path[0] == '1':
        path.pop(0)
        for i in mt.opt(path):
            name = i[0].replace('.log', '.xyz')
            w = open (name, 'w')
            w.write(i[1])
            w.flush
    if path[0] == '2':
        path.pop(0)
        u = ps.cycles(path)
        w = open('ceneriges.txt', 'w')
        w.write(u)
        w.flush
    if path[0] == '3':
        path.pop(0)
        u = mt.scan(path)
        w = open('scan.txt', 'w')
        w.write(u)
        w.flush

sel(fp)
