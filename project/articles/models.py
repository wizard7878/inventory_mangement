from django.db import models
# from .utils import slugify_instance_title
from django.db.models.signals import pre_save,post_save
import random
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)


def slugify_instance_title(instance,save=False, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(300_000,500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance,save,new_slug= slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance

def article_pre_save(sender, instance ,*args,**kwargs):
    print("Pre Save")
    print(args,kwargs)
    if instance.slug is None:
        slugify_instance_title(instance)


pre_save.connect(article_pre_save,sender=Article)


def article_post_save(sender, instance , created,*args,**kwargs):
    print("Post Save")
    print(args,kwargs)
    slugify_instance_title(instance,created)


post_save.connect(article_post_save,sender=Article)