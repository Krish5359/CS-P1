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