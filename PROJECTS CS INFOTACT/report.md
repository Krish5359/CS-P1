# PHI/PII Redaction Pipeline - Final Report
Internship Project - CS Infotact Solutions
Made by: Krish Kanani

## Project Overview
This project builds an automated redaction pipeline for healthcare data.
It detects and removes sensitive patient information before sending 
clinical notes to external AI systems.

## Problem Statement
Healthcare organizations face strict privacy laws like HIPAA.
Sending unredacted patient data to external AI APIs is illegal.
This pipeline solves that problem by automatically cleaning the data first.

## Solution
We built a two step pipeline:
- Step 1: Detect and hide sensitive data using Regex patterns
- Step 2: Replace real names with fake names using Pseudonymization

## Technologies Used
- Python
- Regex (re library)
- Random (for fake name generation)
- Logging (for audit trail)
- Time (for speed measurement)

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
We tested the pipeline speed on multiple clinical notes.
The pipeline processes each note in milliseconds.
This is fast enough for real time clinical use.

### Speed Test Results
- Note 1 (Patient John Smith): processed in < 1 millisecond
- Note 2 (Patient Sarah Johnson): processed in < 1 millisecond
- Note 3 (Full Pipeline Test): processed in < 1 millisecond

## Risk Assessment

### What is Re-identification Risk?
Re-identification risk means someone could use the 
redacted data to figure out who the real patient is.

### Risks in Our Pipeline
| Risk | Level | How We Handle It |
|---|---|---|
| Name not detected | Low | We use both Regex and fake name replacement |
| Fake name matches real person | Low | Names are randomly generated |
| Mapping vault gets leaked | Medium | Mapping is stored locally only |
| Partial data reveals identity | Low | We redact all 7 key identifiers |

### How We Reduce Risk
- Real names are never sent to external AI
- Fake names are randomly generated each time
- Name mappings are stored locally and never shared
- Pipeline processes data in milliseconds before sending

## HIPAA Compliance

### What is HIPAA?
HIPAA (Health Insurance Portability and Accountability Act) 
is a US law that protects patient privacy. It says hospitals 
and healthcare organizations must protect patient data at all times.

### What is Safe Harbor Method?
Safe Harbor is a method defined by HIPAA. It says if you 
remove all 18 specific identifiers from patient data, 
the data is considered safe to use.

### How Our Pipeline Follows HIPAA Safe Harbor
| Requirement | Our Solution |
|---|---|
| Remove patient names | ✅ Replaced with fake names |
| Remove phone numbers | ✅ Replaced with [PHONE] |
| Remove email addresses | ✅ Replaced with [EMAIL] |
| Remove SSN | ✅ Replaced with [SSN] |
| Remove dates | ✅ Replaced with [DATE] |
| Remove addresses | ✅ Replaced with [ADDRESS] |
| Remove medical record numbers | ✅ Replaced with [MEDICAL_RECORD] |

## Conclusion

### What We Built
We successfully built a two step PHI/PII redaction pipeline 
that protects patient data before sending to external AI systems.

### Key Achievements
- Built a Regex based redaction system for structured data
- Built a Pseudonymization engine for patient and doctor names
- Pipeline processes notes in less than 1 millisecond
- Covers 7 out of 18 HIPAA Safe Harbor identifiers
- System is fully reversible - original data can be restored
- Added error handling and logging for production use

### What We Learned
- Healthcare data requires multiple layers of protection
- Pseudonymization is better than simple deletion for AI systems
- Speed is critical when building proxy services for healthcare
- HIPAA compliance requires careful attention to all 18 identifiers

### Future Improvements
- Cover remaining 11 HIPAA Safe Harbor identifiers
- Add Redis cache for storing name mappings securely
- Integrate with real hospital systems
- Add encryption for the mapping vault
- Build a web interface for doctors to use easily