'''
Define a req as taking NUM out of the reqs specified in list REQS.
A req is a list of courses or reqs.
'''
class Req():
    def __init__(self, reqs, num=-1):
        self.reqs = reqs
        self.num = num
        self.all = num == -1 #I don't understand what this means
        