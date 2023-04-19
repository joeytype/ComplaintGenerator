from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random

from Complaint import Complaint


def fill_form(complaint, link):
    # Create a new instance of the Firefox browser
    driver = webdriver.Firefox()
    # Navigate to the provided link
    driver.get(link)

    # Find the input fields for the form and fill them with the provided input values
    first_name_input = driver.find_element(By.NAME,"first name")
    first_name_input.send_keys(complaint.first_name)

    surname_input = driver.find_element(By.NAME,"last name")
    surname_input.send_keys(complaint.surname)

    address_input = driver.find_element(By.NAME,"address")
    address_input.send_keys(complaint.address)

    state_select = Select(driver.find_element(By.NAME,"state"))
    state_select.select_by_value(complaint.state_abbrev)

    city_input = driver.find_element(By.NAME,"city")
    city_input.send_keys(complaint.city)

    zip_code_input = driver.find_element(By.NAME,"zip_code")
    zip_code_input.send_keys(complaint.zip_code)

    details_input = driver.find_element(By.NAME,"details")
    details_input.send_keys(complaint.details)

    email_input = driver.find_element(By.NAME,"email")
    email_input.send_keys(complaint.email)

    phone_input = driver.find_element(By.NAME,"phone_number")
    phone_input.send_keys(complaint.phone)
    # Find the submit button and click it to submit the form
    submit_button = driver.find_element(By.NAME,"submit")
    submit_button.click()

    # Close the browser window
    driver.quit()


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