from typing import List, Dict, Union, Generator
from math import sqrt

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for elem in data:
        if elem.get('name') is not None:
            elem['name'] = elem['name'].capitalize()
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for elem in data:
        for del_key in redundant_keys:
            elem.pop(del_key)
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """

    return [elem for elem in data for item in elem.values() if item == value]


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    return min(data) if len(data) > 0 else None


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    if data:
        result = [str(x) for x in data]
        result_length = [len(x) for x in result]
        min_length_index = result_length.index(min(result_length))
        return result[min_length_index]


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    dict_values_by_key = [x.get(key) for x in data]
    min_value = min(x for x in dict_values_by_key if x is not None)
    min_value_index = dict_values_by_key.index(min_value)
    return data[min_value_index]


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    result_list = []
    for elem in data:
        result_list.extend(elem)
    # return max(max(data))
    return max(result_list)

def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    return sum(ord(elem) for elem in text)


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """

    n = 201
    # d = int(sqrt(n))
    index_for_delete = [0] * n

    for i in range(2, int(sqrt(n)) + 1):
        for j in range(i * i, n, i):
            index_for_delete[j] = 1

    for ind in range(n):
        if index_for_delete[ind] == 0 and ind > 1:
            yield ind

