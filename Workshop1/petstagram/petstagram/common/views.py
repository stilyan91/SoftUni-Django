from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.models import Like
from petstagram.photos.models import Photo



def index(request):
    all_photos = Photo.objects.all()

    context = {
        "all_photos": all_photos
    }
    return render(request, 'common/home-page.html', context=context)

@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_objects = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_objects:
        liked_objects.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META["HTTP_REFERER"] + f'#{photo_id}')


@login_required
def share_functionality(request, photo_id):
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

@login_required
def comment_functionality(request, photo_id):
    pass

    # photo = Photo.objects.get(id=photo_id)
    #
    # if request.method == "POST":
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)

