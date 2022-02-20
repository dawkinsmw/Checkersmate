from checkersmate.game import Game
from checkersmate.player.human import human_player
from checkersmate.player.deep import deep_player

if __name__ == '__main__':
    g = Game(p1=human_player(),p2=deep_player())
    g.play()
#     n = 10000
#     results = []
#     for i in range(n):
#         g = Game(p1=deep_player(),silent=True)
#         results.append(g.play())
#     print(sum(results)/n)

    