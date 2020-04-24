class instanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        instanceCounter.count +=1 

    def self_val(self,newVal):
        self.val = newVal

    def get_val(self):
        return self.val
    

    def get_count(self):
        return instanceCounter.count


a = instanceCounter(9)
b = instanceCounter(18)
c = instanceCounter(27)


for obj in (a, b, c):
    print('val of obj: %s' %(obj.get_val()))
    print('count: %s' %(obj.get_count()))