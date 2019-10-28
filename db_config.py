from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///student_info.db?check_same_thread=False', echo=True)

Base = declarative_base()


class StudentInfo(Base):
    __tablename__ = 'student_info'

    student_id = Column(String(15), primary_key=True)
    student_name = Column(String(30), nullable=False)
    id_number = Column(String(20), unique=True, nullable=False)
    is_wireless_password_unmodified = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return "<StudentInfo(student_id='%s',student_name='%s',id_number='%s',is_wireless_password_unmodified='%s')>" % (
            self.student_id, self.student_name, self.id_number, self.is_wireless_password_unmodified)


Session = sessionmaker(bind=engine)


def add_student_info(student_info):
    session = Session()
    session.add(student_info)
    session.commit()
    session.close()


def query_password_unmodified_student_info_list():
    session = Session()
    student_info_list = session.query(StudentInfo).filter(StudentInfo.is_wireless_password_unmodified == True).all()
    session.close()
    return student_info_list


def update_student_info(student_id):
    session = Session()
    student_info = session.query(StudentInfo).filter_by(student_id=student_id).first()
    student_info.is_wireless_password_unmodified = not student_info.is_wireless_password_unmodified
    session.commit()
