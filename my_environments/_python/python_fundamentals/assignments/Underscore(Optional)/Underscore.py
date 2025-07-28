class Underscore:

    def map(self, iterable, callback):
        result = []
        for item in iterable:
            result.append(callback(item))
        return result

    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None  # if nothing matched

    def filter(self, iterable, callback):        
        result = []
        for item in iterable:
            if callback(item):
                result.append(item)
        return result

    def reject(self, iterable, callback):
        result = []
        for item in iterable:
            if not callback(item):
                result.append(item)
        return result

_ = Underscore()
print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6,55], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1, 2, 3, 4, 5, 6, 88], lambda x: x % 2 == 0))
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]
print(_.reject([33,42,5,6], lambda x: x%2==0))