from django.contrib import admin

from .models import Address, Author, Book


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
