from django.db import models

# Create your models here.
class LocalPurchaseModel(models.Model):
   ref_no = models.CharField(max_length=32, blank=True,null=True)
   indentor_name = models.CharField(max_length=128, blank=True,null=True)
   your_email = models.EmailField(max_length=256, blank=True,null=True)
   requester_email = models.EmailField(max_length=256, blank=True,null=True)
   requested_by = models.CharField(max_length=128, blank=True,null=True)
   purpose = models.TextField(blank=True,null=True)
   item_to_purchase = models.TextField( blank=True,null=True)
   item_quantity = models.TextField(blank=True,null=True)
   item_with_quantity = models.TextField(blank=True,null=True)
   date_of_purchase = models.DateField(null=True)
   vendor_details = models.TextField(blank=True,null=True)
   localtion_of_purchase = models.CharField(max_length=256, blank=True,null=True)
   COA_CHOICE = [('','SELECT'),
   ('Repair and Maintenance','Repair and Maintenance'),
   ('Travel Expenses','Travel Expenses'),
   ('Postage, Telephone and Communication Charges','Postage, Telephone and Communication Charges'),
   ('Printing and Stationery','Printing and Stationery'),
   ('Transportation and Conveyance Expenses','Transportation and Conveyance Expenses'),
   ('Books, Journals and Subscription','Books, Journals and Subscription'),
   ('Gas Refilling Charges','Gas Refilling Charges'),
   ('Fuel charges','Fuel charges'),
   ('Welfare Expenses','Welfare Expenses'),
   ('Other','Other'),
   ]
   coa = models.CharField(choices=COA_CHOICE,max_length=256,blank=True,null=True, verbose_name="CoA")
   approximate_distance = models.CharField(max_length=32,blank=True,null=True)
   approximate_amount =  models.CharField(max_length=32,blank=True,null=True)
   amount_approved =  models.CharField(max_length=32,blank=True,null=True)
   assigned_to = models.CharField(max_length=256,blank=True,null=True)
   any_other_details = models.TextField(blank=True,null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   ao_approval = models.CharField(max_length=32,blank=True,null=True)
   ao_approval_remarks = models.TextField(blank=True,null=True)
   purchase_to_made_by_admin = models.CharField(max_length=8,blank=True,null=True)
   
   def __str__(self):
      return f'LocalPurchase: {self.ref_no}  - indentor : {self.indentor_name} , requested by : {self.requested_by}'


class LPBillSubmissionModel(models.Model):
   bill_no = models.CharField(max_length=128, blank=True,null=True)
   bill_date = models.DateField()
   source_name = models.TextField(null=True,blank=True)
   bill_amount = models.CharField(max_length=32, blank=True,null=True)
   particulars = models.TextField(null=True,blank=True)
   transportation_vehicle_no = models.CharField(max_length=128, blank=True,null=True)
   ref_no = models.CharField(max_length=32)
   indentor_name = models.CharField(max_length=128)
   requested_by = models.CharField(max_length=128, blank=True,null=True)
   transport_expence = models.TextField(null=True, blank=True, verbose_name="Remarks / Transport Expence(if any)")
   any_other_details = models.TextField(blank=True,null=True)
   coa = models.CharField(max_length=256,blank=True,null=True, verbose_name="CoA")
   
   def __str__(self):
      return f'Bill Submission: {self.ref_no} bill No.: {self.bill_no} - bill_amount: {self.bill_amount} - indentor : {self.indentor_name}'
