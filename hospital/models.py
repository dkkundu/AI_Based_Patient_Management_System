from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from address.models import District, Division, Upazila
from django.utils.translation import gettext_lazy as _


class Slider(models.Model):
    caption = models.CharField(max_length=150)
    slogan = models.CharField(max_length=120)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.caption[:20]

    class Meta:
        verbose_name_plural = 'Slider'


class Speciality(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Doctor Speciality'


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    items = models.ManyToManyField(to='Item',)
    thumbnail = models.ImageField(upload_to='services/')
    cover = models.ImageField(upload_to='services/')
    image1 = models.ImageField(upload_to='services/', blank=True, null=True)
    image2 = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="doctor"
    )
    name = models.CharField(max_length=120, null=True, blank=True)

    speciality = models.ForeignKey(
        Speciality, on_delete=models.PROTECT,
        blank=True, null=True, related_name="speciality"
    )
    picture = models.ImageField(
        upload_to="doctors/", null=True, blank=True
    )
    details = models.TextField(blank=True, null=True)
    present_hospital = models.CharField(max_length=120, blank=True, null=True)
    expertize = models.ManyToManyField(to='Expertize', blank=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    division = models.ForeignKey(
        Division, models.SET_NULL,
        related_name='doctor_division',
        null=True
    )
    district = models.ForeignKey(
        District, models.SET_NULL,
        related_name='doctor_district',
        null=True
    )
    upazila = models.ForeignKey(
        Upazila, models.SET_NULL,
        related_name='doctor_upazila',
        null=True
    )
    post_code = models.PositiveIntegerField(
        null=True,
        help_text='Numeric 4 digits (ex: 1234)',
        validators=[RegexValidator(
            r"^[\d]{4}$", message='Numeric 4 digits (ex: 1234)'
        )]
    )
    address = models.TextField(
        null=True, help_text='Ex: 2/17, Mirpur-11'
    )

    def __str__(self):
        return str(self.name)

    @property
    def get_full__address(self):
        save_present_address = ''
        if self.address:
            save_present_address = ''.join(self.address)
        if self.upazila:
            save_present_address += f', {self.upazila} ,'
        if self.district:
            save_present_address += f' {self.district}'
        if self.post_code:
            save_present_address += f' - {self.post_code} ,'
        if self.division:
            save_present_address += f'{self.division} ,'
        save_present_address += 'Bangladesh '

        return save_present_address


class Expertize(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Gallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galleries"


class Contact(models.Model):
    name = models.CharField(
        max_length=120, null=True, blank=True
    )
    email = models.EmailField(
        _('Email Address'), max_length=255, blank=True, null=True
    )
    phone = models.CharField(
        _('Mobile Phone'), max_length=12, unique=True,
        validators=[RegexValidator(  # min: 10, max: 12 characters
            r'^[\d]{10,12}$', message='Format (ex: 0123456789)'
        )]
    )
    subject = models.CharField(
        max_length=120, null=True
    )

    message = models.TextField(
        blank=True, null=True
    )
    response = models.BooleanField(
        default=False
    )

    def __str__(self):
        return str(self.name)
