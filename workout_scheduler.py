import datetime

current_date = datetime.datetime.now()
day_of_week = current_date.weekday()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_name = days[day_of_week]

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []

workout = ""
day_input = ""
capitalized_input = ""


def display_menu():
    print('1. View Today\'s Workout.')
    print('2. Edit a workout.')
    print('3. Remove an exercise.')
    print('4. Mark an exercise as complete.')
    print('5. Review a previous workout.')
    print('6. Create a new workout.')


def todays_workout(workout_scheduler):
    if day_name == 'Monday':
        print('You will perform the following workouts today:\n', *monday)
    elif day_name == 'Tuesday':
        print('You will perform the following workouts today:\n', *tuesday)
    elif day_name == 'Wednesday':
        print('You will perform the following workouts today:\n', *wednesday)
    elif day_name == 'Thursday':
        print('You will perform the following workouts today:\n', *thursday)
    elif day_name == 'Friday':
        print('You will perform the following workouts today:\n', *friday)
    elif day_name == 'Saturday':
        print('You will perform the following workouts today:\n', *saturday)
    elif day_name == 'Sunday':
        print('You will perform the following workouts today:\n', *sunday)


# This function allows the user to create a workout routine that will be saved for a specific day of the week
def create_workout(workout_scheduler):
    global workout
    global day_input
    for _ in days:
        print(_)
    day_input = input('Select a day of the week that you would like to perform this workout: (1 - 7)\n')
    try:
        day = int(day_input)
        if 1 <= day <= 7:
            if day == 1:
                enter_workout(workout_scheduler)
                monday.append(capitalized_input)
            elif day == 2:
                enter_workout(workout_scheduler)
                tuesday.append(capitalized_input)
            elif day == 3:
                enter_workout(workout_scheduler)
                wednesday.append(capitalized_input)
            elif day == 4:
                enter_workout(workout_scheduler)
                thursday.append(capitalized_input)
            elif day == 5:
                enter_workout(workout_scheduler)
                friday.append(capitalized_input)
            elif day == 6:
                enter_workout(workout_scheduler)
                saturday.append(capitalized_input)
            elif day == 7:
                enter_workout(workout_scheduler)
                sunday.append(capitalized_input)
            else:
                print('Invalid entry, try again')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')


def enter_workout(workout_scheduler):
    global workout
    global day_input
    global capitalized_input
    try:
        day_index = int(day_input) - 1  # Adjusting index to match 0-based index
        if 0 <= day_index < len(days):
            day_name = days[day_index]
            workout = input('Enter a name for the workout you will perform on ' + day_name + ': \n')
            capitalized_input = workout.title()
            print('You entered', capitalized_input, 'as the workout you would like to perform on ' + day_name + '.\n')
        else:
            print('Invalid day index. Please enter a valid index.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')


# This function allows the user to edit previous workout routines.
def edit_workout(workout_scheduler):
    global workout
    global day_input
    for _ in days:
        print(_)
    day_input = input('Select a day of the week that you would like to edit: ')
    try:
        day = int(day_input)
        if 1 <= day <= 7:
            if day == 1:
                monday.remove(workout)
                enter_workout(workout_scheduler)
                monday.append(workout)
            elif day == 2:
                tuesday.remove(workout)
                enter_workout(workout_scheduler)
                tuesday.append(workout)
            elif day == 3:
                wednesday.remove(workout)
                enter_workout(workout_scheduler)
                wednesday.append(workout)
            elif day == 4:
                thursday.remove(workout)
                enter_workout(workout_scheduler)
                thursday.append(workout)
            elif day == 5:
                friday.remove(workout)
                enter_workout(workout_scheduler)
                friday.append(workout)
            elif day == 6:
                saturday.remove(workout)
                enter_workout(workout_scheduler)
                saturday.append(workout)
            elif day == 7:
                sunday.remove(workout)
                enter_workout(workout_scheduler)
                sunday.append(workout)
            else:
                print('Invalid entry, try again')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')


def remove_workout(workout_scheduler):
    global workout
    global day_input
    for _ in days:
        print(_)
    day_input = input('Select a day of the week that you would like to edit: ')
    try:
        day = int(day_input)
        if 1 <= day <= 7:
            if day == 1:
                print('Workouts for Monday:\n')
                for i, workout in enumerate(monday):
                    print(f'{i + 1}. {workout}')
                index = int(input('Select the index of the workout you would like to remove.\n')) - 1
                if 0 <= index < len(monday):
                    monday.pop(index)
                else:
                    print('Invalid index, try again.')
            elif day == 2:
                print('Workouts for Tuesday:\n')
                for i, workout in enumerate(tuesday):
                    print(f'{i + 1}. {workout}')
                index = int(input('Select the index of the workout you would like to remove.\n')) - 1
                if 0 <= index < len(tuesday):
                    tuesday.pop(index)
                else:
                    print('Invalid index, try again.')
            elif day == 3:
                print('Workouts for Wednesday:\n')
                for i, workout in enumerate(wednesday):
                    print(f'{i + 1}. {workout}')
                index = int(input('Select the index of the workout you would like to remove.\n')) - 1
                if 0 <= index < len(wednesday):
                    wednesday.pop(index)
                else:
                    print('Invalid index, try again.')
            elif day == 4:
                thursday.remove(workout)
            elif day == 5:
                friday.remove(workout)
            elif day == 6:
                saturday.remove(workout)
            elif day == 7:
                sunday.remove(workout)
            else:
                print('Invalid entry, try again')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')


def complete_exercise(workout_scheduler):
    complete = input('Select a workout you would like to mark as completed: ')


def review_workout(workout_scheduler):
    review = input('Select the week you would like to review: ')


def workout_scheduler_app():
    workout_scheduler = []
    while True:
        print('\nHello and Happy', day_name, '!\n')
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            todays_workout(workout_scheduler)
        elif choice == '2':
            edit_workout(workout_scheduler)
        elif choice == '3':
            remove_workout(workout_scheduler)
        elif choice == '4':
            complete_exercise(workout_scheduler)
        elif choice == '5':
            review_workout(workout_scheduler)
        elif choice == '6':
            create_workout(workout_scheduler)
        else:
            print('\nInvalid entry, please try again.')
            display_menu()


workout_scheduler_app()
