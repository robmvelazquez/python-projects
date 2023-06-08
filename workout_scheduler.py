def display_menu():
    print('1. Create a new workout.')
    print('2. Edit a workout.')
    print('3. Remove an exercise.')
    print('4. Mark an exercise as complete.')
    print('5. Review a previous workout.')


def create_workout(workout_scheduler):
    print('Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday')
    day_input = input('Select a day of the week that you would like to complete this workout (1-7): ')
    try:
        day = int(day_input)
        if 1 <= day <= 7:
            if day == 1:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                print('You entered', workout)
            elif day == 2:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                print('You entered', workout)
            elif day == 3:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                print('You entered', workout)
            elif day == 4:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                print('You entered', workout)
            elif day == 5:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                print('You entered', workout)
            elif day == 6:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
                print('You entered', workout)
            elif day == 7:
                workout = input('Enter a name for the workout you will perform on Sunday: ')
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
    workout_scheduler = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_workout(workout_scheduler)
        elif choice == '2':
            edit_workout(workout_scheduler)
        elif choice == '3':
            remove_workout(workout_scheduler)
        elif choice == '4':
            complete_exercise(workout_scheduler)
        elif choice == '5':
            review_workout(workout_scheduler)
        else:
            print('\nInvalid entry, please try again.')
            display_menu()


workout_scheduler_app()