class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
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
        """
        :rtype: int
        """
        return self.n.pop(0)
      
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n