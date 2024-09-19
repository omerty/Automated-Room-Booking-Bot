from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://booking.carleton.ca/index.php")

try:
    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "spanLogin"))
    )

    login_button.click()
    

    #Login Logic 
    try:
        email_field = wait = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.NAME, "txtUsername"))
        ).send_keys("omerMohiuddin")
        password_field = wait = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.NAME, "txtPassword"))
        ).send_keys("mahnazNoon!11")
        login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnLogin"))
        )
        login_button.click()
    except Exception as e:
        print(f"error: {e}")
    

    #Booking Logic
    try:
        Book_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Find a Room']"))
        )
        Book_button.click()

        dropdown = Select(driver.find_element(By.ID, 'cboRequestType'))
        dropdown.select_by_index(1)
        time.sleep(2)
        dropdown2 = Select(driver.find_element(By.ID, 'cboDuration'))
        dropdown2.select_by_index(5)
        dropdown3 = Select(driver.find_element(By.ID, 'cboStartTime'))
        dropdown3.select_by_index(26)
        dropdown4 = Select(driver.find_element(By.ID, 'cboEndTime'))
        dropdown4.select_by_index(31)
        continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnAnyDate"))
        )
        continue_button.click()

        calender_cells = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dayCell"))
)

        for cell in calender_cells:
            day_number = cell.find_element(By.CSS_SELECTOR, "div").text

            # Check if the day is unavailable
            if "dayUnavailable" in cell.get_attribute("class"):
                print(f"Day {day_number} is unavailable")

            # Check if the day is available
            elif "dayAvailable" in cell.get_attribute("class"):
                print(f"Day {day_number} is available")

                try:
                    # Wait until the element is clickable
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable(cell)
                    )
                    cell.click()
                    print(f"Clicked on day {day_number}")
                    break  # Break after clicking on the first available day
                except Exception as e:
                    print(f"Error clicking on day {day_number}: {e}")

            else:
                print(f"Day {day_number} is either past or today")
            

        room_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ClickableRow"))
        )

        for row in room_rows:
            building = row.find_element(By.XPATH, ".//td[1]").text
            room_number = row.find_element(By.XPATH, ".//td[3]").text
            print(f"Found room: {building} {room_number}")
            row.click()
            print(f"Clicked on room {room_number}")
            break

        try:
            Book_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnOK"))
                )
            Book_button.click()
            Button_1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnConfirm"))
                )
            Button_1.click()
            Button_2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnOK"))
                )
            Button_2.click()

        except Exception as e:
            print(f"error: {e}")

    except Exception as e:
        print(f"error: {e}")


except Exception as e:
    print(f"Error: {e}")

time.sleep(45)
driver.quit()
