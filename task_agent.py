import os
from dotenv import load_dotenv
from openai import OpenAI 


#load env
load_dotenv()

client = OpenAI()


# read task from file
def readTasks(filePath):
    with open(filePath, "r") as f:
       return f.read()

#make a call to openai with prompt to categories our tasks

def summariseTasks(tasks):
    prompt = f"""
    You are a smart task planning agenet. GIven a list f of tasks categorise them into three
    categories/priorities bucket:
    - High Priority
    - Medium priority
    - Low Priority

    Tasks: 
    {tasks}
    
    Return the response in this format:
    High Priority
        - Task 1
        - Task 2
    Medium Priority
        - Task 1
        - Task 2
    Low Priority
        - Task 1
        - Task 2
"""

    response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)


    return response.choices[0].message.content


if __name__ == "__main__":
    taskText = readTasks("taskfile.txt") 
    summary = summariseTasks(taskText)


    print("\n Task Summary \n")
    print("-" * 30)
    print(summary)
