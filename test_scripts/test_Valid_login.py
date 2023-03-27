import pytest

from generic.base_setup import BaseSetup
from pages.loginpage import LoginPage
from pages.enter_time_track import EnterTimeTrackPage
from generic.excel import Excel

class TestValidLogin(BaseSetup):

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un=Excel.get_data( self.xl_path,"TestValidLogin",2,1)
        pw=Excel.get_data( self.xl_path,"TestValidLogin",2,2)
        # 1. Enter Valid UN
        loginpage = LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. Enter Valid PW
        loginpage.set_password(pw)
        # 3. Click on login Button
        loginpage.click_loginbutton()
        # 4. Verify that Home page is Displayed
        ett_page=EnterTimeTrackPage(self.driver)
        displayed=ett_page.verify_home_page_is_displayed(self.wait)
        assert displayed
        print('THE END')

