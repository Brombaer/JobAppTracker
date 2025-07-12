import json
import os
from datetime import datetime
class JobTracker:
    def __init__(self, filename="data/applications.json"):
        """
        Constrtor for the JobTracker class.

        Initializes the tracker with a filename for saving job data.
        Automatically loads exisiting job applications from the file (if available)
        """
        self.filename = filename
        self.jobs = []
        self.load_jobs()

    def load_jobs(self):
        """
        Loads previously saved job applications from a JSON file.

        If the file exists and contains valid JSON, the data is stored in self.jobs.
        If the file doesn't exist or is corrupted, it initializes with an empty list.    
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try: 
                    self.jobs = json.load(f)
                except json.JSONDecodeError:
                    # If the file is empty or currupted, fall back to empty list
                    self.jobs = []
        else:
            self.jobs = []
    
    def save_jobs(self):
        """
        Saves the current list of job applications to the JSON file.

        This method is called after adding a new job entry to ensure persistence.
        """
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.jobs, f, indent=4, ensure_ascii=False)
    
    def add_job(self):
        """
        Prompts the user to input details about a job application.

        The job is stored as a dictionary with keys like company, title, date, etc.
        If the data is left blank, it defaults to the current data.
        """
        company = input("Enter company name: ").strip()
        title = input("Enter job title: ").strip()
        date = input("Enter date (leave blank for today): ").strip()
        status = input("Enter application status (e.g., Applied, Interview, Offer): ").strip()
        notes = input("Any notes or comments?: ").strip()

        if not date:
            date = datetime.now().strftime("%Y-%m-%d") # use todays date if left blank

        job_entry = {
            "company": company,
            "title": title,
            "date": date,
            "status": status,
            "notes": notes
        }

        # Save job to the internal list and persist to disk
        self.jobs.append(job_entry)
        self.save_jobs()

        print("\n Job added successfully!\n")
    
    def show_jobs(self):
        """
        Display all saved job applications in a formatted list.

        If no jobs are saved, it informs the user. Otherwise, it prints each jobs details.
        """

        if not self.jobs:
            print("No applications found.")
            return
        
        print("Job Applications:")
        print("-" * 50)
        for idx, job in enumerate(self.jobs, 1):
            print(f"{idx}. {job['company']} - {job['title']}")
            print(f"    Date: {job['date']}")
            print(f"    Status: {job['status']}")
            if job['notes']:
                print(f"    Notes: {job['notes']}")
            print("-" * 50)