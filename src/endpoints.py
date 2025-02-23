from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.schemas import (
    UserCreate, UserResponse, 
    CompanyCreate, CompanyResponse,
    TodoListCreate, TodoListResponse,
    TaskCreate, TaskResponse
)
from src.crud import (
    create_user, get_users, 
    create_company, get_companies, 
    create_todo_list, get_todo_lists, get_todo_lists_by_user, 
    create_task, get_tasks, get_tasks_by_todo_list
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/companies", response_model=CompanyResponse)
def add_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return create_company(db, company)

@router.get("/companies", response_model=list[CompanyResponse])
def list_companies(db: Session = Depends(get_db)):
    return get_companies(db)

@router.post("/users", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/todo_lists", response_model=TodoListResponse)
def add_todo_list(todo_list: TodoListCreate, db: Session = Depends(get_db)):
    return create_todo_list(db, todo_list)

@router.get("/todo_lists", response_model=list[TodoListResponse])
def list_todo_lists(db: Session = Depends(get_db)):
    return get_todo_lists(db)

@router.get("/users/{user_id}/todo_lists", response_model=list[TodoListResponse])
def list_todo_lists_by_user(user_id: int, db: Session = Depends(get_db)):
    return get_todo_lists_by_user(db, user_id)

@router.post("/tasks", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.get("/todo_lists/{todo_list_id}/tasks", response_model=list[TaskResponse])
def list_tasks_by_todo_list(todo_list_id: int, db: Session = Depends(get_db)):
    return get_tasks_by_todo_list(db, todo_list_id)