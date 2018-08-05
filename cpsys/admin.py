from django.contrib import admin
from django.db import models

from .models import TeamRecord, Member, SetSold, MailingList

admin.site.site_header = "Red 5 Saladmaster Admin"
admin.site.site_title = "Red 5 Saladmaster Admin Portal"
admin.site.index_title = "Welcome to Red 5 Saladmaster Admin Portal"
admin.site.disable_action("delete_selected")


@admin.register(TeamRecord)
class TeamRecordAdmin(admin.ModelAdmin):
    actions = [
        "delete_selected",
        "clear_points",
        "separator_1",
        "option_1",
        "option_2",
        "option_3",
        "option_4",
        "separator_2",
        "option_5",
        "option_6",
        "option_7",
        "option_8",
        "option_9",
        "separator_3",
        "option_10",
        "option_11",
        "option_12",
        "option_13",
        "option_14",
        "option_15",
        "option_16",
        "option_17",
        "option_18",
        "option_19",
        "separator_4",
        "option_20",
        "option_21",
        "option_22",
        "option_23",
        "option_24",
        "option_25",
        "option_26",
    ]
    list_display = (
        "__str__",
        "booking",
        "cooking",
        "general",
        "negative",
        "total_points",
    )
    readonly_fields = ("member_id", "total_points")

    # ----------------------------Booking Category-----------------------------

    def clear_points(self, request, queryset):
        queryset.update(booking=0)
        queryset.update(cooking=0)
        queryset.update(general=0)
        queryset.update(negative=0)

    clear_points.short_description = "Clear All Points"

    # ----------------------------Booking Category-----------------------------

    def option_1(self, request, queryset):
        queryset.update(booking=models.F("booking") + 50)
        

    option_1.short_description = "Completed Blast Off's In 10 Days"

    def option_2(self, request, queryset):
        queryset.update(booking=models.F("booking") + 10)
        
    option_2.short_description = "3 Dinners Booked & Cooked (Monday-Thursday)"

    def option_3(self, request, queryset):
        queryset.update(booking=models.F("booking") + 20)
        

    option_3.short_description = (
        "Each Set Sold During Blast Off (First 6 Dinners In 10 Days)")

    def option_4(self, request, queryset):
        queryset.update(booking=models.F("booking") + 10)

    # ----------------------------Cooking Category-----------------------------

    option_4.short_description = "6/10 Dinners Booked & Cooked In A Week"

    def option_5(self, request, queryset):
        queryset.update(cooking=models.F("cooking") + 50)

    option_5.short_description = "Completed Ice Break In First 6 Weeks"

    def option_6(self, request, queryset):
        queryset.update(cooking=models.F("cooking") + 25)

    option_6.short_description = "Cooked 6 Dinners In A Week"

    def option_7(self, request, queryset):
        queryset.update(cooking=models.F("cooking") + 60)

    option_7.short_description = "Delivered 2 Sets In A Week"

    def option_8(self, request, queryset):
        queryset.update(cooking=models.F("cooking") + 20)

    option_8.short_description = "Collected 50 Percent Deposit On A Sold Set"

    def option_9(self, request, queryset):
        queryset.update(cooking=models.F("cooking") + 200)

    option_9.short_description = "Sold And Delivered A Chef Set"

    # -----------------------General Activity Category--------------------------

    def option_10(self, request, queryset):
        queryset.update(general=models.F("general") + 60)

    option_10.short_description = "Earned The First Rhino Pin"

    def option_11(self, request, queryset):
        queryset.update(general=models.F("general") + 100)

    option_11.short_description = "Earned A 10/10 Jacket"

    def option_12(self, request, queryset):
        queryset.update(general=models.F("general") + 20)

    option_12.short_description = (
        "Recruited An Associate Who Completed Blast Off In 10 Days")

    def option_13(self, request, queryset):
        queryset.update(general=models.F("general") + 50)

    option_13.short_description = "Recruited A Stock Programmer"

    def option_14(self, request, queryset):
        queryset.update(general=models.F("general") + 25)

    option_14.short_description = "Recruited A D12 Club Member"

    def option_15(self, request, queryset):
        queryset.update(general=models.F("general") + 25)

    option_15.short_description = "Upgraded A Customer"

    def option_16(self, request, queryset):
        queryset.update(general=models.F("general") + 5)

    option_16.short_description = "Invited A Client To Attend Cook School/ Usage Class"

    def option_17(self, request, queryset):
        queryset.update(general=models.F("general") + 100)

    option_17.short_description = "Collected USD 30,000+ In A Week"

    def option_18(self, request, queryset):
        queryset.update(general=models.F("general") + 300)

    option_18.short_description = "Collected USD 50,000+ In A Week"

    def option_19(self, request, queryset):
        queryset.update(general=models.F("general") + 200)

    option_19.short_description = "Delivered 25 Sets In A Month"

    # --------------------------------Negative Points--------------------------------

    def option_20(self, request, queryset):
        queryset.update(negative=models.F("negative") + 2)

    option_20.short_description = "3 Dinners Cancelled In A Week"

    def option_21(self, request, queryset):
        queryset.update(negative=models.F("negative") + 5)

    option_21.short_description = "Arrived Late For A Dinner"

    def option_22(self, request, queryset):
        queryset.update(negative=models.F("negative") + 10)

    option_22.short_description = "Returned An Office Set Dirty & Unkept"

    def option_23(self, request, queryset):
        queryset.update(negative=models.F("negative") + 10)

    option_23.short_description = "Cooked A Dinner Not On DATA Without Admin's Approval"

    def option_24(self, request, queryset):
        queryset.update(negative=models.F("negative") + 5)

    option_24.short_description = "Missed Training Two Days In A Week"

    def option_25(self, request, queryset):
        queryset.update(negative=models.F("negative") + 15)

    option_25.short_description = "Consultant cooking dinner with no phone close"

    def option_26(self, request, queryset):
        queryset.update(negative=models.F("negative") + 15)

    option_26.short_description = "Distributor of a consultant with no phone close"

    # ------------------------------------Separators-----------------------------------

    def separator_1(self, request, queryset):
        pass

    separator_1.short_description = "- " * len(option_12.short_description)

    def separator_2(self, request, queryset):
        pass

    separator_2.short_description = "- " * len(option_12.short_description)

    def separator_3(self, request, queryset):
        pass

    separator_3.short_description = "- " * len(option_12.short_description)

    def separator_4(self, request, queryset):
        pass

    separator_4.short_description = "- " * len(option_12.short_description)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "member_id",
        "__str__",
        "member_age", 
        "phone_number",
        "type_of_member",
        "national_id",
        "email",
        "contract_signed",
        )





@admin.register(SetSold)
class SetAdmin(admin.ModelAdmin):
    list_display = (
        "set_sold",
        "__str__",
        "date_sold"
        )



@admin.register(MailingList)
class MailListAdmin(admin.ModelAdmin):
    list_display = [
    "person_name",
    "email"
    ]