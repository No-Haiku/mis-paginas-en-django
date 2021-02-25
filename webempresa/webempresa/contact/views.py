from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form= ContactForm()
    if request.method == "POST":
        contact_form= ContactForm(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name', '')
            email= request.POST.get('email', '')
            content= request.POST.get('content', '')
            # Enviar correo y redireccionar
            email= EmailMessage(
                "La caffettiera: nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["gian.f-neira@live.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #si falla redireccionamos a FAIL

                 return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
