from prescription_data import *

trial_patients = ['Denise', 'Georgia', 'Kenny', 'Frank', 'Eddie', 'Anne']

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except:
        print(f"Patient {patient} is not taking Warfarin. "
              f"Remove {patient} from the trial.")
    print(patient, prescription)
