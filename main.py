import os
from dotenv import load_dotenv
from monicaPython.monica import calls, activities
from helpers.calls import manage_calls
from helpers.activities import manage_activities


if __name__ == "__main__":
  manage_calls()
  # manage_activities()