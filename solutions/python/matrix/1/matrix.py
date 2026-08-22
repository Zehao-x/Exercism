class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(element) for element in row_string.split()] for row_string in matrix_string.split("\n")]


    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column = []
        for i in range(len(self.matrix)):
            column.append(self.matrix[i][index-1])

        return column
            
        
