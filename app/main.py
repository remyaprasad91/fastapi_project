
from fastapi import FastAPI,Response,HTTPException,status, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models,schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)



app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



while True:
    try:
        conn =psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='remyap@1', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connected successfully!")
        break
    except Exception as error:
        print("Connectin to database failed")
        print("Error:", error)
        time.sleep(2)

my_posts = [{"title":"title of post 1","content":"content of post 1","id": 1},
{"title":"favourite food","content":"I like burger","id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"]== id:
            return p
        

def find_index_posts(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
            


@app.get("/")
def root():
    return {"message": "Welcome Puttuuuu"}


@app.get("/posts",response_model=List[schemas.Post])
def get_post(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts= cursor.fetchall()
    posts=db.query(models.Post).all()
    return posts

@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) Returning * """,(post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # print(new_post)
    # conn.commit()
    
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}",response_model=schemas.Post)
def get_posts(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id= %s """, (str( id)))
    # post = cursor.fetchone()
    post=db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"post with {id} was not found")
    return  post

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id :int,db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id= %s RETURNING * """, (str( id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post=db.query(models.Post).filter(models.Post.id == id)

    if post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"post with {id} was not found") 
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE  id = %s RETURNING * """, (Post.title,Post.content,Post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"post with {id} was not found")
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()