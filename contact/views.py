from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    contact_form= ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #ENVIAMOS EL CORREO Y DIRRECIONAMOS
            email= EmailMessage(
                "La cafeteria: Nuevo mensaje de contacto",
                "DE {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "sandbox.smtp.mailtrap.io",
                ["angello.nahum22@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #TDOD DSLAIO BIEN REDIRRECIOANS A OK
                return redirect(reverse('contact')+"?ok")

            except:
                #ALGO NO ANDA BIEN REDIRRECIOANMSOA A FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html",{'form':contact_form })