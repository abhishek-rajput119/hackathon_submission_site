from .models import Hackathon,Registration,Submission
from .constants import User
import datetime
import base64
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
            'type_of_submission': int(data.POST.get("file_type")),
            'background_image':self.encode_image(data.FILES.get('background_image')),
            'hackathon_image':self.encode_image(data.FILES.get('hackathon_image'))
        }
        
        try:
            hackathon = Hackathon.objects.create(**hackathon_query_dict)
        except Exception as e:
            print(f"Error in creating hackathon entry {e}")
            return None, 0
        
        return hackathon, None
    
    def register_for_hackathon(self, id, user):
        query_dict = {
            "user_id":user.id,
            "hackathon_id": id
        }
        try:
            registration = Registration.objects.create(**query_dict)
            return registration, None
        except Exception as e:
            return None, e
        
    def encode_image(self, image):
        if not image:
            return ""
        encoded_string = base64.b64encode(image.read())
        
        return encoded_string
    
    def add_submission(self, data, file, hackathon_obj, user):
        query_dict = {
            "hackathon_id" : hackathon_obj.id,
            "user_id" : user.id,
            "title" : data.get("title"),
            "summary" : data.get("summary"),
        }
        if hackathon_obj.type_of_submission == 2:
            query_dict.update({"link": data.get("submission")})
        else:
            query_dict.update({"file": self.encode_image(file.get("submission"))})
            
        try:
            Submission.objects.create(**query_dict)
        except Exception as e:
            print(f"Error on creating submission data {e}")
            return None, e