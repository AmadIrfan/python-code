class cars:
    carBrandName = ""
    carColor = ""
    carModel = ""
    carPlateNumber = ""
    carRpd = 0
    carStatus = ""
    carConditions = ""

    def __init__(self,BrandName,carColor,carModel,PlateNumber,carRpd,carStatus,carConditions):
        self.carBrandName =BrandName  
        self.carColor = carColor 
        self.carModel = carModel 
        self.carPlateNumber = PlateNumber 
        self.carRpd = carRpd
        self.carStatus =carStatus  
        self.carConditions =carConditions  
