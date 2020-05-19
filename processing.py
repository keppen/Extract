import methods as mt

def cycles (data):
    otp = ''
    print ('in process', mt.ener(data))
    elist = mt.ener(data)
    for f in elist[0]:

        otp += f[0]
        otp += '\n'
        for i in range(1, len(f)):
            otp += '%3i\t%f\n' % (i, f[i])

    otp += '\n'
    for i in range(len(data)):
        otp += '\tElectron correaltion\n'
        otp += '%3i\t%f\t%f\n\n' % (i, elist[1][i][1], elist[1][i][2])
    return (otp)
