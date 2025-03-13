import pytest
from ci_with_python import User

def test_user() -> None:
  user = User('Matheus', 19)

  assert user.name is 'Matheus'
  assert user.age is 19

  user.name = 'João'
 
  assert user.name is 'João'
  assert user.age is 19

# Expect a failure
@pytest.mark.xfail
def test_divide_by_zero():
  assert 1 / 0 is 1

# Skip test
@pytest.mark.skip(reason="Not implemented yet")
def test_user_field_validations():
  with pytest.raises(Exception) as e_info:
    User('', -1)

# Test with multiple parameters
@pytest.mark.parametrize("test_input,expected", [
  ({'name': 'Matheus', 'age': 19}, 19),
  ({'name': 'João', 'age': 38}, 38),
  ({'name': 'Ana', 'age': 19}, 19),
  ({'name': 'Leonardo', 'age': 20}, 20),
  ({'name': 'Alexandre', 'age': 39}, 39),
])
def test_multiple_user_creations(test_input, expected):
  assert User(test_input['name'], test_input['age']).age is expected
