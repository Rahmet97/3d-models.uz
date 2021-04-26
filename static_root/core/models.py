from django.db import models
from django.urls import reverse
from urllib.parse import urlparse, parse_qs
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify

class AboutUs(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name="Title")

    image = models.ImageField(upload_to="about-us-images/%Y/%m/%d/", blank=True, null=True, verbose_name='Image')
    video = models.FileField(upload_to='about-us-videos/%Y/%m/%d/', blank=True, null=True, verbose_name='Video')

    description = models.TextField(verbose_name="Description")

    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + " | " + str(self.pk)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url
    class Meta:
        ordering = ["pub_date"]
        verbose_name_plural = "About Us"

class VideoModel(models.Model):
    video_url   = models.URLField(unique=True, blank=True, null=True, verbose_name='Video URL')
    video_file  = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, null=True, verbose_name='Video File')

    title       = models.CharField(max_length=300, verbose_name='Video Title')
    description = models.TextField(verbose_name='Video Description')

    published_at = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['-published_at',]
        verbose_name_plural="Videos"
    
    def __str__(self):
        return self.title
    
    def extract_video_id(self):
        # Examples:
        # - http://youtu.be/SA2iWivDJiE
        # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        # - http://www.youtube.com/embed/SA2iWivDJiE
        # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        if self.video_url:
            query = urlparse(self.video_url)
            if query.hostname == 'youtu.be': return query.path[1:]
            if query.hostname in {'www.youtube.com', 'youtube.com'}:
                if query.path == '/watch': return parse_qs(query.query)['v'][0]
                if query.path[:7] == '/embed/': return query.path.split('/')[2]
                if query.path[:3] == '/v/': return query.path.split('/')[2]
        # fail?
        return None




class PortFolio(models.Model):
    image       = ImageField(upload_to="portfolio/%Y/%m/%d/", verbose_name='Image')
    caption     = models.CharField(max_length=300, blank=True, null=True, verbose_name='Caption')

    name        = models.CharField(max_length=300, verbose_name='Name')
    slug        = models.SlugField(max_length=320)

    short_info  = models.CharField(max_length=500, default="3D model", verbose_name="Short Info")
    description = models.TextField(verbose_name='Description')
    
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['published_at', 'updated_at']
        verbose_name_plural = 'PortFolio'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('Core:portfolio-detail-view', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def is_updated(self):
        if self.published_at == self.updated_at:
            return self.published_at
        else:
            self.updated_at
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Images(models.Model):
    portfolio   = models.ForeignKey(PortFolio,  on_delete=models.CASCADE, related_name="portfolio_images", verbose_name="3D Model")
    image  = ImageField(upload_to='portfolio-images/%Y/%m/%d/', verbose_name="Image")
    caption = models.CharField(max_length=300, blank=True, null=True, verbose_name='Caption:')
    
    class Meta:
        verbose_name_plural = "Portfolio' Images"

    def __str__(self):
        return self.portfolio.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 



class ArticleModel(models.Model):
    image        = models.ImageField(upload_to="article/%Y/%m/%d/", verbose_name='Image')
    caption      = models.CharField(max_length=300, blank=True, null=True, verbose_name='Caption')

    title        = models.CharField(max_length=350, unique=True, verbose_name='Title')
    slug         = models.SlugField(max_length=400)
    description  = models.TextField(verbose_name='Description')
    author       = models.CharField(max_length=50, default='Mehroj', verbose_name = 'Author')
    view_counter = models.PositiveIntegerField(default=0)

    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    updated_at   = models.DateTimeField(auto_now=True, verbose_name='Updated')

    class Meta:
        ordering            = ['published_at', 'updated_at',]
        verbose_name        = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("Core:article-detail-view", kwargs={"slug": self.slug})
    
    def is_updated(self):
        if self.published_at == self.updated_at:
            return self.published_at
        else:
            return self.updated_at
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    