from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime
from django.contrib import auth
from django.http import Http404
from myapp.models import MEM
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import IssueForm
from .forms import ReportForm
from myapp.models import REWARD
from myapp.models import buy
from django.utils import timezone
from myapp.models import ORDER
from django.db.models import Sum, Subquery
from .models import buy, ORDER
from myapp.serializers import myappSerializer
from rest_framework import viewsets
#-----------
from myapp.models import USER
from django.contrib.auth.models import User
import requests
from django.views.decorators.csrf import csrf_exempt

SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"
serverngrok="https://1628-114-32-188-99.jp.ngrok.io"
from myapp.models import LOGIN
def login2_view(request):
    sum=""
    rand=LOGIN.objects.create()
    # print(rand.FKcheck)
    # print(type(rand.FKcheck))
    url = SACCngrok+'/RESTapiApp/Line_1/?Rbackurl='+serverngrok+'/api2/?fk='+rand.FKcheck
    req=requests.get(url,headers = {'Authorization': 'Token 3177f1710c1360a482fb5ea84bf33f38462f7520','ngrok-skip-browser-warning': '7414'})
    # print(req.json())
    req_read = req.json()
    # print(req_read["Rstate"])
    LOGIN.objects.filter(FKcheck = rand.FKcheck).update(Rstate=req_read["Rstate"])
    firstLogin="https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri="+SACCngrok+"/LineLoginApp/callback&state="+req_read["Rstate"]+"&scope=profile%20openid%20email&promot=consent&ui_locales=zh-TW?http://example.com/?ngrok-skip-browser-warning=7414"

    return render(request, 'login2.html', locals())

def api2(request):
    if request.method == 'GET':
        fknum = request.GET.get('fk')
        nomatter=LOGIN.objects.filter(FKcheck = fknum)
        sum=''
        for i in nomatter:
            sum=i.Rstate
    url = SACCngrok+'/RESTapiApp/Line_2/?Rstate='+sum
    req=requests.get(url,headers = {'Authorization': 'Token 3177f1710c1360a482fb5ea84bf33f38462f7520','ngrok-skip-browser-warning': '7414'})
    
    req_read = req.json()
    # print(req_read)
    UID=req_read["RuserID"]
    # print(UID)
    access_code=req_read["Raccess_code"]
    # print(req_read["Raccess_code"])
    if MEM.objects.filter(USERID=UID):
      MEM.objects.update(ACCESSCODE=access_code)
    else:
      MEM.objects.create(USERID=UID, ACCESSCODE=access_code)

    return Login_and_AddSession(request, UID)

# def login2(request):


def login2(request):
    
    results=MEM.objects.filter(USERID =request.session['USERID'])
    ac_code=''
    for result in results:
        ac_code = result.ACCESSCODE
    url2=SACCngrok+'/RESTapiApp/Access/?Raccess_code='+ac_code
    req2=requests.get(url2,headers = {'Authorization': 'Token 3177f1710c1360a482fb5ea84bf33f38462f7520','ngrok-skip-browser-warning': '7414'})
    
    req_read2 = req2.json()
    print(req_read2)
    user= {
        'user_pic':req_read2['sPictureUrl'],
        'user_nickname':req_read2['sNickName'],
        'user_name':req_read2['sName'],
        'user_phone':req_read2['sPhone']
    }
    return user
    # print(type(req2.status_code))
    # print(type(req2.status_code))
    # if (req2.status_code!=200):
    #     print("================================")
    #     messages.error(request, '存取權已過期，請重新登入')
    #     logout(request)
    # else:
    
    #     pic=req_read2["sPictureUrl"]
    #     print(pic)

    #     return pic
# @csrf_exempt
def Login_and_AddSession(request, UID):
    print("login"+UID)
    # userID = UID
    if 'USERID' in request.session:
        try:
            del request.session['USERID']
        except:
            pass
    request.session['USERID'] = UID
    
    # USERDATA=USER.objects.get(userID=request.session['USERID'])
    # userUID=USER.USERID
    # access_code=USER.ACCESSCODE
     
    request.session.modified = True
    request.session.set_expiry(60*30) #存在30分鐘
    return HttpResponseRedirect('/member')

