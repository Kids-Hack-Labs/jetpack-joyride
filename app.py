import pygame

from engine.game_env import Game

def main():
    title = 'Game'
    window_size = (320, 180)
    
    game = Game(title, window_size)
    game.run()

if __name__ == '__main__':
    main()
