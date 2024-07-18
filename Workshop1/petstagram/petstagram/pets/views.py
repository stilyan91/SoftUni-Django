from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def add_pet(request):
    return render(request, 'pets/pet-add-page.html')

@login_required
def pet_details(request, username, pet_name):
    return render(request, 'pets/pet-details-page.html')

@login_required
def pet_edit(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')

@login_required
def pet_delete(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')