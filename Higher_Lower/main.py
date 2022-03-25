import random
from art import logo,vs
from game_data import data
from replit import clear

print(logo)



score = 0

print("\n")
 
# Function
def higher_lower ():
  global score 

  # Compare random choice
  first = random.choice(data)

  # For while Loop
  correct = True
  
  while correct:
   
    second = random.choice(data)
    
    #Scores
    if score > 0:
      print(f"Your current score is: {score}")

    #Compare Choice
    name1 = first["name"]
    des = first["description"]
    country = first["country"]
    follow = first["follower_count"]
    a = follow
    print(f"Compare A: {name1}, is a/an {des}, from {country}. \n")

    # VS logo
    print(f"{vs} \n")

    #Against Choice
    name2 = second["name"]
    des2 = second["description"]
    country2 = second["country"]
    follow2 = second["follower_count"] 
    b = follow2
    print(f"Against B: {name2}, is a/an {des2}, from {country2}. ")


    #Conditional Statement, if same choice is pulled

    if name1 == name2:
      clear()
      continue

    #Userinput 
    print("\n")
    prediction = input("Who has more followers? Type A or B: ").lower()

    
    #Conditional Statements
    
    if prediction == "b" and b > a:
      clear()
      score +=  1
      first = second
      print(logo)
      
      
    elif prediction == "a" and a > b:
      clear()
      score += 1
      first = second
      print(logo)
      
      
    else:
      correct = False
      clear()
      print(logo)
      print(f"Wrong!!! Game over, your final score: {score}")
      

higher_lower()

