import random

class WeightedList(dict):
    def cum_weights(self):
        keys = []
        weights = []
        last = 0
        for i in self:
            keys += [i]
            weights += [self[i] + last]
            last = weights[-1]
        return(keys, weights)
    def pick_over(self, target):
        keys, weights = self.cum_weights()
        for k,w in zip(keys, weights):
            if w > target: return(k)
    def get_random(self):
        keys, weights = self.cum_weights()
        target = random.randrange(0,max(weights))
        return self.pick_over(target)
