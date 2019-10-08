import math
import string


def task_1(list_1, list_2):
    """
    Take two lists, say for example these two:
      a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
      b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements
    that are common between the lists (without duplicates).
    """
    # return sorted(list(set(list_1 + list_2)))
    return list(set(x for x in list_1 if x in list_2))


def task_2(value):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """
    return value.count("a")


def task_3(value):
    """
    Write a Python program to check if a given positive integer is a power of three
    Input : 9
    Output : True
    """
    if isinstance(value, int):
        return int(math.log(value, 3)) == math.log(value, 3)
    else:
        raise ValueError("value not int")


def task_4(value):
    """
    Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
    Input : 48
    Output : 3
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5
    """
    while len(str(value)) > 1:
        value = sum(int(x) for x in str(value))
    return value


def task_5(value):
    """
    Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    return [x for x in value if x > 0] + [0] * value.count(0)


def task_6(value):
    """
    Write a Python program to check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such
    that the difference between the consecutive terms is constant.
    For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.
    """
    diff = set()
    for i in range(len(value) - 1):
        diff.add(value[i + 1] - value[i])
    return len(diff) == 1


def task_7(value):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    return [x for x in set(value) if value.count(x) == 1]


def task_8(value):
    """
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    result = []
    for i in range(len(value) - 1):
        if value[i + 1] - value[i] > 1:
            result.append(value[i] + 1)
    return result


def task_9(value):
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    """
    inc = 0
    for i in range(len(value)):
        if not isinstance(value[i], tuple):
            inc += 1
        else:
            break
    return inc
    # return [value.index(x) for x in value if isinstance(x, tuple)][0]


def task_10(value):
    """
    Write a program that will take the str parameter being passed and return the string in reversed order.
    For example: if the input string is "Hello World and Coders" then
    your program should return the string sredoC dna dlroW olleH.
    """
    return value[::-1]


def task_11(value):
    """
    Write a program that will take the num parameter being passed and
    return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    return f"{value // 60}:{value % 60}"


def task_12(value):
    """
    Write a program that will take the parameter being passed and
    return the largest word in the string.
    If there are two or more words that are the same length,
    return the first word from the string with that length.
    Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time

    Input:"I love dogs"
    Output:love
    """
    prepared = value.translate(str.maketrans('', '', string.punctuation)).split()
    return max(prepared, key=lambda x: len(x))


def task_13():
    """
    Write a program (using functions!) that asks the user for a long string containing multiple words.
    Print back to the user the same string, except with the words in backwards order.
    For example:
    Input: My name is Michele
    Outout: Michele is name My
    """
    value = input("Long string: ")
    return ' '.join(value.split()[::-1])


def task_14():
    """
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
    Take this opportunity to think about how you can use functions.
    Make sure to ask the user to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum
    of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
    """
    value = int(input("how many Fibonnaci numbers to generate: "))

    def fibonacci(n):
        if n in [1, 2]:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    return [fibonacci(x) for x in range(1, value + 1)]
    # value = int(input("how many Fibonnaci numbers to generate: "))
    # result = [1] * value
    # if value > 2:
    #     result[0], result[1] = 1, 1
    #     for i in range(2, value):
    #         result[i] = result[i - 2] + result[i - 1]
    # return result


def task_15(value):
    """
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and
    makes a new list that has only the even elements of this list in it.
    """
    return [x for x in value if x % 2 == 0]


def task_16(value):
    """
    Write a program that will add up all the numbers from 1 to input number.
    For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    return sum(list(range(value + 1)))


def task_17(value):
    """
    Write a program that will take the parameter being passed and return the factorial of it.
    For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.

    """
    # result = 1
    # for num in range(1, value + 1):
    #     result *= num
    return value * task_17(value - 1) if value > 1 else 1


def task_18(value):
    """
    Write a program that will take the str parameter being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the alphabet (ie. cbecomes d, zbecomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
    Input: abcd
    Output: bcdE

    """
    list_of_char = string.ascii_lowercase + 'a'
    value = [list_of_char[list_of_char.index(x) + 1] for x in value]
    value = [x.upper() if x in ["a", "e", "i", "o", "u"] else x for x in value]
    return ''.join(x for x in value)


def task_19(value):
    """
    Write a program that will take the str string parameter being passed and
    return the string with the letters in alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde

    """
    return ''.join(sorted(value.translate(str.maketrans('', '', string.punctuation + string.digits))))


def task_20(num1, num2):
    """
    Write a program that will take both parameters being passed and return the true if num2 is greater than num1,
    otherwise return the false. If the parameter values are equal to each other then return the string -1
    """
    if num2 > num1:
        return True
    elif num2 < num1:
        return False
    else:
        return "-1"
