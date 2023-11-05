print("Welcome to AskPython Quiz") #Печатаем приветствие и название игры
 

answer = input("Are you ready to play the Quiz? (yes/no) :") #Спрашиваем у пользователя готов ли он играть в викторину


score = 0
total_questions = 3 #Инициализируем переменные score и total_questions


if answer.lower() == "yes": #Если пользователь ответил "yes", задаем ему три вопроса и проверяем правильность ответов
   
    answer = input("Question 1: What is your Favourite programming language?") #Задаем первый вопрос и проверяем, правильный ли ответ
    if answer.lower() == "python":
        score += 1
        print("correct")  
    else:
        print("Wrong Answer :(") 

    
    answer = input("Question 2: Do you follow any author on AskPython? ") #Задаем второй вопрос и проверяем, правильный ли ответ
    if answer.lower() == "yes":
        score += 1
        print("correct")  
    else:
        print("Wrong Answer :(")  

  
    answer = input(
        "Question 3: What is the name of your favourite website for learning Python?" #Задаем третий вопрос и проверяем, правильный ли ответ
    )
    if answer.lower() == "askpython":
        score += 1
        print("correct")  
    else:
        print("Wrong Answer :(")  


print(
    "Thank you for Playing this small quiz game, you attempted", #Печатаем сообщение с количеством правильных ответов
    score,
    "questions correctly!",
)
mark = int((score / total_questions) * 100) #Вычисляем оценку в процентах и печатаем ее
print(f"Marks obtained: {mark}%")


print("BYE!") #Печатаем прощание