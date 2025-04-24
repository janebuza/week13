def findMaxInList (numbers):
    max = 0;
    count = 0;
    while count < len(numbers):
        if numbers[count] > max:
            max = numbers[count];
        count+=1;
    return max;

listOfNumbers = [3, 9, 15, 2, 360, 47.8, 365];
print(findMaxInList(listOfNumbers));