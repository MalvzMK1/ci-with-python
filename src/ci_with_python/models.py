class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class CourseClass:
  def __init__(self, teacher: User) -> None:
    self.teacher = teacher
    self.__students: list[User] = []
  
  @property
  def students(self) -> list[User]:
    return self.__students
  
  def add_student(self, student: User) -> None:
    self.__students.append(student)
  
  def remove_student_by_idx(self, idx: int) -> None:
    for i, student in enumerate(self.__students):
      if i == idx:
        self.__students.remove(student)

        return
