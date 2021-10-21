class Python_list_methods:

    def __init__(self):
        
        foo = [1,2,3]

        foo.append(4)       # [1,2,3,4]
        foo.insert(1,8)     # [1,8,2,3,4]
        foo.pop(1)          # [1,2,3,4]

        foo = [1,2,2,3]
        foo.remove(2)       # [1,2,3]
        foo.reverse()       # [3,2,1]

        foo = [2,3,1]
        foo.sort()          # [1,2,3]
        foo.index(3)        # 2

        foo = [1,2,3,3]
        foo.count(3)        # 3
