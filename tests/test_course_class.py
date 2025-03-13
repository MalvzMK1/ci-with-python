from ci_with_python import CourseClass, User

def test_course_class() -> None:
  teacher = User('Caio', 32)
  course_class = CourseClass(teacher)

  assert course_class.teacher is teacher
  assert course_class.students.__len__() is 0

  student = User('Matheus', 19)

  course_class.add_student(student)

  assert course_class.students.__len__() is 1
  assert course_class.students[0] is student

  course_class.remove_student_by_idx(0)

  assert course_class.students.__len__() is 0