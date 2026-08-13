# test_hubomega.py
"""
Tests for HubOmega module.
"""

import unittest
from hubomega import HubOmega

class TestHubOmega(unittest.TestCase):
    """Test cases for HubOmega class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HubOmega()
        self.assertIsInstance(instance, HubOmega)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HubOmega()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
