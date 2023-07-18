from tasks import Task

def test_can_call_endpoint():
    task = Task()
    response = task.get_task()
    assert response.status_code == 200
    
def test_can_create_task():
    try:
        task = Task()

        payload = task.new_task_payload()
        create_task_response = task.create_task(payload)
        assert create_task_response.status_code == 200

        data = create_task_response.json()
        print(data)

        task_id = data['task']['task_id']
        get_task_response = task.get_task_id(task_id)

        assert get_task_response.status_code == 200
        get_task_json = get_task_response.json()
        assert get_task_json['content'] == payload['content']
        assert get_task_json['user_id'] == payload['user_id']

    except Exception as ex:
        print(ex)

def test_can_update_task():
    task = Task()
    #Create a task
    payload = task.new_task_payload()
    create_task_response = task.create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']
    #Update the task
    new_payload = {
        "content": "new user content",
        "user_id": payload['user_id'],
        "task_id": task_id,
        "is_done": True
    }
    update_task_response = task.update_task(new_payload)
    assert update_task_response.status_code == 200
    #Get and validate the changes
    get_task_response = task.get_task_id(task_id)
    assert update_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']

def test_can_list_tasks():
    task = Task()
    #Create N tasks
    n = 3 
    payload = task.new_task_payload()
    for _ in range(n):
        create_task_response = task.create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload['user_id']
    list_task_response = task.list_task(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data['tasks']
    assert len(tasks) == n
    print(data)
    
def test_can_delete_task():
    task = Task()
    #create a task
    payload = task.new_task_payload()
    create_task_response = task.create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']
    #delete the task
    delete_task_response = task.delete_task(task_id)
    assert delete_task_response.status_code == 200
    #get the task and check that its not found
    get_tast_response = task.get_task_id(task_id)
    assert get_tast_response.status_code == 404
    pass
        