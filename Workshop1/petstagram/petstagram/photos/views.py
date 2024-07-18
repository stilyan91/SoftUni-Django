from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def add_photo(request):
    return render(request, "photos/photo-add-page.html")
@login_required
def show_photo_details(request, pk):
    return render(request, 'photos/photo-details-page.html')

@login_required
def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')
