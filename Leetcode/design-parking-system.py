class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big:
                self.big -= 1
            else:
                return False
        elif carType == 2:
            if self.medium:
                self.medium -= 1
            else:
                return False
        else:
            if self.small:
                self.small -= 1
            else:
                return False
        return True
