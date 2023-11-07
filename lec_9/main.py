import random;

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows;
        self.columns = columns;
        self.matrix = [[random.randint(1, 9) for _ in range(self.columns)] for _ in range(self.rows)];

    def __str__(self):
        matrixString = "";
        for row in self.matrix:
            matrixString += " ".join(str(element) for element in row) + "\n";
        return matrixString;

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns);
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j];
            return result;
        else:
            print("Matrix sizes are not incorrect.");

    def __sub__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns);
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j];
            return result;
        else:
            print("Matrix sizes are not incorrect.");

    def __mul__(self, other):
        if self.columns == other.rows:
            result = Matrix(self.rows, other.columns);
            for i in range(result.rows):
                for j in range(result.columns):
                    result.matrix[i][j] = 0;
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j];
            return result;
        else:
            print("Matrix sizes are incorrect.");

matrix1 = Matrix(3, 3)
matrix2 = Matrix(3, 3)

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Matrix Addition:")
print(matrix1 + matrix2)

print("Matrix Subtraction:")
print(matrix1 - matrix2)

print("Matrix Multiplication:")
print(matrix1 * matrix2)
