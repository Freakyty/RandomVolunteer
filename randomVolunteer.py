import random

def selectRandomVolunteer():
    # Open the selected volunteers list.
    selectedVolunteersFile = open("SelectedVolunteers.txt", "r+")
    # Open the volunteers list.
    volunteersFile = open("Volunteers.txt", "r")
    # Create a list for each file.
    selectedVolunteers = selectedVolunteersFile.readlines()
    volunteers = volunteersFile.readlines()
    # Create a list of available volunteers.
    availableVolunteers = generateAvailableVolunteers(volunteersList=volunteers, selectedVolunteersList=selectedVolunteers)

    # If all volunteers have been selected...
    if (len(selectedVolunteers) >= len(volunteers) or len(availableVolunteers) == 0):
        # Reset the selectedVolunteers file.
        selectedVolunteersFile.truncate(0)
        # Close the selected volunteers list.
        selectedVolunteersFile.close()
        # Close the volunteers list.
        volunteersFile.close()
        return ""

    # Close the selected volunteers list.
    selectedVolunteersFile.close()
    # Close the volunteers list.
    volunteersFile.close()
    # Choose a random volunteer from the available volunteers list and return.
    return random.choice(availableVolunteers)

def generateAvailableVolunteers(volunteersList, selectedVolunteersList):
    # Create an empty list.
    availableVolunteers = []
    # Append a volunteer if they have not already been selected.
    for volunteer in volunteersList:
        if (volunteer not in selectedVolunteersList):
            availableVolunteers.append(volunteer.strip())
    # Return the list.
    return availableVolunteers

def writeSelectedVolunteer(selectedVolunteer):
    # Open the selected volunteer list.
    lastVolunteerFile = open("SelectedVolunteers.txt", "a")
    # Append the selectedVolunteer.
    lastVolunteerFile.write(selectedVolunteer + "\n")
    # Close the selected volunteer list.
    lastVolunteerFile.close()

def main():
    # Initialize the selected volunteer.
    selectedVolunteer = ""
    # Loop until we get a volunteer.
    while(selectedVolunteer == ""):
        # Store the selected volunteer.
        selectedVolunteer = selectRandomVolunteer()
    # Write to the selected volunteer file.
    writeSelectedVolunteer(selectedVolunteer)

if __name__ == "__main__":
    main()