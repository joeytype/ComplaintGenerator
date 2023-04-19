from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from Complaint import Complaint

def fill_form(complaint, link, driver):
    # Navigate to the provided link
    driver.get(link)

    # Wait for the page to load completely
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the input fields to become visible, then fill them with the provided input values
    wait = WebDriverWait(driver, 10)
    first_name_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-1")))
    first_name_input.send_keys(complaint.first_name)

    surname_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-2")))
    surname_input.send_keys(complaint.surname)

    address_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-3")))
    address_input.send_keys(complaint.address)

    state_dropdown = wait.until(EC.presence_of_element_located((By.ID, "Dropdown-1")))
    state_select = Select(state_dropdown)
    state_select.select_by_value(complaint.state_abbrev)

    city_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-4")))
    city_input.send_keys(complaint.city)

    zip_code_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-5")))
    zip_code_input.send_keys(complaint.zip_code)

    details_input = wait.until(EC.presence_of_element_located((By.ID, "Textarea-1")))
    details_input.send_keys(complaint.details)

    email_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-6")))
    email_input.send_keys(complaint.email)

    phone_input = wait.until(EC.presence_of_element_located((By.ID, "Textbox-7")))
    phone_input.send_keys(complaint.phone)

    # Scroll to the submit button to make it visible, then click it to submit the form
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
    submit_button.click()



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
    return f"({area_code}) {prefix}-{line_number}"

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