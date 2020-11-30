from typing import Tuple, List, Set, Optional
import random

def read_sudoku(filename: str) -> List[List[str]]:
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(grid: List[List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(grid[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values: List[str], n: int) -> List[List[str]]:
    main = []
    str = 0
    pos = 0
    for x in range(n):
        main.append([])
    for x in list(values):
        if type(x) == list:
            for y in x:
                if pos == n:
                    pos = 0
                    str += 1
                main[str].append(x)
                pos += 1
        else:
            if pos == n:
                pos = 0
                str += 1
            main[str].append(x)
            pos += 1
    return main

def get_row(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    return grid[pos[0]]
""" Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """


def get_col(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    main = []
    for x in grid:
        main.append(x[pos[1]])
    return main


def get_block(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    str = (pos[1] // 3) * 3
    strf = str
    stolb = (pos[0] // 3) * 3
    main = []
    for x in range(3):
        for y in range(3):
            main.append(grid[stolb][str])
            str += 1
        stolb += 1
        str = strf
    return main


def find_empty_positions(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == ".":
                return (x, y)
    


def find_possible_values(grid: List[List[str]], pos: Tuple[int, int]) -> Set[str]:
    """ Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    main = {"1", "2", '3', '4', '5', '6', '7', '8', '9'}
    str = set()
    for x in main:
        if x in get_row(grid, pos) or x in get_col(grid, pos) or x in get_block(grid, pos):
            continue
        else:
            str.add(x)
    return str


def solve(grid: List[List[str]]) -> Optional[List[List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty = find_empty_positions(grid)

    if not empty:
        return grid

    possible_num = find_possible_values(grid, empty)
    possible_num = list(possible_num)
    for num in possible_num:
        grid[empty[0]][empty[1]] = num
        if solve(grid):
            return grid
        else:
            grid[empty[0]][empty[1]] = '.'


def check_solution(solution: List[List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    isright = 0
    main = {'0', '1', '2', '3', '4', '5', '6', '7', '8'}
    isright = 0
    main = {'9', '1', '2', '3', '4', '5', '6', '7', '8'}
    for x in range(9):
        for y in range(9):
            tuple = (x, y)
            if len(set(get_col(solution, (x, y))) & main) == 9 and len(set(get_row(solution, (x, y))) & main) == 9 and len(set(get_block(solution, (x, y))) & main) == 9:
                continue
            else:
                return False
    return True


def generate_sudoku(N: int) -> List[List[str]]:
    import random
    grid = []
    f = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = ['4', '5', '6', '7', '8', '9', '1', '2', '3']
    t = ['7', '8', '9', '1', '2', '3', '4', '5', '6']
    fo = ['2', '3', '4', '5', '6', '7', '8', '9', '1']
    fi = ['5', '6', '7', '8', '9', '1', '2', '3', '4']
    si = ['8', '9', '1', '2', '3', '4', '5', '6', '7']
    se = ['3', '4', '5', '6', '7', '8', '9', '1', '2']
    e = ['6', '7', '8', '9', '1', '2', '3', '4', '5']
    n = ['9', '1', '2', '3', '4', '5', '6', '7', '8']
    grid = [f, s, t, fo, fi, si, se, e, n]
    for x in range(1000):
        n = random.randint(0, 2)
        n2 = random.randint(0, 2)
        while n == n2:
            n2 = random.randint(0, 2)
        pos1, pos2 = random.randint(n*3, n*3+2), random.randint(n*3, n*3+2)
        while pos1 == pos2:
            pos2 = random.randint(n*3, n*3+2)
        grid[pos1], grid[pos2] = grid[pos2], grid[pos1]
        for x in range(9):
            grid[x][pos1], grid[x][pos2] = grid[x][pos2], grid[x][pos1]
    for x in grid:
        print(x)
    N = 81 - N
    if N > 0:
        while N > 0:
            pos1, pos2 = random.randint(0, 8), random.randint(0, 8)
            if grid[pos1][pos2] != '.':
                grid[pos1][pos2] = '.'
                N -= 1
    return grid


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
