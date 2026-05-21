from sinch import SinchClient
from sinch.core.pagination import Paginator
from sinch.domains.numbers.models.v1.response import AvailableRegion
import os
from dotenv import load_dotenv

load_dotenv()


KEY_ID = os.getenv("SINCH_KEY_ID")
KEY_SECRET = os.getenv("SINCH_KEY_SECRET")
PROJECT_ID = os.getenv("SINCH_PROJECT_ID")

client = SinchClient(key_id=KEY_ID, key_secret=KEY_SECRET, project_id=PROJECT_ID)


## Original snippet uses number_type, this is a wrong parameter, ¿How do I suppose to know that MOBILE means phone numbers?
# MOBILE: Numbers that belong to a specific range.
# LOCAL: Numbers that are assigned to a specific geographic region.
# TOLL_FREE: Number that are free of charge for the calling party but billed for all arriving calls.
available_regions: Paginator[AvailableRegion] = client.numbers.regions.list()

for region in available_regions.iterator():
    print(region)
