from django.db import models
# from ckeditor_uploader.fields import RichTextField
from django.core.validators import RegexValidator, MinValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
#
# from taggit.managers import TaggableManager


class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Image = models.ImageField()
    Content = RichTextUploadingField(blank=True)
    Tag = models.CharField(max_length=200)
    imageHeading = models.CharField(max_length=220, null=True)
    Slug = models.SlugField(max_length=200, unique=True)
    Date = models.DateField(auto_now_add=True)
    ###############################################################################
    # tags = TaggableManager()

    class Meta:
        ordering = ('-Date', '-pk',)

    def __str__(self):
        return self.Title

    def __unicode__(self):
        return u'%s' % self.Title


class Comment(models.Model):
    Post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Body = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default=True)
    Parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return ('Comment By {}'.format(self.Name))


class Contact(models.Model):
    name = models.CharField(max_length=55, default='')
    email = models.EmailField(max_length=255)
    phone_no = models.IntegerField(validators=[RegexValidator(
        "^0?[5-9]{1}\d{9}$")], null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.name


class SubscribeNewsletter(models.Model):
    subscriberemail = models.EmailField(max_length=255)

    def __str__(self):
        return self.subscriberemail


class LetsConnect(models.Model):
    firstname = models.CharField(max_length=55, default='')
    lastname = models.CharField(max_length=55, default='')
    lc_email = models.EmailField(max_length=255)
    lc_phone_no = models.IntegerField(validators=[RegexValidator(
        "^0?[5-9]{1}\d{9}$")], null=True, blank=True)
    lc_message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.firstname
