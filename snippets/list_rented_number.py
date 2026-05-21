from sinch import SinchClient
from sinch.core.pagination import Paginator
from sinch.domains.numbers.models.v1.response import ActiveNumber
import os
from dotenv import load_dotenv

load_dotenv()


KEY_ID = os.getenv("SINCH_KEY_ID")
KEY_SECRET = os.getenv("SINCH_KEY_SECRET")
PROJECT_ID = os.getenv("SINCH_PROJECT_ID")
PHONE_NUMBER = os.getenv("SINCH_PHONE_NUMBER")

client = SinchClient(key_id=KEY_ID, key_secret=KEY_SECRET, project_id=PROJECT_ID)

#Something happens with the typping of the list method, not showing the correct parameters types dont understand why
number_rented: ActiveNumber = client.numbers.list()

print(number_rented)
