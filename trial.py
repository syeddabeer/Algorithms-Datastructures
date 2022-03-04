class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x:x[1]-x[0])
        energy=0
        for task in tasks:
            energy = task[0]+max(energy, task[1]-task[0])
        return energy