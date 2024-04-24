"""
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
"""


def minion_game(string):
    # your code goes here
    kevin, stuart = 0, 0
    s = len(string)
    for i in range(s):
        if string[i].lower() in 'aeiou':
            kevin += s - i
        else:
            stuart += s - i
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = 'BAANANAS'
    minion_game(s)
