from models import Patient, Hospital
from utils import triage_priority, find_available_hospital

#Data Setup

hospitals = {
    "Korle-Bu": Hospital("Korle-Bu", 2),
    "37 Military": Hospital("37 Military", 3000),
    "Tema General": Hospital("Tema General", 2000),
    "Cape Coast Teaching": Hospital("Cape Coast Teaching", 1500),
    "Komfo Anokye Teaching": Hospital("Komfo Anokye Teaching", 10000),
    "Tamale Teaching": Hospital("Tamale Teaching", 8000),
    "Ho Teaching": Hospital("Ho Teaching", 5000),
    "Sunyani Regional": Hospital("Sunyani Regional", 3000),
    "Effia Nkwanta Regional": Hospital("Effia Nkwanta Regional", 2000),
    "Cape Coast Regional": Hospital("Cape Coast Regional", 1500),
    "Koforidua Regional": Hospital("Koforidua Regional", 1000),
    "Bolgatanga Regional": Hospital("Bolgatanga Regional", 500)
}

def run_system():
    print("--- Emergency Bed Referral System ---")
    
    # Main loop: keep adding patients until user types 'exit'
    while True:
        name = input("\nEnter Patient Name (or 'exit'): ")
        if name.lower() == 'exit': 
            break
        
        age = int(input("Enter Age: "))
        severity = int(input("Enter Severity (1-5): "))
        
        patient = Patient(name, age, severity)
        priority = triage_priority(patient)
        
        print(f"Triage Result: {priority} PRIORITY")

        # Core logic: If/Else/Elif for bed allocation
        target_hospital = find_available_hospital(hospitals)
        
        if target_hospital:
            if target_hospital.allocate_bed():
                print(f"SUCCESS: Bed assigned at {target_hospital.name}.")
            else:
                print("CRITICAL: Bed allocation failed unexpectedly.")
        else:
            # The 'No Bed Syndrome' Trigger
            print("ALERT: NO BEDS AVAILABLE in the network! Initiate emergency protocols.")
    
    # Discharge loop: allow user to free up beds
    print("\n--- Discharge Patients ---")
    while True:
        name_hospital = input("\nEnter Hospital Name to discharge a bed (or 'exit'): ")
        if name_hospital.lower() == 'exit':
            break
        
        if name_hospital in hospitals:
            if hospitals[name_hospital].discharge():
                print(f"SUCCESS: Bed freed at {name_hospital}. Occupied beds: {hospitals[name_hospital].occupied_beds}")
            else:
                print(f"No beds to discharge at {name_hospital}.")
        else:
            print("Hospital not found. Please check the name.")

if __name__ == "__main__":
    run_system()