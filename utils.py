def triage_priority(patient):

    #nested if logic to determine the urgency.
    if patient.severity >= 4:
        if patient.age > 60 or patient.age < 5:
            return "IMMEDIATE"
        else:
            return "URGENT"
    elif patient.severity >= 2:
        return "STABLE"
    else:
        return "NON-URGENT"



def find_available_hospital(hospital_list):
    for hospital in hospital_list.values():
        if hospital.has_space():
            return hospital
    return None
