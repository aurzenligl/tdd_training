'''
You see this function in your codebase.
Maybe you want to change/extend its functionality, maybe you want to fix a bug.
You don't know what it does and don't understand implementation.

Luckily, you've got a suite of tests which serve as the only readable documentation of what this does.
You can run those and see that they pass.

How would you approach refactoring this function, so as to make it readable?
'''

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
