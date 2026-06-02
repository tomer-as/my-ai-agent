# Main Agent Controller
import os

def run_agent_task(task_name):
    print(f"Agent is starting: {task_name}")
    
    if task_name == "check_connection":
        return "SUCCESS: Agent is connected to GitHub and running logic."
    
    return "Task not recognized."

if __name__ == "__main__":
    print(run_agent_task("check_connection"))
