class removeStagParantheses:
    def minRemove(self, st):
        idx_to_remove=set()
        stack=[]
        for i, c in enumerate(st):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(i)
            elif not stack:
                idx_to_remove.add(i)
            else:
                stack.pop()
        print("indexes_to_remove",idx_to_remove)
        idx_to_remove = idx_to_remove.union(set(stack))
        print("indexes_to_remove",idx_to_remove)
        string_builder=[]
        for i, c in enumerate(st):
            if i not in idx_to_remove:
                string_builder.append(c)
        return "".join(string_builder)
        
removestagparantheses=removeStagParantheses()
st="iam(t(he)be)st)"
print(removestagparantheses.minRemove(st))