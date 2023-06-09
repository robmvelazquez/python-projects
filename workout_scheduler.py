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


def display_menu():
    print('1. View Today\'s Workout.')
    print('2. Edit a workout.')
    print('3. Remove an exercise.')
    print('4. Mark an exercise as complete.')
    print('5. Review a previous workout.')
    print('6. Create a new workout.')


def todays_workout(workout_schedule):
    if day_name == 'Monday':
        print(*monday)
    elif day_name == 'Tuesday':
        print(*tuesday)
    elif day_name == 'Wednesday':
        print(*wednesday)
    elif day_name == 'Thursday':
        print(*thursday)
    elif day_name == 'Friday':
        print(*friday)
    elif day_name == 'Saturday':
        print(*saturday)
    elif day_name == 'Sunday':
        print(*sunday)


def create_workout(workout_scheduler):
    for _ in days:
        print(_)
    day_input = input('Select a day of the week that you would like to complete this workout (1-7): ')
    try:
        day = int(day_input)
        if 1 <= day <= 7:
            if day == 1:
                workout = input('Enter a name for the workout you will perform on Monday: ')
                monday.append(workout)
                print('You entered', workout)
            elif day == 2:
                workout = input('Enter a name for the workout you will perform on' + day_name + ': ')
                tuesday.append(workout)
                print('You entered', workout)
            elif day == 3:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                wednesday.append(workout)
                print('You entered', workout)
            elif day == 4:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                thursday.append(workout)
                print('You entered', workout)
            elif day == 5:
                workout = input('Enter a name for the workout you will perform on ' + day_name + ': ')
                friday.append(workout)
                print('You entered', workout)
            elif day == 6:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                saturday.append(workout)
                print('You entered', workout)
            elif day == 7:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                sunday.append(workout)
                print('You entered', workout)
            else:
                print('Invalid entry, try again')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')


def edit_workout(workout_scheduler):
    edit = input('Select a workout you would like to edit: ')


def remove_workout(workout_scheduler):
    remove = input('Select a workout you would like to remove: ')


def complete_exercise(workout_scheduler):
    complete = input('Select a workout you would like to mark as completed: ')


def review_workout(workout_scheduler):
    review = input('Select the week you would like to review: ')


def workout_scheduler_app():

    while True:
        print('Hello and happy', day_name, '!')
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
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
