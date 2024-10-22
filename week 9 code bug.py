def calculate_average(numbers):
    if not numbers:
        return "The list is empty, cannot calculate average."
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)  # Use = for assignment, not ==
    return average

numbers = [10, 20, 30, 40, 50]

# Fix the function call and format the output correctly
print("The average is:", calculate_average(numbers))
