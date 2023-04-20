from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from stem.control import Controller
from stem import Signal
import random
import time

def fill_form(complaint, link):
    # Set up the browser with options to clear cache and cookies
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.cache.disk.enable", False)
    options.set_preference("browser.cache.memory.enable", False)
    options.set_preference("browser.cache.offline.enable", False)
    options.set_preference("network.cookie.cookieBehavior", 2)

    # Create the browser object with the configured options
    driver = webdriver.Firefox(options=options)

    # Navigate to the provided link
    driver.get(link)

    # Wait for the page to load completely
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "Textbox-1")))

    # Fill in the form fields with the provided input values
    driver.find_element(By.ID, "Textbox-1").send_keys(complaint.first_name)
    driver.find_element(By.ID, "Textbox-2").send_keys(complaint.surname)
    driver.find_element(By.ID, "Textbox-3").send_keys(complaint.address)
    Select(driver.find_element(By.ID, "Dropdown-1")).select_by_value(complaint.state_abbrev)
    driver.find_element(By.ID, "Textbox-4").send_keys(complaint.city)
    driver.find_element(By.ID, "Textbox-5").send_keys(complaint.zip_code)
    driver.find_element(By.ID, "Textarea-1").send_keys(complaint.details)
    driver.find_element(By.ID, "Textbox-6").send_keys(complaint.email)
    driver.find_element(By.ID, "Textbox-7").send_keys(complaint.phone)

    # Wait for the user to fill the captcha and hit submit
    input("Please fill the captcha and hit submit, then press enter to continue...")

    driver.quit()


#old function from before captchagate
# def fill_form(complaint, link):
#
#     # Create the browser object with the configured options
#     driver = webdriver.Firefox()
#
#     # Navigate to the provided link
#     driver.get(link)
#
#     # Wait for the page to load completely
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait for the input fields to become visible, then fill them with the provided input values
#     wait = WebDriverWait(driver, 10)
#     first_name_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-1")))
#     first_name_input.send_keys(complaint.first_name)
#
#     surname_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-2")))
#     surname_input.send_keys(complaint.surname)
#
#     address_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-3")))
#     address_input.send_keys(complaint.address)
#
#     state_dropdown = wait.until(EC.presence_of_element_located((By.ID, "Dropdown-1")))
#     state_select = Select(state_dropdown)
#     state_select.select_by_value(complaint.state_abbrev)
#
#     city_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-4")))
#     city_input.send_keys(complaint.city)
#
#     zip_code_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-5")))
#     zip_code_input.send_keys(complaint.zip_code)
#
#     details_input = wait.until(EC.presence_of_element_located((By.ID, "Textarea-1")))
#     details_input.send_keys(complaint.details)
#
#     email_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-6")))
#     email_input.send_keys(complaint.email)
#
#     phone_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-7")))
#     phone_input.send_keys(complaint.phone)
#
#     # Scroll to the submit button to make it visible, then click it to submit the form
#     submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
#     submit_button.click()
#
#     driver.quit()


def pick_random_value(strings_list):
    random_index = random.randint(0, len(strings_list)-1)
    return strings_list[random_index]

def read_file_to_list(filename):
    string_list = []
    with open(filename, "r") as file:
        for line in file:
            string_list.append(line.strip())
    return string_list

def generate_missouri_zipcode():
    number = random.randint(0, 999)
    number_str = str(number)
    return "63" + number_str

def generate_missouri_phone_number():
    area_code = random.choice(["314", "417", "573", "636", "660", "816"])
    prefix = random.randint(200, 999)
    line_number = random.randint(1000, 9999)
    return f"({area_code}){prefix}{line_number}"

def generate_email(first_name, surname):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com"]
    name = first_name.lower() + "." + surname.lower()
    numbers = [str(random.randint(0, 9)) for _ in range(3)]
    domain = random.choice(domains)
    return name + "".join(numbers) + "@" + domain

def print_complaint(complaint):
        print("First Name:", complaint.first_name)
        print("Surname:", complaint.surname)
        print("Address:", complaint.address)
        print("City:", complaint.city)
        print("Zip Code:", complaint.zip_code)
        print("State:", complaint.state_abbrev)
        print("Details:", complaint.details)
        print("Email:", complaint.email)
        print("Phone:", complaint.phone)