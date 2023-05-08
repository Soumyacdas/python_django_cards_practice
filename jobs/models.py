from django.db import models

# Create your models here.
class Jobs(models.Model):
    job=models.CharField(max_length=150)
    description=models.TextField()
    def __str__(self):
        return self.job
class Personal(models.Model):
    name=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    profile_pic=models.ImageField(upload_to='profile')
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()

    def __str__(self):
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
class Entry(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    authors=models.ManyToManyField(Author)
    rating=models.IntegerField()

    def __str__(self):
        return self.headline
    

