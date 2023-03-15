from django.shortcuts import render
from django.core.mail import send_mail
import string

# Create your views here.
from project import checkCurrentAlert
def index(request):
    message = checkCurrentAlert()
    if message  == None:
        message = "No alert found."
    return render(request, "alert/alert.html",{
        "message": str(message)
    })

def sendEmail(request):
    message  = checkCurrentAlert()
    if message  == None:
        print("no")
        return render(request, "alert/alert.html",{
        "message": "No alert found."
        })

    else:
        message = message.get_text()

    from_email = "YourGmail@gmail.com"
    recipient_list = ["yourPhoneNumber@msg.koodomobile.com"]

    start_index = message.find('Hazard:')
    end_index = message.find('Timing:')
    text = message[start_index:end_index]
    text = text.translate(str.maketrans(string.punctuation, "!" * len(string.punctuation)))

    # Print the new string
    send_mail("", text, from_email, recipient_list)
    return render(request, "alert/alert.html",{
        "message": "Alert Found! Sent SMS to phone"
    })
