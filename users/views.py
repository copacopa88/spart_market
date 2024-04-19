from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        'member':member,
    }
    return render(request, 'profile.html', context)

@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
        #지금 프로필 페이지를 보고있는, 팔로우 하려는 유저 = menber
        #지금 로그인 한, 클라이언트 유저 = request.user
            if member.followers.filter(pk=request.user.pk).exists():
                    member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect(profile, username=member.username)
            
    else:
        return redirect('accounts:login')