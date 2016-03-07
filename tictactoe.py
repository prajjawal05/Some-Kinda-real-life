board={'top-L':' ','top-M':' ','top-R':' ' ,
          'mid-L':' ','mid-M':' ' ,'mid-R':' ' ,
          'low-L': ' ','low-M':' ','low-R':' '}
def printboard(board):
    print(board['top-L'] + '|'+board['top-M']+'|'+board['top-R'])
    print('-'+'+'+'-'+'+'+'-')
    print(board['mid-L'] + '|'+board['mid-M']+'|'+board['mid-R'])
    print('-'+'+'+'-'+'+'+'-')
    print(board['low-L'] + '|'+board['low-M']+'|'+board['low-R'])

print('Position map of TIC-TAC-TOE board..')
print()
print('top-L' + '|'+'top-M'+'|'+'top-R')
print('     '+'|'+  '     '+'|'+'     ')
print('-----'+'+'+'-----'+'+'+'-----')
print('mid-L'+ '|'+'mid-M'+'|'+'mid-R')
print('     '+'|'+  '     '+'|'+'     ')
print('-----'+'+'+'-----'+'+'+'-----')
print('low-L' + '|'+'low-M'+'|'+'low-R')
print('     '+'|'+  '     '+'|'+'     ')
print()
print()
print('Who want to start the game...(x or o)?')
player=input()
print()
print('LETS BEGIN......')
print()
for i in range(0,9,1):
    printboard(board)
    print('player of '+player+'. Move on which place....?')
    move=input()
    board[move]=player
    if (board['top-L']==board['mid-M']==board['low-R']!=' ' or board['top-R']==board['mid-M']==board['low-R']!=' ' or board['top-L']==board['top-M']==board['top-R']!= ' ' or board['mid-L']==board['mid-R']== board['mid-M']!=' ' or board['low-R']==board['low-M']==board['low-L']!=' ' or board['top-R']== board['mid-R']==board['low-R']!=' ' or board['top-M']==board['mid-M']==board['low-M']!=' ' or board['top-L']==board['mid-L']==board['low-L']!=' '):
        printboard(board)
        print()
        print(player + ' WINS the match......')
        k=1;
        break;
    if player =='x':
        player ='o'
    else:
        player ='x'
if(k!=1):
    printboard(board)
