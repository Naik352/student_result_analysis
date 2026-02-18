from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.PositiveIntegerField(unique=True)
    subject1 = models.PositiveIntegerField()
    subject2 = models.PositiveIntegerField()
    subject3 = models.PositiveIntegerField()
    address = models.CharField(max_length=50)

    def total(self):
        return self.subject1 + self.subject2 + self.subject3
    def percentage(self):
        return self.total() / 3
    def result(self):
        if self.subject1 >= 35 and self.subject2 >= 35 and self.subject3 >= 35:
            return "pass"
        else:
            return "fail"

        
    def __str__(self):
        return self.name
    

    


