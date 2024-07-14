from django.shortcuts import render, redirect

from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.


def index(request):
    all_photos = Photo.objects.all()

    context = {
        "all_photos": all_photos
    }
    return render(request, 'common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_objects = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_objects:
        liked_objects.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META["HTTP_REFERER"] + f'#{photo_id}')