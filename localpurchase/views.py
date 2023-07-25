from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from .models import LocalPurchaseModel, LPBillSubmissionModel
from .forms import LocalPurchaseForm, LPBillSubmissionForm
from django.db.models import Max
from datetime import date
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.conf import settings
import ast

# Create your views here.
def checkRefNo():
    if LocalPurchaseModel.objects.count() == 0:
        todays_date = date.today()
        yr = str(todays_date.year)
        mnt = str(todays_date.month)
        ref_no = "LPF"+yr+mnt+"0"+"1"
        return ref_no
    else:
        todays_date = date.today()
        yr = str(todays_date.year)
        mnt = str(todays_date.month)
        cont = int(LocalPurchaseModel.objects.count())+1
        ref_no = "LPF"+yr+mnt+"0"+str(cont)
        return ref_no
###############################################################################

def index(request):
    return render(request,'localpurchase/view-record.html',{
        'records':LocalPurchaseModel.objects.all().order_by('-id')
    })

########################## View Record  ####################################

def viewSingleRecord(request):
    if request.method == 'GET':
        id = request.GET['id']
        print(id)
        ref_no = request.GET['ref_no']
        print(ref_no)
        lprecord = LocalPurchaseModel.objects.get(ref_no=ref_no, id=id)
        context = {
        'lprecord':lprecord
        }
#        print(f"LPRECORD : {lprecord}")
        return render(request,'localpurchase/record.html',context)

############################ Add Record ########################################

def add(request):
    if request.method == 'POST':
        indentor_name =request.POST['indentor_name'] 
        your_email = request.POST['your_email']
        requester_email = request.POST['requester_email']
        requested_by = request.POST['requested_by'] 
        purpose = request.POST['purpose'] 
        item_to_purchase=request.POST.getlist('item_to_purchase[]')
        item_quantity=request.POST.getlist('item_quantity[]')
        approximate_amount = request.POST['approximate_amount'] 
        date_of_purchase=request.POST['date_of_purchase']
        vendor_details=request.POST['vendor_details']
        localtion_of_purchase=request.POST['localtion_of_purchase']
        coa=request.POST['coa']
        approximate_distance=request.POST['approximate_distance']
        assigned_to=request.POST['assigned_to']
        any_other_details=request.POST['any_other_details']
        purchase_to_made_by_admin = request.POST['purchase_to_made_by_admin']
        ref_no = checkRefNo()
        item_with_quantity = zip(item_to_purchase, item_quantity)
        item_with_quantity = dict(item_with_quantity);
        lpm = LocalPurchaseModel.objects.create(
            ref_no = ref_no,
            indentor_name =indentor_name,
            your_email = your_email,
            requester_email = requester_email,
            requested_by = requested_by,
            purpose = purpose,
            item_to_purchase=item_to_purchase,
            item_quantity = item_quantity,
            date_of_purchase=date_of_purchase,
            vendor_details=vendor_details,
            localtion_of_purchase=localtion_of_purchase,
            coa=coa,
            approximate_distance=approximate_distance,
            assigned_to=assigned_to,
            any_other_details=any_other_details,
            approximate_amount = approximate_amount,
            item_with_quantity = item_with_quantity,
            purchase_to_made_by_admin = purchase_to_made_by_admin
            )
        pkid = lpm.pk
            ### To Send Email ###
        html_admin = render_to_string('localpurchase/sendmailform.html',{
            'ref_no' :ref_no,
            'indentor_name':indentor_name,
            'your_email': your_email,
            'requested_by': requested_by,
            'requester_email':requester_email,
            'purpose': purpose,
            'item_with_quantity' : item_with_quantity,
            'date_of_purchase': date_of_purchase,
            'vendor_details' : vendor_details,
            'localtion_of_purchase' : localtion_of_purchase,
            'coa': coa,
            'approximate_distance': approximate_distance,
            'approximate_amount':approximate_amount,
            'assigned_to':assigned_to,
            'any_other_details': any_other_details,
            'purchase_to_made_by_admin':purchase_to_made_by_admin,
            'pkid':pkid,
            'url': reverse('approval')
            })
        html_user =  render_to_string('localpurchase/sendmailformuser.html',{
            'ref_no' :ref_no,
            'indentor_name':indentor_name,
            'your_email': your_email,
            'requester_email':requester_email,
            'requested_by': requested_by,
            'purpose': purpose,
            'item_with_quantity':item_with_quantity,
            'date_of_purchase': date_of_purchase,
            'vendor_details' : vendor_details,
            'localtion_of_purchase' : localtion_of_purchase,
            'coa': coa,
            'approximate_distance': approximate_distance,
            'approximate_amount':approximate_amount,
            'assigned_to':assigned_to,
            'any_other_details': any_other_details,
            'purchase_to_made_by_admin':purchase_to_made_by_admin,
            'pkid':pkid,
            'url': reverse('approval')
            })
        ### End ###
        #snd_mail = send_mass_mail((message1,message2),fail_silently=False)
        send_msg_admin = send_mail(
        subject = "Local Purchase Form: " + ref_no,
        message = 'You Have New Submission kindly go through details for approval',
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [settings.EMAIL_ADMIN_CENS,'indresh@cens.res.in'],
        html_message = html_admin
        )
        send_msg_user = send_mail(
        subject = "Local Purchase Form: " + ref_no,
        message = 'Thank you for your Submission',
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [your_email,requester_email],
        html_message = html_user
        )
        item_with_quantity = zip(item_to_purchase, item_quantity)
        item_with_quantity = dict(item_with_quantity);
        print("-----------dic-------")
        print(item_with_quantity)
        lpm.item_with_quantity = item_with_quantity
        savedmsg = lpm.save()
