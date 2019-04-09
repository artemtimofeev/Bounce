import game
from choose_ball import choose


def main():
    Player = choose()
    game.play(Player)


if __name__ == "__main__":
    main()
