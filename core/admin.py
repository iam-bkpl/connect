from django.contrib import admin
from django.http import HttpResponse
import csv
import csv
from django.contrib import admin
from django.http import HttpResponse
from core.models import Membership

from core.models import (
    AdminBank,
    Timing,
    HomePageImage,
    AboutUs,
    Team,
    UsefulPage,
    Service,
    Partners,
    Event,
    MainService,
    Contact,
    Membership,
    SubscriptionPlan,
    UserContact,
    NewsLetter,
    MembershopPhoto,
    HomeAboutUs,
)

# from core.views import download_csv

from .csv_generator import generate_membership_csv


class MembershipAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "membership_duration"]

    def download_csv(self, request, queryset):
        # Generate the CSV file
        csv_data = generate_membership_csv()

        # Create the HTTP response with CSV file
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="memberships.csv"'

        # Write the CSV file content to the response
        writer = csv.writer(response)
        writer.writerow(["User", "Phone", "Membership Duration"])  # Add header row
        for membership in queryset:
            writer.writerow(
                [membership.user, membership.phone, membership.membership_duration]
            )

        return response

    download_csv.short_description = (
        "Download CSV"  # Action description in the admin site
    )


#


# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ["user", "phone", "membership_duration"]

#     def download_csv(self, request, queryset):
#         # Generate the CSV file
#         csv_data = generate_membership_csv()

#         # Create the HTTP response with CSV file
#         response = HttpResponse(content_type="text/csv")
#         response["Content-Disposition"] = 'attachment; filename="memberships.csv"'

#         # Write the CSV file content to the response
#         writer = csv.writer(response)

#         # Write the header row
#         header = [
#             "User",
#             "First Name",
#             "Last Name",
#             "Email",
#             "Address",
#             "Phone",
#             "Membership Type",
#             "Membership Duration",
#             "Agree Terms Condition",
#         ]
#         writer.writerow(header)

#         # Write the data rows
#         for membership in queryset:
#             data_row = [
#                 membership.user.username,
#                 membership.user.first_name,
#                 membership.user.last_name,
#                 membership.user.email,
#                 membership.address,
#                 membership.phone,
#                 membership.get_membership_type_display(),
#                 membership.get_membership_duration_display(),
#                 membership.agree_terms_condition,
#             ]
#             writer.writerow(data_row)

#         return response

#     download_csv.short_description = (
#         "Download CSV"  # Action description in the admin site
#     )


admin.site.add_action(MembershipAdmin.download_csv, "membership_download_csv")

admin.site.register(AdminBank)
admin.site.register(Timing)
admin.site.register(HomePageImage)
admin.site.register(AboutUs)
admin.site.register(HomeAboutUs)
admin.site.register(Team)
admin.site.register(Service)
admin.site.register(Partners)
admin.site.register(Event)
admin.site.register(MainService)
admin.site.register(Contact)
admin.site.register(Membership, MembershipAdmin)
# admin.site.register(Membership)
admin.site.register(SubscriptionPlan)
admin.site.register(UserContact)
admin.site.register(NewsLetter)
admin.site.register(UsefulPage)
admin.site.register(MembershopPhoto)
