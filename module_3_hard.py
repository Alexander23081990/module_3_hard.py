def calculate_structure_sum(data_structure):
    calc_ = 0
    if isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            calc_ += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            calc_ += calculate_structure_sum(key)
            calc_ += calculate_structure_sum(value)
    elif isinstance(data_structure, (int, float)):
        calc_ += data_structure
    elif isinstance(data_structure, str):
        calc_ += len(data_structure)
    return calc_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
