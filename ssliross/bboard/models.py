
from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from ssliross.settings import ALLOWED_HOSTS
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .utilities import get_timestamp_path

class Hero(models.Model):
    top = models.CharField(max_length=200, verbose_name='Top Text')
    bottom = models.CharField(max_length=200, verbose_name='Bottom Text')
    is_active = models.BooleanField(default=True,db_index=True, verbose_name='In Slider?')
    class Meta:
        verbose_name_plural = 'Sliders'
        verbose_name = 'slider'
        ordering = ['is_active']

class Works(models.Model):
    cetegory = models.ForeignKey('Category', on_delete=models.CASCADE)
    name_work = models.CharField(max_length=20, verbose_name='Name')
    description = models.CharField(max_length=150, verbose_name='Description')
    is_active = models.BooleanField(default=True,db_index=True, verbose_name='In work?')
    image = models.ImageField(blank=False, upload_to = get_timestamp_path, verbose_name='Image')
    class Meta:
        verbose_name_plural = 'Works'
        verbose_name = 'Work'
        ordering = ['is_active']


class Category(models.Model):
    namee = models.CharField(max_length=20, verbose_name='Category')

    def __str__(self):
        return self.namee
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
class OurAvesome(models.Model):
    textt = models.CharField(max_length=20, verbose_name='Text')
    textt2 = models.TextField(verbose_name='Description')
    class Meta:
        verbose_name_plural = 'OurAwesomes'
        verbose_name = 'OurAwesome'


class DescriptionOur(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Description', blank=False)
    is_active = models.BooleanField(default=True, verbose_name='In work?')
    class Meta:
        verbose_name_plural = 'Our Description'
        verbose_name = 'Our Description'
        ordering = ['is_active']

class WhoAreWe(models.Model):
    who_are = models.CharField(max_length=30, verbose_name='Table of contents')
    description_who = models.TextField(verbose_name='Description')
    class Meta:
        verbose_name = 'Who are We'
        verbose_name_plural = 'Who are We'

class OurProc(models.Model):
    text1 = models.CharField(max_length=30, blank=False, verbose_name='Category')
    text2 = models.TextField(verbose_name='description')
    class Meta:
        verbose_name_plural = 'Our Proc'
        verbose_name = 'Our Proc'

class OurTeam(models.Model):
    name = models.CharField(max_length=20,blank=False, verbose_name='Name')
    position = models.CharField(max_length=20, verbose_name='Position')
    description = models.TextField(blank=True,verbose_name='Description')
    facebook = models.CharField(max_length=60,blank=True, verbose_name='Facebook')
    twitter = models.CharField(max_length=60,blank=True, verbose_name='Twitter')
    skype = models.CharField(max_length=60,blank=True, verbose_name='Skype')
    gmail = models.EmailField(max_length=60,unique=True, verbose_name='Gmail')
    image = models.ImageField(upload_to=get_timestamp_path,blank=True, verbose_name='Image')
    is_active = models.BooleanField(default=True, verbose_name='In work?')
    class Meta:
        verbose_name_plural = 'OurTeam'
        verbose_name = 'OurTeam'

class Button(models.Model):
    text = models.CharField(max_length=60, blank=False, verbose_name='Text')
    description = models.TextField(verbose_name='Desc')
    is_active = models.BooleanField(verbose_name='In Page?', default=False)
    button = models.CharField(max_length=40, blank=True, verbose_name='Text on button')
    class Meta:
        verbose_name='Button and Text'
        verbose_name_plural = 'Button and Text'
        ordering = ['is_active']

class Feedback(models.Model):
    name = models.CharField(max_length=40, blank=False, verbose_name='Name')
    avatar = models.ImageField(upload_to=get_timestamp_path, blank=True, verbose_name='Avatar')
    description = models.TextField(verbose_name='Desc')
    is_active= models.BooleanField(default=True, verbose_name='In feedback?')
    class Meta:
        verbose_name='Feedback'
        verbose_name_plural = 'Feedbacks'

class GetInTuch(models.Model):
    contactName = models.CharField(max_length=50, blank=False, verbose_name='Name')
    contactEmail = models.EmailField(verbose_name='Email', blank=False)
    contactSubject = models.CharField(max_length=60, verbose_name='Subject')
    contactMessage = models.TextField(blank=False, verbose_name='Message')
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date')
    def __str__(self):
        return self.contactName
    class Meta:
        verbose_name='1Customer'
        verbose_name_plural = '1Customers'
        ordering = ['date']

class CompanyData(models.Model):
    description = models.CharField(max_length=250, verbose_name='Text')
    adress = models.CharField(max_length=80,verbose_name='Address')
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, verbose_name='Phone Number')
    facebook = models.CharField(max_length=40, verbose_name='Facebook')
    twitter = models.CharField(max_length=40, verbose_name='Twitter')
    youtube = models.CharField(max_length=40, verbose_name='YouTube')
    vimeo = models.CharField(max_length=40, verbose_name='Vimeo')
    flick = models.CharField(max_length=40, verbose_name='Flickr')
    skype = models.CharField(max_length=40, verbose_name='Skype')
    num = models.SmallIntegerField(verbose_name='Number')
    class Meta:
        verbose_name = 'Company Data'
        verbose_name_plural = 'Company Data'




def send_customer(sender, **kwargs):
    if kwargs['created']:
        
        xxx = kwargs['instance'].contactName
        context = { 'xxx':xxx }
        subject_text = render_to_string('email/activation_letter_subject.txt', context)
        body_text = render_to_string('email/activation_letter_body.txt', context)
        x = kwargs["instance"].contactEmail
        ce = EmailMessage(subject=subject_text, body=body_text, to=['asdasdsad@dsd.sad'])
        ce.send()

post_save.connect(send_customer, sender=GetInTuch)
