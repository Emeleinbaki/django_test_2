from django.contrib import admin
from blog.models import Post, Author, Category, CustomUser, Comments

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)

# class CustomUserAdmin(UserAdmin):
admin.site.register(CustomUser)
admin.site.register(Comments)