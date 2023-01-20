import unittest

from src.thecodingsociety import valid

class TestParse(unittest.TestCase):
    def test_correct_rollno(self):
        self.assertTrue(valid('2021PECCB901'))
        self.assertTrue(valid('2021PECCB012'))
        self.assertTrue(valid('2021PECCB123'))
        self.assertTrue(valid('2021PECCB234'))
        self.assertTrue(valid('2021PECCB345'))
        self.assertTrue(valid('2021PECCB456'))
        self.assertTrue(valid('2021PECCB567'))
        self.assertTrue(valid('2021PECCB678'))
        self.assertTrue(valid('2021PECCB789'))
        self.assertTrue(valid('2021PECCB890'))

    def test_correct_dept(self):
        self.assertTrue(valid('2021PECCB000'))
        self.assertTrue(valid('2021PECCS000'))
        self.assertTrue(valid('2021PECIT000'))
        self.assertTrue(valid('2021PECEC000'))
        self.assertTrue(valid('2021PECEE000'))
        self.assertTrue(valid('2021PECCE000'))
        self.assertTrue(valid('2021PECME000'))
        self.assertTrue(valid('2021PECAD000'))

    def test_correct_year(self):
        self.assertTrue(valid('2018PECCB000'))
        self.assertTrue(valid('2019PECCB000'))
        self.assertTrue(valid('2020PECCB000'))
        self.assertTrue(valid('2021PECCB000'))
        self.assertTrue(valid('2022PECCB000'))
        self.assertTrue(valid('2023PECCB000'))
        self.assertTrue(valid('2024PECCB000'))
        self.assertTrue(valid('2025PECCB000'))
        self.assertTrue(valid('2026PECCB000'))
        self.assertTrue(valid('2027PECCB000'))
        self.assertTrue(valid('2028PECCB000'))
        self.assertTrue(valid('2029PECCB000'))
        self.assertTrue(valid('2030PECCB000'))

    def test_lettercase(self):
        self.assertTrue(valid('2021peccb000'))
        self.assertTrue(valid('2021PECCB000'))
        self.assertTrue(valid('2021PeCcB000'))
        self.assertTrue(valid('2021pEcCb000'))

    def test_invalid_rollno(self):
        self.assertFalse(valid('2021PECCB00'))
        self.assertFalse(valid('2021PECCB0000'))
        self.assertFalse(valid('2021PECCB00000'))
        self.assertFalse(valid('2021PECCB000000'))
        self.assertFalse(valid('2021PECCB0000000'))
        self.assertFalse(valid('2021PECCBXXX'))
        self.assertFalse(valid('2021PECCB000X'))
        self.assertFalse(valid('2021PECB00X0'))
        self.assertFalse(valid('2021PECB00X0'))
    
    def test_invalid_dept(self):
        self.assertFalse(valid('2021PEC11000'))
        self.assertFalse(valid('2021PEC22000'))
        self.assertFalse(valid('2021PEC33000'))
        self.assertFalse(valid('2021PEC44000'))
        self.assertFalse(valid('2021PEC55000'))
        self.assertFalse(valid('2021PEC66000'))
        self.assertFalse(valid('2021PEC000'))
        self.assertFalse(valid('2021PEC0B000'))
        self.assertFalse(valid('2021PEC1B000'))
        self.assertFalse(valid('2021PEC2B000'))
        self.assertFalse(valid('2021PEC3B000'))
        self.assertFalse(valid('2021PEC4B000'))
        self.assertFalse(valid('2021PEC5B000'))
        self.assertFalse(valid('2021PEC6B000'))
        self.assertFalse(valid('2021PEC7B000'))
        self.assertFalse(valid('2021PEC8B000'))
        self.assertFalse(valid('2021PEC9B000'))

    def test_invalid_year(self):
        self.assertFalse(valid('2007PECCB000'))
        self.assertFalse(valid('2008PECCB000'))
        self.assertFalse(valid('2009PECCB000'))
        self.assertFalse(valid('2000PECCB000'))
        self.assertFalse(valid('1000PECCB000'))
        self.assertFalse(valid('0000PECCB000'))
        self.assertFalse(valid('0009PECCB000'))
        self.assertFalse(valid('9900PECCB000'))
        self.assertFalse(valid('9999PECCB000'))

    def test_pec(self):
        self.assertFalse(valid('2021PITCB000'))
        self.assertFalse(valid('2021PITCB000'))
        self.assertFalse(valid('2021PCECB000'))
        self.assertFalse(valid('2021BECCB000'))
        self.assertFalse(valid('2021EPCCB000'))
        self.assertFalse(valid('2021MECCB000'))
        self.assertFalse(valid('2021CECCB000'))
        self.assertFalse(valid('2021EECCB000'))
        self.assertFalse(valid('2021PEXCB000'))
        
        
        
if __name__ == '__main__':
    unittest.main()
