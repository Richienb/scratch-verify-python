import random
import string
from time import time as now
import requests

__all__ = ["create_code", "verify_code"]

def create_code() -> str:
	"""
	Generate a verification code for the user to provide at https://scratch.mit.edu/projects/440710593. This is just a convenience method - you can use any numerical code.

	Returns:
		A 6-digit number.
	"""

	return "".join(random.SystemRandom().choices(string.digits, k=6))

def verify_code(username: str, code: str, completion_timeout: int = float("inf")) -> bool:
	"""
	Verify whether the user is authenticated.

	Arguments:
		username: The username to authenticate.
		code: The code to check for.
		completion_timeout: The maximum amount of seconds that can pass since the user provided the code before it is no longer accepted.

	Returns:
		Whether the user has authenticated.
	"""

	cloud_data = requests.get("https://clouddata.scratch.mit.edu/logs", params={
		"projectid": 440710593,
		"limit": 1000,
		"offset": 0
	}).json()

	for entry in cloud_data:
		if (entry["verb"] == "set_var" and
			entry["name"] == "☁ Verification code" and
			entry["user"] == username and
			entry["value"] == code and
			entry["timestamp"] / 1000 >= now() - completion_timeout):
				return True

	return False
