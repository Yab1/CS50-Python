from random import randint

print('Welcome to my quiz!')

playing = input('Do you want to play? ')

if playing.strip().capitalize() != 'Yes':
 quit()

quizDict = [
    {'question': 'What is a primary storage component in computers?', 'answer': 'RAM'},
    {'question': 'Which hardware component displays visual output on a computer?', 'answer': 'Monitor'},
    {'question': 'What type of memory stores data even when the computer is turned off?', 'answer': 'ROM'},
    {'question': 'What do you call the brain of the computer?', 'answer': 'CPU'},
    {'question': 'What is the device used to input information into the computer?', 'answer': 'Keyboard'},
    {'question': 'Which component cools the computer and keeps it from overheating?', 'answer': 'Cooling fan'},
    {'question': 'Which hardware device stores data permanently?', 'answer': 'Hard drive'},
    {'question': 'What connects various hardware components allowing them to communicate?', 'answer': 'Motherboard'},
    {'question': 'What type of device reads and writes data on removable media?', 'answer': 'Optical drive'},
    {'question': 'Which part of the computer connects all devices to the CPU?', 'answer': 'Bus'}
]

random_num = randint(0,9)
user_answer = input(quizDict[random_num]['question']+" ")

if  user_answer.strip().capitalize()== quizDict[random_num]['answer']:
 print("Great job! 🎉 Your answer is correct!")
else:
 quit()