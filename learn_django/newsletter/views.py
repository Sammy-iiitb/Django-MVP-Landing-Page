from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
    title ="Welcome"
    form = SignUpForm(request.POST or None)
    #if request.user.is_authenticated():
    #    title = "My Title %s" %(request.user)
    #add a form
    context = {
        "title": title,
        "form" :form
    }

    if form.is_valid():
        # commit = false doesn't save data in the database
        instance = form.save(commit=False)
        instance.save()
        #print instance.email
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
            # print form.cleaned_data.get(key)
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'samyak3mt@gmail.com']
        contact_message = "%s: %s via %s"%(full_name,message,email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True)
    context = {
        "form": form,
    }
    return render(request, "forms.html", context)
