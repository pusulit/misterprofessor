from django.db import models
from django.contrib.auth.models import User
from misterprofessor import constant
from django.forms import ModelForm, widgets
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User)
    skype = models.CharField(max_length=50)
    hangout = models.CharField(max_length=50)
    feedback = models.IntegerField()
    firstlanguage = models.CharField(max_length=3, choices=constant.LANGUAGES)
    secondlanguage = models.CharField(max_length=3, choices=constant.LANGUAGES)
    thirdlanguage = models.CharField(max_length=3, choices=constant.LANGUAGES)
    def  __unicode__(self):
        return self.user.username
    def toList(self):
        return self.skype + "" + self.hangout

class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Profile)
    language = models.CharField(max_length=3, choices=constant.LANGUAGES)
    description = models.CharField(max_length=300)
    lessons = models.IntegerField()
    def __unicode__(self):
        return self.name
    
class Lesson(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    time = models.DateTimeField()
    def __unicode__(self):
        return self.name
    
class Subscription(models.Model):
    student = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    subscription = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.student.username + " at " + self.course.name
    
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def  __unicode__(self):
        return self.name

class MenuElement(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu)
    order = models.IntegerField(default=100)
    text = models.CharField(max_length=50)
    link  = models.CharField(max_length=50)
    def  __unicode__(self):
        return self.text

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'skype', 'hangout']
        
class SearchForm(forms.Form):
    languages = forms.MultipleChoiceField(required=False, widget=forms.SelectMultiple, choices=constant.LANGUAGES)
