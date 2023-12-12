# Input the percentage score from the user
percentage = int(input("Enter the percentage score: "))

 # Determine the letter grade based on the percentage
if 90 <= percentage <= 100:
     grade = "A+"
elif 80 <= percentage < 90:
     grade = "A"
elif 70 <= percentage < 80:
     grade = "B"
elif 60 <= percentage < 70:
     grade = "C"
elif 50 <= percentage < 60:
     grade = "D"
elif 0 <= percentage < 50:
     grade = "F"
else:
     grade = "Invalid input"

# # Print the corresponding letter grade
print("Your grade is:", grade)


