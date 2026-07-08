# Project 2 - PHI/PII Redaction Pipeline
Internship Project - CS Infotact Solutions

## Project Overview
An automated redaction pipeline that detects and removes 
sensitive patient information from clinical notes before 
sending to external AI systems.

## Problem Statement
Healthcare organizations face strict privacy laws like HIPAA.
Sending unredacted patient data to external AI APIs is illegal.
This pipeline solves that problem by automatically cleaning 
the data first.

## Solution
We built a two step pipeline:
- Step 1: Detect and hide sensitive data using Regex patterns
- Step 2: Replace real names with fake names using Pseudonymization

## Project Files
- PRO 2.py - Main redaction pipeline with error handling and logging
- pseudonymizer.py - Fake name generator and reverse mapping
- report.md - Final HIPAA compliance report
- README.md - Project documentation

## What We Redact
- Patient Names
- Doctor Names
- Phone Numbers
- Email Addresses
- Social Security Numbers (SSN)
- Dates of Birth
- Medical Record Numbers
- Addresses and Zipcodes

## HIPAA Compliance
This pipeline follows HIPAA Safe Harbor method by removing
7 out of 18 required patient identifiers.

## Week 1 - Completed
- Basic regex redaction
- Phone, email, SSN, date hiding

## Week 2 - Completed
- Added patient name redaction
- Added doctor name redaction
- Added medical record number redaction
- Added address and zipcode redaction
- Added support for multiple patients

## Week 3 - Completed
- Created pseudonymizer.py file
- Added fake name generator
- Added fake doctor name generator
- Added fake address generator
- Added fake phone generator
- Added fake email generator
- Added name mapping dictionary
- Added reverse mapping function
- Combined redactor and pseudonymizer
- Tested with multiple patients

## Week 4 - Completed
- Created final report file
- Added pipeline timing and speed measurement
- Added HIPAA Safe Harbor 18 identifiers list
- Added speed test results to report
- Added error handling to pipeline
- Added logging to pipeline
- Added more test cases
- Added risk assessment to report
- Added HIPAA compliance section to report
- Added conclusion to report
- Final cleanup of all files

## Made By
Krish Kanani
Internship Project - CS Infotact Solutions