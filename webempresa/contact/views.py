from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
	contac_form = ContactForm()
	if request.method == "POST":
		contact_form = ContactForm(data=request.POST)

		if contact_form.is_valid():
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			content = request.POST.get('content', '')
			# Enviamos el correo y redireccionamos
			email = EmailMessage(
				"La Caffettiera: Nuevo mensaje de contacto",
				"De {} <{}> \n\nEscribió:\n\n{}".format(name,email,content),
				"no-contestar@inbox.mailtrap.io",
				["m.jcacll@gmail.com"],
				reply_to=[email]
			)
			try:
				email.send()
			except:
				#Algo no ha ido bien, redireccionamos a fail
				return redirect(reverse('contact')+"?fail")
			return redirect(reverse('contact')+"?ok")


	return render(request, "contact/contact.html",{'form':contac_form})
