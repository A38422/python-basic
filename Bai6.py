class FindThreeNumber:
    def __init__(self, arr):
        self.arr = arr
    def find(self):
        num1 = 0
        num2 = 0
        num3 = 0
        result = []
        for i in range(0, len(self.arr)):
            for j in range(0, len(self.arr)):
                for k in range(0, len(self.arr)):
                    if self.arr[i] + self.arr[j] + self.arr[k] == 0:
                        num1 = i
                        num2 = j
                        num3 = k
                        if [i, j, k] not in result:
                            result.append([i, j, k])
        return result

arr = [1.2, 2.3, -5.2, -0.3, -0.7, 3.6, -0.9, 1]
x = FindThreeNumber(arr)
print(x.find())