import random
import string
import threading
import multiprocessing
import time

def measureExecutionTime(func):
    def wrapper(*args, **kwargs):
        if multiprocessing.current_process().name == 'MainProcess':
            start_time = time.time();
            result = func(*args, **kwargs);
            end_time = time.time();
            execution_time = end_time - start_time;
            print(f"{func.__name__} executed in {execution_time} seconds");
            return result;
        else:
            return func(*args, **kwargs);
    return wrapper;

@measureExecutionTime
def generateFile(filePath, size):
    file = open(filePath, 'w');
    for _ in range(size):
        sentence = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 10))) for _ in range(random.randint(3, 20))]);
        file.write(sentence + '\n');

@measureExecutionTime
def countWords(filePath):
    wordFreq = {};
    file = open(filePath, 'r');
    for line in file:
        words = line.split()
        for word in words:
            wordFreq[word] = wordFreq.get(word, 0) + 1;
    return wordFreq;

@measureExecutionTime
def countWordsWithThreads(filePath, threadsCount):
    wordFreq = {}
    lock = threading.Lock()

    def countChunkWords(chunk):
        nonlocal wordFreq;
        localWordFreq = {};
        for line in chunk:
            words = line.split();
            for word in words:
                word = word.strip('.,');
                localWordFreq[word] = localWordFreq.get(word, 0) + 1;

        with lock:
            for word, count in localWordFreq.items():
                wordFreq[word] = wordFreq.get(word, 0) + count;

    file = open(filePath, 'r');
    lines = file.readlines();
    chunkSize = len(lines) // threadsCount;
    chunks = [lines[i:i + chunkSize] for i in range(0, len(lines), chunkSize)];

    threads = [];
    for chunk in chunks:
        thread = threading.Thread(target=countChunkWords, args=(chunk,));
        threads.append(thread);
        thread.start();

    for thread in threads:
        thread.join();
    
    return wordFreq;

def countChunkWords(chunk):
    localWordFreq = {};
    for line in chunk:
        words = line.split()
        for word in words:
            localWordFreq[word] = localWordFreq.get(word, 0) + 1;

    return localWordFreq;

@measureExecutionTime        
def countWordsWithMultiprocessing(filename, processesCount):
    file = open(filename, 'r');
    lines = file.readlines();

    chunkSize = len(lines) // processesCount;
    chunks = [lines[i:i + chunkSize] for i in range(0, len(lines), chunkSize)];

    results = [];
    
    if __name__ == '__main__':
        with multiprocessing.Pool(processes=processesCount) as pool:
            results = pool.map(countChunkWords, chunks);

    wordFreq = {};
    for localWordFreq in results:
        for word, count in localWordFreq.items():
            wordFreq[word] = wordFreq.get(word, 0) + count;

    return wordFreq;

filePath = 'lec_13//test.txt';
generateFile(filePath, 100000);
wordFrequencies = countWords(filePath);
wordFrequenciesWithThreads = countWordsWithThreads(filePath, 4);
wordFrequenciesWithMultiprocessing = countWordsWithMultiprocessing(filePath, 4);
