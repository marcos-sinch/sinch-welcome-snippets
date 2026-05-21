from sinch import SinchClient
from sinch.core.pagination import Paginator
from sinch.domains.numbers.models.v1.response import ActiveNumber
import os
from dotenv import load_dotenv

load_dotenv()


KEY_ID = os.getenv("SINCH_KEY_ID")
KEY_SECRET = os.getenv("SINCH_KEY_SECRET")
PROJECT_ID = os.getenv("SINCH_PROJECT_ID")

client = SinchClient(key_id=KEY_ID, key_secret=KEY_SECRET, project_id=PROJECT_ID)


# Search for available US local numbers that start with "504" (New Orleans area code).
# number_pattern: digit sequence to match (e.g. "504")
# number_search_pattern: where to match — START, CONTAINS, or END
available_numbers: Paginator[ActiveNumber] = client.numbers.search_for_available_numbers(
    region_code="US",
    number_type="LOCAL",
    number_pattern="504",
    number_search_pattern="START",
)


for number in available_numbers.iterator():
    print(number)
