import pygame
import mido
from mido import Message
import time


# down = index 1 - c - 60
# triangle = index 4 - c# - 61
# left = index 0 - d - 62
# x = index 6 - e - 64
# up = index 2 - f - 65
# o = index 7 - g - 67
# right = index 3 - a - 69
# square = index 5 - b - 71
# select = index 8 - d# - 63
# back = index 9 - f# - 66
notes = { 0:62, 1:60, 2:65, 3:69, 4:61, 5:71, 6:64, 7:67, 8:63, 9:66 }


# Initialize Pygame and Joystick
pygame.init()
pygame.joystick.init()

# Create a joystick object
joystick1 = pygame.joystick.Joystick(0)
joystick1.init()

# Create a second joystick object
joystick2 = pygame.joystick.Joystick(1)
joystick2.init()

# Initialize MIDI 1
port_name1 = 'Pad1 1' 
outport1 = mido.open_output(port_name1)

# Initialize MIDI 2
port_name2 = 'Pad2 2' 
outport2 = mido.open_output(port_name2)

# Define MIDI note values
velocity = 64  # Velocity of the note

def send_midi_message(outport, message_type, button_index, velocity):
    """Send MIDI message."""
    print(notes[button_index])
    try:
        message = Message(message_type, note=notes[button_index], velocity=velocity)
        outport.send(message)
        print(f"Sent MIDI message: {message}")
        print(button_index)
    except Exception as e:
        print(f"Error sending MIDI message: {e}")

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.joy == 0:  # Joystick 1
                send_midi_message(outport1, 'note_on', event.button, velocity)
            elif event.joy == 1:  # Joystick 2
                send_midi_message(outport2, 'note_on', event.button, velocity)
        elif event.type == pygame.JOYBUTTONUP:
            if event.joy == 0:  # Joystick 1
                send_midi_message(outport1, 'note_off', event.button, 0)  # Note-off message with zero velocity
            elif event.joy == 1:  # Joystick 2
                send_midi_message(outport2, 'note_off', event.button, 0)  # Note-off message with zero velocity

pygame.quit()

