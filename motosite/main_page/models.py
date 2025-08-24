from django.db import models

# Create your models here.
class Motorcycle(models.Model):
    brand = models.ForeignKey('MotorcycleBrand', on_delete=models.PROTECT, null=True)
    model = models.CharField(max_length=100)
    type = models.ForeignKey('MotorcycleType', on_delete=models.PROTECT, null=True)
    engine = models.ForeignKey('EngineType', on_delete=models.PROTECT, null=True)
    engine_displacement = models.IntegerField()
    power = models.IntegerField()
    transmission = models.ForeignKey('TransmissionType', on_delete=models.PROTECT, null=True)
    number_of_gears = models.IntegerField(blank=True, null=True)
    drive_system = models.ForeignKey('DriveSystem', on_delete=models.PROTECT, null=True)
    brakes = models.CharField(max_length=100)
    suspension = models.CharField(max_length=100)
    weight = models.IntegerField()
    length = models.FloatField()
    seat_height = models.IntegerField()
    wheelbase = models.IntegerField()
    top_speed = models.IntegerField()
    description = models.TextField()
    image_link = models.URLField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.type}"

    class Meta:
        db_table = "motorcycle"
        verbose_name = "Motorcycle"
        verbose_name_plural = "Motorcycles"

class MotorcycleType(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = "motorcycle_type"
        verbose_name = "MotorcycleType"
        verbose_name_plural = "MotorcycleTypes"

class EngineType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = "engine_type"
        verbose_name = "EngineType"
        verbose_name_plural = "EngineTypes"

class TransmissionType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = "transmission_type"
        verbose_name = "Transmission"
        verbose_name_plural = "Transmissions"

class DriveSystem(models.Model):
    system_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.system_type}"

    class Meta:
        db_table = "drive_system"
        verbose_name = "Drive System"
        verbose_name_plural = "Drive Systems"

class MotorcycleBrand(models.Model):
    brand = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.brand}"

    class Meta:
        db_table = "motorcycle_brand"
        verbose_name = "MotorcycleBrand"
        verbose_name_plural = "MotorcycleBrands"
