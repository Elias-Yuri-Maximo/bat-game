import random
import sys
from typing import Text
from game.point import Point
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    #def ball_vertical_collision(self, ball): 
    #    current_direction = ball.get_velocity()
            
    #    current_direction.set_y(current_direction.get_y * -1)

    #    ball.set_direction(current_direction)

        
    #def ball_horizontal_collision(self, ball):




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
        bricks = cast["brick"]
        marquee = cast["marquee"][0]

        #if the ball hits one of the bricks 
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text('')
                index = bricks.index(brick)
                bricks.pop(index)

                current_string = marquee.get_text().split(':')
                current_score = int(current_string[1])
                if current_score==0:
                    sys.exit()
                current_score-=1
                current_string.pop()
                current_string.append(':')
                current_string.append(str(current_score))
                text =''
                for line in current_string: 
                    text+=line    
                marquee.set_text(text)
                #bricks.remove(brick)
                #Change if hits top
                #self.ball_vertical_colision(ball)
        
        #BALL_VERTICAL_COLISION METHOD
                current_direction = ball.get_velocity()
            
                altered_direction = Point(current_direction.get_x(), current_direction.get_y() * -1)

                ball.set_velocity(altered_direction)

        #x = paddle.get_position().get_x()  
        #x_list = []
        
    
        
        for i in range(12):
            ball_x = ball.get_position().get_x()
            ball_y = ball.get_position().get_y()
            paddle_x = paddle.get_position().get_x()
            paddle_y = paddle.get_position().get_y()


               
            if (ball_y == paddle_y) and (ball_x == paddle_x + i):  
                #description = brick.get_description()
                #marquee.set_text(description)
                #self.ball_horizontal_collision(ball)
                current_direction = ball.get_velocity()
            
                altered_direction = Point(current_direction.get_x(), current_direction.get_y()* -1)

                ball.set_velocity(altered_direction)


