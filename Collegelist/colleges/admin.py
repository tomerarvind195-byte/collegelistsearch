from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'phone',
        'city',
        'state',
        'target_exam',
        'preferred_stream',
    )

    search_fields = (
        'user__username',
        'first_name',
        'last_name',
        'email',
    )