#        print ("Saved Message : "  + str(savedmsg))
 #       print(type(savedmsg))
  #      print ("Admin Message : "  + str(send_msg_admin))
   #     print ("Emailed Message : " + str(send_msg_user))
        return render(request,'localpurchase/add.html',{
                'form': LocalPurchaseForm(),
                'success': True
            })
    else:
        form = LocalPurchaseForm()
        data = {
        'ref_no' : checkRefNo()
        }       
    return render(request,'localpurchase/add.html',data)

#################################  Approval  ##################################################

def approval(request):
    if request.method=='GET':
        pk_id = request.GET['pk']
        ref_no = request.GET['ref_no']
        context ={}
        print("------------")
        print(pk_id)
        print(ref_no)
        print("------------")
        data = LocalPurchaseModel.objects.get(ref_no=ref_no, id=pk_id)
        lpobj = LocalPurchaseModel.objects.get(ref_no=ref_no, id=pk_id)
        itm_qnts = lpobj.item_quantity
        itm_with_qty = lpobj.item_with_quantity
        itms = ast.literal_eval(itm_with_qty) #convert string to list / dic  
        itm_qnts = ast.literal_eval(itm_qnts)
        context = {
        'itms' : itms,
        'data':data,
        'itm_qnts':itm_qnts
        }
#        print(itms)
 #       print(type(itms))
  #      print(context)
   #     print("--Item quantity--")
    #    print(itms)
     #   print("---jdata--")
        # print(jdata)
        #return JsonResponse({'jdata':'test'})
        return render(request, 'localpurchase/approval.html',context)

    elif request.method=='POST':
        ao_approval = request.POST['ao_approval']
        id=request.POST['pkid']
        ref_no=request.POST['ref_no']
        user_email = request.POST['user_email']
        itm_name = request.POST.getlist('itm[]')
        itm_qt = request.POST.getlist('itm_qnt[]')
        ao_approval_remarks = request.POST['ao_approval_remarks']
        amount_approved = request.POST['amount_approved']
        requested_by = request.POST['requested_by']
        indentor_name = request.POST['indentor_name']
        requester_email = request.POST['requester_email']
        itm_with_qty = zip(itm_name,itm_qt)
        itm_with_qty = dict(itm_with_qty)
