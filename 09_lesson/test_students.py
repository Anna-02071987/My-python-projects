from db.models import Student

def test_create_student(db_session):
    """Тест создания студента"""
    # 1. Создаём студента
    student = Student(email="test_student@example.com")
    db_session.add(student)
    db_session.commit()
    
    # 2. Проверяем, что студент появился в БД
    saved_student = (
        db_session.query(Student)
        .filter_by(email="test_student@example.com")
        .one()
    )
    
    assert saved_student.email == "test_student@example.com"
    assert saved_student.deleted_at is None
    
    # 3. Удаляем за собой данные
    db_session.delete(saved_student)
    db_session.commit()

def test_update_student_email(db_session):
    """Тест обновления email студента"""
    # 1. Создаём студента
    student = Student(email="old_email@example.com")
    db_session.add(student)
    db_session.commit()
    
    # 2. Меняем email
    student.email = "new_email@example.com"
    db_session.commit()
    
    # 3. Проверяем, что email обновился
    updated_student = db_session.query(Student).filter_by(id=student.id).one()
    assert updated_student.email == "new_email@example.com"
    
    # 4. Удаляем за собой данные
    db_session.delete(updated_student)
    db_session.commit()

def test_soft_delete_student(db_session):
    """Тест мягкого удаления студента"""
    # 1. Создаём студента
    student = Student(email="delete_me@example.com")
    db_session.add(student)
    db_session.commit()
    
    # 2. Мягко удаляем
    student.soft_delete()
    db_session.commit()
    
    # 3. Проверяем, что студент помечен как удалённый
    deleted_student = db_session.query(Student).filter_by(id=student.id).one()
    assert deleted_student.deleted_at is not None
    
    # 4. Удаляем за собой данные (физически)
    db_session.delete(deleted_student)
    db_session.commit()