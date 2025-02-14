from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry

@login_required
def home_view(request):
    entries = PasswordEntry.objects.filter(user=request.user)
    for entry in entries:
        entry.decrypted_password = entry.get_password()  # Giải mã mật khẩu
    return render(request, 'password_manager/home.html', {'entries': entries})

@login_required
def add_password_view(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        username = request.POST.get('username')
        password = request.POST.get('password')
        entry = PasswordEntry(user=request.user, website=website, username=username)
        entry.set_password(password)  # Mã hóa mật khẩu
        entry.save()
        return redirect('home')
    return render(request, 'password_manager/add_password.html')

@login_required
def delete_password_view(request, entry_id):
    entry = PasswordEntry.objects.get(id=entry_id)
    entry.delete()
    return redirect('home')