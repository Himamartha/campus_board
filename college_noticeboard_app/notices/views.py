from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import Notice
from .forms import NoticeForm, NoticeSearchForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

def is_admin(user):
    return user.is_staff

@login_required
def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')
    search_form = NoticeSearchForm(request.GET)
    
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search')
        department = search_form.cleaned_data.get('department')
        notice_type = search_form.cleaned_data.get('notice_type')
        
        if search_query:
            notices = notices.filter(title__icontains=search_query) | notices.filter(content__icontains=search_query)
        if department:
            notices = notices.filter(department=department)
        if notice_type:
            notices = notices.filter(notice_type=notice_type)
    
    # Show notices that either have no expiration date or haven't expired yet
    notices = notices.filter(valid_until__isnull=True) | notices.filter(valid_until__gte=timezone.now().date())
    
    context = {
        'notices': notices,
        'search_form': search_form,
        'is_admin': request.user.is_staff
    }
    return render(request, 'notices/notice_list.html', context)

@login_required
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice': notice,
        'is_admin': request.user.is_staff
    }
    return render(request, 'notices/notice_detail.html', context)

@user_passes_test(is_admin)
def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()
            messages.success(request, 'Notice created successfully!')
            return redirect('notice_list')
    else:
        form = NoticeForm()
    return render(request, 'notices/notice_form.html', {'form': form, 'action': 'Create'})

@user_passes_test(is_admin)
def notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notice updated successfully!')
            return redirect('notice_list')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'notices/notice_form.html', {'form': form, 'action': 'Edit'})

@user_passes_test(is_admin)
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        notice.delete()
        messages.success(request, 'Notice deleted successfully!')
        return redirect('notice_list')
    return render(request, 'notices/notice_confirm_delete.html', {'notice': notice})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')
