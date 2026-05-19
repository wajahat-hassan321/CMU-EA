from django.urls import path
from .views import  upload_csv , email_status

urlpatterns = [
    path('', upload_csv, name='upload_csv'),
    path('send-emails/', email_status, name='send_bulk_emails'),
    # path('sent-email/', sent_email,name='sent-email')
]