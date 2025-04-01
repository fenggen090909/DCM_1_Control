from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

Base = declarative_base()

class Parameters(Base):
    __tablename__ = "crawler_parameters"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    crawler_name = Column(String(100))
    parameter_key = Column(String(100))
    parameter_value = Column(String(200))
    parameter_type = Column(String(50))

    def __repr__(self):
        return f"<Parameters(crawler_name='{self.crawler_name}')>"


class Question(Base):
    __tablename__ = "stackoverflow_questions"
    
    question_id = Column(String(30), primary_key=True)
    tag1 = Column(String(1), default=0)
    title = Column(String(150), default="")

    task_id_p = Column(UUID(as_uuid=True), nullable=True)
    spider_p = Column(String(30), nullable=True)
    ip_p  = Column(String(45), nullable=True)
    docker_id_p = Column(String(64), nullable=True)    
    worker_id_p = Column(String(64), nullable=True) 
    time_p = Column(DateTime, nullable=True) 

    task_id_c = Column(UUID(as_uuid=True), nullable=True)
    spider_c = Column(String(30), nullable=True)
    ip_c  = Column(String(45), nullable=True)
    docker_id_c = Column(String(64), nullable=True)    
    worker_id_c = Column(String(64), nullable=True) 
    time_c = Column(DateTime, nullable=True)       

    def __repr__(self):
        return f"<Question(title='{self.title}')>"


class Competition(Base):
    __tablename__ = "competition_list"

    id = Column(Integer, primary_key=True)   
    tag1 =  Column(String(1), default="0")
    name = Column(String(200), default="")

    task_id_p = Column(UUID(as_uuid=True), nullable=True)
    spider_p = Column(String(30), nullable=True)
    ip_p  = Column(String(45), nullable=True)
    docker_id_p = Column(String(64), nullable=True)    
    worker_id_p = Column(String(64), nullable=True) 
    time_p = Column(DateTime, nullable=True) 

    task_id_c = Column(UUID(as_uuid=True), nullable=True)
    spider_c = Column(String(30), nullable=True)
    ip_c  = Column(String(45), nullable=True)
    docker_id_c = Column(String(64), nullable=True)    
    worker_id_c = Column(String(64), nullable=True) 
    time_c = Column(DateTime, nullable=True)       

    def __repr__(self):
        return f"<Competition(name='{self.name}')>"


class Dataset(Base):
    __tablename__ = "dataset_list"

    id = Column(Integer, primary_key=True)    
    url = Column(String(200), default="")
    tag1 =  Column(String(1), default="0")

    task_id_p = Column(UUID(as_uuid=True), nullable=True)
    spider_p = Column(String(30), nullable=True)
    ip_p  = Column(String(45), nullable=True)
    docker_id_p = Column(String(64), nullable=True)    
    worker_id_p = Column(String(64), nullable=True) 
    time_p = Column(DateTime, nullable=True) 

    task_id_c = Column(UUID(as_uuid=True), nullable=True)
    spider_c = Column(String(30), nullable=True)
    ip_c  = Column(String(45), nullable=True)
    docker_id_c = Column(String(64), nullable=True)    
    worker_id_c = Column(String(64), nullable=True) 
    time_c = Column(DateTime, nullable=True)       

    def __repr__(self):
        return f"<Dataset(url='{self.url}')>"


class Kernel(Base):
    __tablename__ = "kernel_list"

    id = Column(Integer, primary_key=True)    
    competitionId = Column(Integer)
    kernelId = Column(Integer)
    tag1 =  Column(String(1), default="0")

    task_id_p = Column(UUID(as_uuid=True), nullable=True)
    spider_p = Column(String(30), nullable=True)
    ip_p  = Column(String(45), nullable=True)
    docker_id_p = Column(String(64), nullable=True)    
    worker_id_p = Column(String(64), nullable=True) 
    time_p = Column(DateTime, nullable=True) 

    task_id_c = Column(UUID(as_uuid=True), nullable=True)
    spider_c = Column(String(30), nullable=True)
    ip_c  = Column(String(45), nullable=True)
    docker_id_c = Column(String(64), nullable=True)    
    worker_id_c = Column(String(64), nullable=True) 
    time_c = Column(DateTime, nullable=True)       

    def __repr__(self):
        return f"<Dataset(id='{self.id}')>"