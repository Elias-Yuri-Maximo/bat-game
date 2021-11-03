import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #this will handle the collision
        #if it intersected with a brick then it will erase that brick and ball will bounce (change ball's velocity)
        #if it intersected with the borders it will bounce back (change ball's velocity)
        #if it intersected with the paddle, it will bounce back (change ball's velocity)
        #if it intersected with the side wall, it will bounce back, (change ball's velocity)
        #if it intersected with the bottom line, it then ends the game.

        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        brick = cast["brick"]
    
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                #Here the code should set the brick text to ''
                
                
                #description = brick.get_description()
                #marquee.set_text(description) 