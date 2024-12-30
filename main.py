from pynput.keyboard import Key, Listener # Import for use in on_press and main functions
import random #Import for use in get_term_definition function

def read_file(filename):#This function reads a file and extracts the data as a list seperated by the lines in the flies. 
    with open(filename, "r") as f:
        return f.read().splitlines()
    
#The below reads the 3 associated files and stores the data as lists
years = read_file("years.txt")
places = read_file("places.txt")
tasks = read_file("tasks.txt")

def get_term_definition(): #This creates a list of possible questions, there will always be (len(years))*(len(places))*(len(tasks)) number of possible questions. Each item in the question that can vary is cosen at random. Once one has been made, a check if made if that is already in the list, if it is not it is added. This prevents duplicite questions.
    set = []
    while len(set) != (len(years))*(len(places))*(len(tasks)):
        year = random.choice(years)
        place = random.choice(places)
        task = random.choice(tasks)
        question = "Describe the " + task + " of empires in " + place + " in the year " + year + "."
        if question not in set:
            set.append(question)
    return set 

a = 0

def on_press(key):
    global a
    result = get_term_definition()
    try:
        #Check if all questions have been answered
        if key.char == 'q' and a >= (len(result)):
            print("You have completed every question!")
            return False 
        # Check if the 'q' key was pressed
        elif key.char == 'q':
            print(f"Question {a+1}:  {result[a]}")
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