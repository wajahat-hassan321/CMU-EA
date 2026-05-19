from django.http import HttpResponse
from .models import Complaint
from .utils import send_complaint_email
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import Complaint

def send_test_email(request):

    complaint = Complaint.objects.first()
    send_complaint_email(complaint)
    return HttpResponse("Email Sent")


def upload_csv(request):

    error_message = None
    success_message = None

    if request.method == 'POST':

        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():

            try:

                csv_file = request.FILES['file']

                df = pd.read_csv(csv_file)

                for index, row in df.iterrows():

                    try:

                        Complaint.objects.get_or_create(

                            crn_no=str(row['crn-no']),

                            defaults={

                                'customer_name': str(row['customer-name']),
                                'status': str(row['status']),
                                'email': str(row['email']).strip(),
                            }
                        )

                    except Exception as e:

                        print(e)

                success_message = "CSV Uploaded Successfully"
                return redirect('sent-email')
            except Exception as e:

                error_message = str(e)
        return redirect('send_bulk_emails')
    else:

        form = CSVUploadForm()

    context = {
        'form': form,
        'error_message': error_message,
        'success_message': success_message,
    }

    return render(request,'upload_csv.html',context,)  



def email_status(request):

    complaints = Complaint.objects.filter(email_sent=False)

    success = 0
    failed = 0

    for complaint in complaints:

        try:

            send_complaint_email(complaint)

            complaint.email_sent = True
            complaint.email_error = ""

            complaint.save()

            success += 1

        except Exception as e:

            complaint.email_error = str(e)

            complaint.save()

            failed += 1

            print(e)

    return render(request,
                  'email_status.html',
                  {
                      'complaints': complaints,
                      'success': success,
                      'failed': failed
                  }
)