import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# --- Configuration ---
NUM_PATIENTS = 200
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 9, 15)

# --- Generate Patient Demographics ---
patient_ids = list(range(101, 101 + NUM_PATIENTS))
patients = []
for pid in patient_ids:
    patients.append({
        'patient_id': pid,
        'age': random.randint(18, 90),
        'gender': random.choice(['Male', 'Female']),
        'ethnicity': random.choices(['Caucasian', 'African American', 'Hispanic', 'Asian', 'Other'], weights=[0.6, 0.15, 0.15, 0.05, 0.05], k=1)[0],
        'insurance_provider': random.choice(['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealthcare', 'Humana', 'Other'])
    })
patient_demographics_df = pd.DataFrame(patients)
patient_demographics_df.to_csv('data/raw/patient_demographics.csv', index=False)

# --- Generate Clinical Events (Long Format) ---
events = []
event_id_counter = 1
vitals_options = {'heart_rate': (60, 100, 'bpm'), 'blood_pressure': (None, None, 'mmHg'), 'temperature': (97.0, 99.5, 'F')}
lab_options = {'glucose': (70, 150, 'mg/dL'), 'cholesterol': (150, 250, 'mg/dL'), 'hemoglobin': (12.0, 17.5, 'g/dL')}
medication_options = {'aspirin': (81, 325, 'mg'), 'lisinopril': (5, 40, 'mg'), 'metformin': (500, 1000, 'mg')}

for pid in patient_ids:
    num_events = random.randint(5, 15)
    patient_start_date = fake.date_time_between(start_date=START_DATE, end_date=END_DATE - timedelta(days=30))
    for _ in range(num_events):
        event_type = random.choices(['vitals', 'lab', 'medication'], weights=[0.5, 0.3, 0.2], k=1)[0]
        event_timestamp = fake.date_time_between(start_date=patient_start_date, end_date=patient_start_date + timedelta(days=7))
        
        if event_type == 'vitals':
            vital, (low, high, unit) = random.choice(list(vitals_options.items()))
            if vital == 'blood_pressure':
                value = f"{random.randint(110, 140)}/{random.randint(70, 90)}"
            else:
                value = round(random.uniform(low, high), 1)
            event_name = vital
        elif event_type == 'lab':
            lab, (low, high, unit) = random.choice(list(lab_options.items()))
            value = round(random.uniform(low, high), 1)
            event_name = lab
        else: # medication
            med, (low, high, unit) = random.choice(list(medication_options.items()))
            value = random.choice(range(low, high, (high-low)//4 if high-low > 4 else 1))
            event_name = med

        events.append({
            'event_id': event_id_counter,
            'patient_id': pid,
            'event_type': event_type,
            'event_name': event_name,
            'event_timestamp': event_timestamp,
            'event_value': value,
            'event_unit': unit
        })
        event_id_counter += 1
clinical_events_df = pd.DataFrame(events)
clinical_events_df.to_csv('data/raw/clinical_events.csv', index=False)


# --- Generate Medical Procedures (Wide Format) ---
procedures = []
record_id_counter = 1
procedure_options = {
    'appendectomy': (60, 120), 'angiography': (45, 90), 'cholecystectomy': (90, 150),
    'colonoscopy': (30, 60), 'arthroscopy': (60, 100), 'biopsy': (20, 40),
    'cataract surgery': (15, 30), 'endoscopy': (30, 50), 'hernia repair': (80, 130),
    'tonsillectomy': (40, 60)
}
for pid in patient_ids:
    if random.random() < 0.8: # 80% chance of having a procedure
        num_procedures = random.randint(1, 3)
        procedure_start_date = fake.date_time_between(start_date=START_DATE, end_date=END_DATE - timedelta(days=30))
        for _ in range(num_procedures):
            proc_name, (min_dur, max_dur) = random.choice(list(procedure_options.items()))
            procedures.append({
                'record_id': record_id_counter,
                'patient_id': pid,
                'procedure_type': proc_name,
                'procedure_timestamp': fake.date_time_between(start_date=procedure_start_date, end_date=procedure_start_date + timedelta(days=2)),
                'duration_minutes': random.randint(min_dur, max_dur),
                'complication': random.choices(['none', 'bleeding', 'infection', 'anesthesia reaction'], weights=[0.9, 0.04, 0.04, 0.02], k=1)[0]
            })
            record_id_counter += 1
medical_procedures_df = pd.DataFrame(procedures)
medical_procedures_df.to_csv('data/raw/medical_procedures.csv', index=False)

print(f"Generated {len(patient_demographics_df)} patient demographic records.")
print(f"Generated {len(clinical_events_df)} clinical event records.")
print(f"Generated {len(medical_procedures_df)} medical procedure records.")
