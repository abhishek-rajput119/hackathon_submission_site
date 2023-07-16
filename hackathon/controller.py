from .models import Hackathon,Registration,Submission
from .constants import User
import datetime
import base64
from hackathon_submission_site.settings import BASE_DIR
class HackthonUtil:
    def add_hackathon(self, data):
        # if data.user.id is None:
        #     return None, User.NOT_LOGGED_IN
        dir_path = str(BASE_DIR) +"/hackathon_images"
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
            'background_image':self.create_file(data.FILES.get('background_image'), dir_path),
            'hackathon_image':self.create_file(data.FILES.get('hackathon_image'), dir_path)
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
        dir_path = str(BASE_DIR) + "/submission_images"
        query_dict = {
            "hackathon_id" : hackathon_obj.id,
            "user_id" : user.id,
            "title" : data.get("title"),
            "summary" : data.get("summary"),
        }
        if hackathon_obj.type_of_submission == 2:
            query_dict.update({"link": data.get("submission")})
        else:
            query_dict.update({"file": self.create_file(file.get("submission"), dir_path)})
            
        try:
            Submission.objects.create(**query_dict)
        except Exception as e:
            print(f"Error on creating submission data {e}")
            return None, e
        
    def create_file(self, file, output_path):
        try:
            name = file.name
            file_obj = file.read()
            file_path = output_path + "/" + name
            if file_obj != "":
                with open(file_path, mode="wb") as file:
                    file.write(file_obj)
                return file_path

            return None
        except Exception as e:
            print(f"Error while creating image to upload : {e}")
            return None
