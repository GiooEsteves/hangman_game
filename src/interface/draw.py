estagios = [
    """
    ______
    |    |
    |
    |
    |
    |
   *********
    """,
    """
    ______
    |    |
    |    O
    |       
    |       
    |
   *********
   """,
    """
    ______
    |    |
    |    O
    |    |    
    |      
    |
   *********
   """,
    """
    ______
    |    |
    |    O
    |    |    
    |    |    
    |
   *********
   """,
    """
    ______
    |    |
    |    O
    |   /|    
    |    |    
    |
   *********
   """,
    """
    ______
    |    |
    |    O
    |   /|\    
    |    |    
    |
   *********
   """,
    """
    ______
    |    |
    |    O
    |   /|\    
    |   /|    
    |
   *********
   """,
    """
    ______
    |    |
    |    O
    |   /|\    
    |   /|\    
    |
   *********
   """
]

def drawHangman(tentativa):
    match(tentativa):
        case 0:
            print(estagios[0])
        case 1:
            print(estagios[1])
        case 2:
            print(estagios[2])
        case 3:
            print(estagios[3])
        case 4:
            print(estagios[4])
        case 5:
            print(estagios[5])
        case 6:
            print(estagios[6])
        case 7:
            print(estagios[7])
        