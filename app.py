import turtle
import colorsys
import pygame
import os

def colorful_spiral():
    # Initialize the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Enhanced Colorful Spiral")

    # Initialize the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()

    # Set the color mode to RGB
    turtle.colormode(255)

    # Initialize pygame for background music
    pygame.mixer.init()

    # Ensure the music file exists
    music_file = "song.mp3"  # Replace with your music file path
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # Loop the music indefinitely
    else:
        print(f"Music file '{music_file}' not found. Proceeding without music.")

    # Function to draw the spiral
    def draw_spiral():
        if not screen._root:  # Check if the screen is still open
            return
        t.clear()  # Clear previous drawing
        t.penup()
        t.goto(0, 0)  # Reset position to the center
        t.pendown()

        # Spiral parameters
        num_loops = 300  # Number of loops in the spiral
        length = 10      # Initial length of the segment
        hue = 0          # Starting hue for color transition
        angle = 45       # Angle of rotation for each segment

        # Draw the spiral
        for i in range(num_loops):
            if not screen._root:  # Stop drawing if the screen is closed
                break
            # Change pen color dynamically
            color = colorsys.hsv_to_rgb(hue, 1, 1)
            t.pencolor(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

            # Draw a segment of the spiral
            t.forward(length)
            t.right(angle)
            length += 2
            hue += 0.003
            if hue > 1:
                hue = 0  # Reset hue if it exceeds 1

    # Function to stop the program
    def stop_program():
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        screen.bye()

    # Function to restart the drawing
    def restart_drawing():
        if not screen._root:  # Check if the screen is still open
            return
        draw_spiral()
        screen.ontimer(restart_drawing, 1000)  # Restart after 1 second

    # Bind the 'q' key to stop the program
    screen.listen()
    screen.onkey(stop_program, "q")

    # Start the first drawing
    restart_drawing()

    screen.mainloop()

if __name__ == "__main__":
    colorful_spiral()
