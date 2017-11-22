'No client should be forced to depend on methods it does not use'

class IWorker(object):
    def work(self):
        raise NotImplementedError
    def eat(self):
        raise NotImplementedError

class Worker(IWorker):
    def work(self):
        print('Worker works')
    def eat(self):
        print('Worker eats')

class SuperWorker(IWorker):
    def work(self):
        print('SuperWorker works')
    def eat(self):
        print('SuperWorker eats')

class RoboWorker(IWorker):
    def work(self):
        print('RoboWorker works')

def work(workers):
    for w in workers:
        w.work()

def eat(workers):
    for w in workers:
        w.eat()

workers = [
    Worker(),
    SuperWorker(),
    RoboWorker(),
]

work(workers)
try:
    eat(workers)
except Exception as e:
    print(type(e))
















'''
By separating worker and eater interfaces we can use only single interface at a time.

Separation of interfaces is less important in duck-typed language like Python,
where you need to depend on entire source code of imported module anyway
and don't pay the cost of static typing interface specification.
'''

class IWorker(object):
    def work(self):
        raise NotImplementedError

class IEater(object):
    def eat(self):
        raise NotImplementedError

class Worker(IWorker, IEater):
    def work(self):
        print('Worker works')
    def eat(self):
        print('Worker eats')

class SuperWorker(IWorker, IEater):
    def work(self):
        print('SuperWorker works')
    def eat(self):
        print('SuperWorker eats')

class RoboWorker(IWorker):
    def work(self):
        print('RoboWorker works')

def work(workers):
    for w in workers:
        if isinstance(w, IWorker):
            w.work()

def eat(workers):
    for w in workers:
        if isinstance(w, IEater):
            w.eat()

workers = [
    Worker(),
    SuperWorker(),
    RoboWorker(),
]

work(workers)
eat(workers)

'''
The same effect can be achieved by grouping workers according to their ability
and calling "work" and "eat" with relevant groups. Python containers may keep
heterogenous objects, and Python functions may attempt to call functions which
may not exist.

Specifying interface just to call isinstance on it sounds like a mediocre idea.
'''
