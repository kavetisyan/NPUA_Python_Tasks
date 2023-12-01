def multiply_vector_matrix(vector, matrix, fileName):    
    if len(vector) != len(matrix):
        print("Vector and matrix dimensions are not correct.");
        return;
    
    result = [sum(vector[i] * matrix[j][i] for i in range(len(vector))) for j in range(len(matrix))];
    file = open(fileName, 'w');
    file.write(','.join(map(str, result)));
    print("Successfully calculated.");

vector = [3, 2, 1];
matrix = [[1, 2, 3], [4, 5, 6], [3, 2, 1]];
fileName = 'lab_3//result.txt';
multiply_vector_matrix(vector, matrix, fileName);
