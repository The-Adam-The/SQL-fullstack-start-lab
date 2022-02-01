import pdb 
from models.task import Task
import repositories.task_repository as task_repository  

task_repository.delete_all()

task1 = Task("Go for a run", "Jack Jarvis", 20)
task2 = Task("Eat cake", "Marie Antoinette", 10)

task_repository.save(task1)
task_repository.save(task2)

task1.mark_complete()
task2.mark_complete()

result = task_repository.select_all()

for task in result:
    print(task.__dict__)

pdb.set_trace()