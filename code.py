import keypad
import board

# ONLY EDIT CODE WITHIN main()

# You are free to add more functions to help you finish the project
        
def main():

    user_number = 1
    target_number = 4

    number_of_guesses = 0
    max_guesses = 3

    print("VALID KEYS: UP, DOWN, A, START")

    # Game Loop
    # This will run forever, unless exit conditions are met
    while True:
        event = k.events.get()

        if event:
            
            key_event = Key(event)
            
            if key_event.pressed == False:
                continue

            print(key_event.key)

            # exit the game if the "START button is pressed"
            if key_event.key == "START":
                break
                        


# If you have any need for extra functions, implement them here
            
# def helper_function():
#   return "I helped!"



# DO NOT EDIT ANYTHING BELOW HERE
# Read through and get a basic understanding of how things are working

# this is some built-in stuff that is necessary to work with the board
# don't worry too much about understanding this
k = keypad.ShiftRegisterKeys(
    clock=board.BUTTON_CLOCK,
    data=board.BUTTON_OUT,
    latch=board.BUTTON_LATCH,
    key_count=8,
    value_when_pressed=True,
)



# this is a class that helps us handle key presses/releases
class Key:
    def __init__(self, event):
        key_mapping = {
            6: "UP",
            5: "DOWN",
            7: "LEFT",
            4: "RIGHT",
            1: "A",
            0: "B",
            3: "SELECT",
            2: "START"
        }

        # pybadge uses integers to represent each button, the mapping converts the integer to a more intuitive key
        # for example: key_mapping[2] is "START"

        self.key = key_mapping[event.key_number]

        # pressed will be True if the button was pressed, false if the button was released
        self.pressed = event.pressed

    def __eq__(self, other):
        return self.key == other.key and self.pressed == other.pressed


# This ensures that the main() function runs when the script is run by pybadge
if __name__ == "__main__":
    main()