def projects_list_key(user_id: int) -> str:
    return f"projects:list:user:{user_id}"

def tasks_list_key(project_id: int, user_id: int) -> str:
    return f"tasks:list:project:{project_id}:user:{user_id}"
