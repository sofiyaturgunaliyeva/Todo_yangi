from django.db import models
from django.contrib.auth.models import User



class Talaba(models.Model):
    ism = models.CharField(max_length=20)
    yosh = models.SmallIntegerField()
    kurs = models.SmallIntegerField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.ism

class Plan(models.Model):
    HOLATLAR = (
        ("Yangi","Yangi"),
        ("Bajarilyapti","Bajarilyapti"),
        ("Bajarildi","Bajarildi")
    )
    sarlavha = models.CharField(max_length=150)
    batafsil = models.TextField()
    holat = models.CharField(max_length=20,choices=HOLATLAR)
    vaqt = models.DateField(auto_now_add=True)
    talaba = models.ForeignKey(Talaba,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.sarlavha


