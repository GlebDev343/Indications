from datetime import datetime
import Indication
from Indication.views import IndicationController

def save_value(cv, an):
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return IndicationController.post(current_value=cv, time_of_taking=time_now, account_number=an)