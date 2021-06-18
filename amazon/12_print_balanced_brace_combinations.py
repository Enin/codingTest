# Print all braces combinations for a given value n so that they are balanced.
# For this solution, we will be using recursion.
# recursion: 재귀함수 사용하기
# left, right brace를 각각 컨트롤 하는것이 중요하다.
import copy

def print_all_braces(n, left_count, right_count, output, result):

    if left_count >= n and right_count >= n:
        print('output+')
        result.append(copy.copy(output))

    if left_count < n:
        print('left+')
        output += '{'
        print_all_braces(n, left_count + 1, right_count, output, result)
        print('left-')
        output.pop()


    if right_count < left_count:
        print('right+')
        output += '}'
        print_all_braces(n, left_count, right_count + 1, output, result)
        print('right-')
        output.pop()

def print_braces(n):
    output = []
    result = []
    print_all_braces(n, 0, 0, output, result)
    return result

if __name__ == '__main__':

    result = print_braces(3)

    for i in result:
        print(''.join(i), end='')
        print()