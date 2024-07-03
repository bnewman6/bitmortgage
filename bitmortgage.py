from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/myapi', methods=['GET'])
def my_api():
    # Extract request data
    data = request.json
    
    # Call your Python code with the data
    result = convert_data(data)
    
    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

data_dict = {}

with open("statesdata.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            state, home_value, groceries_cost, property_tax, utility_bill, new_car_bill, used_car_bill = line.split(' ')
            home_value = float(home_value)
            groceries_cost = float(groceries_cost)
            property_tax = float(property_tax)
            utility_bill = float(utility_bill)
            used_car_bill = float(used_car_bill)
            new_car_bill = float(new_car_bill)
            car_bill = float((used_car_bill * 43.1 + new_car_bill * 15.3) / (43.1 + 15.3))
            data_dict[state.upper()] = {"HOME_VALUE": home_value, "GROCERIES_COST": groceries_cost, "PROPERTY_TAX": property_tax, "UTILITY" : utility_bill, "CAR" : car_bill}

def mortgage_calculator(mortgage_value_init, mortgage_interest, time):
    return mortgage_value_init * (1 + time * mortgage_interest)

def calculate_saving_percentage(income, rate, saving_var):
    return (rate * saving_var) / income

def convert_data(data):
    # Open the JSON file
    with open(data) as f:
        # Load the contents of the file into a Python object
        data = json.load(f)
        stats = {}

        income = data["INCOME"] / 12
        state = data["STATE"]
        credit = data["CREDIT"]
        cost = data["COST"]
        time = data["TIME"]
        interest = data["INTEREST"]
        property_tax = float(data_dict[state]["PROPERTY_TAX"] / 100)
        avg_property_value = float(data_dict[state]["HOME_VALUE"])
        ur_value = .28
        lr_value = .36

        filters = data["FILTERS"][:3]
        other = data["FILTERS"][4]
        saving_rates = [2/3, 1, 2/3]
        saved_value = [data_dict[state]["UTILITY"], data_dict[state]["CAR"], data_dict[state]["GROCERIES_COST"]]

        if data["FILTERS"][3]:
            ur_value = .5
            lr_value = .39
        else:
            if other is not None:
                lr_value += calculate_saving_percentage(income, saving_rates[1], other)
            for i in range(3):
                if filters[i]:
                    lr_value += calculate_saving_percentage(income, saving_rates[i], saved_value[i])

        if data["PLAN"]:
            final_payment = mortgage_calculator(cost, interest, time-1)
            total_cost = cost * (1 + (time+1)*interest/2)
            if time > 120:
                ten_years = mortgage_calculator(cost, interest, 120)
                if time > 240:
                    twenty_years = mortgage_calculator(cost, interest, 240)
                else:
                    twenty_years = None
            else:
                ten_years = None
                twenty_years = None
            
            if ((cost + (avg_property_value * property_tax)) / income) < (ur_value):
                good = True
            else:
                good = False
        else:
            loan_amount = cost * .8
            mortgage_value_init = loan_amount / time
            final_payment = mortgage_calculator(mortgage_value_init, interest, time)
            total_cost = mortgage_value_init * (1 + (time+1)*interest/2)
            ten_years = mortgage_calculator(mortgage_value_init, interest, 120)
            if time > 240:
                twenty_years = mortgage_calculator(mortgage_value_init, interest, 240)
            else:
                twenty_years = None
            
            if ((mortgage_value_init + property_tax * cost) / income) < (ur_value):
                good = True
            else:
                good = False
        

        stats["USER"] = {"PAYMENTS" : [ten_years, twenty_years, final_payment, total_cost], "GOOD" : good}

        return(stats)
