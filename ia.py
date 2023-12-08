import random
def ia(board,signe,level):
    if level==1:
        positions_disponibles = [(i // 3, i % 3) for i in range(9) if board[i // 3][i % 3] == 0]
        random.shuffle(positions_disponibles)
        if positions_disponibles:
            choix = random.choice(positions_disponibles)
            return choix
        else:
            return False
    if level==2:
        positions_disponibles = [(i // 3, i % 3) for i in range(9) if board[i // 3][i % 3] == 0]
        random.shuffle(positions_disponibles)
        def possibilite_de_gagner(symbole):
            for i in range(3):
                if board[i][0] == board[i][1] == symbole and board[i][2] == 0:
                    return (i, 2)
                elif board[i][0] == board[i][2] == symbole and board[i][1] == 0:
                    return (i, 1)
                elif board[i][1] == board[i][2] == symbole and board[i][0] == 0:
                    return (i, 0)
                elif board[0][i] == board[1][i] == symbole and board[2][i] == 0:
                    return (2, i)
                elif board[0][i] == board[2][i] == symbole and board[1][i] == 0:
                    return (1, i)
                elif board[1][i] == board[2][i] == symbole and board[0][i] == 0:
                    return (0, i)
            if board[0][0] == board[1][1] == symbole and board[2][2] == 0:
                return (2, 2)
            elif board[0][0] == board[2][2] == symbole and board[1][1] == 0:
                return (1, 1)
            elif board[1][1] == board[2][2] == symbole and board[0][0] == 0:
                return (0, 0)
            elif board[0][2] == board[1][1] == symbole and board[2][0] == 0:
                return (2, 0)
            elif board[0][2] == board[2][0] == symbole and board[1][1] == 0:
                return (1, 1)
            elif board[1][1] == board[2][0] == symbole and board[0][2] == 0:
                return (0, 2)
            return None
        possibilite_gagnante = possibilite_de_gagner(signe)
        if possibilite_gagnante:
            return possibilite_gagnante
        if positions_disponibles:
            choix = random.choice(positions_disponibles)
            return choix
        else:
            return False
    if level == 3:
         positions_disponibles = [(i // 3, i % 3) for i in range(9) if board[i // 3][i % 3] == 0]
         random.shuffle(positions_disponibles)
         def possibilite_de_gagner(symbole):
            for i in range(3):
                if board[i][0] == board[i][1] == symbole and board[i][2] == 0:
                    return (i, 2)
                elif board[i][0] == board[i][2] == symbole and board[i][1] == 0:
                    return (i, 1)
                elif board[i][1] == board[i][2] == symbole and board[i][0] == 0:
                    return (i, 0)
                elif board[0][i] == board[1][i] == symbole and board[2][i] == 0:
                    return (2, i)
                elif board[0][i] == board[2][i] == symbole and board[1][i] == 0:
                    return (1, i)
                elif board[1][i] == board[2][i] == symbole and board[0][i] == 0:
                    return (0, i)
            if board[0][0] == board[1][1] == symbole and board[2][2] == 0:
                return (2, 2)
            elif board[0][0] == board[2][2] == symbole and board[1][1] == 0:
                return (1, 1)
            elif board[1][1] == board[2][2] == symbole and board[0][0] == 0:
                return (0, 0)
            elif board[0][2] == board[1][1] == symbole and board[2][0] == 0:
                return (2, 0)
            elif board[0][2] == board[2][0] == symbole and board[1][1] == 0:
                return (1, 1)
            elif board[1][1] == board[2][0] == symbole and board[0][2] == 0:
                return (0, 2)
            return None
         possibilite_gagnante = possibilite_de_gagner(signe)
         if possibilite_gagnante:
            return possibilite_gagnante
         adversaire = 3 - signe
         possibilite_adversaire = possibilite_de_gagner(adversaire)
         if possibilite_adversaire:
            return possibilite_adversaire
         coins = [(0, 0), (0, 2), (2, 0), (2, 2)]
         for coin in coins:
            if coin in positions_disponibles:
                return coin
         if positions_disponibles:
            choix = random.choice(positions_disponibles)
            return choix
         else:
            return False