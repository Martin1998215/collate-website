from django.contrib import admin
from . models import My_business, Message, My_updates, Updates


class My_businessAdmin(admin.ModelAdmin):
    list_display = ("name", "business_type",
                    "phone_number", "email", "location")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("business_name", "business_type",
                    "phone_number", "email", "message")


class My_updatesAdmin(admin.ModelAdmin):
    show_updates = ("title", "text", "my_date", "posted_by")


admin.site.register(Message, MessageAdmin)
admin.site.register(My_business, My_businessAdmin)
admin.site.register(Updates, My_updatesAdmin)

admin.site.site_header = "Landing Page"
admin.site.site_title = "Collate AI"
admin.site.index_title = "Welcome To Collate AI"

# Register your models here.
