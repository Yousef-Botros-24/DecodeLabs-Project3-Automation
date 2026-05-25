# Project 3: The Python Orchestrator

A Python-based automation and storage engine designed to handle file system operations, text processing, and structured data management (CSV & JSON). This project satisfies the Phase 1 requirements of the DecodeLabs training program.

## 📁 Features & Architecture

### 1. File Automation Wizard
- Automatically provisions local directories and handles file paths dynamic creation.
- Performs file input/output operations (`File I/O`) to write and read verification strings securely.

### 2. Structured Storage Management
- Generates and populates tabular structures utilizing the `csv` core module.
- Maps object structures into serialized `json` formats for interoperability.
- Validates data integrity by reading back stored records into the terminal.

## 🛠️ File Structure
- `automation_wizard.py`: Core logic for directory and text file creation.
- `storage_manager.py`: Core logic for data serialization (CSV & JSON handling).
- `README.md`: System documentation.
