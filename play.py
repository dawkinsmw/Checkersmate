from checkersmate.game import Game
# from checkersmate.Rules import legal_moves

if __name__ == '__main__':
    # players = {1:Player(),-1:Player()}
    results = []
    for i in range(1):
        g = Game(silent=True, output="result.log")
        results.append(g.play())
    
    print(results)