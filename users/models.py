from django.db import models

class Fanlar(models.Model):
    f_name = models.CharField(max_length=128)


    def __str__(self):
        return self.f_name
    
    class Meta:
        verbose_name = 'FAN'
        verbose_name_plural= 'FANLAR'



class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    tel_num = models.IntegerField()
    fan = models.ForeignKey(Fanlar,on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    

    class Meta:
        verbose_name = 'STUDENT'
        verbose_name_plural= 'STUDENTS'

        

        
