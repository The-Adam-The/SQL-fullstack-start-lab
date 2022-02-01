import pdb 
from models.task import Task
from models.user import User

import repositories.task_repository as task_repository
import repositories.user_repository as user_respository

user_respository.delete_all()
task_repository.delete_all()

user_1 = User("Jack", "Jarvis")
user_respository.save(user_1)

user_2 = User("Victor", "McDade")
user_respository.save(user_2)

users = user_respository.select_all()

task = Task("Walk the dog", user_1, 60)
task_repository.save(task)

tasks_of_user_1 = task_repository.task_for_user(user_1)

print(tasks_of_user_1[0].description)


# for user in users:
#     print(user.__dict__)

# for task in result:
#     print(task.__dict__)

pdb.set_trace()