import LCD1602
import time 
import math



 #check if  rpi . gpio is installed chuma.

chatbot_words = [ 'Hello!','Good Bye!', 'How are you?' , 'What is your name?','ask any question!']

 # questions = ['Whatis pi?','What is logarithm?']
question1 = input('What are the first three numbers of  pi?')
answers = {
    question1 : 3.14 ,
    chatbot_words[1]: 'Hope you have a good day!',
    chatbot_words[2]: 'I am good. How are you ?',
    chatbot_words[3]: 'My name is logan, what is your name?'

}
userexit = input ('do you want to exit' + 'y/n')
if userexit == 'y':
    exit()
    
    

 # setup the rasberry pi
def setup():
    LCD1602.init(0x27,1) 
    LCD1602.write(0,0,'Hello')
    LCD1602.write(1,1,'From AI')
    time.sleep(2)
    LCD1602.clear()


def question():
    LCD1602.write(0,0,question[0])
    if question1 ==  3.14:
        LCD1602.write(0,0,'Good')
def cleanup():
    LCD1602.clear()

def destroy():

    try:
        setup()

    except KeyboardInterrupt():
        destroy


