import pygame

from engine.game_env import Game

def main():
    title = 'Game'
    window_size = (1280, 720)
    
    game = Game(window_size, title)
    game.run()

if __name__ == '__main__':
    main()
