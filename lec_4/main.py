def classify_numbers(numbers):
    oddNumbers = [];
    evenNumbers = [];
    for i in numbers:
        if(i % 2 == 0):
            evenNumbers.append(i);
        else:
            oddNumbers.append(i);
    return oddNumbers, evenNumbers;

Numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
OddNumbers, EvenNumbers = classify_numbers(Numbers);
print("Odd Numbers:", OddNumbers);
print("Even Numbers:", EvenNumbers);
