class OpticalDisc:
    def __init__(self, capacity, rotations, laser_thickness_nm):
        self.capacity = capacity  
        self.rotations = rotations  
        self.laser_thickness_nm = laser_thickness_nm  

    def bytes_per_20_seconds(self):
        bytes_per_rotation = self.capacity / (self.rotations * 60)
        return bytes_per_rotation * 20

class CD(OpticalDisc):
    def __init__(self, capacity, rotations, laser_thickness_nm, cd_type):
        super().__init__(capacity, rotations, laser_thickness_nm)
        self.cd_type = cd_type 

    def average_rotation_time(self):
        return 60 / self.rotations 

class DVD(OpticalDisc):
    def __init__(self, capacity, rotations, laser_thickness_nm, dvd_layer):
        super().__init__(capacity, rotations, laser_thickness_nm)
        self.dvd_layer = dvd_layer  

    def average_rotation_time(self):
        return 60 / self.rotations 

if __name__ == "__main__":
    cd = CD(capacity=700 * 1024 * 1024, rotations=200, laser_thickness_nm=780, cd_type="CD-R")
    dvd = DVD(capacity=4700 * 1024 * 1024, rotations=1200, laser_thickness_nm=650, dvd_layer=2)

    print(f"CD: Байт за 20 секунд: {cd.bytes_per_20_seconds()}")
    print(f"CD: Среднее время одного оборота: {cd.average_rotation_time()} секунд")

    print(f"DVD: Байт за 20 секунд: {dvd.bytes_per_20_seconds()}")
    print(f"DVD: Среднее время одного оборота: {dvd.average_rotation_time()} секунд")