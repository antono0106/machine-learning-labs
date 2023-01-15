import fuzzy_variable_input as finput
import fuzzy_variable_output as foutput
import fuzzy_system as fsys


def init_temp():
    temp = finput.FuzzyInputVariable('Temperature', 10, 40, 100)
    temp.add_triangular('Cold', 10, 10, 25)
    temp.add_triangular('Medium', 15, 25, 35)
    temp.add_triangular('Hot', 25, 40, 40)
    return temp


def init_humidity():
    humidity = finput.FuzzyInputVariable('Humidity', 20, 100, 100)
    humidity.add_triangular('Wet', 20, 20, 60)
    humidity.add_trapezoidal('Normal', 30, 50, 70, 90)
    humidity.add_triangular('Dry', 60, 100, 100)
    return humidity


def init_pressure():
    pressure = finput.FuzzyInputVariable('Pressure', 10, 50, 100)
    pressure.add_triangular('Low', 10, 15, 20)
    pressure.add_triangular('Normal', 25, 30, 35)
    pressure.add_triangular('High', 40, 45, 50)
    return pressure


def init_living_condition():
    living_condition = foutput.FuzzyOutputVariable('Living Condition', 10, 100, 100)
    living_condition.add_triangular('Bad', 10, 15, 30)
    living_condition.add_triangular('Normal', 30, 50, 70)
    living_condition.add_triangular('Good', 65, 85, 100)
    return living_condition


def init_system_with_fuzzy_rules(system: fsys.FuzzySystem):
    system.add_rule(
        {'Temperature': 'Cold',
         'Humidity': 'Dry',
         'Pressure': 'High'
         },
        {'Living Condition': 'Bad'})

    system.add_rule(
        {'Temperature': 'Cold',
         'Humidity': 'Wet',
         'Pressure': 'High'
         },
        {'Living Condition': 'Normal'})

    system.add_rule(
        {'Temperature': 'Cold',
         'Humidity': 'Normal',
         'Pressure': 'High'
         },
        {'Living Condition': 'Good'})

    system.add_rule(
        {'Temperature': 'Medium',
         'Humidity': 'Wet',
         'Pressure': 'Normal'
         },
        {'Living Condition': 'Bad'})

    system.add_rule(
        {'Temperature': 'Medium',
         'Humidity': 'Normal',
         'Pressure': 'Normal'
         },
        {'Living Condition': 'Good'})

    system.add_rule(
        {'Temperature': 'Medium',
         'Humidity': 'Dry',
         'Pressure': 'Normal'
         },
        {'Living Condition': 'Good'})

    system.add_rule(
        {'Temperature': 'Hot',
         'Humidity': 'Dry',
         'Pressure': 'Low'
         },
        {'Living Condition': 'Bad'})

    system.add_rule(
        {'Temperature': 'Hot',
         'Humidity': 'Normal',
         'Pressure': 'Low'
         },
        {'Living Condition': 'Normal'})

    system.add_rule(
        {'Temperature': 'Hot',
         'Humidity': 'Wet',
         'Pressure': 'Low'
         },
        {'Living Condition': 'Good'})




def main():
    temp_f_var = init_temp()
    humidity_f_var = init_humidity()
    pressure_f_var = init_pressure()
    living_condition = init_living_condition()

    system = fsys.FuzzySystem()
    system.add_input_variable(temp_f_var)
    system.add_input_variable(humidity_f_var)
    system.add_input_variable(pressure_f_var)
    system.add_output_variable(living_condition)
    init_system_with_fuzzy_rules(system)

    output = system.evaluate_output({
        'Temperature': 11,
        'Humidity': 59,
        'Pressure': 41
    })

    print(output)

    system.plot_system()


if __name__ == '__main__':
    main()
