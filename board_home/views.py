# board_home/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .notice_crawler import crawl_and_store_notices
from .models import Notice


def home(request):
    return render(request, 'board_home/home.html')


from .forms import CustomUserCreationForm, CustomAuthenticationForm

def study_list(request):
    # 스터디 모집 게시글 목록 가져오기 (예시)
    # studies = Study.objects.all()
    return render(request, 'board_home/study_list.html')  # , {'studies': studies}

def club_list(request):
    # 동아리 모집 게시글 목록 가져오기 (예시)
    # clubs = Club.objects.all()
    return render(request, 'board_home/club_list.html')  # , {'clubs': clubs}
def login_signup_view(request):
    login_form = CustomAuthenticationForm()
    signup_form = CustomUserCreationForm()

    if request.method == 'POST':
        if 'signup_submit' in request.POST:
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, '회원가입이 완료되었습니다.')
                return redirect('login_signup')
            else:
                print("회원가입 에러:", signup_form.errors)

        elif 'login_submit' in request.POST:
            login_form = CustomAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')

    # 💡 여기에서 무조건 렌더링하도록 함
    return render(request, 'board_home/login_signup.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })

def school_notice_view(request):
    crawl_and_store_notices()
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')

    notices = Notice.objects.all()

    if category:
        notices = notices.filter(category=category)
    if search:
        notices = notices.filter(title__icontains=search)

    notices = notices.order_by('-date')[:30]

    return render(request, 'board_home/school_notice.html', {'notices': notices})


def classchat(request):
    return render(request, 'board_home/classchat.html')  # ✅ 경로 수정


def room(request, room_name):
    return render(request, 'board_home/room.html', {'room_name': room_name})  # ✅ 경로 수정
