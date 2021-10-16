#!/bin/sh

import Tkinter as tk
import datetime
import time
import os

window = tk.Tk()
window.geometry("200x400")

day_var = tk.IntVar()
month_var = tk.IntVar()
year_var = tk.IntVar()
hours_var = tk.IntVar()
minutes_var = tk.IntVar()

def create_alarm(window_text):
    alarm_window = tk.Tk()
    alarm_window.geometry("50x50")
    alarm_text = tk.Label(alarm_window, text=window_text)
    alarm_text.pack()
    
    duration = 1
    frequency = 440
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, frequency))

    return

def today():
    day = day_var.get()
    month = month_var.get()
    year = year_var.get()
    
    current_time = datetime.datetime.now()
    
    if day == current_time.day and month == current_time.month and year == current_time.year:
        return True

    return False

def now():
    hours = hours_var.get()
    minutes = minutes_var.get()
    
    current_time = datetime.datetime.now()
    
    if hours == current_time.hour and minutes == current_time.minute:
        return True

    return False

def submit():
    hours = hours_var.get()
    minutes = minutes_var.get()

    while True:

        if today() and now(): 
            print("now matching")
            create_alarm("Alarm!")
            break

    hours_var.set("")
    minutes_var.set("")

day_label = tk.Label(window, text="Day")
day_entry = tk.Entry(window, textvariable=day_var)

month_label = tk.Label(window, text="Month")
month_entry = tk.Entry(window, textvariable=month_var)

year_label = tk.Label(window, text="Year")
year_entry = tk.Entry(window, textvariable=year_var)

hours_label = tk.Label(window, text="Hours")
hours_entry = tk.Entry(window, textvariable=hours_var)

minutes_label = tk.Label(window, text="Minutes")
minutes_entry = tk.Entry(window, textvariable=minutes_var)

submit_button = tk.Button(window, text="Submit", command=submit)

day_label.grid(row=0, column=0)
day_entry.grid(row=0, column=1)
month_label.grid(row=1, column=0)
month_entry.grid(row=1, column=1)
year_label.grid(row=2, column=0)
year_entry.grid(row=2, column=1)
hours_label.grid(row=3, column=0)
hours_entry.grid(row=3, column=1)
minutes_label.grid(row=4, column=0)
minutes_entry.grid(row=4, column=1)
submit_button.grid(row=5, column=1)

window.mainloop()
