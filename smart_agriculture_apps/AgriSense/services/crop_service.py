from models import Crop

class CropService:
    @staticmethod
    def get_crop_health(crop_id):
        crop = Crop.query.get(crop_id)
        return crop.health_status if crop else None
