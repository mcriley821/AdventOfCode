#!/usr/bin/env python
# Day 18 - Advent of Code 2020 
# --- Day 18: Operation Order ---
# 
# As you look out the window and 
# notice a heavily-forested 
# continent slowly appear over the 
# horizon, you are interrupted by 
# the child sitting next to you. 
# They're curious if you could help 
# them with their math homework. 
# 
# Unfortunately, it seems like this 
# "math" follows different rules 
# than you remember. 
# 
# The homework (your puzzle input) 
# consists of a series of 
# expressions that consist of 
# addition (+), multiplication (*), 
# and parentheses ((...)). Just like 
# normal math, parentheses indicate 
# that the expression inside must be 
# evaluated before it can be used by 
# the surrounding expression. 
# Addition still finds the sum of 
# the numbers on both sides of the 
# operator, and multiplication still 
# finds the product. 
# 
# However, the rules of operator 
# precedence have changed. Rather 
# than evaluating multiplication 
# before addition, the operators 
# have the same precedence, and are 
# evaluated left-to-right regardless 
# of the order in which they appear. 
# 
# For example, the steps to evaluate 
# the expression 1 + 2 * 3 + 4 * 5 + 
# 6 are as follows: 
# 
# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#       9   + 4 * 5 + 6
#          13   * 5 + 6
#              65   + 6
#                  71
# Parentheses can override this 
# order; for example, here is what 
# happens if parentheses are added 
# to form 1 + (2 * 3) + (4 * (5 + 
# 6)): 
# 
# 1 + (2 * 3) + (4 * (5 + 6))
# 1 +    6    + (4 * (5 + 6))
#      7      + (4 * (5 + 6))
#      7      + (4 *   11   )
#      7      +     44
#             51
# Here are a few more examples:
# 
# 2 * 3 + (4 * 5) becomes 26.
# 5 + (8 * 3 + 9 + 3 * 4 * 3) 
# becomes 437. 
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 
# 6 * 4)) becomes 12240. 
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 
# 6) + 2 + 4 * 2 becomes 13632. 
# Before you can help with the 
# homework, you need to understand 
# it yourself. Evaluate the 
# expression on each line of the 
# homework; what is the sum of the 
# resulting values? 
# 
# --- Part Two ---
# 
# You manage to answer the child's 
# questions and they finish part 1 
# of their homework, but get stuck 
# when they reach the next section: 
# advanced math. 
# 
# Now, addition and multiplication 
# have different precedence levels, 
# but they're not the ones you're 
# familiar with. Instead, addition 
# is evaluated before 
# multiplication. 
# 
# For example, the steps to evaluate 
# the expression 1 + 2 * 3 + 4 * 5 + 
# 6 are now as follows: 
# 
# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#   3   *   7   * 5 + 6
#   3   *   7   *  11
#      21       *  11
#          231
# Here are the other examples from 
# above: 
# 
# 1 + (2 * 3) + (4 * (5 + 6)) still 
# becomes 51. 
# 2 * 3 + (4 * 5) becomes 46.
# 5 + (8 * 3 + 9 + 3 * 4 * 3) 
# becomes 1445. 
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 
# 6 * 4)) becomes 669060. 
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 
# 6) + 2 + 4 * 2 becomes 23340. 
# What do you get if you add up the 
# results of evaluating the homework 
# problems using these new rules? 
# 
from get_input import get_input

    
def extract(string, advanced=False):
    while '(' in string:
        open_count = 0
        closed_count = 0
        copy_string = string
        for ind, char in enumerate(copy_string):
            if char == '(':
                open_count += 1
                if open_count == 1:
                    start = ind
            elif char == ')':
                closed_count += 1
                end = ind + 1
            else:
                continue
            if open_count == closed_count and open_count != 0:
                subs = string[start:end]
                if advanced:
                    string = string.replace(subs, str(solve_advanced(subs[1:-1])), 1)
                else:
                    string = string.replace(subs, str(solve_basic(subs[1:-1])), 1)
                break
    return string
    

def solve_basic(string):
    if '+' not in string and '*' not in string:
        return int(string)
    if '(' in string:
        string = extract(string)
    left = 0
    right = 0
    total = 0
    op = None
    num_or_op = ''
    for char in string + ' ':
        if char.isnumeric():
            num_or_op += char
        else:
            if op is not None:
                right = int(num_or_op)
                if op == '+':
                    total = left + right
                elif op == '*':
                    total = left * right
                left = total
                num_or_op = ''
                right = 0
                op = char
            else:    
                left += int(num_or_op) if num_or_op != '' else 0
                op = char
                num_or_op = ''
    return total
    

def solve_advanced(string):
    # precedence on addition +
    if '(' in string:
        string = extract(string, True)
    while '+' in string:
        string = f' {string} '
        start_ind = string.index('+')
        right = ''
        left = ''
        ind = start_ind
        while string[ind + 1].isnumeric():
            right += string[ind + 1]
            ind += 1
        ind = start_ind
        while string[ind - 1].isnumeric():
            left = string[ind - 1] + left
            ind -= 1
        subs = f'{left}+{right}'
        string = string.replace(subs, f'{int(left) + int(right)}', 1)
    return solve_basic(string.replace(' ',''))


def main():
    given = get_input(18, 2020)
    given = [i.replace(' ', '') for i in given.split('\n') if i != '']
    print(f"Part 1: {sum(solve_basic(i) for i in given)}")
        
    print(f"Part 2: {sum(solve_advanced(i) for i in given)}")


if __name__ == "__main__":
    main()

