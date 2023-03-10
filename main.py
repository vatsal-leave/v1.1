import json

# Employee data

# Define employee data
employee_data = [
    {
        "PS.No.": "123456",
        "Employee Name": "Vatsal Shah",
        "DOB": "2000-07-26",
        "DOJ": "2022-12-26",
        "DOR": "NA",
        "Email": "vatsal@gmail.com",
        "Contact": "9999999999",
        "Designation": "Associate Engineer",
        "Business Unit": "DMS",
        "Base Location": "Baroda",
        "LTTS Grade": "2"
    },
    {
        "PS.No.": "234567",
        "Employee Name": "Shubham Patil",
        "DOB": "2000-07-25",
        "DOJ": "2022-12-26",
        "DOR": "NA",
        "Email": "Shubham@gmail.com",
        "Contact": "7777777777",
        "Designation": "Associate Engineer",
        "Business Unit": "DMS",
        "Base Location": "Baroda",
        "LTTS Grade": "2"
    },
{
        "PS.No.": "3456789",
        "Employee Name": "ShivaPradeep",
        "DOB": "2001-01-01",
        "DOJ": "2023-01-26",
        "DOR": "NA",
        "Email": "ShivaP@gmail.com",
        "Contact": "5555555555",
        "Designation": "Associate Engineer",
        "Business Unit": "DMS",
        "Base Location": "Chennai",
        "LTTS Grade": "2"
    }
]

# Create JSON file
with open('Employee.json', 'w') as f:
    json.dump({"employee": employee_data}, f)
