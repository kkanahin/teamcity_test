# -*- encoding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from teamcity import underTeamcity
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from teamcity.unittestpy import TeamcityTestRunner
from pyvirtualdisplay import Display
import unittest



class TestTeamcityMessages(unittest.TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://boutique.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def testPass(self):

        assert 1 == 1

    

#    def testAssertEqual(self):
#
#        self.assertEqual("1", "2")
#
#
#
#    def testAssertEqualMsg(self):
#
#        self.assertEqual("1", "2", "message")

    

#    def testAssert(self):
#
#        self.assert_(False)
#
#
#
#    def testFail(self):
#
#        self.fail("failed")
#
#
#
#    def testException(self):
#
#        raise Exception("some exception")

#    def testUserQuery(self):
#        user = User.objects.all().values_list()
#        print user
#        self.assertEqual('admi',user.username,'message db')

    def test_1(self):
        driver = self.driver
        driver.get(self.base_url + "/new_arrivals/womensclothesandaccesories/e92539ba-648c-11e2-9791-12313b097c2f/#")
        driver.find_element_by_link_text("CACHAREL").click()
        driver.find_element_by_css_selector("#q_2080a28b-436d-11e1-a7d5-0050569500d1 img").click()
        driver.find_element_by_id("add-to-cart").click()
#        driver.find_element_by_id("cart-gobuy").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.display.stop()

if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':

    if underTeamcity():

        runner = TeamcityTestRunner()

    else:

        runner = unittest.TextTestRunner()

    unittest.main(testRunner=runner)