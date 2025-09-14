#!/usr/bin/env python3
import numpy as np

""" checkmate.py """

def checkmate(board):
    """ checkmate.py """
    pass

if __name__ == "__main__":
    board = """\
R.PP
.K..
..P.
P..P\
"""
    try :
        print(board)
        data = [i for i in board.replace('\n', '')]
        data = np.array(data)
        n = int(np.sqrt(len(data)))
        data = data.reshape(n, n)
        print(data)
        print(data.shape)
        
        #Unit Position
        print(np.argwhere(data == 'P'))
        print(np.argwhere(data == 'B'))
        print(np.argwhere(data == 'R'))
        print(np.argwhere(data == 'Q'))
        
        print(np.argwhere(data == 'K'))
        
        #P Range
        all_p_pos = np.argwhere(data == 'P')
        print(all_p_pos)

        for p_pos in all_p_pos:
            print(p_pos)
            if p_pos[0] != 0 and p_pos[1] != 0 and p_pos[1] != n - 1:
                data[p_pos[0]-1, p_pos[1]+1] = 'X'
                data[p_pos[0]-1, p_pos[1]-1] = 'X'
            elif p_pos[0] != 0 and p_pos[1] == 0:
                data[p_pos[0]-1, p_pos[1]+1] = 'X'
            elif p_pos[0] != 0 and p_pos[1] == n-1:
                data[p_pos[0]-1, p_pos[1]-1] = 'X'
                
        #R Range
        all_r_pos = np.argwhere(data == 'R')
        print(all_r_pos)

        for r_pos in all_r_pos:
            data[r_pos[0], :] = 'X'  # Horizontal line
            data[:, r_pos[1]] = 'X'  # Vertical line
        
        #B Range
        all_b_pos = np.argwhere(data == 'B')
        print(all_b_pos)

        for b_pos in all_b_pos:
            i = 1
            while True:
                if b_pos[0]+i == n-1 or b_pos[1]+i == n-1:
                    data[b_pos[0]+i, b_pos[1]+i] = 'X'
                i += 1
            #data[b_pos[0], :] = 'X'  # Horizontal line
            #data[:, b_pos[1]] = 'X'  # Vertical line
        
        #Check Range
        print('Check Range:', data, sep='\n')
        
    except ValueError:
        print("Wrong Dimension")