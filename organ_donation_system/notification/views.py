from django.shortcuts import render

# Create notification/views.py

from django.http import JsonResponse
from .matching import match_urgency_based

# Example data (this should come from your database in a real application)
donors = [
    {"id": 1, "blood_type": "O+", "organ": "Kidney", "location": "Delhi", "age": 40},
    {"id": 2, "blood_type": "A-", "organ": "Heart", "location": "Mumbai", "age": 30},
    {"id": 3, "blood_type": "B+", "organ": "Liver", "location": "Delhi", "age": 50},
]

recipients = [
    {"id": 1, "blood_type": "O+", "organ_required": "Kidney", "location": "Delhi", "waiting_time": 150, "severity": 9, "age": 35, "tissue_match": 90},
    {"id": 2, "blood_type": "A-", "organ_required": "Heart", "location": "Mumbai", "waiting_time": 50, "severity": 8, "age": 45, "tissue_match": 85},
    {"id": 3, "blood_type": "O+", "organ_required": "Kidney", "location": "Delhi", "waiting_time": 200, "severity": 7, "age": 60, "tissue_match": 95},
]

# View to get matched donors and recipients
def match_donors_and_recipients(request):
    matched_pairs = match_urgency_based(donors, recipients)
    return JsonResponse(matched_pairs, safe=False)
ate your views here.
