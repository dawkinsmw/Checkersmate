from checkersmate.game import Game
# from checkersmate.Rules import legal_moves

if __name__ == '__main__':
    # players = {1:Player(),-1:Player()}
    results = []
    for i in range(500):
        g = Game(silent=True)
        results.append(g.play())
    
    print(results)