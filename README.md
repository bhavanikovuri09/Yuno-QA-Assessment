# Yuno-QA-Assessment
QA Automation assessment using Python + Behave (BDD).  
This repo contains:
•⁠  ⁠Gherkin feature files (⁠ features/.feature ⁠)
•⁠  ⁠Step definitions (⁠ features/steps/.py ⁠)
•⁠  ⁠Supporting utilities (⁠ utils/ ⁠)
•⁠  ⁠Test data (⁠ testdata/ ⁠)
•⁠  ⁠Test case documentation (⁠ documents/ ⁠)

## Tech Stack
•⁠  ⁠Python 3.10+ (recommended)
•⁠  ⁠Behave (BDD)
•⁠  ⁠Requests (API testing)
•⁠  ⁠Selenium + WebDriver Manager (optional UI support)

## Test Coverage
The following scenarios are covered as part of this assessment:
•⁠  ⁠Create payment (minimal and maximal payloads)
•⁠  ⁠Authorization and capture flows
•⁠  ⁠Payment verification
•⁠  ⁠Refund scenarios (partial and full)
•⁠  ⁠Negative scenarios for invalid inputs and authentication

## Test Strategy & Tagging
Scenarios are tagged to allow selective execution:
•⁠  ⁠⁠ @sanity ⁠ – critical smoke tests
•⁠  ⁠⁠ @regression ⁠ – full coverage suite
•⁠  ⁠⁠ @negative ⁠ – validation and error handling

## Setup
```bash
python -m venv .venv
source .venv/bin/activate      # mac/linux
# .venv\Scripts\activate       # windows

pip install -r requirements.txt

