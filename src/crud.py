from sqlalchemy.orm import Session
from src.models import User, Company, TodoList, Task
from src.schemas import (
    UserCreate, CompanyCreate, TodoListCreate, TaskCreate
)

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(name=company.name)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_companies(db: Session):
    return db.query(Company).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, company_id=user.company_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def create_todo_list(db: Session, todo_list: TodoListCreate):
    db_todo_list = TodoList(title=todo_list.title, user_id=todo_list.user_id)
    db.add(db_todo_list)
    db.commit()
    db.refresh(db_todo_list)
    return db_todo_list

def get_todo_lists(db: Session):
    return db.query(TodoList).all()

def get_todo_lists_by_user(db: Session, user_id: int):
    return db.query(TodoList).filter(TodoList.user_id == user_id).all()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        description=task.description, 
        completed=task.completed, 
        todo_list_id=task.todo_list_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_tasks_by_todo_list(db: Session, todo_list_id: int):
    return db.query(Task).filter(Task.todo_list_id == todo_list_id).all()