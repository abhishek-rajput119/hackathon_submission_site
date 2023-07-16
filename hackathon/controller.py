from .models import Hackathon
from .constants import User
import datetime
class HackthonUtil:
    def add_hackathon(self, data):
        # if data.user.id is None:
        #     return None, User.NOT_LOGGED_IN
        hackathon_query_dict = {
            'user_id': data.user.id ,
            'title': data.POST.get("title"),
            'description': data.POST.get("description"),
            'reward': int(data.POST.get("reward")),
            'start_time': data.POST.get("start_time"),
            'end_time' : data.POST.get("end_time"),
            'created': datetime.datetime.now(),
            'updated': datetime.datetime.now(),
            'active' : 1,
        }
        
        try:
            hackathon = Hackathon.objects.create(**hackathon_query_dict)
        except Exception as e:
            print(f"Error in creating hackathon entry {e}")
            return None, 0
        
        return hackathon, None
    