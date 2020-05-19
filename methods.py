#!/usr/bin/env python3
# -*- coding: utf-8 -*-

elements = {'1': 'H', '6': 'C',
            '8': 'O', '9': 'F',
            '7': 'N','15': 'P' }

#extracting energies form .log
#return list of enegies of each cycle
def ener (data):

    e = []
    c = []
    for f in data:
        fenergy = [f]
        fcorr = [f]
        with open(f, 'r') as o:


            for i in o :
                line = i.split()
                if len(line) > 3:

                    if line[0] == 'E=':
                        fenergy.append (float (line[1]) )
                    elif line[0] == 'Iteration':
                        fenergy.append (float (line[3]) )
                    elif line[2] == 'E(RHF)=':
                        fenergy.appand (float (line[4]) )
                    elif line[0] == 'E2' and line[3] == 'EUMP2':
                        l1 = line[2].replace('D', 'e').replace('+', '')
                        l2 = line[5].replace('D', 'e').replace('+', '')
                        fcorr.append(float (l1) )
                        fcorr.append(float (l2) )
        e.append(fenergy)
        c.append(fcorr)
    return e, c


#extracting optimalized structure form .log
#retuns formated string
def opt (data):
    a = []
    for f in data:

        with open(f, 'r') as o:

            for i in o:
                line = i.split()
                if len(line) > 0:
                    if line[0] == "NAtoms=":
                        natoms = int(line[1])
                        break

            for i in o:
                if i.strip() == 'Standard orientation:':
                    c = 0
                    line = []
                    for j in o:
                        line.append(j)
                        c += 1
                        if c == natoms + 5:
                            break

            xyz = str (natoms) + '\n'
            xyz += '\n'
            for i in range(4, len(line) - 1):
                l = line[i].split()
                xyz += '%2s %13.6f %13.6f %13.6f\n' % (elements[l[1]],
                                                        float(l[3]),
                                                        float(l[4]),
                                                        float(l[5]) )
            coord = [str(f), xyz]
        a.append(coord)
    return a


def inp (data):
    a = []
    for f in data:

        with open(f, 'r') as o:
            lines = o.readlines()
            inp = '# HF/6-31G(d) Opt'
            inp += '\n \n \n0 1\n'

            for i in range (2, len(lines)):
                inp += lines[i]
            coord = [f, inp]
        a.append(coord)
    return a

def scan (data):
    a = []
    otp = ''
    for f in data:
        temp =[]
        with open(f, 'r') as o:
            for i in o:
                l = i.split()
                if len(l) > 5:
                    if l[:3] == ['4','4','H']:
                        temp.append(l[10].replace('(', ''))
                        a.append(temp)
                        temp = []
                    elif l[2] == 'E(RHF)':
                        temp.append(l[4].replace('D', 'e'))
        a.pop(0)
        otp += f[0] +'\n'
    for i in a:
        otp += '%9.4f\t%13.9f\n' % (float(i[0]), float( i[1]))
    return (otp)
