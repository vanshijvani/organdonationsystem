
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RecipientRegistrationForm

def register_recipient(request):
    if request.method == 'POST':
        form = RecipientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Recipient registered successfully!')
            return redirect('recipient_success')  # Redirect to a success page
    else:
        form = RecipientRegistrationForm()

    return render(request, 'recipient/register.html', {'form': form})
