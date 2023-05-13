import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test main class of this application"""

    def test_int(self):
        base = BaseModel()
        base.name = "Mohammed"
        base.age = 22
        self.assertEqual(base.name, "Mohammed")


if __name__ == "__main__":
    unittest.main()
