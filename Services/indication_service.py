from datetime import datetime
import Indication
from Indication.views import IndicationController

def save_value(cv, an):
    current_value = cv
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return IndicationController.post(current_value=current_value, time_of_taking=time_now, account_number=an)