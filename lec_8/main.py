import random;

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows;
        self.columns = columns;
        self.matrix = [[random.randint(1, 9) for _ in range(self.columns)] for _ in range(self.rows)];
        
    def printMatrix(self):
        for row in self.matrix:
            print(row);
    
    def calculateMean(self):
        total = 0;
        for row in self.matrix:
            total += sum(row);
        mean = total / (self.rows * self.columns);
        return mean;
    
    def calculateRowSum(self, n):
        if 0 <= n < self.rows:
            return sum(self.matrix[n]);
        else:
            return "Row number is not correct";
    
    def calculateColumnAverage(self, n):
        if 0 <= n < self.columns:
            total = sum(row[n] for row in self.matrix);
            average = total / self.rows;
            return average;
        else:
            return "Column number is not correct";
    
    def printSubmatrix(self, col1, col2, row1, row2):
        submatrix = [[self.matrix[i][j] for j in range(col1, col2+1)] for i in range(row1, row2+1)]
        for row in submatrix:
            print(row)

matrix = Matrix(3, 4);
matrix.printMatrix();
print("Mean of the matrix:", matrix.calculateMean());
row = 1;
print(f"Sum of row {row}: {matrix.calculateRowSum(row)}");
column = 2;
print(f"Average of column {column}: {matrix.calculateColumnAverage(column)}");
col1 = 1;
col2 = 2;
row1 = 0;
row2 = 1;
print(f"Submatrix With columns from {col1} to {col2} and rows from {row1} to {row2}");
matrix.printSubmatrix(col1, col2, row1, row2);
