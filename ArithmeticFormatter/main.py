def arithmetic_arranger(num_array, display_answers = False):
    operations_dictionary = getOperationsDictionary(num_array)
    
    # Check if operations_dictionary returned an error
    if isinstance(operations_dictionary, str):
        return operations_dictionary
    
    # Row strings
    top_row = ''
    bottom_row = ''
    middle_row = ''
    result_row = ''
    
    # Iterate over the values in operations_dictionary
    for dic_operation in operations_dictionary.values():
        # Get the numbers and the operator
        num1 = str(dic_operation['num1'])
        num2 = str(dic_operation['num2'])
        operator = dic_operation['operator']
        result = str(dic_operation['result'])
        
        # Determine the maximum length needed
        max_length = max(len(num1), len(num2)) + 2  # +2 for the operator and space
        
        # Format each part of the arithmetic problem
        top_row += num1.rjust(max_length) + '    '
        bottom_row += operator + num2.rjust(max_length - 1) + '    '
        middle_row += '-' * max_length + '    '
        result_row += result.rjust(max_length) + '    '
    
    if display_answers:
        arranged_problems = f"{top_row.rstrip()}\n{bottom_row.rstrip()}\n{middle_row.rstrip()}\n{result_row.rstrip()}"
    else:
        arranged_problems = f"{top_row.rstrip()}\n{bottom_row.rstrip()}\n{middle_row.rstrip()}"
    
    return arranged_problems
    
    print(arranged_problems)  #Print the arranged problems
   
def getOperationsDictionary(num_array):
    # Initialize the dictionary to store operations
    dic = {}
    
    # Iterate over each arithmetic problem
    for iteration, num in enumerate(num_array):
        # Initialize result variable
        result = 0
        
        # Split the operation into its components
        num_operation = num.split(" ")
        num1, operator, num2 = num_operation[0], num_operation[1], num_operation[2]
        
        # Check if both parts contain only numbers
        if not (num1.isnumeric() and num2.isnumeric()):
            return "Error: Numbers must only contain digits."
        
        # Check for digit length
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        #Check for too many problems
        if len(num_array) > 5:
            return 'Error: Too many problems.'
        
        # Get the operation result
        if operator == '+':
            result = int(num1) + int(num2)
        elif operator == '-':
            result = int(num1) - int(num2)
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Add the current operation to the dictionary
        dic[iteration] = {
            'length': max(len(num1), len(num2)),
            'num1': num1,
            'num2': num2,
            'operator': operator,
            'result': str(result)  # Store result as string for formatting
        }
    
    return dic

given_num_array = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
arithmetic_arranger(given_num_array)
