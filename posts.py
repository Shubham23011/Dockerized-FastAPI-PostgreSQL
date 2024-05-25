from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
import models
import Schema
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get('/', response_model=List[Schema.CreatePost])
def test_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()

    return post


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[Schema.CreatePost])
def create_posts(post_create: Schema.CreatePost, db: Session = Depends(get_db)):
    new_post = models.Post(**post_create.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]