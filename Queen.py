def queensAttack(n, k , r_q, c_q, obstacles):
    up = n-r_q#the up's distance 
    d_wn = r_q-1#down 's distance
    r = n-c_q#right's distance 
    l = c_q-1#left's distance 
    r_up = min(up, r)# the diagonale up right distance
    r_dwn = min(r, d_wn)#the diagonale down right distance
    l_up =  min(up , l )#the diagonale up s left distance
    l_dwn = min(l, d_wn)#the diagonale down's left

    for obs in obstacles:#looping through the obstacles
        if obs[1] == c_q:#if the column of the obstacle == column of the queen
            if obs[0] < r_q:# if the row of the obstacle < row of the queen
                d_wn = min(d_wn, r_q-1-obs[0])#then down s squares
            else:#
                up = min(up, obs[0]-r_q-1)# up s square
        elif obs[0] == r_q:#if the row of the obstacle == row of the queen
            if obs[1] < c_q:# if the column of the obstacle == column of the queen 
                l = min(l, c_q-1-obs[1])#left s squares
            else:
                r =  min(r, obs[1]-c_q-1)#right s squares 
            
        elif abs(obs[0]-r_q) == abs(obs[1] - c_q):#now comes the diagonal
            if obs[1] > c_q:
                if obs[0] > r_q:
                    r_up = min(r_up, obs[1]-c_q-1)
                else:
                    r_dwn = min(r_dwn, obs[1]-c_q-1)
            else:
                if obs[0]> r_q:
                    l_up = min(l_up, c_q-1-obs[1])
                else:
                    l_dwn = min(l_dwn, c_q-1-obs[1])

    return up + d_wn + l + r + l_dwn + l_up + r_up + r_dwn