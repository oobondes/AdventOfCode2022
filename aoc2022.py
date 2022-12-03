#!/usr/bin/python3

from sys import argv
from pathlib import Path
import bs4, requests
from getpass import getpass

def r_p_s(me, them):
    '''
    a method to play rock pape scissors in support of the day 2 challenge
    '''
    if me==them:
        return 'draw'
    elif (me == 'rock' and them == 'paper') or (me == 'paper' and them == 'scissors') or (me == 'scissors' and them == 'rock'):
        return 'lose'
    else:
        return 'win'

def day_1(file):
    print(max([sum([int(calorie) for calorie in elf.split()]) for elf in file.split('\n\n')]))

def day_1_final1_final(file):
    print(sum(sorted([sum([int(calorie) for calorie in elf.split()]) for elf in file.split('\n\n')])[::-1][:3]))

def day_2(file):
    score = {'X':1,'Y':2,'Z':3,'win':6,'draw':3,'lose':0}
    my_choices = {'X':'rock','Y':'paper','Z':'scissors'}
    their_choices = {'A':'rock','B':'paper','C':'scissors'}
    my_score = 0
    for match in file.split('\n'):
        if match == '': continue
        them, me = match.split()
        outcome = r_p_s(my_choices[me],their_choices[them])
        my_score += score[me] + score[outcome]
    print(my_score)

def day_2_final(file):
    score = {'X':1,'Y':2,'Z':3,'win':6,'draw':3,'lose':0}
    my_choices = {'rock':'X','paper':'Y','scissors':'Z'}
    their_choices = {'A':'rock','B':'paper','C':'scissors'}
    my_goal = {'X':'lose','Y':'draw','Z':'win'}
    my_score = 0
    for match in file.split('\n'):
        if match == '': continue
        them, me = match.split()
        goal = my_goal[me]
        them = their_choices[them]
        if goal == 'draw':
            me = them
        elif goal == 'win':
            if them == 'scissors': me = 'rock'
            elif them == 'rock': me = 'paper'
            else: me = 'scissors'
        else:
            if them == 'scissors': me = 'paper'
            elif them == 'rock': me = 'scissors'
            else: me = 'rock'
        outcome = r_p_s(me,them)
        my_score += score[my_choices[me]] + score[outcome]
    print(my_score)

def day_3(file):
    print('day 3 not implemented yet')

def day_3_final(file):
    print('day 3 final is not implemented yet')

def day_4(file):
    print('day 4 not implemented yet')

def day_4_final(file):
    print('day 4 final is not implemented yet')

def day_5(file):
    print('day 5 not implemented yet')

def day_5_final(file):
    print('day 5 final is not implemented yet')

def day_6(file):
    print('day 6 not implemented yet')

def day_6_final(file):
    print('day 6 final is not implemented yet')

def day_7(file):
    print('day 7 not implemented yet')

def day_7_final(file):
    print('day 7 final is not implemented yet')

def day_8(file):
    print('day 8 not implemented yet')

def day_8_final(file):
    print('day 8 final is not implemented yet')

def day_9(file):
    print('day 9 not implemented yet')

def day_9_final(file):
    print('day 9 final is not implemented yet')

def day_10(file):
    print('day 10 not implemented yet')

def day_10_final(file):
    print('day 10 final is not implemented yet')

def day_11(file):
    print('day 11 not implemented yet')

def day_11_final(file):
    print('day 11 final is not implemented yet')

def day_12(file):
    print('day 12 not implemented yet')

def day_12_final(file):
    print('day 12 final is not implemented yet')

def day_13(file):
    print('day 13 not implemented yet')

def day_13_final(file):
    print('day 13 final is not implemented yet')

def day_14(file):
    print('day 14 not implemented yet')

def day_14_final(file):
    print('day 14 final is not implemented yet')

def day_15(file):
    print('day 15 not implemented yet')

def day_15_final(file):
    print('day 15 final is not implemented yet')

def day_16(file):
    print('day 16 not implemented yet')

def day_16_final(file):
    print('day 16 final is not implemented yet')

def day_17(file):
    print('day 17 not implemented yet')

def day_17_final(file):
    print('day 17 final is not implemented yet')

def day_18(file):
    print('day 18 not implemented yet')

def day_18_final(file):
    print('day 18 final is not implemented yet')

def day_19(file):
    print('day 19 not implemented yet')

def day_19_final(file):
    print('day 19 final is not implemented yet')

def day_20(file):
    print('day 20 not implemented yet')

def day_20_final(file):
    print('day 20 final is not implemented yet')

def day_21(file):
    print('day 21 not implemented yet')

def day_21_final(file):
    print('day 21 final is not implemented yet')

def day_22(file):
    print('day 22 not implemented yet')

def day_22_final(file):
    print('day 22 final is not implemented yet')

def day_23(file):
    print('day 23 not implemented yet')

def day_23_final(file):
    print('day 23 final is not implemented yet')

def day_24(file):
    print('day 24 not implemented yet')

def day_24_final(file):
    print('day 24 final is not implemented yet')

def day_25(file):
    print('day 25 not implemented yet')

def day_25_final(file):
    print('day 25 final is not implemented yet')


def main(day_num, online = False):
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    login_data = {
        'commit': 'Sign in',
        'utf8': '%E2%9C%93',
        'login': input('username: ') if online else '',
        'password': getpass() if online else ''
    }
    url = "https://github.com/session"
    s = requests.Session()
    r = s.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.content, 'html5lib')
    login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
    r = s.post(url, data=login_data, headers=headers)

    git = 'https://adventofcode.com/auth/github'
    day = 'https://adventofcode.com/2022/day/{}/input'
    s.get(git)
    puzzle_input = s.get(day.format(day_num)).content.decode() if online else Path(f'day{day_num}.txt').read_text()
    print(f'day {day_num} part 1:')
    exec(f'day_{day_num}(puzzle_input)')
    try:
        print(f'day {day_num} part 2:')
        exec(f'day_{day_num}_final(puzzle_input)')
    except:
        print('final part is not yet implemented for day {}'.format(day_num))
    




if __name__ == '__main__':
    #exec(f'day_{argv[1]}(file)')
    main(argv[1])
