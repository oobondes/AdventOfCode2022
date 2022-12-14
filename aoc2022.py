#!/usr/bin/python3

import bs4, requests, argparse
from pathlib import Path
from getpass import getpass
from re import findall
from itertools import islice
import pprint


#HELPER FUNCTIONS FOR PUZZLES:

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

class tree():
    def __init__(self, value='/', next=None, directory=True, size=0, parent=None):
        self.value = value
        self.next = next or list()
        self.directory = directory
        self.size = int(size)
        self.parent = parent

    def get_size(self):
        if self.directory and len(self.next) == 0:
            return 0
        return sum([x.size if not x.directory else x.get_size() for x in self.next])

    def traverse(self):
        all_nodes = list()
        for node in self.next:
            if node.directory:
                all_nodes.append(node)
                for sub_nodes in node.traverse():
                    all_nodes.append(sub_nodes)
        return all_nodes

    def __str__(self, indent = 0):
        if not self.directory:
            return f'{self.value} - {self.size}'
        string = '-'*indent + self.value + '\n' + '-'*(indent+1)
        for node in self.next:
            string += node.value + ', '
        for node in self.next:
            if node.directory:
                string += '\n' + node.__str__(indent +1)
        return string

    def __repr__(self):
        return self.__str__()
    
#FUNCTIONS TO ANSWER THE PUZZLES HERE:

def day_1(file: str):
    ans = max([sum([int(calorie) for calorie in elf.split()]) for elf in file.split('\n\n')])
    print(ans)
    return ans

def day_1_final(file: str):
    ans = sum(sorted([sum([int(calorie) for calorie in elf.split()]) for elf in file.split('\n\n')])[::-1][:3])
    print(ans)
    return ans

def day_2(file: str):
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
    return my_score

def day_2_final(file: str):
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
    return my_score

def day_3(file: str):
    priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
    rucksacks = file.split()
    ans = 0
    for ruck in rucksacks:
        halfway = len(ruck)//2
        first = ruck[:halfway]
        second = ruck[halfway:]
        pri = [c for c in first if c in second][0]
        ans += priority[pri]
    print(ans)
    return ans

def day_3_final(file: str):
    priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
    rucksacks = file.split()
    ans = 0
    for i in range(0,len(rucksacks),3):
        pri = [c for c in rucksacks[i] if c in rucksacks[i+1] and c in rucksacks[i+2]][0]
        ans += priority[pri]
    print(ans)
    return ans

def day_4(file: str):
    groups = [ [(int(a),int(b)),(int(c),int(d))] for a,b,c,d in findall('(\d*)-(\d*),(\d*)-(\d*)',file)]
    count = 0
    for group in groups:
        elf1_start, elf1_stop = group[0]
        elf2_start, elf2_stop = group[1]
        if (elf1_start <= elf2_start and elf2_stop <= elf1_stop) or (elf2_start <= elf1_start and elf1_stop <= elf2_stop):
            count += 1
    print(count)
    return count

def day_4_final(file: str):
    groups = [ [(int(a),int(b)),(int(c),int(d))] for a,b,c,d in findall('(\d*)-(\d*),(\d*)-(\d*)',file)]
    count = 0
    for group in groups:
        elf1_start, elf1_stop = group[0]
        elf2_start, elf2_stop = group[1]
        if elf1_start <= elf2_start <= elf1_stop or elf2_start <= elf1_start <= elf2_stop:
            count += 1
    print(count)
    return count

def day_5(file: str):
    cargo, moves = file.split('\n\n')
    cargo, numpiles = '\n'.join(cargo.split('\n')[:-1]), cargo.split('\n')[-1]
    numpiles = max([int(c) for c in numpiles.split(' ') if c])
    piles = [[] for _ in range(numpiles)]
    for row in findall('.(.).[\s\n]?'*numpiles,cargo):
        for i, column in enumerate(row):
            if column != ' ':
                piles[i].append(column)
    for num_to_move, start_pos, end_pos in findall('move (\d*) from (\d*) to (\d*)',moves):
        num_to_move = int(num_to_move)
        start_pos = int(start_pos)-1
        end_pos = int(end_pos)-1
        for i in range(num_to_move):
            piles[end_pos].insert(0,piles[start_pos][0])
            del piles[start_pos][0]
    
    ans = ''.join([c[0] for c in piles])
    print(ans)
    return ans

