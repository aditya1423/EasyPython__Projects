

print("Welcome to my Quiz game")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    quit()

print("Let's play the game!!")

score = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("False")

# Question 2
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("False")

# Question 3
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("False")

# Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("False")

# Final score and percentage
print("You got " + str(score) + " questions correct.")
print("You scored " + str((score / 4) * 100) + "%.")


