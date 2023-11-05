def sum_of_elements(numbers, excludeNegatives = False):
    result = 0;
    for i in numbers:
        if (not excludeNegatives or (excludeNegatives and i > 0)):
            result += i;
    return result;

Numbers = list(map(int, input("Enter numbers separated by spaces: ").split()));
UserAnswer = input("Do You want to exclude negative numbers?")
while(UserAnswer != "yes" and UserAnswer != "no"):
    UserAnswer = input("Do You want to exclude negative numbers? Enter yes/no: ");

print("Sum of elements in array: ", sum_of_elements(Numbers, UserAnswer=="yes"));
