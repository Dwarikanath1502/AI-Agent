import os
from dotenv import load_dotenv
from openai import OpenAI 


#load env
load_dotenv()

client = OpenAI()


# read task from file
def readTasks(filePath):
    with open(filePath, "r") as f:
        f.read()

#make a call to openai with prompt to categories our tasks

def summeriseTasks(tasks):
    prompt = f""" My Prompt"""

    client.chat.completions.create(
        model = ""
    )