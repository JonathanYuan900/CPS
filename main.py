import os
import time

from dotenv import load_dotenv

from create_file import create_file
from login import login
from problem_codes import solved_problems
from submission_processing import best_submission
from submission_processing import process_submission


# create DMOJ_USERNAME and DMOJ_PASSWORD environment variables as defined in .env
load_dotenv()

# load them into the program
DMOJ_USERNAME = os.getenv('DMOJ_USERNAME')
DMOJ_PASSWORD = os.getenv('DMOJ_PASSWORD')
TARGET_DIRECTORY = os.getenv('TARGET_DIRECTORY')

session = login(DMOJ_USERNAME, DMOJ_PASSWORD)

problem_list = solved_problems(DMOJ_USERNAME, session)

for i, problem_code in enumerate(problem_list):

    print(
        f'Creating files... [{i + 1}/{len(problem_list)}]', end='\r', flush=True)

    submission_id = best_submission(DMOJ_USERNAME, problem_code, session)
    source_code = process_submission(submission_id, session)
    create_file(problem_code, source_code, TARGET_DIRECTORY)

    time.sleep(1)
