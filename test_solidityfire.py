# test_solidityfire.py
"""
Tests for SolidityFire module.
"""

import unittest
from solidityfire import SolidityFire

class TestSolidityFire(unittest.TestCase):
    """Test cases for SolidityFire class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityFire()
        self.assertIsInstance(instance, SolidityFire)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityFire()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
