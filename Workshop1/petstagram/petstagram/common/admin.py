from django.contrib import admin

from petstagram.common.models import Comment, Like


# Register your models here.
@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass


@admin.register(Like)
class AdminLike(admin.ModelAdmin):
    pass