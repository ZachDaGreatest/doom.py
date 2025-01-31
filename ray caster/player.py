from math import sin,cos

class player():
    def __init__(self):
        self.pos = (2,2)
        self.direction = 0
        self.x_speed = 0
        self.y_speed = 0
        self.acceleration = .1
    def move_forward(self):
        self.x_speed += self.acceleration * cos(self.direction)
        self.y_speed += self.acceleration * sin(self.direction)
    def move_backward(self):
        self.x_speed -= self.acceleration * cos(self.direction)
        self.y_speed -= self.acceleration * sin(self.direction)
    def move_right(self):
        self.y_speed += self.acceleration * cos(self.direction)
        self.x_speed -= self.acceleration * sin(self.direction)
    def move_left(self):
        self.y_speed -= self.acceleration * cos(self.direction)
        self.x_speed += self.acceleration * sin(self.direction)
    def pos_update(self):
        self.pos = (self.pos[0] + self.x_speed, self.pos[1] + self.y_speed)
    def stop(self):
        self.y_speed = 0
        self.x_speed = 0
    def turn_right(self):
        self.direction += .1
    def turn_left(self):
        self.direction -= .1