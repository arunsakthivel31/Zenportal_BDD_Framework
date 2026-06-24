from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://v2.zenclass.in/login"

# Enter your credentials
VALID_USER = "arunsakthivel@outlook.com"
VALID_PASS = "1234567"


@given("User opens Zen Portal")
def step_open(context):
    context.driver.get(URL)


@when("User enters valid username and password")
def step_valid_login(context):
    WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='text']")
        )
    ).send_keys(VALID_USER)

    context.driver.find_element(
        By.XPATH,
        "//input[@type='password']"
    ).send_keys(VALID_PASS)


@when("User enters invalid username and password")
def step_invalid_login(context):
    WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='text']")
        )
    ).send_keys("wrong@gmail.com")

    context.driver.find_element(
        By.XPATH,
        "//input[@type='password']"
    ).send_keys("wrong123")


@when("User clicks login button")
def step_click_login(context):
    context.driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()


@then("Login should be successful")
def step_success(context):
    WebDriverWait(context.driver, 20).until(
        EC.url_changes(URL)
    )

    assert "login" not in context.driver.current_url.lower()


@then("Login should fail")
def step_fail(context):
    assert "login" in context.driver.current_url.lower()


@then("Username textbox should be displayed")
def step_username(context):
    username = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='text']")
        )
    )

    assert username.is_displayed()


@then("Password textbox should be displayed")
def step_password(context):
    password = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='password']")
        )
    )

    assert password.is_displayed()


@then("Login button should be enabled")
def step_button(context):
    button = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    assert button.is_enabled()


@given("User logged into portal")
def step_logged(context):
    context.driver.get(URL)

    WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='text']")
        )
    ).send_keys(VALID_USER)

    context.driver.find_element(
        By.XPATH,
        "//input[@type='password']"
    ).send_keys(VALID_PASS)

    context.driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()

    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body")
        )
    )

# @when("User clicks logout")
# def step_logout(context):
#
#     wait = WebDriverWait(context.driver, 30)
#
#     # Placement Guidance Popup
#     try:
#         placement_close = wait.until(
#             EC.presence_of_element_located(
#                 (By.XPATH,
#                  "//div[contains(@class,'common-popup-close-icon-container')]")
#             )
#         )
#
#         context.driver.execute_script(
#             "arguments[0].click();",
#             placement_close
#         )
#
#         print("Placement popup closed")
#
#     except:
#         print("Placement popup not present")
#
#     # New Launch Alert Popup
#     try:
#         launch_close = WebDriverWait(context.driver, 10).until(
#             EC.element_to_be_clickable(
#                 (
#                     By.XPATH,
#                     "//button[@aria-label='Close popup']"
#                 )
#             )
#         )
#
#         context.driver.execute_script(
#             "arguments[0].click();",
#             launch_close
#         )
#
#         print("Launch popup closed")
#
#     except Exception as e:
#         print("Launch popup not present:", e)
#
#     # Wait until backdrop disappears
#     try:
#         wait.until(
#             EC.invisibility_of_element_located(
#                 (
#                     By.XPATH,
#                     "//div[contains(@class,'MuiBackdrop-root')]"
#                 )
#             )
#         )
#     except:
#         pass
#
#     # Click Avatar
#     avatar = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//img[contains(@class,'MuiAvatar-img')]"
#             )
#         )
#     )
#
#     context.driver.execute_script(
#         "arguments[0].click();",
#         avatar
#     )
#
#     # Click Logout
#     logout = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.XPATH,
#                 "//li[contains(.,'Log out')]"
#             )
#         )
#     )
#
#     context.driver.execute_script(
#         "arguments[0].click();",
#         logout
#     )

@when("User clicks logout")
def step_logout(context):

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    wait = WebDriverWait(context.driver, 30)

    # =====================================
    # Close Placement Guidance Popup
    # =====================================
    try:
        placement_close = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'common-popup-close-icon-container')]"
                )
            )
        )

        context.driver.execute_script(
            "arguments[0].click();",
            placement_close
        )

        print("Placement popup closed")

    except Exception:
        print("Placement popup not present")

    # =====================================
    # Close New Launch Alert Popup
    # =====================================
    try:
        launch_close = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@aria-label='Close popup']"
                )
            )
        )

        context.driver.execute_script(
            "arguments[0].click();",
            launch_close
        )

        print("Launch popup closed")

    except Exception:
        print("Launch popup not present")

    # =====================================
    # Wait for backdrop disappear
    # =====================================
    try:
        wait.until(
            EC.invisibility_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'MuiBackdrop-root')]"
                )
            )
        )
    except:
        pass

    time.sleep(2)

    # =====================================
    # Click Avatar
    # =====================================
    avatar = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@class,'MuiAvatar-img')]"
            )
        )
    )

    context.driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        avatar
    )

    context.driver.execute_script(
        "arguments[0].click();",
        avatar
    )

    print("Avatar clicked")

    time.sleep(3)

    # =====================================
    # Click Logout
    # =====================================
    logout_xpath = (
        "//*[contains(text(),'Log out') "
        "or contains(text(),'Logout') "
        "or contains(text(),'Sign Out')]"
    )

    logout = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, logout_xpath)
        )
    )

    context.driver.execute_script(
        "arguments[0].click();",
        logout
    )

    print("Logout clicked")

@then("User should logout successfully")
def step_logout_success(context):
    WebDriverWait(context.driver, 20).until(
        EC.url_contains("login")
    )

    assert "login" in context.driver.current_url.lower()
