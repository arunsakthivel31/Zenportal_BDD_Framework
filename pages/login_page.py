from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "YOUR_ZEN_PORTAL_URL"

    USERNAME = (By.XPATH, "//input[@type='text']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    PROFILE = (
        By.CSS_SELECTOR,
        "img.MuiAvatar-img"
    )

    LOGOUT = (
        By.XPATH,
        "//*[contains(text(),'Logout')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_portal(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.LOGIN_BTN
            )
        ).click()

    def is_username_displayed(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        ).is_displayed()

    def is_password_displayed(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        ).is_displayed()

    def is_login_enabled(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.LOGIN_BTN
            )
        ).is_enabled()

    def logout(self):

        avatar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.PROFILE
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            avatar
        )

        logout = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.LOGOUT
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout
        )