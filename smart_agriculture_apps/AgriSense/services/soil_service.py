from models import Soil

class SoilService:
    @staticmethod
    def get_soil_moisture(soil_id):
        soil = Soil.query.get(soil_id)
        return soil.moisture_level if soil else None
