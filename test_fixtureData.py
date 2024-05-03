import pytest

from BaseTest import BaseTest

pytest.mark.usefixtures("dataload")
class Testexample2(BaseTest):


    def test_editProfile(self,dataload):
       log = self.getloggerfunction()
       log.info(dataload)
       log.info(dataload[0])
       log.info(dataload[1])
       log.info(dataload[2])
       # print(dataload)
       # print(dataload[0])
       # print(dataload[1])
       # print(dataload[2])