def day_5_final(file: str):
    cargo, moves = file.split('\n\n')
    cargo, numpiles = '\n'.join(cargo.split('\n')[:-1]), cargo.split('\n')[-1]
    numpiles = max([int(c) for c in numpiles.split(' ') if c])
    piles = [[] for _ in range(numpiles)]
    for row in findall('.(.).[\s\n]?'*numpiles,cargo):
        for i, column in enumerate(row):
            if column != ' ':
                piles[i].append(column)
    for num_to_move, start_pos, end_pos in findall('move (\d*) from (\d*) to (\d*)',moves):
        num_to_move = int(num_to_move)
        start_pos = int(start_pos)-1
        end_pos = int(end_pos)-1
        for i in range(num_to_move-1,-1,-1):
            piles[end_pos].insert(0,piles[start_pos][i])
        del piles[start_pos][0:num_to_move]
    
    ans = ''.join([c[0] for c in piles])
    print(ans)
    return ans

def day_6(file: str):
    for i in range(len(file)):
        a,b,c,d = file[i:i+4]
        if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
            ans = i+4
            print(a,b,c,d)
            print(ans)
            return ans

def day_6_final(file: str):
    for i in range(len(file)):
        window = file[i:i+14]
        if all([window.count(c)==1 for c in window]):
            ans = i+14
            print(ans)
            return ans

def day_7(file: str):
    commands = file.split('\n')
    root = tree()
    pointer = root
    for number,command in enumerate(commands[1:]):
        if command[0] == '$':
            ls = False
            if 'ls' in command.split():
                continue
            elif 'cd' in command:
                print(f'command #{number}: ',end='')
                _, cd, new_dir = command.split()
                if new_dir == '..': 
                    pointer = pointer.parent
                    print('moved up to: ',pointer.value)
                else:
                    pointer = [x for x in pointer.next if x.value == new_dir][0]
                    print('moved in to ',pointer.value)
                continue
        elif command[:3] == 'dir':
            directory = command.split()[1]
            nxt = tree(value=directory,directory=True,parent=pointer)
            pointer.next.append(nxt)
        else:
            size, directory = command.split() 
            pointer.next.append(tree(value=directory,directory=False,size=int(size)))
    ans = sum([x.get_size() for x in root.traverse() if x.get_size() < 100000])
    print(root)
    print(ans)
    return ans

def day_7_final(file: str):
    commands = file.split('\n')
    root = tree()
    pointer = root
    for number,command in enumerate(commands[1:]):
        if command[0] == '$':
            ls = False
            if 'ls' in command.split():
                continue
            elif 'cd' in command:
                print(f'command #{number}: ',end='')
                _, cd, new_dir = command.split()
                if new_dir == '..': 
                    pointer = pointer.parent
                    print('moved up to: ',pointer.value)
                else:
                    pointer = [x for x in pointer.next if x.value == new_dir][0]
                    print('moved in to ',pointer.value)
                continue
        elif command[:3] == 'dir':
            directory = command.split()[1]
            nxt = tree(value=directory,directory=True,parent=pointer)
            pointer.next.append(nxt)
        else:
            size, directory = command.split() 
            pointer.next.append(tree(value=directory,directory=False,size=int(size)))
    print(root)
    space_left = 70000000 - root.get_size()
    print(space_left)
    ans = min([x.get_size() for x in root.traverse() if x.directory and (space_left + x.get_size()) >= 30000000])
    return ans

def day_8(file: str):
    forest = [[int(c) for c in line] for line in file.split('\n')]
    height = len(forest)
    width = len(forest[0])
    count = 0
    for x in range(1,height-1):
        for y in range(1,width-1):
            if  not (
                any([forest[i][y] >= forest[x][y] for i in range(0,x)]) and 
                any([forest[i][y] >= forest[x][y] for i in range(x+1,height)]) and 
                any([forest[x][i] >= forest[x][y] for i in range(0,y)]) and 
                any([forest[x][i] >= forest[x][y] for i in range(y+1, width)])):
                count +=1
    return count + (height + width)*2 -4

