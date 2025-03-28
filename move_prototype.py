from camera import *
from graphic import *

window = MainWindow()

cam = Camera(0, 0)
cam.set_speed(20)


def move():
    cam.move()
    print (f"{cam._X} {cam._Y}")
    cam.draw()

def turn_left():
    cam.turn(10)
    print (f"{cam._gaze_direction}")
    
def turn_right():
    cam.turn(-10)
    print (f"{cam._gaze_direction}")

window.listen()

window.key_bind(lambda: turn_left(), 'd')
window.key_bind(lambda: turn_right(), 'a')
window.key_bind(lambda: move(), 'w')
window.key_bind(lambda: window.close(), 'Escape')

window.screen.mainloop()

print("Прервано")
