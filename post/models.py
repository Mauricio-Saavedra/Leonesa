from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='post')
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return self.title
    
        #Con ésto debo ser capaz de editar el panel lateral
    class Meta:
        verbose_name='Publicación'
        verbose_name_plural='Publicaciones'
        ordering = ['-created'] #ésto es para que las publicaciones se muestren en el orden de creación
        app_label = 'post'