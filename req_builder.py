'''
Define a req as taking NUM out of the reqs specified in list REQS.
A req is a list of courses or reqs.
'''
class Req():
    def __init__(self, reqs, units, num=-1):
        self.reqs = reqs
        self.num = num
        self.units = units
        self.all = num == -1 #I don't understand what this means
        