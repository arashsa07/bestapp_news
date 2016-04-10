from django.db import models
from tinymce import models as tinymce_models
from django.core.urlresolvers import reverse


class Agency(models.Model):
    name = models.CharField('Agency Name', max_length=50, unique=True)

    class Meta:
        db_table = 'agencies'
        verbose_name_plural = 'agencies'

    def __unicode__(self):
        return '%s' % self.name


class News(models.Model):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField('Photo',  upload_to="news", blank=True)
    body = tinymce_models.HTMLField()
    source = models.CharField('Source', max_length=70)
    writer = models.ForeignKey('Person', related_name='news_writer')
    date_added = models.DateTimeField('Added Date', auto_now_add=True)
    date_modify = models.DateTimeField('Modified Date', auto_now=True)

    class Meta:
        db_table = 'news'
        verbose_name_plural = 'news'

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('view_news_post', None, [self.id, self.slug])

    @property
    def url(self):
        return self.get_absolute_url()


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='category_childs', null=True, blank=True)
    agency = models.ForeignKey('agency')
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'
        unique_together = ('agency', 'parent', 'title')

    def __unicode__(self):
        return '%s - %s' % (self.agency, self.title)

    def clean(self):
        if self.slug:
            self.slug = self.slug.lower()

#    def get_absolute_url(self):
#        return ('view_news_category', None, { 'slug': self.slug })


class Person(models.Model):
    name = models.CharField('Name', max_length=50)
    family = models.CharField('Family', max_length=50)
    photo = models.ImageField('Photo',  upload_to="people", blank=True)
    email = models.EmailField('Email', blank=True)

    @property
    def person_name(self):
        return "%s %s" % (self.name, self.family)

    class Meta:
        db_table = 'person'

    def __unicode__(self):
        return "%s %s" % (self.name, self.family)
