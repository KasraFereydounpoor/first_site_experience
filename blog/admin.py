from django.contrib import admin

from blog.models import Post

# Register your models here.
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    #fields = ('title',)
    list_display = ('title', 'counted_views' , 'status','published_date' , 'created_date')
    list_filter = ('status' ,)
    #ordering = ['-created_date']
    search_fields = [ 'title' , 'content'] 
    
admin.site.register(Post , PostAdmin)
#@admin.register(Post)
#u can register like this 