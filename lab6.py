class OpticalDisc:
    def __init__(self, capacity, rotations, laser_thickness_nm):
        self.capacity = capacity  
        self.rotations = rotations  
        self.laser_thickness_nm = laser_thickness_nm  

    def bytes_per_20_seconds(self):
        bytes_per_rotation = self.capacity / (self.rotations * 60)
        return bytes_per_rotation * 20

    def __add__(self, other):
        if isinstance(other, self.__class__):
            new_capacity = self.capacity + other.capacity
            return self.__class__(
                capacity=new_capacity,
                rotations=self.rotations,  
                laser_thickness_nm=self.laser_thickness_nm,  
                **self._get_additional_args()  
            )
        else:
            raise TypeError(f"Нельзя сложить {self.__class__.__name__} с {other.__class__.__name__}")

    def _get_additional_args(self):
        return {}


class CD(OpticalDisc):
    def __init__(self, capacity, rotations, laser_thickness_nm, cd_type="Unknown"):
        super().__init__(capacity, rotations, laser_thickness_nm)
        self.cd_type = cd_type

    def average_rotation_time(self):
        return 60 / self.rotations 

    def _get_additional_args(self):
        return {"cd_type": self.cd_type}


class DVD(OpticalDisc):
    def __init__(self, capacity, rotations, laser_thickness_nm, dvd_layer=1):
        super().__init__(capacity, rotations, laser_thickness_nm)
        self.dvd_layer = dvd_layer  

    def average_rotation_time(self):
        return 60 / self.rotations  

    def _get_additional_args(self):
        return {"dvd_layer": self.dvd_layer}


if __name__ == "__main__":
    cd1 = CD(capacity=700 * 1024 * 1024, rotations=200, laser_thickness_nm=780, cd_type="CD-R")
    cd2 = CD(capacity=800 * 1024 * 1024, rotations=200, laser_thickness_nm=780, cd_type="CD-RW")

    dvd1 = DVD(capacity=4700 * 1024 * 1024, rotations=1200, laser_thickness_nm=650, dvd_layer=2)
    dvd2 = DVD(capacity=8500 * 1024 * 1024, rotations=1200, laser_thickness_nm=650, dvd_layer=2)

    cd_sum = cd1 + cd2
    print(f"CD1 + CD2: Ёмкость = {cd_sum.capacity / (1024 * 1024)} МБ, Тип = {cd_sum.cd_type}")

    dvd_sum = dvd1 + dvd2
    print(f"DVD1 + DVD2: Ёмкость = {dvd_sum.capacity / (1024 * 1024)} МБ, Слоёв = {dvd_sum.dvd_layer}")

    try:
        invalid_sum = cd1 + dvd1
    except TypeError as e:
        print(e)