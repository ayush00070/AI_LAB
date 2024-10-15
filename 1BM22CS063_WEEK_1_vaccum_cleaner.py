def vacuum_world():
    # Initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0
    
    # User input for the location of the vacuum
    location_input = input("Enter Location of Vacuum (A or B): ").strip().upper()
    # User input for the status of the current location
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ").strip()
    
    # Determine the status of the other location
    other_location = 'B' if location_input == 'A' else 'A'
    status_input_complement = input(f"Enter status of {other_location} (0 for Clean, 1 for Dirty): ").strip()
    
    print("Initial Location Condition:", goal_state)
    
    # Action based on the location of the vacuum
    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            # Suck the dirt and mark it as clean
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("Cost for CLEANING A:", cost)
            print("Location A has been Cleaned.")
        
        if status_input_complement == '1':
            # if B is Dirty
            print("Location B is Dirty.")
            print("Moving right to Location B.")
            cost += 1  # cost for moving right
            print("COST for moving RIGHT:", cost)
            # Suck the dirt and mark it as clean
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("COST for SUCK:", cost)
            print("Location B has been Cleaned.")
        else:
            print("Location B is already clean.")
    
    elif location_input == 'B':
        print("Vacuum is placed in Location B")
        if status_input == '1':
            print("Location B is Dirty.")
            # Suck the dirt and mark it as clean
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("COST for CLEANING B:", cost)
            print("Location B has been Cleaned.")
        
        if status_input_complement == '1':
            # if A is Dirty
            print("Location A is Dirty.")
            print("Moving LEFT to Location A.")
            cost += 1  # cost for moving left
            print("COST for moving LEFT:", cost)
            # Suck the dirt and mark it as clean
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("COST for SUCK:", cost)
            print("Location A has been Cleaned.")
        else:
            print("Location A is already clean.")
    
    # Done cleaning
    print("GOAL STATE:", goal_state)
    print("Performance Measurement (Total Cost):", cost)

# Call the function to execute the vacuum world simulation
vacuum_world()
