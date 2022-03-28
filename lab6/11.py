def print_operation_table(operation = 1, num_rows=9, num_columns=9):
    for row in range(1, num_rows + 1):
        table = []
        for column in range(1, num_columns):
            table.append(operation(row, column))
        print(''.join(f'{el:< 4}' for el in table))

print_operation_table(lambda x, y: x * y)