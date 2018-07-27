from django.db import models

class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280)
    #author = models.ForeignKey('users.User', verbose_name='Autor', on_delete=models.CASCADE, related_name='tuites')
    author = models.ForeignKey('users.User', verbose_name='Autor', default=1, on_delete=models.SET_DEFAULT, related_name='tuites')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    class Meta:
        # no painel, está ordenando os tuites pelo content (alfabeticamente por default)
        ordering = ('content', )