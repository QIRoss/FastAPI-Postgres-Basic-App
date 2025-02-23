from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class CompanyBase(BaseModel):
    name: str

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UserBase(BaseModel):
    name: str
    company_id: int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TodoListBase(BaseModel):
    title: str
    user_id: int

class TodoListCreate(TodoListBase):
    pass

class TodoListResponse(TodoListBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TaskBase(BaseModel):
    description: str
    completed: bool = False
    todo_list_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TodoListWithTasks(TodoListResponse):
    tasks: List[TaskResponse] = []

class UserWithTodoLists(UserResponse):
    todo_lists: List[TodoListResponse] = []
