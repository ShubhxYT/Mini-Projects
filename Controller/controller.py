import pygame
import sys

def get_ps4_controller_input():
    # Initialize Pygame
    pygame.init()

    # Set up display
    width, height = 1280, 720
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PS4 Controller Input Display")

    # Set up font
    font = pygame.font.SysFont(None, 36)

    # PS4 controller button mapping
    ps4_buttons = {
        0: ("X", (1000, 500)),
        1: ("Circle", (1100, 450)),
        2: ("Square", (900, 450)),
        3: ("Triangle", (1000, 400)),
        4: ("Share", (200, 600)),
        5: ("PS", (600, 650)),
        6: ("Options", (1000, 300)),
        7: ("L3", (300, 300)),
        8: ("R3", (1000, 300)),
        9: ("R1", (1100, 200)),
        10: ("L1", (100, 200)),
        11: ("Up", (600, 100)),
        12: ("Down", (600, 200)),
        13: ("Left", (500, 150)),
        14: ("Right", (700, 150)),
        15: ("TouchPad", (600, 300)),
    }

    left_joystick_center = (450, 325)
    right_joystick_center = (900, 325)
    joystick_radius = 100
    trigger_bar_length = 400
    trigger_bar_height = 20

    running = True
    while running:
        window.fill((0, 0, 0))  # Fill the window with black

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get joystick information (also to check if there is a controller)
        joystick_count = pygame.joystick.get_count()

        if joystick_count > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

            buttons = joystick.get_numbuttons()

            # Get axis values
            left_axis_x = joystick.get_axis(0)
            left_axis_y = joystick.get_axis(1)
            right_axis_x = joystick.get_axis(2)
            right_axis_y = joystick.get_axis(3)
            LT = joystick.get_axis(4)
            RT = joystick.get_axis(5)

            # Draw joystick positions
            pygame.draw.circle(window, (100, 100, 100), left_joystick_center, joystick_radius, 1)
            left_stick_position = (int(left_joystick_center[0] + left_axis_x * joystick_radius),
                                   int(left_joystick_center[1] + left_axis_y * joystick_radius))
            pygame.draw.circle(window, (0, 255, 0), left_stick_position, 10)

            pygame.draw.circle(window, (100, 100, 100), right_joystick_center, joystick_radius, 1)
            right_stick_position = (int(right_joystick_center[0] + right_axis_x * joystick_radius),
                                    int(right_joystick_center[1] + right_axis_y * joystick_radius))
            pygame.draw.circle(window, (0, 0, 255), right_stick_position, 10)

            # Draw trigger positions
            pygame.draw.rect(window, (100, 100, 100), (100, 650, trigger_bar_length, trigger_bar_height), 1)
            pygame.draw.rect(window, (255, 0, 0), (100, 650, trigger_bar_length * (LT + 1) / 2, trigger_bar_height))

            pygame.draw.rect(window, (100, 100, 100), (780, 650, trigger_bar_length, trigger_bar_height), 1)
            pygame.draw.rect(window, (255, 0, 0), (780, 650, trigger_bar_length * (RT + 1) / 2, trigger_bar_height))

            pressed_buttons = []
            for i in range(buttons-1):
                button = joystick.get_button(i)
                button_name, button_position = ps4_buttons.get(i, (f"Button {i}", (0, 0)))
                color = (0, 255, 0) if button == 1 else (255, 255, 255)
                text = font.render(button_name, True, color)
                window.blit(text, button_position)
                if button == 1:
                    pressed_buttons.append((button_name, button))

            pygame.display.flip()

            # Return values if any button is pressed
            # if pressed_buttons:
            #     return left_axis_x, left_axis_y, right_axis_x, right_axis_y, RT, LT, pressed_buttons
        else:
            text = font.render("No controller connected", True, (255, 255, 255))
            window.blit(text, (20, 20))
            pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

# Example usage
while True:
    controller_input = get_ps4_controller_input()
    # if controller_input:
    #     print(controller_input)
