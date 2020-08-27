import itertools
import random
import math

def has_consecutive_number_before_and_after(target: int, array: []):
    """対象の数字が、対象の数字の前後+-1となる数字をもつことの判定
    :param array: 数字の組み合わせの配列
    :param target: 連続していることを確認する対象の数字
    :return: bool 対象の数字の前後+-1となる数字を同じ配列上に持つかどうか
    """

    count = 0 # targetの+-1の数の個数

    if target+1 in array:
        count += 1
    if target-1 in array:
        count += 1

    return count > 0


def has_one_consecutive_numbers(array: []):
    """対象の組み合わせが、連続する数字のペアを1つだけもつことの判定
    :param array: 数字の組み合わせ
    :return: bool 連続する数字のペアが一つかどうか
    """

    count = 0 # 前後に連続する数字をもつ数字の数

    for num in array:
        if has_consecutive_number_before_and_after(num, array):
            count += 1

    return count == 2

def has_one_same_last_digit_number(target: int, array: []):
    """対象の数字が、下一桁が同じ数字を1つだけもつことの判定
    :param array: 数字の組み合わせの配列
    :param target: 連続していることを確認する対象の数字
    :return: bool 対象の数字の下一桁が同じ数字を同じ配列上に持つかどうか
    """

    count = 0 # targetと下一桁が同じ数字の個数

    for num in array:
        if num != target and num % 10 == target % 10:
            count += 1

    return count == 1

def has_one_pair_same_last_digit_numbers(array: []):
    """対象の組み合わせが、下一桁が同じ数字のペアを1つだけもつことの判定
    :param array: 数字の組み合わせ
    :return: bool 下一桁が同じ数字のペアが一つかどうか
    """

    count = 0 # 下一桁が同じ数字をもつ数字の数

    for num in array:
        if has_one_same_last_digit_number(num, array):
            count += 1

    return count == 2

def get_number_set_list():
    color1 = set()
    color2 = set()
    color3 = set()
    color4 = set()
    color5 = set()
    color6 = set()
    color7 = set()
    for i in range(44):
        if i == 0:
            continue
        if i % 7 == 1:
            color1.add(i)
        if i % 7 == 2:
            color2.add(i)
        if i % 7 == 3:
            color3.add(i)
        if i % 7 == 4:
            color4.add(i)
        if i % 7 == 5:
            color5.add(i)
        if i % 7 == 6:
            color6.add(i)
        if i % 7 == 0:
            color7.add(i)
    return [color1, color2, color3, color4, color5, color6, color7]

def get_ball_number_sets():
    reds =    {1, 8, 15, 22, 29, 36, 43}
    yellows = {2, 9, 16, 23, 30, 37}
    beiges =  {3, 10, 17, 24, 31, 38}
    greens =  {4, 11, 18, 25, 32, 39}
    blues =   {5, 12, 19, 26, 33, 40}
    navys =   {6, 13, 20, 27, 34, 41}
    purples = {7, 14, 21, 28, 35, 42}

    number_set_list = get_number_set_list()
    print("number_set_list: ", number_set_list)
    print("number_set_list[0]: ", number_set_list[0])
    colorSet = (0, 1, 2, 3, 4, 5, 6)
    colorcombs = list(itertools.combinations(colorSet, 6))
    ball_number_sets = ()
    for colorcomb in colorcombs:
        color_list = list(colorcomb)
        print("color_list: ", color_list)
        ball_number_sets = set(itertools.product(
            number_set_list[color_list[0]],
            number_set_list[color_list[1]],
            number_set_list[color_list[2]],
            number_set_list[color_list[3]],
            number_set_list[color_list[4]],
            number_set_list[color_list[5]]))
    return ball_number_sets


    # numbers_set = {}
    # for colors in colorcombs:
    #     numbers_set = set(itertools.product(colors[0], colors[1], colors[2], colors[3], colors[4], colors[5]))
    # print('numbers_set', numbers_set)
    # return array in numbers_set



def main():
    """コマンドで実行する場合には引数として、リストの数字をスペース区切りで入力します
    ex: 整列対象が　[3,8,0,4,2,5,9,1]　の時、
        => # python3 quick_sort 3 8 0 4 2 5 9 1
    """
    seeds = [4, 5, 6, 11, 12, 13, 14, 17, 18, 19, 20, 21, 27, 28, 29, 36, 37, 38, 39, 40]

    combinations = set(itertools.combinations(seeds, 6))
    combinationList = list(combinations)
    fixedList = []

    for combination in combinationList:
        tmp = -1
        left = 0
        numArray = list(combination)
        if has_one_consecutive_numbers(numArray):
            if has_one_pair_same_last_digit_numbers(numArray):
                fixedList.append(combination)

    size = len(fixedList)
    print("size: ", size)

    count = 0
    total = 0
    numbers = []
    ball_number_sets = get_ball_number_sets()
    print("ball_number_sets", ball_number_sets)

    while count < 30:
        result = fixedList[random.randint(0, size-1)]
        if result in ball_number_sets:
            print('apply: ',result)
            array = list(result)
            for num in array:
                numbers.append(num)
                total += num
            count += 1
        # else:
            # print('not apply: ', result)

    # average = total / len(numbers)
    # print('average: ', average)
    # totaldev = 0.0
    # for num in numbers:
    #     totaldev += (num - average)**2
    # variance = totaldev / len(numbers)
    # print('stdev: ', math.sqrt(variance))

if __name__ == '__main__':
    main()