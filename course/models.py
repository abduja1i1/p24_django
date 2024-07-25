from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "subject"

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subjects = models.ManyToManyField(Subject, related_name="speciality")

    class Meta:
        verbose_name_plural = "Specialities"
        verbose_name = "Speciality"
        db_table = "speciality"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    email = models.EmailField(max_length=56)
    salary = models.DecimalField(max_digits=26, decimal_places=2)
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
    subjects = models.ManyToManyField(Subject, related_name="teachers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    username = models.CharField(max_length=56)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="info")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=56)
    address = models.TextField()

    class Mete:
        verbose_name_plural = "StudentInfo"
        verbose_name = "StudentInfo"
        db_table = "StudentInfo"

    def __str__(self):
        return f"{self.email}"

