from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactF

# Create your views here.
def contact(request):
    contact_form = ContactF()
    
    if request.method == "POST":
        contact_form = ContactF(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Creamos el correo:
            mail = EmailMessage(
                "Consultoria Leonesa: Muevo Mensaje de contacto",               #Asunto
                "De {} - {} - \nEscribió:\n\n{}".format(name,email,content),    #Mensaje
                "correo@ConsultoriaLeonesa.com",                                #Emailorigen dominio
                ["micorreodecontactopublico@gmail.com"],                  #Email de destino registro mailtrap
                # reply_to=[email]
            )
            #Lo enviamos y redireccionamos:
            try:
                mail.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                return redirect(reverse('contacto')+"?fail")
    return render(request, 'contacto.html', {'form':contact_form})