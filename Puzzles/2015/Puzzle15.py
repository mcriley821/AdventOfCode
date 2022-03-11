#!/usr/bin/env python
# Day 15 - Advent of Code 2015 
# --- Day 15: Science for Hungry 
# People --- 
# 
# Today, you set out on the task of 
# perfecting your milk-dunking 
# cookie recipe. All you have to do 
# is find the right balance of 
# ingredients. 
# 
# Your recipe leaves room for 
# exactly 100 teaspoons of 
# ingredients. You make a list of 
# the remaining ingredients you 
# could use to finish the recipe 
# (your puzzle input) and their 
# properties per teaspoon: 
# 
# capacity (how well it helps the 
# cookie absorb milk) 
# durability (how well it keeps the 
# cookie intact when full of milk) 
# flavor (how tasty it makes the 
# cookie) 
# texture (how it improves the feel 
# of the cookie) 
# calories (how many calories it 
# adds to the cookie) 
# You can only measure ingredients 
# in whole-teaspoon amounts 
# accurately, and you have to be 
# accurate so you can reproduce your 
# results in the future. The total 
# score of a cookie can be found by 
# adding up each of the properties 
# (negative totals become 0) and 
# then multiplying together 
# everything except calories. 
# 
# For instance, suppose you have 
# these two ingredients: 
# 
# Butterscotch: capacity -1, 
# durability -2, flavor 6, texture 
# 3, calories 8 
# Cinnamon: capacity 2, durability 
# 3, flavor -2, texture -1, calories 
# 3 
# Then, choosing to use 44 teaspoons 
# of butterscotch and 56 teaspoons 
# of cinnamon (because the amounts 
# of each ingredient must add up to 
# 100) would result in a cookie with 
# the following properties: 
# 
# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76
# Multiplying these together (68 * 
# 80 * 152 * 76, ignoring calories 
# for now) results in a total score 
# of 62842880, which happens to be 
# the best score possible given 
# these ingredients. If any 
# properties had produced a negative 
# total, it would have instead 
# become zero, causing the whole 
# score to multiply to zero. 
# 
# Given the ingredients in your 
# kitchen and their properties, what 
# is the total score of the 
# highest-scoring cookie you can 
# make? 
# 
# --- Part Two ---
# 
# Your cookie recipe becomes wildly 
# popular! Someone asks if you can 
# make another recipe that has 
# exactly 500 calories per cookie 
# (so they can use it as a meal 
# replacement). Keep the rest of 
# your award-winning process the 
# same (100 teaspoons, same 
# ingredients, same scoring system). 
# 
# For example, given the ingredients 
# above, if you had instead selected 
# 40 teaspoons of butterscotch and 
# 60 teaspoons of cinnamon (which 
# still adds to 100), the total 
# calorie count would be 40*8 + 60*3 
# = 500. The total score would go 
# down, though: only 57600000, the 
# best you can do in such trying 
# circumstances. 
# 
# Given the ingredients in your 
# kitchen and their properties, what 
# is the total score of the 
# highest-scoring cookie you can 
# make with a calorie total of 500? 
# 
from get_input import get_input
from random import randint


def generate_nums(length):
    for w in range(101):
        for x in range(101 - w):
            for y in range(101 - x - w):
                z = 100 - w - x - y
                yield [w, x, y, z]
    
    
def score(ingredients, ratios, calories=False):
    scores = []
    for each in ratios:
        amount, ingredient = each
        ingredient = ingredients[ingredient]
        ingredient_scores = []
        for effect in ingredient:
            ingredient_scores.append(ingredient[effect] * amount)
        scores.append(ingredient_scores)
    totals = []
    for i in range(len(scores[0])):
        t = sum(scores[j][i] for j in range(len(scores)))
        if t < 0:
            t = 0
        totals.append(t)
    out = 1
    for each in totals[:-1]:
        out *= each
    if calories:
        if totals[-1] != 500:
            return 0
    return out
        

def main():
    given = get_input(15, 2015)
    ingredients = {}
    for line in given.split('\n'):
        if line != '':
            ing, effects = line.split(': ')
            ingredients.update({ing: {}})
            for effect in effects.split(', '):
                name, val = effect.split(' ')
                ingredients[ing].update({name: int(val)})
    iters = sum(1 for _ in generate_nums(len(ingredients)))
    max_score = 0
    max_score_cal = 0
    for ind, nums in enumerate(generate_nums(len(ingredients))):
        scored = score(ingredients, [(i, j) for i, j in zip(nums, ingredients.keys())])
        calories = score(ingredients, [(i, j) for i, j in zip(nums, ingredients.keys())], True)
        max_score = max(scored, max_score)
        max_score_cal = max(calories, max_score_cal)
        print(f'\r{ind * 100/ iters:.2f}%', end='\r')
    print(f'\rPart 1: {max_score}')
    print(f'Part 2: {max_score_cal}')
    

if __name__ == "__main__":
    main()

