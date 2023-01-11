import os
from dotenv import load_dotenv
from monicaPython.monica import calls, activities
from helpers.calls import manage_calls


if __name__ == "__main__":
  manage_calls()