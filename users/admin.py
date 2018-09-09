from django.contrib import admin

from tuites.models import Tuite
from users.models import User


class InlineTuiteAdmin(admin.StackedInline):
    model = Tuite


# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('following', )
    readonly_fields = ('username', )
    inlines = [InlineTuiteAdmin, ]
    fieldsets = (
        ('Dados pessoais', {
            'fields': ('username', 'email', 'date_joined'),
        }),
        ('Tuirer', {
            'fields': ('following', 'followers'),
            'description': 'Coisas relacionadas ao nosso sistema',
        })
    )


admin.site.register(User, UserAdmin)
