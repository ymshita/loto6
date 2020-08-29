import itertools
import random
import asyncio
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
    :param target: 連続していることを確認する対象の数字
    :param array: 数字の組み合わせの配列
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
    """loto6で使われる数字のグループのリストを返却します
    :return: intのsetのリスト
    """
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

def get_all_combinations():
    """loto6で使われる7つ数字のグループからそれぞれ1つずつとりだし、6つの数字を選ぶ組み合わせの全てのセットを返却
    :return: 組み合わせのセット
    """
    number_set_list = get_number_set_list()
    colorSet = (0, 1, 2, 3, 4, 5, 6)
    colorcombs = list(itertools.combinations(colorSet, 6))
    ball_number_sets = set()
    for colorcomb in colorcombs:
        color_list = list(colorcomb)
        ball_number_sets = ball_number_sets | set(itertools.product(
            number_set_list[color_list[0]],
            number_set_list[color_list[1]],
            number_set_list[color_list[2]],
            number_set_list[color_list[3]],
            number_set_list[color_list[4]],
            number_set_list[color_list[5]]))
    return ball_number_sets

def get_num_combinations(set_list: []):
    """色分けされた7つのグループから6つ選択する組み合わせのセットを返す
    :param array: シードの数字を色分けされたセットに分けた配列
    :return: set
    """
    colorSet = (0, 1, 2, 3, 4, 5, 6)
    colorcombs = list(itertools.combinations(colorSet, 6))
    combinations = ()
    for colorcomb in colorcombs:
        color_list = list(colorcomb)
        combinations = set(itertools.product(
            set_list[color_list[0]],
            set_list[color_list[1]],
            set_list[color_list[2]],
            set_list[color_list[3]],
            set_list[color_list[4]],
            set_list[color_list[5]]))
    return combinations

async def is_in_right_combinations(combination, right_combinations):
    """対象のセットがいずれかのセット球(クジに使う色違いのボールのセット)のパターンを満たすか判定
    :pram combination: 判定対象のセット
    :pram right_combinations: セット球(クジに使う色違いのボールのセット)のパターンのセット
    :return: bool 判定結果
    """
    return combination in right_combinations

async def get_right_combination_or_blank(combination, right_combinations):
    """対象の組み合わせがセット球(クジに使う色違いのボールのセット)のパターンを満たす場合には返却、満たさない場合には空セットを返却
    :pram combination: 判定対象のセット
    :pram right_combinations: セット球(クジに使う色違いのボールのセット)のパターンのセット
    :return: set 対象のセットが、セット球のパターンに合っていれば返却、それ以外はからセットを返却
    """
    loop = asyncio.get_event_loop()
    is_ok = await is_in_right_combinations(combination, right_combinations)

    if is_ok:
        return combination
    else:
        return set()

def show_set_balls(list: []):
    """セット球のリストを表示します。
    :param list: セット球のリスト
    """
    print("set1: ", list[0])
    print("set2: ", list[1])
    print("set3: ", list[2])
    print("set4: ", list[3])
    print("set5: ", list[4])
    print("set6: ", list[5])
    print("set7: ", list[6])

def main():
    """コマンドで実行する場合には引数として、リストの数字をスペース区切りで入力します
    対象が　[1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 17, 18, 19, 24, 25, 30, 31, 32, 40, 41]　の時、
    `# python3 loto6 1 2 3 4 5 10 11 12 13 14 17 18 19 24 25 30 31 32 40 41`
    """

    seeds = [4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26, 27, 28, 29, 36, 37, 38, 39]
    # seeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    seed_set = set(seeds)
    number_set_list = get_number_set_list()
    
    print('以下のセットそれぞれから1つ以上の数字を選択する必要があります。')
    print('==================================')
    show_set_balls(number_set_list)
    print('==================================')

    blocked_seeds = []

    for number_set in number_set_list:
        if (number_set & seed_set) == set():
            raise ValueError(f'組み合わせの数字を{number_set}から1つ以上選択してください。')
        else:
            blocked_seeds.append(number_set & seed_set)
    print('次のセットから1つずつ取り出し、6つの数字の組み合わせを作ります')
    print('==================================')
    show_set_balls(blocked_seeds)
    print('==================================')

    combinations = get_num_combinations(blocked_seeds)
    combinationList = list(combinations)
    all_combinations = get_all_combinations()
    statements = []

    for combination in combinationList:
        numArray = list(combination)
        if has_one_consecutive_numbers(numArray):
            if has_one_pair_same_last_digit_numbers(numArray):
                statements.append(get_right_combination_or_blank(combination, all_combinations))

    gather = asyncio.gather(*statements)
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(gather)

    size = len(results)
    print("total: ", size)

    count = 0
    total = 0
    numbers = []

    random.shuffle(results)

    while count < 50:
        result = results[count]
        array = list(result)
        array.sort()
        print(array)
        for num in array:
            numbers.append(num)
            total += num
        count += 1

    average = total / len(numbers)
    print('average: ', average)
    totaldev = 0.0
    for num in numbers:
        totaldev += (num - average)**2
    variance = totaldev / len(numbers)
    print('stdev: ', math.sqrt(variance))

if __name__ == '__main__':
    main()