from occurences import count_occurences

def test_occurences():
    input = [1, 2, 1, 2, 3, 3, 4, 4, 6]
    uniques = set(input)
    output = {uniq: input.count(uniq) for uniq in uniques}

    assert count_occurences(input) == output
