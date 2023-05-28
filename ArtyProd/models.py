from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    

class equipe(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Equipes"

class Service(models.Model):
    Services = [
        ("graphic design", "graphic design"),
        ("Web Design", "Web Design"),
        ("Vaudiovisual production", "audiovisual production"),
        (" Animation 3D ", "Animation 3D ")
    ]
    ServiceName = models.CharField(
        choices=Services, default="Web Design", max_length=50)
    Ser_description = models.TextField(null=True)
    img = models.ImageField(upload_to='servicesPhoto/', blank=True)
    tag = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.ServiceName


class Personel(models.Model):
    POSTS = [
        ('Graphic Designer', 'Graphic Designer'),
        ('Web Designer', 'Web Designer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Creative Director', 'Creative Director'),
        ('Art Director', 'Art Director'),
        ('Copywriter', 'Copywriter'),
        ('Web Developer', 'Web Developer'),
    ]
    nom = models.CharField(max_length=50)
    file_cv = models.FileField(
        upload_to='cv/', max_length=100, blank=True)
    post = models.CharField(choices=POSTS, max_length=50,
                            default='Graphic Designer')
    photo = models.ImageField(upload_to='perPhoto/', blank=True)
    eqp = models.ForeignKey(equipe, on_delete=models.CASCADE)
    linkedin_url = models.URLField(null=True)
    fcb_url = models.URLField(null=True)
    github_url = models.URLField(null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Personnels"


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Demande(models.Model):
    TYPE_CHOICES = [
        ("Web Design", "Web Design"),
        ("conception 3D", "Conception 3D"),
        ("production audiovisuelle", "Production audiovisuelle"),
        ("design graphique", "Design graphique"),
    ]

    client_name = models.CharField(max_length=50, null=True)
    number_client = models.CharField(max_length=50, null=True)
    Type = models.CharField(choices=TYPE_CHOICES, default="Web Design", max_length=50)
    image = models.ImageField(upload_to="photos/", blank=True)
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    


class Project(models.Model):
    DONE = [
        ("Planning", "Planning"),
        ("In progress", "In progress"),
        ("Reviewing", "Reviewing"),
        ("Completed", "Completed"),
        ("Required", "Required"),
    ]
    client_name = models.CharField(max_length=50 , null=True)
    number_client = models.CharField(max_length=50 , null=True)
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    type = models.ManyToManyField(Service, blank=True)
    description = models.TextField()

    image = models.ImageField(upload_to="photos/")
    team = models.OneToOneField(Team, on_delete=models.CASCADE, null=True)
    dateD = models.DateField(auto_now_add=True)
    dateF = models.DateField(blank=True, null=True)
    status = models.CharField(choices=DONE, max_length=50, default="Required")

    def get_tags(self):
        return [service.tag for service in self.type.all()]

    def __str__(self):
        return self.libelle