def day_8_final(file: str):
    forest = [[int(c) for c in line] for line in file.split('\n')]
    height = len(forest)
    width = len(forest[0])
    spots = list()
    scenic_scores = list()
    for x in range(1,height-1):
        for y in range(1,width-1):
            if  not (
                any([forest[i][y] >= forest[x][y] for i in range(0,x)]) and 
                any([forest[i][y] >= forest[x][y] for i in range(x+1,height)]) and 
                any([forest[x][i] >= forest[x][y] for i in range(0,y)]) and 
                any([forest[x][i] >= forest[x][y] for i in range(y+1, width)])):
                spots.append((x,y))
    for x,y in spots:
        count = 0
        scores = list()
        for i in range(x-1,-1,-1):
            if forest[i][y] < forest[x][y]:
                count += 1
            elif forest[i][y] == forest[x][y]:
                count +=1
                scores.append(count)
                break
            else:
                count +=1
                scores.append(count)
                break
        else:
            scores.append(count)
        count = 0
        for i in range(x+1,height):
            if forest[i][y] < forest[x][y]:
                count += 1
            elif forest[i][y] == forest[x][y]:
                count +=1
                scores.append(count)
                break
            else:
                count +=1
                scores.append(count)
                break
        else:
            scores.append(count)
        count=0
        for i in range(y-1,-1,-1):
            if forest[x][i] < forest[x][y]:
                count += 1
            elif forest[x][i] == forest[x][y]:
                count +=1
                scores.append(count)
                break
            else:
                count +=1
                scores.append(count)
                break
        else:
            scores.append(count)
        count = 0
        for i in range(y+1,width):
            if forest[x][i] < forest[x][y]:
                count += 1
            elif forest[x][i] == forest[x][y]:
                count +=1
                scores.append(count)
                break
            else:
                count +=1
                scores.append(count)
                break
        else:
            scores.append(count)
        scenic_scores.append(scores[0]*scores[1]*scores[2]*scores[3])
    ans = max(scenic_scores)
    return ans

def day_9(file: str):
    print('day 9 not implemented yet')

def day_9_final(file: str):
    print('day 9 final is not implemented yet')

def day_10(file: str):
    print('day 10 not implemented yet')

def day_10_final(file: str):
    print('day 10 final is not implemented yet')

def day_11(file: str):
    print('day 11 not implemented yet')

def day_11_final(file: str):
    print('day 11 final is not implemented yet')

def day_12(file: str):
    print('day 12 not implemented yet')

def day_12_final(file: str):
    print('day 12 final is not implemented yet')

def day_13(file: str):
    print('day 13 not implemented yet')

def day_13_final(file: str):
    print('day 13 final is not implemented yet')

def day_14(file: str):
    print('day 14 not implemented yet')

def day_14_final(file: str):
    print('day 14 final is not implemented yet')

def day_15(file: str):
    print('day 15 not implemented yet')

def day_15_final(file: str):
    print('day 15 final is not implemented yet')

def day_16(file: str):
    print('day 16 not implemented yet')

def day_16_final(file: str):
    print('day 16 final is not implemented yet')

def day_17(file: str):
    print('day 17 not implemented yet')

def day_17_final(file: str):
    print('day 17 final is not implemented yet')

def day_18(file: str):
    print('day 18 not implemented yet')

def day_18_final(file: str):
    print('day 18 final is not implemented yet')

def day_19(file: str):
    print('day 19 not implemented yet')

def day_19_final(file: str):
    print('day 19 final is not implemented yet')

def day_20(file: str):
    print('day 20 not implemented yet')

def day_20_final(file: str):
    print('day 20 final is not implemented yet')

def day_21(file: str):
    print('day 21 not implemented yet')

def day_21_final(file: str):
    print('day 21 final is not implemented yet')

def day_22(file: str):
    print('day 22 not implemented yet')

def day_22_final(file: str):
    print('day 22 final is not implemented yet')

def day_23(file: str):
    print('day 23 not implemented yet')

def day_23_final(file: str):
    print('day 23 final is not implemented yet')

def day_24(file: str):
    print('day 24 not implemented yet')

