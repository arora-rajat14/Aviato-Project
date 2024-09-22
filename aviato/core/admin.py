from django.contrib import admin
from .models import Candidate


# Customizing the CandidateAdmin class
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone_number",
        "age",
        "gender",
        "created_at",
        "modified_at",
    )

    search_fields = ("name", "email", "phone_number")
    list_filter = ("age", "gender")
    readonly_fields = ("id", "created_at", "modified_at")


admin.site.register(Candidate, CandidateAdmin)
