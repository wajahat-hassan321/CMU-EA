import win32com.client


def send_complaint_email(complaint):

    outlook = win32com.client.Dispatch('Outlook.Application')

    mail = outlook.CreateItem(0)

    mail.To = complaint.email

    mail.Subject = f"Complaint Update - {complaint.crn_no}"

    mail.HTMLBody = f"""
    <html>
    <body>

        <h2>Complaint Status Update</h2>

        <p>
            Dear <b>{complaint.customer_name}</b>,
        </p>

        <p>
            Your complaint with CRN:
            <b>{complaint.crn_no}</b>
        </p>

        <p>
            Current Status:
            <b>{complaint.status}</b>
        </p>

        <p>
            Regards,<br>
            Complaint Management Team
        </p>

    </body>
    </html>
    """

    mail.Send()