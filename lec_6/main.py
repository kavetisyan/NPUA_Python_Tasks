import random;

def generate_random_matrix(columns, rows):
    return [[random.randint(1, 9) for _ in range(columns)] for _ in range(rows)];

def get_column_sum(matrix, column):
    result = 0;
    for i in matrix:
        result += i[column];
    return result;

def get_row_sum(matrix, row):
    return sum(matrix[row]);   

def printMatrix(matrix):
    for x in matrix:
        print(x);

matrix = generate_random_matrix(4, 5);
printMatrix(matrix);
print("Sum of elements in column with index of 2: ", get_column_sum(matrix, 2));
print("Sum of elements in row with index of 2: ", get_row_sum(matrix, 3));
