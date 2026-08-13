from django.contrib import admin
from .models import Resident, Room

@admin.register(Resident)
class ResidentAdmin( admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "gender",
        "nationality",
        "phone",
        "status",
        "admission_date",
    )

    search_fields = (
        "first_name",
        "last_name",
        "phone",
    )

    list_filter = (
        "gender",
        "status",
        "admission_date",
    )

    ordering = (
        "last_name",
        "first_name",
    )

    fieldsets = (
        ("Information personnelles", {
            "fields": (
                "photo",
                "first_name",
                "last_name",
                "birth_date",
                "gender",
                "nationality",
            )
        }),
        ("Contact", {
            "fields":(
                "phone",
                "emergency_contact",
                "emergency_phone",
            )
        }),
        ("Informations médicales", {
            "fields":(
                "allergies",
                "diseases",
                "medical_notes",
            )
        }),
        ("Autres", {
            "fields":(
                "observations",
                "status",
                "admission_date",
            )
        }),
    )

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "capacity", "occupancy", "is_full")
    search_fields = ("number",)
