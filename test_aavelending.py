# test_aavelending.py
"""
Tests for AaveLending module.
"""

import unittest
from aavelending import AaveLending

class TestAaveLending(unittest.TestCase):
    """Test cases for AaveLending class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AaveLending()
        self.assertIsInstance(instance, AaveLending)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AaveLending()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
