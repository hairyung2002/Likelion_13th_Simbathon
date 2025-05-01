# 큰 틀만 잡아둔 상태라 지금은 많이 비효율적 구조입니다...
# 연휴 중으로 디벨롭 해 보겠습니다...!

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *

#LoginPage : 로그인 창창
def LoginPage(request):
    return render(request, 'main/LoginPage.html')

#JoinPage로 이름 변경 예정 : 회원가입 페이지지
def MembershipPage(request):
    return render(request, "main/MembershipPage.html")

def MyPage(request):
    return render(request, "main/MyPage.html")

#회원가입 시 데이터 받아오기기
#User.objects.creat_user를 이용해 구현할 예정.
def Create_Member(request):
    new_Member = Member()

    new_Member.id = request.POST['id']
    new_Member.password = request.POST['password'] #보안을 위해 비밀번호 authenticate 변경 필요요
    new_Member.name = request.POST['name']
    new_Member.email = request.POST['email']

    new_Member.save()

    return redirect('main:LoginPage') 

#로그인 시 가입된 정보와 일치하는지 확인
def Check_Member(request):
    check_id = request.POST['id']
    check_pw = request.POST['password']

    #데이터베이스 계정 존재 여부 체크
    account = Member.objects.filter(id = check_id)

    if account.exists():#계정이 존재할 경우
        member = account.first()

        if member.password == check_pw: #비밀번호 일치 확인
            return redirect('main:MyPage')
        else:
            return redirect('main:LoginPage.html', {'Error':'비밀번호가 일치하지 않습니다'})
        
    else:
        return redirect('main:LoginPage.html', {'Error':'존재하지 않는 ID입니다다'})