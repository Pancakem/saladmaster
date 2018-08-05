from random import randrange

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.conf import settings
    
def default_id():
    RANDOM_ID = randrange(1000, 9999)
    return RANDOM_ID

class Member(models.Model):

    member_id = models.PositiveSmallIntegerField(
        default=default_id,
        help_text="Member's ID",
        primary_key=True,
        unique=True,
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        verbose_name="ID"
    )
    first_name = models.CharField(
        max_length=20,
        help_text="Member's First Name",
        validators=[RegexValidator(r"^[a-zA-Z]+$")]
    )
    last_name = models.CharField(
        max_length=20,
        help_text="Member's Last Name",
        validators=[RegexValidator(r"^[a-zA-Z]+$")],
    )    

    member_age = models.PositiveSmallIntegerField(
        help_text="Member's Age",
        verbose_name="Age",
        validators=[MinValueValidator(0), MaxValueValidator(80)]
        )

    phone_number = models.CharField(
        max_length=15,
        help_text="Member's Phone Number",
        validators=[RegexValidator(r"^[0-9]+$")]
        )
    email = models.EmailField(
        blank=False,
        default=None
        )

    national_id = models.IntegerField(
        unique=True,
        help_text="National ID/Passport Number",
        validators=[MinValueValidator(11111111), MaxValueValidator(99999999)]
        )

    type_of_member = models.CharField(
        max_length=50,
        choices=[("Associate", "Associate"), ("Consultant", "Consultant"), ("Senior Consultant", "Senior Consultant"), ("Distributor","Distributor"), ("Dealer", "Dealer")],
        help_text="Member's rank"
        )

    contract_signed = models.BooleanField(
        help_text="Contract status",
        verbose_name="Contract Status")
    # team = models.CharField(
    #     help_text="What team do you beong to?",
    #     choices=[]
    #     )

    date_added = models.DateTimeField(
        auto_now=True, help_text="When Was Member's Record Added?"
    )

    def __str__(self):
        return " ".join([self.first_name, self.last_name])

class TeamRecord(models.Model):
    # REDEEM_OPTION_A = "Deposit On Any Personal Saladmaster Set"
    # REDEEM_OPTION_B = "Obtain Dinner Food For Individual Sales Activity"
    # REDEEM_OPTION_C = "Obtain Transport Voucher To & From Dinners"
    # REDEEM_OPTION_D = "Contribute To Travel Club Accounts"
    # REDEEM_OPTION_E = "Purchase Red 5/Saladmaster Memorabilia"
    # REDEEM_CHOICES = (
    #     (
    #         (REDEEM_OPTION_A, "Deposit On Any Personal Saladmaster Set"),
    #         (REDEEM_OPTION_B, "Obtain Dinner Food For Individual Sales Activity"),
    #         (REDEEM_OPTION_C, "Obtain Transport Voucher To & From Dinners"),
    #         (REDEEM_OPTION_D, "Contribute To Travel Club Accounts"),
    #         (REDEEM_OPTION_E, "Purchase Red 5/Saladmaster Memorabilia"),
    #     ),
    # )
    member = models.ForeignKey(
        Member, 
        unique=True, 
        on_delete=models.CASCADE,
        verbose_name="Member Name" )
    booking = models.PositiveSmallIntegerField(
        default=0,
        editable=False,
        help_text="Total Points In The Booking Category",
        verbose_name="Booking Category",
    )
    cooking = models.PositiveSmallIntegerField(
        default=0,
        editable=False,
        help_text="Total Points In The Cooking Category",
        verbose_name="Cooking Category",
    )
    general = models.PositiveSmallIntegerField(
        default=0,
        editable=False,
        help_text="Total Points In The General Activity Category",
        verbose_name="General Activity Category",
    )
    negative = models.PositiveSmallIntegerField(
        default=0,
        editable=False,
        help_text="Total Deductable Points",
        verbose_name="Negative Points",
    )
    
    class Meta:
        #db_table = "member_records"
        verbose_name_plural = "Member Points"

    def __str__(self):
        return " ".join([self.member.first_name, self.member.last_name])

    def total_points(self):
        a = self.booking
        b = self.cooking
        c = self.general
        d = self.negative
        summation = (a + b + c) - d
        return summation


# class ExcelRecords(models.Model):
#     id = models.IntegerField(primary_key=True)
#     first_column = models.TextField()
#     second_column = models.TextField()
#     third_column = models.TextField()
#     fourth_column = models.TextField()
#     fifth_column = models.TextField()
#     sixth_column = models.TextField()

#     class Meta:
#         db_table = "excel_records"
#         ordering = ["first_column", 'second_column']
#         verbose_name = "Excel Record"


class SetSold(models.Model):
    set_sold = models.CharField(
        max_length=20,
        verbose_name="Set"
        )
    seller = models.ForeignKey(
        Member, 
        default=None,
        on_delete=models.CASCADE,
        verbose_name="Set Sold By",
        help_text="Set Sold By"
        )
    date_sold = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["set_sold", "seller", "date_sold" ]
        verbose_name_plural = "Sets Sold"


    def __str__(self):
        return " ".join([self.seller.first_name, self.seller.last_name])


class MailingList(models.Model):
    person_name = models.CharField(
        max_length=30,
        help_text="Name of email receiver",
        verbose_name="Mail to"
        )

    email = models.EmailField(
        blank=True,
        default=None
        )

    class Meta:
        verbose_name_plural = "Mailing List"