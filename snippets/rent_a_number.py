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

# ¿Why the overloadding, there are 3 methods with the same signature? 
number_rented: ActiveNumber = client.numbers.rent(
    phone_number=PHONE_NUMBER,
    sms_configuration={"service_plan_id": "SP123"},
    voice_configuration={"type": "EST"},
)

print(number_rented)
