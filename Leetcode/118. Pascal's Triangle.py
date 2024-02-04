class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1, 2]]

        box = [1, 1]
        for i in range(1, numRows):
            new_box = []
            new_box.append(0, 1)
            size = len(box)
            while i < size:
                new_box[i] = box[i]+box[i+1]
                i += 1
        box = new_box
        return box
