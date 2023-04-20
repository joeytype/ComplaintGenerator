import methods
from Complaint import Complaint
import random
from selenium import webdriver

firstnames = methods.read_file_to_list("first_names.txt")
surnames = methods.read_file_to_list("surnames.txt")
streetnames = methods.read_file_to_list("street_names.txt")
types_of_people = methods.read_file_to_list("types_of_people.txt")
trans_activities = methods.read_file_to_list("transgender_activities.txt")
cities = methods.read_file_to_list("cities.txt")
supplementary_details = methods.read_file_to_list("supplementary_details.txt")

def create_complaint():
    complaint = Complaint("", "", "", "", "", "", "", "", "")
    complaint.first_name = methods.pick_random_value(firstnames)
    complaint.surname = methods.pick_random_value(surnames)
    complaint.email = methods.generate_email(complaint.first_name, complaint.surname)
    complaint.phone = methods.generate_missouri_phone_number()
    complaint.city = methods.pick_random_value(cities)
    complaint.address = "" + (str(random.randint(1, 300))) +" "+ methods.pick_random_value(streetnames)
    complaint.zip_code = methods.generate_missouri_zipcode()
    complaint.state_abbrev = "MO"
    complaint.details = "the " + (methods.pick_random_value(types_of_people)) + " " + ((methods.pick_random_value(trans_activities))) + " and " + (methods.pick_random_value(supplementary_details))
    return complaint

#if you wanna see how a generated complaint looks uncomment these

# complaint1 = create_complaint()
# methods.print_complaint(complaint1)


#from before captchagate this was originally intended to loop and spam the form 500 times
# for i in range (500):
#     complaint = create_complaint()
#     methods.fill_form(complaint, "https://ago.mo.gov/file-a-complaint/transgender-center-concerns")


complaint = create_complaint()
methods.fill_form(complaint, "https://ago.mo.gov/file-a-complaint/transgender-center-concerns")
