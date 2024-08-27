# ps4_controller.py
import pygame
import sys

class PS4Controller:
    def __init__(self):
        pygame.init()
        self.joystick = None
        self.initialize_controller()

    def initialize_controller(self):
        joystick_count = pygame.joystick.get_count()
        if joystick_count > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        else:
            print("No controller connected")

    def get_input(self, button_name=None):
        if self.joystick:
            # Get axis values
            left_axis_x = round(self.joystick.get_axis(0), 2)
            left_axis_y = round(self.joystick.get_axis(1), 2)
            right_axis_x = round(self.joystick.get_axis(2), 2)
            right_axis_y = round(self.joystick.get_axis(3), 2)
            LT = round(self.joystick.get_axis(4), 2)
            RT = round(self.joystick.get_axis(5), 2)

            # Get button values
            button_values = {
                "X": self.joystick.get_button(0),
                "Circle": self.joystick.get_button(1),
                "Square": self.joystick.get_button(2),
                "Triangle": self.joystick.get_button(3),
                "Share": self.joystick.get_button(4),
                "PS": self.joystick.get_button(5),
                "Options": self.joystick.get_button(6),
                "L3": self.joystick.get_button(7),
                "R3": self.joystick.get_button(8),
                "L1": self.joystick.get_button(9),
                "R1": self.joystick.get_button(10),
                "Up": self.joystick.get_button(11),
                "Down": self.joystick.get_button(12),
                "Left": self.joystick.get_button(13),
                "Right": self.joystick.get_button(14),
                "TouchPad": self.joystick.get_button(15),
                "left_axis_x": left_axis_x,
                "left_axis_y": left_axis_y,
                "right_axis_x": right_axis_x,
                "right_axis_y": right_axis_y,
                "LT": LT,
                "RT": RT
            }

            if button_name:
                return button_values.get(button_name, None)
            else:
                return button_values
        else:
            return None

    def quit(self):
        pygame.quit()
        sys.exit()

def controller_inputs(lst):
    controller = PS4Controller()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            controller.quit()
    
    pygame.event.get()
    pygame.time.Clock().tick(60)
    pygame.event.get()
    
    button = []
    
    for i in range(len(lst)):
        value = controller.get_input(lst[i])
        button.append(value)
    return button

def controller_get_input(input):
    controller = PS4Controller()
        
    pygame.event.get()
    pygame.time.Clock().tick(60)
    pygame.event.get()
    
    value = controller.get_input(input)
    return value
   
if __name__ == "__main__":
    X = controller_get_input("X")
    print(X)
    values = controller_inputs(["X", "left_axis_x", "left_axis_y"])
    print(values)

    while True:
        
        #using the main function with list of inputs
        input = ["X", "left_axis_x", "left_axis_y"]
        values = controller_inputs(input)
        # print(values)

        #using the get_input function
        x_button_state = controller_get_input("X")
        left_axis_x = controller_get_input("left_axis_x")
        left_axis_y = controller_get_input("left_axis_y")
        
        print(f"Button: {x_button_state}, Left Stick: ({left_axis_x}, {left_axis_y})")
        
        
