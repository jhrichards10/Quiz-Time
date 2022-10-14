# Print a fun header
print(r"""
::::\ ::| ::|::::::| <::::\  ::::::|::::::|::::::|::::::|
::|,::|::|_::|  ::|  ,:::::/    ::|    ::|  :::"::|:::>   
 :::::\`:::::|::::::|`:::::>    ::|  ::::::|::| ::|::::::|
""")
print()

# Welcome player to the quiz
print("Welcome to Quiz Time! You will answer a few True or False questions. Please only enter True or False when it`s your turn to answer. Have fun and good luck! ")
print()

# Generate questions with corresponding answers
questions = ("Q1. George Washington was the first president of th United States of America.", "Q2. Massahusetts was the first state.", "Q3. The Los Angelos Rams are the defending super bowl champions.", "Q4. Venus is the closest planet to the sun.")

answers = ("True", "False", "True", "False")

# Count guesses
count = 0

# Create a loop to ask the questions
numberOfQuestions = len(questions)
enterAnswer = ""

for index in range(numberOfQuestions):
  print(questions[index])
  while(enterAnswer != "True" and enterAnswer != "False"):
    enterAnswer = input("Please enter 'True' or 'False': ")
  if(enterAnswer == answers[index]):
    count += 1
  enterAnswer = ""
  print()
       
# Print how many were guessed correct
print(f"You got {count} out of 4 correct! Thanks for playing!")