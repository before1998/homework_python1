import pytest
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Настройка подключения
# (ЗАМЕНИ myuser, mypassword, mydatabase на свои реальные данные!)
DATABASE_URL = (
    "postgresql+psycopg2://postgres:Skypro12345@localhost:5432/school"
)
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()


# 2. Описание модели (адаптируй поля под свою таблицу students)
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    is_deleted = Column(Boolean, default=False)


# 3. Фикстура для сессии БД
@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()
    yield session
    session.rollback()  # Откатываем транзакции
    session.close()


# 4. Фикстура для очистки данных (гарантирует стабильность тестов)
@pytest.fixture(scope="function")
def cleanup_students(db_session):
    created_ids = []
    yield created_ids
    # Teardown: удаляем созданные записи физически
    if created_ids:
        db_session.query(Student)\
            .filter(Student.id.in_(created_ids))\
            .delete(synchronize_session=False)
        db_session.commit()


# 5. Тесты
def test_add_student(db_session, cleanup_students):
    """Тест на добавление студента"""
    new_student = Student(name="Тестовый Студент", age=20)
    db_session.add(new_student)
    db_session.commit()

    # Добавляем ID в список для последующей очистки
    cleanup_students.append(new_student.id)

    # Проверка
    assert new_student.id is not None
    assert new_student.name == "Тестовый Студент"


def test_update_student(db_session, cleanup_students):
    """Тест на изменение студента"""
    # Создаем тестовые данные
    new_student = Student(name="Студент до изм.", age=19)
    db_session.add(new_student)
    db_session.commit()
    cleanup_students.append(new_student.id)

    # Изменяем данные
    student_to_update = db_session.query(Student)\
        .filter_by(id=new_student.id)\
        .first()
    student_to_update.name = "Студент после изменения"
    student_to_update.age = 21
    db_session.commit()

    # Проверка
    updated_student = db_session.query(Student)\
        .filter_by(id=new_student.id)\
        .first()
    assert updated_student.name == "Студент после изменения"
    assert updated_student.age == 21


def test_delete_student_soft(db_session, cleanup_students):
    """Тест на удаление студента (демонстрация Soft Delete)"""
    # Создаем тестовые данные
    new_student = Student(name="Студент для удаления", age=22)
    db_session.add(new_student)
    db_session.commit()
    student_id = new_student.id
    cleanup_students.append(student_id)

    # Выполняем Soft Delete
    student_to_delete = db_session.query(Student)\
        .filter_by(id=student_id)\
        .first()
    student_to_delete.is_deleted = True
    db_session.commit()

    # Проверка: запись существует, но помечена как удаленная
    deleted_student = db_session.query(Student)\
        .filter_by(id=student_id)\
        .first()
    assert deleted_student is not None
    assert deleted_student.is_deleted is True
