# Create-A-Quiz Assignment
print("Welcome to the Runaway Horses Quiz!")
completion = False

# Main Program Loop 
loop = True
while loop:
  # Print Main Menu
  print("\nMAIN MENU")
  print("1: Quiz")
  print("2: Answer Key")
  print("3: Exit Quiz")

  # Get Menu Selection from User
  selection = input("Enter Selection (1-3): ")

  # Take Action Based on Menu Selection  
  if selection == "1":

    # Input
    print("\nRUNAWAY HORSES QUIZ")
    
    # Set score
    score = 0

    # Question 1
    ans1 = input("How old is Shigekuni Honda at the start of the book? ").lower()
    if ans1 == "38" or ans1 == "38 years" or ans1 == "thirty-eight years" or ans1 == "thirty-eight":
      print("Correct!")
      score = score + 1
    else:
      print("Incorrect.")

    # Question 2
    ans2 = input("What is the driving motivation behind Isaos actions? ").lower()
    if ans2 == "nationalism" or ans2 == "patriotism" or ans2 == "honor":
      print("Correct!")
      score = score + 1
    else:
      print("Incorrect.")
    
    # Question 3
    ans3 = input("Who does Honda think Isao is the reincarnation of? ").lower()
    if ans3 == "kiyoaki" or ans3 == "kiyoaki matsugae":
      print("Correct!")
      score = score + 1
    else:
      print("Incorrect.")
    
    # Question 4
    ans4 = input("Who does Isao consult for military support? ").lower()
    if ans4 == "lieutenant hori" or ans4 == "hori":
      print("Correct!")
      score = score + 1
    else: 
      print("Incorrect.")

    # (Output) Give score/specialized input
    percent = (score / 4) * 100
    print("Your result is " + str(score) + "/4. (" + str(percent) + "%)")
    if percent == 100:
      print("Very impressive!")
    elif percent == 75: 
      print("Don't beat yourself up on that one!")
    elif percent == 50: 
      print("Back to the drawing board, huh?")
    elif percent == 25:
      print("Study harder next time!")
    elif percent == 0:
      print("Very dissapointing...")

    # Indicate a previous completion of the test
    completion = True
  

  elif selection == "2":
    if completion == True:
      print()
      print("RUNAWAY HORSES ANSWER KEY")
      print("1 - How old is Shigekuni Honda at the start of the book?")
      print("- Answer is 38 / 38 years / thirty-eight years / thirty-eight.")
      print("")
      print("2 - What is the driving motivation behind Isaos actions?")
      print("- Nationalism / Patriotism / Honor")
      print()
      print("3 - Who does Honda think Isao is the reincarnation of?")
      print("- Kiyoaki / Kiyoaki Matsugae")
      print()
      print("4 - Who does Isao consult for military support?")
      print("- Lieutenant Hori / Hori")
      print()
    else:
      print("\nYou need to have completed the quiz at least once beforehand!")

  elif selection == "3":
    print("EXIT")
    loop = False