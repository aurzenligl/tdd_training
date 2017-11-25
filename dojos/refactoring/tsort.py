def tsort(depvects):
    known = []
    index = 0
    while index < len(depvects):
        skip = False
        for dep in depvects[index][1:]:
            if dep not in known:
                for vec in depvects[index + 1:]:
                    if vec[0] == dep:
                        break
                for i, dv in enumerate(depvects):
                    if dv is vec:
                        break
                depvects.insert(index, depvects.pop(i))
                skip = True
                break
        if skip:
            continue
        known.append(depvects[index][0])
        index += 1
    return depvects
