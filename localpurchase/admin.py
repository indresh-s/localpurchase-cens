from django.contrib import admin
from .models import LocalPurchaseModel, LPBillSubmissionModel
# Register your models here.
admin.site.register(LocalPurchaseModel)
admin.site.register(LPBillSubmissionModel)