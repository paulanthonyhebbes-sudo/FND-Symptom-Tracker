# FND Symptom Tracker

A simple local Python application to track symptoms of Functional Neurological Disorder (FND). This tool allows users to log their symptoms, dates, and comments locally.

## Features
- **Symptom Tracking:** Checkboxes for common FND symptoms.
- **Date Entry:** Record the date of each observation.
- **Comments Box:** Add additional notes or comments.
- **Sliding Scales:** Rate symptoms on a 1-10 scale.
- **Autosave:** Data is saved in a JSON file named `fnd_symptoms.json`.
- **Load Data:** Load previously saved data from the JSON file.

## Installation
1. Ensure Python is installed on your system.
2. Install dependencies using pip:
   ```sh
   pip install pandas

## Usage
1. Run the script using Python:
   ```sh
   python fnd_symptom_tracker.py
2. Enter the date and check the applicable symptoms.
3. Rate each symptom on a 1-10 scale.
4. Add any comments or notes in the comments box.
5. Click “Save” to store the data.
6. Use “Load” to retrieve saved data.

## Notes
The script uses a local JSON file for autosaving. 

Ensure you have write permissions in the repository directory.

The symptom list and scales are hardcoded; no scraping from external sources.
