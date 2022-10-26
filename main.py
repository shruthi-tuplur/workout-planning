# this program will help me plan workouts
# it will have a gui with buttons to pick whether it's an upper body or lower body day and buttons to pick the amount of exercises per day (or random from a range of 4-6
# it will also have a section that shows me the final list of exercises
# buttons: upper body, lower body, 4 exercises, 5 exercises, 6 exercises, random between 4-6, and then a final enter button
# buttons will be highlighted once clicked


from ctypes import alignment
from tkinter import *
import random
from tkinter import font
from turtle import bgcolor, clear, color
 

# constants

FONT = ('Courier', 20, 'normal')
lower_body_exercises = ['leg extensions for quads', 'hamstring curl', 'squats', 'calf machine', 'bulgarian split squat', 'outer thigh abductors', 'good morning', 'leg press']
butt_exercises = ['hip thrusts + KAS (if feeling good)', 'donkey kicks', 'sumo squat']
upper_body_exercises = ['tricep + bicep + upper back cable extensions', 'lateral pulldown for back', 'shoulder press', 'tricep dip machine', 'deltoid fly', 'bicep curl machine', 'pulldown machine for traps', 'crunches']

# creating window
window = Tk()
window.title('Workout Planner')
window.config(height = 500, width = 700, background= 'light pink')

# setting up button functions
def arm_function():
    global what_day
    arm.configure(highlightbackground='#AC218E', fg= '#AC218E')
    what_day = 'arm'
    workout_plan.insert(INSERT, 'UPPER BODY DAY-')
    
def leg_function():
    global what_day
    leg.configure(highlightbackground='#AC218E', fg= '#AC218E')
    what_day = 'leg'
    workout_plan.insert(INSERT, 'LOWER BODY DAY-')
    
    
def four_function():
    global num_exercises
    num_exercises = 4
    four.configure(highlightbackground='#AC218E', fg= '#AC218E')
    workout_plan.insert(END, '\n')
    workout_plan.insert(END, '\nTODAY\'S FOUR EXERCISES ARE:') 
    
def five_function():
    global num_exercises
    num_exercises = 5
    five.configure(highlightbackground='#AC218E', fg= '#AC218E')
    workout_plan.insert(END, '\n')
    workout_plan.insert(END, '\nTODAY\'S FIVE EXERCISES ARE:')     
    
def six_function():
    global num_exercises
    num_exercises = 6
    four.configure(highlightbackground='#AC218E', fg= '#AC218E')
    workout_plan.insert(END, '\n')
    workout_plan.insert(END, '\nTODAY\'S SIX EXERCISES ARE:')             

def you_pick_function():
    global num_exercises
    num_exercises = random.randint(4, 6)
    you_pick.configure(highlightbackground='#AC218E', fg= '#AC218E')
    workout_plan.insert(END, '\n')
    workout_plan.insert(END, f'\nTODAY\'S {num_exercises} EXERCISES ARE:') 
    
def workout_plan_function():
    global today
    today = []
    global what_day
    workout_plan.insert(END, '\n')
    while len(today) < num_exercises:
        if what_day == 'arm':
                current_arm = 1
                while len(today) < num_exercises:
                    exercise = random.choice(upper_body_exercises)
                    if exercise not in today:
                      today.append(exercise)   
                      workout_plan.insert(END, (f'\n{current_arm}) {exercise}'))
                      current_arm += 1
        if what_day == 'leg':
            if num_exercises == 4:
                today_butt = random.choice(butt_exercises)
                today.append(today_butt)
                workout_plan.insert(END, (f'\n1) {today_butt}'))         
                current_less_four = 2
                while len(today) < num_exercises:
                    exercise = random.choice(lower_body_exercises)
                    if exercise not in today:
                      today.append(exercise)   
                      workout_plan.insert(END, (f'\n{current_less_four}) {exercise}')) 
                      current_less_four += 1
            if num_exercises > 4:
              current = 1 
              current_lower = 3
              while len(today) < 2:  
                today_butt = random.choice(butt_exercises)
                if today_butt not in today:
                    today.append(today_butt)
                    workout_plan.insert(END, (f'\n{current}) {today_butt}'))
                    current += 1         
              while len(today) < num_exercises:
                exercise = random.choice(lower_body_exercises)
                if exercise not in today:
                      today.append(exercise)   
                      workout_plan.insert(END, (f'\n{current_lower}) {exercise}')) 
                      current_lower += 1                  
        
          
def clear_screen():    
    global what_day
    global today
    global num_exercises
    workout_plan.delete('1.00', END)
    what_day = ''
    today = []
    num_exercises = 0
    arm.configure(highlightbackground= 'black', fg = 'violet red')
    leg.configure(highlightbackground= 'black', fg = 'violet red')
    four.configure(highlightbackground= 'black', fg = 'violet red')
    five.configure(highlightbackground= 'black', fg = 'violet red')
    six.configure(highlightbackground= 'black', fg = 'violet red')
    you_pick.configure(highlightbackground= 'black', fg = 'violet red')
    
    
# setting up labels
arm_or_leg = Label(text = 'arm day or leg day?', fg = 'violet red', font = ('Courier', 20, 'normal'), bg= 'light pink')
arm_or_leg.grid(column = 0, row = 0)

how_many = Label(text = 'how many\nexercises?', fg = 'violet red', font = ('Courier', 20, 'normal'), bg = 'light pink')
how_many.grid(column = 2, row = 0)


# setting up buttons
arm = Button(text= 'upper bod day', bg='blue', fg = 'violet red', font = FONT, command = arm_function)
arm.grid(row = 1, column = 0)

leg = Button(text= 'lower bod day', bg='white', fg = 'violet red', font = FONT, command = leg_function)
leg.grid(row = 3, column = 0)

four = Button(text= '4 exercises', bg='white', fg = 'violet red', font =  FONT, command = four_function)
four.grid(row = 1, column = 2)

five = Button(text= '5 exercises', bg='white', fg = 'violet red', font =  FONT, command = five_function)
five.grid(row = 2, column = 2)

six = Button(text= '6 exercises', bg='white', fg = 'violet red', font =  FONT, command = six_function)
six.grid(row = 3, column = 2)

you_pick = Button(text= 'you pick', bg='white', fg = 'violet red', font =  FONT, command = you_pick_function)
you_pick.grid(row = 4, column = 2)

generate = Button(text= 'generate', bg='white', fg = 'violet red', font =  FONT, command = workout_plan_function)
generate.grid(row = 5, column = 1)

clear = Button(text= 'clear', bg='white', fg = 'violet red', font =  FONT, command = clear_screen)
clear.grid(row = 7, column = 1)

workout_plan = Text(bg = 'violet red', fg = 'pink')
workout_plan.config(width = 50, height = 15)
workout_plan.grid(row = 6, column = 1)



window.mainloop()