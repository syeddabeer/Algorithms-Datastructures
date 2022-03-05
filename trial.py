class NestedIterator:
    def __init__(self, nestedList):
        def flatten(nl):
            tmp=[]
            for i in nl:
                if i.isInteger():
                    tmp.append(i)
                else:
                    tmp.extend(flatten(i.getList()))
            return tmp

        self.n = flatten(nestedList)
    def next(self):
        return self.n.pop(0)

    def hasNext(self):
        return len(self.n)>0