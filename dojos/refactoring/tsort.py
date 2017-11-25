def tsort(depvects):
    kdepvects = []
    idx = 0
    while idx < len(depvects):
        sdep = False
        for dep in depvects[idx][1:]:
            if dep not in kdepvects:
                for depv in depvects[idx + 1:]:
                    if depv[0] == dep:
                        break
                for inx, dv in enumerate(depvects):
                    if dv is depv:
                        break
                depvects.insert(idx, depvects.pop(inx))
                sdep = True
                break
        if sdep:
            continue
        kdepvects.append(depvects[idx][0])
        idx += 1
    return depvects
