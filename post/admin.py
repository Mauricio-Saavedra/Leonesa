from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Vamos a crear una tabla más completa sobre los valores de los Post:
    list_display = ('id','image','title','content','created',)
    list_display_links = ('id','title',)	#Con esto hacemos que haya un link directo a la publicación desde el titulo.
    # Filtros:
    list_filter = ('created',)
    #Buscador
    search_fields = ('title', 'content',)
    # Si queremos que se muestren datos que no aparecen, epro que solo se muestren y no se editen se hace:
    readonly_fields = ('created',)