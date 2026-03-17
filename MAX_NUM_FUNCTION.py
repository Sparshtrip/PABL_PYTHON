
def find_maximum(numbers):

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        

        if num > max_num:
            max_num = num
            
        elif num<min_num:
            min_num= num
            print(min_num)

    return max_num,min_num

numbers = [12, 45, 23, 67, 34, 89, 10]

maximum_value,minimum_value = find_maximum(numbers)

print("The maximum value in the list is:",maximum_value )
print("The minimum value in the list is:",minimum_value )
