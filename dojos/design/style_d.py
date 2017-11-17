def countWord(filename, word):
    line_count = 0
    word_count = 0
    with open(filename) as f:
        content = f.read()
        for line in content.splitlines():
            found = line.count(word)
            if found:
                line_count += 1
            word_count += found
    return (line_count, word_count)

def countNumber(filename, number):
    line_count = 0
    word_count = 0
    with open(filename) as f:
        content = f.read()
        for line in content.splitlines():
            found = line.count(str(number))
            if found:
                line_count += 1
            word_count += found
    return (line_count, word_count)


























'''
Copy-paste! Having the same or almost the same code in multiple places
in project increases amount of code to maintain with no good reason.

Above toy example sounds silly, but copy-pastes are harder to find
if they exist as private implementation details scattered throughout repository,
or repetitive boilerplate code in various places in repository.

Or if they are a deeply buried part of large function or class,
inaccessible to potential users.
'''

def countWord(filename, word):
    line_count = 0
    word_count = 0
    with open(filename) as f:
        content = f.read()
        for line in content.splitlines():
            found = line.count(word)
            if found:
                line_count += 1
            word_count += found
    return (line_count, word_count)

def countNumber(filename, number):
    return countWord(filename, str(number))
























def countWord(filename, word):
    line_count = 0
    word_count = 0
    with open(filename) as f:
        content = f.read()
        for line in content.splitlines():
            found = line.count(word)
            if found:
                line_count += 1
            word_count += found
    return (line_count, word_count)

def wordCount(filename, word):
    def add(acc, line):
        words, lines = acc
        found = line.count(word)
        return words + found, lines + bool(found)
    with open(filename) as f:
        return reduce(add, f.readlines(), (0, 0))
































'''
This is a less trivial example. Both functions do exactly the same thing,
but the language features used are different. Imagine these are in different
places in codebase, with different identifier names. No automatic tool for
finding code duplication is going to find this kind of superfluous code.

Two ways of coping with them would be:
    - separation of concerns: solve different problems in different places,
      so that you know where to look for building blocks when you have
      particular problem. As long as similar logic is in the same place,
      it's easier to spot reocurring patterns,
    - code review: someone may spot you're reinventing the wheel (or doing
      old thing better!), which may result in ending up with only with
      solution for given problem - the best of the two

I pick reduce variant. Seems shorter to me.
'''

def countWord(filename, word):
    def add(acc, line):
        words, lines = acc
        found = line.count(word)
        return words + found, lines + bool(found)
    with open(filename) as f:
        return reduce(add, f.readlines(), (0, 0))
