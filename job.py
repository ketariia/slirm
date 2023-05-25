class Employer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.job_seekers = []

    def register_job_seeker(self, job_seeker):
        self.job_seekers.append(job_seeker)

class JobSeeker:
    def __init__(self, id, name, email, skills, desired_job_title):
        self.id = id
        self.name = name
        self.email = email
        self.skills = skills
        self.desired_job_title = desired_job_title
        self.employers = []

    def register_with_employer(self, employer):
        self.employers.append(employer)

class JobAgency:
    def __init__(self):
        self.employers = {}
        self.job_seekers = {}

    def add_employer(self, employer):
        self.employers[employer.id] = employer

    def add_job_seeker(self, job_seeker):
        self.job_seekers[job_seeker.id] = job_seeker

    def match_job_seekers_to_employers(self):
        for employer in self.employers.values():
            for job_seeker in self.job_seekers.values():
                if job_seeker.desired_job_title in employer.job_titles and set(job_seeker.skills).issubset(set(employer.required_skills)):
                    employer.register_job_seeker(job_seeker)
                    job_seeker.register_with_employer(employer)