def day_24_final(file: str):
    print('day 24 final is not implemented yet')

def day_25(file: str):
    print('day 25 not implemented yet')

def day_25_final(file: str):
    print('day 25 final is not implemented yet')

# REGISTER ALL METHODS IN A DICTIONARY
day_func = {
    '1':day_1, '1_final':day_1_final,
    '2':day_2, '2_final':day_2_final,
    '3':day_3, '3_final':day_3_final,
    '4':day_4, '4_final':day_4_final,
    '5':day_5, '5_final':day_5_final,
    '6':day_6, '6_final':day_6_final,
    '7':day_7, '7_final':day_7_final,
    '8':day_8, '8_final':day_8_final,
    '9':day_9, '9_final':day_9_final,
    '10':day_10, '10_final':day_10_final,
    '11':day_11, '11_final':day_11_final,
    '12':day_12, '12_final':day_12_final,
    '13':day_13, '13_final':day_13_final,
    '14':day_14, '14_final':day_14_final,
    '15':day_15, '15_final':day_15_final,
    '16':day_16, '16_final':day_16_final,
    '17':day_17, '17_final':day_17_final,
    '18':day_18, '18_final':day_18_final,
    '19':day_19, '19_final':day_19_final,
    '20':day_20, '20_final':day_20_final,
    '21':day_21, '21_final':day_21_final,
    '22':day_22, '22_final':day_22_final,
    '23':day_23, '23_final':day_23_final,
    '24':day_24, '24_final':day_24_final,
    '25':day_25, '25_final':day_25_final,
}


def main(day_num, username=None, password=None, online = False, submit = False, part_one = False, part_two = False):
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    login_data = {
        'commit': 'Sign in',
        'utf8': '%E2%9C%93',
        'login': username if online and  username else '',
        'password': password if online and  password else ''
    }
    url = "https://github.com/session"
    s = requests.Session()
    r = s.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.content, 'html5lib')
    login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
    r = s.post(url, data=login_data, headers=headers)

    git = 'https://adventofcode.com/auth/github'
    day = 'https://adventofcode.com/2022/day/{}/input'
    submit_answer_url = 'https://adventofcode.com/2022/day/{}/answer'

    s.get(git)
    puzzle_input = s.get(day.format(day_num)).content.decode().strip('\n') if online else Path(f'day{day_num}.txt').read_text().strip('\n')
    if part_one:
        print(f'day {day_num} part 1:')
        ans = day_func[day_num](puzzle_input)
        print(ans)
        if submit:
            data = {'level':'1','answer':str(ans)}
            resp=s.post(submit_answer_url.format(day_num),data=data)
            results = b'<span class="day-success">one gold star</span> closer to collecting enough star fruit.' in resp.content
            print('success' if results else 'failed')
    if part_two:
        print(f'day {day_num} part 2:')
        ans = day_func[f'{day_num}_final'](puzzle_input)
        print(ans)
        if submit:
            data = {'level':'2','answer':str(ans)}
            resp=s.post(submit_answer_url.format(day_num),data=data)
            results = b'<span class="day-success">one gold star</span> closer to collecting enough star fruit.' in resp.content
            print('success' if results else 'failed')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument('day', nargs='+', help='sets the day to be ran')
    parser.add_argument('-o','--online', action='store_true', help='this flag causes the script to pull the input from the website. Otherwise, it will use dayX.txt as input.')
    parser.add_argument('-s','--submit',action='store_true',help='this flag will submit the answer generated to advent of code.')
    parser.add_argument('-1','--part_one',action='store_true', help='run the first part of the puzzle')
    parser.add_argument('-2','--part_two',action='store_true', help='run the second part of the puzzle')
    parser.add_argument('-u','--username', help='Github username')
    parser.add_argument('-p','--password', help='github password')
    args = parser.parse_args()
    part_one = True if args.part_one==args.part_two else args.part_one
    part_two = args.part_two
    if args.online:
        username = args.username or input('enter username: ')
        password = args.password or getpass()
    else:
        password = None
        username = None
    for day in args.day:
        main(day, online=args.online, submit=args.submit, username=username, password=password, part_one=part_one, part_two=part_two)
