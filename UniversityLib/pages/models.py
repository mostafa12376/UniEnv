from django.db import models
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class Book(models.Model):

    cat=(('Fantasy','Fantasy'),
    ('Sci-fi','Sci-fi'),
    ('Mystery','Mystery'),
    ('Programming Language','Programming Language'),
    ('Autobiography','Autobiography'),
    ('Historical','Historical'),
    ('Technologies','Technologies'),
    ('Guide / How-to','Guide / How-to'),
    ('Families & Relationships','Families & Relationships'))

    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 300, null = True)
    ISBN = models.CharField(max_length = 13,unique = True)
    pubYear = models.IntegerField(null = True, blank = True)
    category = models.CharField(max_length=24,choices= cat,default=cat[0])
    copies = models.IntegerField(default = 1)

    def __str__(self):
        return self.title

class Account(models.Model):

    user = models.OneToOneField(User,default=1, on_delete=models.CASCADE)
    borrowedBooks = models.ManyToManyField(Book, through = 'Borrow')

    def __str__(self):
        return self.user.username
'''
@receiver(post_save, sender=User)
def create_user_Account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_Account(sender, instance, **kwargs):
    instance.Account.save()
'''


class Borrow(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    borrowStartDate = models.DateField(default=timezone.now())
    borrowPeriod = models.IntegerField(default = 7)

    def __str__(self):
        return ("Borrowed "+self.book.title+" by "+self.account.user.username)
