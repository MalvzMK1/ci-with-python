from ci_with_python import User

def test_user() -> None:
  user = User('Matheus', 19)

  assert user.name is 'Matheus'
  assert user.age is 19

  user.name = 'João'

  assert user.name is 'João'
  assert user.age is 19
