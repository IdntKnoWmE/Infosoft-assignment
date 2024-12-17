# Approach for Question-1

    The DataStream class is designed to manage a stream of data represented by data_strings, ensuring that each data_string can only be output once every 5 seconds.

    1. Data Storage: It uses a dictionary, output_map, where the key is the data_string and the value is the next allowed timestamp (in the form of a timestamp when the data_string can be output again).

    2. Initialization: When a new instance of DataStream is created, the dictionary output_map is initialized as empty.

    3. should_output_data_str function:
        When a data_string is passed to this function along with a timestamp, the function first checks if the data_string has been seen before:
        
            - If not, it means this is the first time the data_string is being encountered, so the function stores the current timestamp plus 5 seconds as the next allowed time for this data_string. It then returns True, allowing the data_string to be output.
    
            - If the data_string has been encountered before, the function checks whether the timestamp is greater than or equal to the next allowed timestamp for that string:
                - If the condition is true, it updates the next allowed time to timestamp + 5 (i.e., the data_string can be output again after 5 seconds) and returns True.
                - If the condition is false, it means that the data_string has already been output within the last 5 seconds, so it returns False, blocking the output.

# Approach with Question - 2

    The FuelStation class is designed to manage the parking slot for the various fuel types cars.

    Initialization: 
        - The class is initialized with three types of fuel car parking spots: diesel, petrol, and electric. It stores the quantities of each fuel car spot in both individual variables (diesel, petrol, electric) and in a dictionary (parking), where the keys are fuel types and the values are the respective quantities.
        - The individual variables holed the maximum spots for a fuel car available.
        - The parking dictionary acts as placeholder for the spots signifying hoe many spots are available in the future if parking is made for a specific fuel car.

    fuel_vehicle method:

        - This method is used to park a vehicle with the specified fuel_type.
        -If there is slot available in the parking (i.e., the quantity of the specified fuel type car slot is greater than 0), it decreases the slot by 1 and returns True to indicate that the parking is available.
        -If the slot is unavailable (quantity is 0), it returns False.
    
    
    open_fuel_slot method:

        -This method is used to "open" a slot for a specific fuel type car (i.e., increase the quantity of slot in the parking).
        -If the quantity of the specified fuel type car in parking is already at its maximum capacity (stored in the individual variable for that fuel type), it returns False and does nothing. It means no slot is there which needs to be empty.
        -If there is a slot for fuel car that is taken(i.e., the quantity is less than the maximum), then the slot is empty and the func increases the fuel car slot in parking by 1 and returns True.


# Approach for Question - 3:

    Debugging checks done on :
        - Overlapping interval logic in if conditions.
        - Moving the interval to the correct child.
    Correction made:
        
        - In insert() function the if condition "if node.start <= self.end:" is correct to "if node.start >= self.end:" as the valid case would be when next node start is >= curr node end otherwise this will cause an overlap. In simple if a next event node has starting time >= curr event node end time then only it is eligible to move on the right side of tree where the events exist that are happening after curr node event.

        - In insert() function both the if conditions are moving shifting to left child even when the curr event node end timing is less then or equal to next event start timing so, the correction is made for the first if condition  where insert func is again call for right child of the curr event node i.e., return self.right_child.insert(node).

        - In case the overlap is there between next event and current event there is no statement for returning False is there so, that's why added the else condition which confirms that events are overlapping and False is returned.

     