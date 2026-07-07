# PHI/PII Redaction Pipeline - Final Report

## Project Overview
This project builds an automated redaction pipeline for healthcare data.
It detects and removes sensitive patient information before sending 
clinical notes to external AI systems.

## Problem Statement
Healthcare organizations face strict privacy laws like HIPAA.
Sending unredacted patient data to external AI APIs is illegal.
This pipeline solves that problem by automatically cleaning the data first.

## Solution
We built a two-step pipeline:
- Step 1: Detect and hide sensitive data using Regex patterns
- Step 2: Replace real names with fake names using Pseudonymization

## Technologies Used
- Python
- Regex (re library)
- Random (for fake name generation)
## HIPAA Safe Harbor - 18 Identifiers

HIPAA law says these 18 items must be removed from patient data:

1. Patient Names
2. Geographic data (address, city, zip code)
3. Dates (birth date, admission date)
4. Phone numbers
5. Fax numbers
6. Email addresses
7. Social Security Numbers (SSN)
8. Medical Record Numbers (MRN)
9. Health plan numbers
10. Account numbers
11. Certificate numbers
12. Vehicle identifiers
13. Device identifiers
14. Web URLs
15. IP addresses
16. Biometric identifiers
17. Full face photos
18. Any unique identifying number

## What Our Pipeline Covers
- Patient Names ✅
- Addresses ✅
- Dates ✅
- Phone Numbers ✅
- Email Addresses ✅
- SSN ✅
- Medical Record Numbers ✅
## Pipeline Speed Test

We tested the pipeline speed on 3 clinical notes.
The pipeline processes each note in milliseconds.
This is fast enough for real-time clinical use.

### Speed Test Results
- Note 1 (Patient John Smith): processed in < 1 millisecond
- Note 2 (Patient Sarah Johnson): processed in < 1 millisecond
- Note 3 (Full Pipeline Test): processed in < 1 millisecond

### Conclusion
The pipeline is fast enough to be used in real healthcare 
systems without causing delays for doctors or clinical staff.