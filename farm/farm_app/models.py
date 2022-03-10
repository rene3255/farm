from django.db import models

class Breed(models.Model):
  description = models.CharField(max_length=20)

  def __str__(self):
    return self.description

# Create your models here.

class Rabbit(models.Model):
  image = models.ImageField(upload_to='media/', null=False, blank=False)
  name=models.CharField(max_length=30)
  birth_date=models.DateField()
  purity=models.IntegerField()
  weight=models.DecimalField(max_digits=2, default=0.0, decimal_places=1)
  breed=models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='rabbit_breed')

  def __str__(self):
    return self.name

class Supply(models.Model):
  acquisition_date=models.DateField()
  folio=models.IntegerField()
  quantity=models.IntegerField()
  description=models.CharField(max_length=150)

  def __str__(self):
    return self.description

class Diary(models.Model):
  note=models.TextField()
  note_date=models.DateField()
  weight=models.DecimalField(max_digits=2, default=0.0, decimal_places=1)
  weight_date=models.DateField()
  rabbit=models.ForeignKey(Rabbit, on_delete=models.CASCADE)

  def __str__(self):
    return self.note