#        print(">>>>>>"+id+"<<<<<<<<")
 #       print("-----dic----")
  #      print(itm_with_qty)
        lpfapprove_update = LocalPurchaseModel.objects.get(id=id)
        lpfapprove_update.ao_approval = ao_approval
        lpfapprove_update.amount_approved = amount_approved
        lpfapprove_update.ao_approval_remarks = ao_approval_remarks
        lpfapprove_update.item_with_quantity = itm_with_qty
        lpfapprove_update.save()
        #### Send Email ####
        html_code = render_to_string('localpurchase/approval-email.html',{
            'ref_no' :ref_no,
            'indentor_name':indentor_name,
            'ao_approval_remarks':ao_approval_remarks,
            'itm_with_qty':itm_with_qty,
            'amount_approved':amount_approved,
            'user_email': user_email,
            'requested_by': requested_by,
            'ao_approval':ao_approval
            })
        send_approval_msg_admin = send_mail(
        subject = "Approval - Local Purchase Form: " + ref_no,
        message = 'Approval status for your indent with ref_No.' + ref_no + 'is : '+ao_approval,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [settings.EMAIL_ADMIN_CENS,settings.EMAIL_BILL_SUBMITER,user_email,requester_email],
        html_message = html_code
        )
        ### / Send Email ###
        return render(request,'localpurchase/approval.html',{
                'form': LocalPurchaseForm(),
                'success': True
            })

#####################  Bill Submission #########################################

def bill_submission(request):
    if request.method == 'GET':
        form = LPBillSubmissionForm()
        ref_no = request.GET['ref_no']
        context ={}
        #print("Context <<<<<before :"+str(context))
        existss = LPBillSubmissionModel.objects.filter(ref_no=ref_no).exists()
        #print(">>>Exists<<<")
        #print(">>>>>Exists<<<<<")
        #print(existss)
        #print(">>>>>Exists<<<<<")
        if existss:
         #   print(">>>>>Context<<<<<")
            return render(request,'localpurchase/bill-submission-list.html',{
                'billrecords':LPBillSubmissionModel.objects.all()
            })
        else:
            indentor_name = request.GET['indentor_name']
            requested_by = request.GET['requested_by']
            ref_no = request.GET['ref_no']
            coa = request.GET['coa']
            return render(request, 'localpurchase/bill-submission.html',{
                'form':LPBillSubmissionForm(),
                'ref_no':ref_no,
                'indentor_name':indentor_name,
                'requested_by':requested_by,
                'coa': coa
                })              

    elif request.method == 'POST':
        #print(">>>>>>>>POSt bills<<<<<<<<<<<<")
        bill_no = request.POST.getlist('bill_no[]')
        bill_date = request.POST.getlist('bill_date[]')
        bill_amount = request.POST.getlist('bill_amount[]')
        ref_no = request.POST['ref_no']
        indentor_name = request.POST['indentor_name']
        coa = request.POST['coa']
        requested_by = request.POST['requested_by']
        source_name = request.POST.getlist('source_name[]')
        particulars = request.POST.getlist('particulars[]')
        for i in range(len(bill_date)):
            lpbs = LPBillSubmissionModel.objects.create(
                ref_no = ref_no,
                indentor_name =indentor_name,
                requested_by =requested_by,
                bill_no = bill_no[i],
                bill_date = bill_date[i],
                bill_amount = bill_amount[i],
                coa = coa,
                source_name = source_name[i],
                particulars=particulars[i]
                )
            lpbs.save()
         #   print(i)
        #    print("loop")
       # print(">>>>>>>>POS<<<<<<<<<<<<")
        return render(request,'localpurchase/bill-submission-list.html',{
                'billrecords':LPBillSubmissionModel.objects.all()
            })

##################### bill_submission_list ########################################

def bill_submission_list(request):
    return render(request,'localpurchase/bill-submission-list.html',{
                'billrecords':LPBillSubmissionModel.objects.all()
            })