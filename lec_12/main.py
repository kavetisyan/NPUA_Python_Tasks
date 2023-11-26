import random;
import time;

def generateFile(filePath):
    file = open(filePath, 'w');
    for _ in range(100):
        line = ' '.join(str(random.randint(1, 100)) for _ in range(20));
        file.write(line + '\n');

def readLinesFromFile(filePath):
    file = open(filePath, 'r');
    lines = file.readlines();
    return list(map(lambda line: list(map(int, line.split())), lines));

def filterNumbers(arr):
    return list(filter(lambda x: x > 40, arr));

def writeArraysInFile(filePath, int_arrays):
    file = open(filePath, 'w');
    for int_array in int_arrays:
        line = ' '.join(map(str, int_array));
        file.write(line + '\n');

def readAsGenerator(filePath):
    file = open(filePath, 'r');
    for line in file:
        yield list(map(int, line.split()));

def measureExecutionTime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time();
        result = func(*args, **kwargs);
        end_time = time.time();
        execution_time = end_time - start_time;
        print(f"{func.__name__} executed in {execution_time} seconds");
        return result;
    return wrapper;

@measureExecutionTime
def executeFunctions(filePath):
    arrays = readLinesFromFile(filePath);
    for line in arrays:
        print(line);
    filteredArrays = [filterNumbers(array) for array in arrays];
    writeArraysInFile(filePath, filteredArrays);
    generatedArrays = readAsGenerator(filePath);
    for line in readAsGenerator(filePath):
        print(line);

try:
    filePath = "lec_12//test.txt";
    generateFile(filePath);
    executeFunctions(filePath);
except FileNotFoundError:
    print("File ", filePath , " not found.");
except Exception as e:
    print(e);
finally:    
    print("File closed.");
