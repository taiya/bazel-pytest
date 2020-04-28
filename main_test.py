"Testing stuff."
import sys
import pytest

def test_dryrun():
  sys.argv = ["train.py", "--dryrun"]
  import main  # pylint: disable=import-outside-toplevel
  print(main.foo)

def test_something():
  assert True

if __name__ == "__main__":
  sys.exit(pytest.main([__file__]))
