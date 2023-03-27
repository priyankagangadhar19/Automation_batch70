import pytest

from generic.base_setup import BaseSetup
from generic.excel import Excel
from pages.loginpage import LoginPage

class TestInvalidLogin(BaseSetup):
    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        un=Excel.get_data( self.xl_path,"TestInvalidLogin",2,1)
        pw=Excel.get_data( self.xl_path,"TestInvalidLogin",2,2)

        # 1. enter invalid un
        loginpage=LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. enter invalid pw
        loginpage.set_password(pw)
        # 3. click on login button
        loginpage.click_loginbutton()
        # 4. verify that err msg is displayed
        displayed=loginpage.verify_err_msg_is_displayed(self.wait)
        assert displayed
