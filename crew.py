# crew.py
from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# Create the Crew instance
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

def run_crew(task_type, topic):
    # Determine the task and its description
    if task_type == 'research':
        task = research_task
        inputs = {'topic': topic}
    elif task_type == 'write':
        task = write_task
        inputs = {'topic': topic}
    else:
        return "Invalid task type selected."
    
    # Execute the task using the Crew instance
    result = crew.kickoff(inputs=inputs)
    
    # Output handling
    if task_type == 'write' and task.output_file:
        # Read the content of the output file
        with open(task.output_file, 'r') as file:
            result = file.read()
    
    return result
