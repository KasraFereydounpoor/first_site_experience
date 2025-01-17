from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    
    
    class Meta:
        ordering = ['-created_date']

    #in dige generale faghat marbut be menuye admin nist
    def __self__(self):
        return "{} - {} ".format(self.title , self.id)
    