#def game():

def search():
    while abertos != []:
        global x 
        x = abertos[0]   
        abertos.pop(0)
        if state_board[x] == board_final:
            print("Sucesso")
            print('')
            print(board)
            break
        else:
            moviment_panel()

#def generating_board:
#    a = {}

def search_empty():
    v = [(index, row.index(0)) for index, row in enumerate(state_board[x]) if 0 in row]
    return v

def moviment_panel():
    global x
    a = search_empty()
    #b = len(state_board)
    board_temp = list(map(list,state_board[x]))
    board_temp_mov = list(map(list,state_board[x]))
    if a == [(0,0)]:
        board_temp_mov[0][0] = board_temp_mov[1][0]
        board_temp_mov[1][0] = 0
        verify_state(board_temp_mov)
        board_temp_mov = reset_board_temp(board_temp)
        board_temp_mov[0][0] = board_temp_mov[0][1]
        verify_state(board_temp_mov)
        board_temp_mov = reset_board_temp(board_temp)

    #if a = [(0,1)]:


    if a == [(1,2)]:
        board_temp_mov[1][2] = board_temp_mov[2][2]
        board_temp_mov[2][2] = 0
        verify_state(board_temp_mov)
        board_temp_mov = reset_board_temp(board_temp)
        board_temp_mov[1][2] = board_temp_mov[1][1]
        board_temp_mov[1][1] = 0
        verify_state(board_temp_mov)
        board_temp_mov = reset_board_temp(board_temp)
        board_temp_mov[1][2] = board_temp_mov[0][2]
        board_temp_mov[0][2] = 0
        verify_state(board_temp_mov)
        board_temp_mov = reset_board_temp(board_temp)

def reset_board_temp(board0):
    global x
    return list(map(list,state_board[x]))

def verify_state(vetor):
    global x
    global state_board
    global state
    y = len(state_board)
    for i in range(y):
        if vetor == state_board[i]:
            break
    state_board.append(vetor)
    if fechados == []:
        fechados.append(x)
    for i in range(len(fechados)):
        if fechados[i] == x:
            break
        else:    
            fechados.append(x)
    state = state + 1
    abertos.append(state)    
         
def draw_board():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

board = [[1,2,3],
         [4,5,0],
         [7,8,6]]
board_final = [[1,2,3],
               [4,5,6],
               [0,7,8]]
state_board = []
state_board.append(board)
abertos = [0]
fechados = []
x = None
state = 0
search()
#test = [[0,1],[2]]
#print(test)
#moviment_panel()
#print([(index, row.index(0)) for index, row in enumerate(board) if 0 in row])
#if ([(index, row.index(0)) for index, row in enumerate(board) if 0 in row] == [(1,2)]):
#    print("Teste")
#draw_board()