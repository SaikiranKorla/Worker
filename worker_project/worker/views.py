# worker/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import Worker  # Make sure you import the Worker model
from .forms import WorkerRegistrationForm, WorkerUpdateForm

def home(request):
    return render(request, 'worker/home.html')

def register_worker(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            worker = form.save()
            # You can add additional logic here, like sending a confirmation email
            return redirect('worker_profile')  # Redirect to worker profile page
    else:
        form = WorkerRegistrationForm()

    return render(request, 'worker/register_worker.html', {'form': form})

def update_worker(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    if request.method == 'POST':
        form = WorkerUpdateForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_profile')  # Redirect to worker profile page
    else:
        form = WorkerUpdateForm(instance=worker)

    return render(request, 'worker/update_worker_contact.html', {'form': form, 'worker': worker})