def member(request):
    user=login2(request)
    user_PictureUrl=user['user_pic']
    user_Name=user['user_name']
    user_NickName=user['user_nickname']
    user_Phone=user['user_phone']
    # userid=request.session['USERID'] 
    # userdata=MEM.objects.get()
    B=request.session.get('USERID')
    members = MEM.objects.get(USERID=B)
    #煤油用--------------------------
    total_gpoint=ORDER.objects.filter(MEMID=B).aggregate(gpoint_sum=Sum('GPOINT'))
    total_eex=buy.objects.filter(bmem=B).aggregate(eex_sum=Sum('ex'))
    total_gpoint=total_gpoint['gpoint_sum']
    total_eex=total_eex['eex_sum']
    if total_eex is None :
            total_eex=0
    if total_gpoint is None :
            total_gpoint=0
            
    total=int(total_gpoint)-int(total_eex)
    num=MEM.objects.get(USERID=B)
    num.POINT=total
    num.save()   
            
    return render(request, 'member.html', locals())

def GDPR(request):
    return render(request, 'GDPR.html')
    
# Create your views here.
#註冊、登入--------------------------/
def index(request):
    return render(request, 'index.html')

def page(request):
    A=request.session.get('USERID')
    members = MEM.objects.get(USERID=A)
    
    return render(request, 'page.html', locals())

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    IDCARD = request.POST.get('IDCARD')
    PASSWORD = request.POST.get('PASSWORD')
    try:
        user=MEM.objects.get(IDCARD=IDCARD)
        if PASSWORD==user.PASSWORD:
                #userlogin = request.session.get(uName)
            username=str(user.IDCARD)

            #request.session["IDCARD"]=IDCARD
            A=request.session.get('IDCARD')
            B=MEM.objects.get(IDCARD=A)
            total_gpoint=ORDER.objects.filter(MEMID=B).aggregate(gpoint_sum=Sum('GPOINT'))
            total_eex=buy.objects.filter(bmem=B).aggregate(eex_sum=Sum('ex'))
            total_gpoint=total_gpoint['gpoint_sum']
            total_eex=total_eex['eex_sum']
            if total_eex is None :
                total_eex=0
            if total_gpoint is None :
                total_gpoint=0
            total=total_gpoint-total_eex
            num=MEM.objects.get(IDCARD=B)
            num.POINT=total
            num.save()
            
            return redirect('/page/')
            #return render(request,'member.html',locals())
        else:
            messages.error(request, '帳號或密碼錯誤！')
            #return render(request,'signin.html',locals())
            return redirect('/signin/')
    except MEM.DoesNotExist:
            messages.error(request, '尚未註冊！')
            #return render(request,'signin.html',locals())
            return redirect('/signin/')


def register(request):
        # 從POST請求中提取出會員註冊表單中的欄位
        PHONE = request.POST['PHONE']
        NAME = request.POST['NAME']
        PASSWORD = request.POST['PASSWORD']
        NICKNAME = request.POST['NICKNAME']
        #POINT = request.POST['POINT']
        IDCARD = request.POST['IDCARD']
        #Invitation = request.POST.get('Invitation')
        # 驗證表單資料
        if MEM.objects.filter(PHONE=PHONE).exists():
                messages.error(request, '此手機號碼已註冊！')
                return redirect('/signup/')
        else:
                # 檢查電子郵件是否已存在
            if  MEM.objects.filter(IDCARD=IDCARD).exists():
                messages.error(request, '此帳號已註冊！')
                return redirect('/signup/')
            else:
                    # 如果資料無誤，則創建新使用者
                MEMBER = MEM(PHONE=PHONE, NAME=NAME, PASSWORD=PASSWORD, NICKNAME=NICKNAME, POINT=0, IDCARD=IDCARD)
                MEMBER.save()
                messages.success(request, '已成功註冊')
                return redirect('/signin/')

#登出、會員資料讀取、修改------------------/
def logout(request):
    request.session.clear()
    return redirect('/')

