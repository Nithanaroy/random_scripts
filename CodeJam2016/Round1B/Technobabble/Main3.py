def find_fakes(l):
    fw = []
    lw = []
    for t in l:
        p1, p2 = t.split(" ")
        fw.append(p1)
        lw.append(p2)
    fwc = fw[::-1]
    lwc = lw[::-1]
    fake = 0
    for i in range(0, len(fw)):
        try:
            fwi = fwc.index(fw[i])
            lwi = lwc.index(lw[i])
            if fwi is not len(fw) - i and lwi is not len(fw) - i:
                fwc.pop(len(fw) - i)
                lwc.pop(len(fw) - i)
                fake += 1
        except ValueError:
            pass
    return fake


print find_fakes(['HYDROCARBON COMBUSTION', 'QUAIL BEHAVIOR', 'QUAIL COMBUSTION'])
