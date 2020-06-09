from glob import glob
from pygame import image

# this class represents all the data needed to play an animation
# it DOES NOT know how to "play" itself
# an animator behaviour takes the information in this class and "plays" it
class Animation:

    @staticmethod
    def get_assets(dirpath):
        filepaths = glob(dirpath + "*.png")

        assets = []
        for filepath in filepaths:
            assets.append( image.load(filepath) )

        if len(assets) == 0:
            print("No sprites found at " + dirpath)

        return assets

    # dirpath should be a directory with the sprites of the animation
    def __init__(self, dirpath):
        # potential future option to "load from sprite sheet"

        self.frames = Animation.get_assets(dirpath)
        self.frame_count = len(self.frames)
        
        self.fps = 0.1

    def get_frame(self, index):
        return self.frames[index]
        

        
        
