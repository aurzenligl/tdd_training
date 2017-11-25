def tsort(depvects):
    known = set()
    index = 0
    while index < len(depvects):
        skip = False
        for dep in depvects[index][1:]:
            if dep not in known:
                found = (candidate for candidate in depvects[index + 1:] if candidate[0] == dep).next()
                found_index = depvects.index(found)
                depvects.insert(index, depvects.pop(found_index))
                skip = True
                break
        if skip:
            continue
        known.add(depvects[index][0])
        index += 1
    return depvects
