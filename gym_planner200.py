# Name: Vicky Richemond
# Program: Personal Gym Planner
# Description: Creates a workout plan and calculates workout totals.
# Help: The Coding Sloth 20 Programming Projects That Will Make You A God At Coding


def calculateVolume(sets, reps, weight):
    volume = sets * reps * weight
    return volume


def calculateReps(sets, reps):
    total = sets * reps
    return total


def displayExercise(exercise, sets, reps, weight):
    print()
    print("Exercise:", exercise)
    print("Sets:", sets)
    print("Reps per set:", reps)
    print("Weight:", weight, "lbs")


def displayMenu():
    print()
    print("-" * 45)
    print("1. Create a workout")
    print("2. View workout instructions")
    print("3. Exit")
    print("-" * 45)


def showInstructions():
    print()
    print("Enter how many exercises you want to plan.")
    print("For each exercise, enter its name.")
    print("Then enter your sets, reps, and weight.")
    print("Enter 0 for weight for a bodyweight exercise.")
    print("Bodyweight is not included in training volume.")
    print("Sets and reps must be greater than zero.")
    print("Your workout totals appear at the end.")


def createWorkout(name, goal):
    print()
    print("=" * 45)
    print("CREATE YOUR WORKOUT")
    print("=" * 45)

    exerciseCount = int(input("How many exercises? "))

    while exerciseCount <= 0:
        print("Enter at least one exercise.")
        exerciseCount = int(input("How many exercises? "))

    allReps = 0
    totalSets = 0
    totalWorkoutVolume = 0
    weightedExercises = 0
    bodyweightExercises = 0

    for exerciseNumber in range(1, exerciseCount + 1):
        print()
        print("-" * 45)
        print("Exercise number", exerciseNumber)
        print("-" * 45)

        exercise = input("Enter an exercise: ").strip()

        while not exercise:
            print("The exercise name cannot be empty.")
            exercise = input("Enter an exercise: ").strip()

        sets = int(input("How many sets will you do? "))
        reps = int(input("How many reps per set? "))

        while sets <= 0 or reps <= 0:
            print("Sets and reps must both be greater than zero.")
            sets = int(input("How many sets will you do? "))
            reps = int(input("How many reps per set? "))

        weight = float(input("How much weight will you use? "))

        while weight < 0:
            print("Weight cannot be negative.")
            weight = float(input("How much weight will you use? "))

        totalReps = calculateReps(sets, reps)
        trainingVolume = calculateVolume(sets, reps, weight)

        allReps += totalReps
        totalSets += sets
        totalWorkoutVolume += trainingVolume

        displayExercise(exercise, sets, reps, weight)

        if weight == 0:
            print("Type: Bodyweight exercise")
            bodyweightExercises += 1
        else:
            print("Type: Weighted exercise")
            weightedExercises += 1

        if sets >= 3 and reps >= 8:
            print("This exercise includes at least 3 sets of 8 reps.")

        if reps <= 5:
            print("Rep category: Low repetitions")
        elif reps <= 12:
            print("Rep category: Moderate repetitions")
        else:
            print("Rep category: High repetitions")

        print("Total repetitions:", totalReps)
        print("Training volume:", trainingVolume, "lbs")

    print()
    print("=" * 45)
    print("WORKOUT SUMMARY")
    print("=" * 45)
    print("Name:", name)
    print("Fitness goal:", goal)
    print("Exercises planned:", exerciseCount)
    print("Weighted exercises:", weightedExercises)
    print("Bodyweight exercises:", bodyweightExercises)
    print("Total sets:", totalSets)
    print("Total repetitions:", allReps)
    print("Total training volume:", totalWorkoutVolume, "lbs")

    averageReps = allReps / exerciseCount
    print("Average total reps per exercise:", format(averageReps, ".2f"))

    if goal == "strength":
        print("Your selected focus is building strength.")
    elif goal == "muscle":
        print("Your selected focus is building muscle.")

    print()
    print(name + ", your workout plan is complete!")
    print("GET BIG!! " * 3)


def main():
    print("          PERSONAL GYM PLANNER")
    print("=" * 45)
    print("Welcome to the Personal Gym Planner!")
    print("This program will help you plan your workout.")
    print()

    name = input("Enter your name: ").strip()

    while not name:
        print("Please enter your name.")
        name = input("Enter your name: ").strip()

    print()
    print("Goal examples: strength, muscle, endurance")
    goal = input("Enter your fitness goal: ").strip().lower()

    while not goal:
        print("Please enter a fitness goal.")
        goal = input("Enter your fitness goal: ").strip().lower()

    print()
    print("Welcome,", name)
    print("Your goal is", goal, sep=": ")

    choice = ""

    while choice != "3":
        displayMenu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            createWorkout(name, goal)
        elif choice == "2":
            showInstructions()
        elif choice == "3":
            print("Thanks for using the Personal Gym Planner.")
        else:
            print("Invalid selection. Try again.")


main()