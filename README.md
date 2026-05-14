# Smart Payroll

Payroll Calculator — a simple payroll management system written in Python for calculating salaries, generating reports, managing employees in a CSV file, and bulk-sending payslips via SMTP.

---

Description
- CLI application that:
  - Loads and stores employee data in `data/payroll.csv`.
  - Calculates salaries (gross → insurance → taxable → tax → net).
  - Generates plain-text payslips and sends them via SMTP (using `EMAIL_USER`/`EMAIL_PASS`).
  - Produces a total company report (total gross, total insurance, total tax, etc.).
- Designed for small teams / practical use — organized into small modules:
  - `main.py` — main entrypoint / menu.
  - `business/` — payroll calculations & reporting.
  - `storage/` — CSV handler.
  - `payslip/` — payslip formatting.
  - `emailservice/` — email sending.
  - `model/` — Employee model.
  - `tests/` — unit tests (unittest).

Key features
- CLI with options:
  1. View Employees and Salaries
  2. Update Overtime hours for employees
  3. Bulk Send Email Payslips
  4. Generate Total Company Report
  5. Add New Employee
  6. Delete Employee
  7. Exit
- CSV persistence at `data/payroll.csv`.
- Email sending via SMTP (Gmail by default).
- Unit tests cover Employee, CSV handler, and Payroll calculator.

Requirements
- Python 3.8+
- Dependencies:
  - python-dotenv (for loading environment variables from .env for email credentials)
  - Unit tests use the stdlib `unittest`

Installation / Quick start
1. Clone the repository:
   ```bash
   git clone https://github.com/Xaralampos-Makridhs/payroll_calculator.git
   cd payroll_calculator
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   ```

3. Install required package:
   ```bash
   pip install python-dotenv
   ```

4. Configure .env for email sending (optional — only if you want to send payslips):
   - Create a `.env` file in the repository root with:
     ```env
     EMAIL_USER=your.email@example.com
     EMAIL_PASS=app-password
     ```
   Note: If using Gmail you may need to create an App Password or allow less secure apps (where applicable). The application uses `smtp.gmail.com:587` by default.

5. Run the application:
   ```bash
   python main.py
   ```
   The menu with options 1–7 will appear.

Project layout (main)
- main.py — CLI and user interaction loop
- model/employee.py — Employee class and helper methods (get_total_gross_salary, calculate_gross_salary, to_dict)
- business/payroll_calculator.py — core payroll calculation
  - Rates used:
    - INSURANCE_RATE = 0.1387 (13.87%)
    - TAX_RATE = 0.20 (20%)
    - EMPLOYER_CONTRIBUTION_RATE = 0.2229 (22.29%) — referenced in the code
- business/generate_company_report.py — generate total company report
- storage/csvhandler.py — create/read/update/delete employees in `data/payroll.csv`
  - Fieldnames: `["ID", "Full Name", "Base Salary", "Department","Email","Overtime Hours", "Hourly Rate"]`
- payslip/format_payslip.py — format payslip text
- emailservice/emailservice.py — send payslips via SMTP
- tests/ — contains unit tests:
  - tests/test_employee.py
  - tests/test_calculator.py
  - tests/test_csvhandelr.py

Example CSV header and row
```csv
ID,Full Name,Base Salary,Department,Email,Overtime Hours,Hourly Rate
1,"Makridhs Xaralampos",1200.0,IT,mak@ex.com,10.0,20.0
```

How calculations are done (brief)
- Gross Salary = Base Salary + Overtime (Overtime = overtime_hours * hourly_rate)
- Insurance = round(Gross * 0.1387, 2)
- Taxable Amount = round(Gross - Insurance, 2)
- Tax = round(Taxable Amount * 0.20, 2)
- Net Salary = round(Taxable Amount - Tax, 2)

Example from unit tests (for verification)
- Employee with base 1000.0, overtime 10h and hourly_rate 20.0:
  - Gross = 1000 + (10 * 20) = 1200.0
  - Insurance ≈ 166.44
  - Tax ≈ 206.71
  - Net ≈ 826.85

Running tests
- Tests use `unittest`. Run:
  ```bash
  python -m unittest discover -s tests -v
  ```

Security & privacy notes
- Do not commit credentials (like EMAIL_PASS) to the repository.
- Use a `.env` file and add `.env` to `.gitignore`.
- Prefer App Passwords for Gmail instead of your main password.

Suggestions / To-Do (improvement ideas)
- Add `requirements.txt` and/or Poetry for reproducible environments.
- Add CI (GitHub Actions) to run tests automatically.
- Improve CLI input validation and error handling.
- Add output options for reports: JSON/Excel/PDF.
- Support email templates (HTML) and retry/queueing logic.

Contributing
- Fork, create a feature/fix branch, open a PR with a description.
- Add tests for any functional changes.

License
- There is no explicit LICENSE file in the repository. If you want an open license, add a LICENSE (e.g., MIT) at the root.