#def member(request):
#    A=request.session.get('IDCARD')
#    members = MEM.objects.get(IDCARD=A)
#    return render(request, 'member.html', locals())

def change(request):
    C=request.POST.get('newNICKNAME')
    D=request.POST.get('newPASSWORD')
    B=request.session.get('IDCARD')
    members = MEM.objects.get(IDCARD=B)
    members.NICKNAME=C
    members.PASSWORD=D
    members.save()
    return render(request, 'member.html', locals())

#問題回報--------------------/
def qa(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('qa')
        else:
            error_message = '表單無效，請再次輸入'
    else:
        form = ReportForm()
        error_message = ''
    return render(request, 'qa.html', {'form': form, 'error_message': error_message})


#碳權存摺、兌換卷--------------------

def point_use_view(request):
    if request.method == 'GET':
        r = REWARD.objects.all()
        A=request.session.get('USERID')
        members = MEM.objects.get(USERID=A)
        user=login2(request)
        user_NickName=user['user_nickname']
        
    elif request.method == 'POST':
        r = REWARD.objects.all()
        A=request.session.get('USERID')
        members = MEM.objects.get(USERID=A)                                                                                                                   

        B=request.POST.get('pname')
        C=request.POST.get('pex')
        if int(members.POINT)-int(C)<0:
            context="f"
            #return HttpResponse('點數不足')
            return render(request, 'point_use.html', locals())
        else:
            context="t"
        N=int(members.POINT)-int(C)
        members.POINT=N
        members.save()
        # D=request.POST.get('palert')
        #total=總點數-C
        buy.objects.create(bmem=A, bname=B, num=1, ex=C, left=N ,bdate=timezone.now())
        #messages.success(request, '已成功兌換 可至碳權存摺查看您的兌換紀錄')
    return render(request, 'point_use.html', locals())

def userbuy(request):
    A=request.session['USERID']
    #A=request.session.get('USERID')
    #members = MEM.objects.get(USERID=A)
    pname=request.GET.get('pname')
    pex=request.GET.get('pex')
    palert=request.GET.get('palert')
    return render(request, 'userbuy.html', locals())

def C_usehistory(request):
    #A=request.session.get('USERID')
    #B=MEM.objects.get(USERID=A)
    B=request.session['USERID']
    members = MEM.objects.get(USERID=B)
    BUYS = buy.objects.filter(bmem=B)
    ORDERS = ORDER.objects.filter(MEMID=B)
    
    total_p=ORDER.objects.filter(MEMID=B).aggregate(p_sum=Sum('GPOINT'))
    total_eex=buy.objects.filter(bmem=B).aggregate(eex_sum=Sum('ex'))
    total_p=total_p['p_sum']
    total_eex=total_eex['eex_sum']
    if total_eex is None :
            total_eex=0
    if total_p is None :
            total_p=0
    total=int(total_p)-int(total_eex)
    # num=request.session['USERID']
    num=MEM.objects.get(USERID=B)
    num.POINT=total
    num.save()
    return render(request, 'C_usehistory.html', locals())
#----------------------/
#Subquery1=ORDER.objects.filter(...).aggregate(subquery1=Sum('GPOINT'))
#Subquery2=buy.objects.filter(...).aggregate(subquery2=Sum('ex'))
#Total = Subquery1['subqery1'] - Subquery2['subquery2']

#difference = ORDER.objects.filter(...).annotate(
#subquery1=Sum('GPOINT')
#).annotate(
#subquery2=Subquery(buy.objects.filter(...).aggregate(subquery2=Sum('ex')))
#).annotate(
#difference=F('subquery1') - F('subquery2').values('difference')
#)

class myappViewSet(viewsets.ModelViewSet):
    queryset = ORDER.objects.all()
    serializer_class = myappSerializer

#rank-------------------------------------------
def rank(request):
    user=login2(request)
    user_PictureUrl=user['user_pic']
    user_Name=user['user_name']
    user_NickName=user['user_nickname']
    user_Phone=user['user_phone']

    A=request.session.get('USERID')
    members = MEM.objects.get(USERID=A)
    return render(request, 'rank.html',locals())