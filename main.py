from pynput.keyboard import Key, Listener
import random

def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

years = read_file("years.txt")
places = read_file("places.txt")
tasks = read_file("tasks.txt")

def get_term_definition():
    set = []
    while len(set) != (len(years))*(len(places))*(len(tasks)):
        year = random.choice(years)
        place = random.choice(places)
        task = random.choice(tasks)
        question = "Describe the " + task + " of empires in " + place + " in the year " + year + "."
        if question not in set:
            set.append(question)
    return set 

def on_press(key):
    a = 1
    try:
        # Check if the 'a' key was pressed
        if key.char == 'q':
            result = get_term_definition()
            print(result[a])
            a += 1
    except AttributeError:
        # Handle special keys
        if key == Key.esc:
            print("Exiting program.")
            return False  # Stop the listener

def main():
    print("Press 'Q' to generate a term definition or 'ESC' to exit.")
    # Start the keyboard listener
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()