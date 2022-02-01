from db.run_sql import run_sql

from models.task import Task
  
def select_all():  
    tasks = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        task = Task(row['description'], row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks 

# CRUD

#CREATE

def save(task):
    sql = """
    INSERT INTO tasks 
    (description, duration, completed) 
    VALUES 
    (%s, %s, %s, %s)
    RETURNING id
    """
    
    values = [task.description, task.duration, task.completed]
    result = run_sql(sql, values)
    task.id = result[0]['id']

#READ ->

def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None: 
        task = Task(
        #destructuring
        **result # description=result['desciption']
        )


#DELETE ALL

def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

#DELETE ONE
def delete(id):
    sql = "DELETE FROM TASKS WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#UPDATE
#task should be already updated on the python side
def update(task):
    sql = """
    UPDATE tasks
    SET (description, duration, completed)
    = (%s, %s, %s, %s)
    WHERE id = %s
    """
    values = [
        task.description,  
        task.duration, 
        task.completed, 
        task.id
        ]
    run_sql(sql, values)