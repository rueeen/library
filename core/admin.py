from django.contrib import admin
from .models import Book, Category, Country, Author

# Register your models here.
# It makes the id field read-only.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id')

# It makes the id field readonly.
class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('id')

# Registering the Book model with the admin site.
admin.site.register(Book)
# Registering the Category model with the admin site.
admin.site.register(Category)
# Registering the Author model with the admin site.
admin.site.register(Author)
# Registering the Country model with the admin site.
admin.site.register(Country)
