class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        return self

    def substract(self, num, *nums):
        self.result -= num
        for number in nums:
            self.result -= number
        return self
# Test    
md = MathDojo()
x = md.add(2).add(2,5,1).substract(2,3).substract(6).result
print(x)
