#!/usr/bin/python3
import os
import aiml
BRAIN_FILE="brain.dump"

k = aiml.Kernel()
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

# Endless loop which passes the input to the bot and prints its response 
try:
    while True:
        input_text = input("Question :>  ")
        if input_text in ["quit","by","byee","bye","close","end","exit"]:
            print("Bot :> Bye")
            exit()
        response = k.respond(input_text)
        print("Bot :>  " + response)
# Delete the dump file 
finally:
    os.remove("brain.dump")