
import unittest

from tests.test_car_insurance import TestCarInsurance
from tests.testHelper import TestHelper

from tests.health_suite import health_suite

from tests.test_home_insurance import TestHomePredict
from tests.test_home_insurance2 import TestHomeData

def suite():
    test_suite = unittest.TestSuite()
    
    test_suite.addTest(unittest.makeSuite(TestCarInsurance))
    test_suite.addTest(unittest.makeSuite(TestHelper))
    
    test_suite.addTest(health_suite())
	
    test_suite.addTest(unittest.makeSuite(TestHomePredict))
    test_suite.addTest(unittest.makeSuite(TestHomeData))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
