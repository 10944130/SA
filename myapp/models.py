from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
#登入註冊--------------------/
class MEM(models.Model):
    #MEMID =  models.CharField('會員ID',max_length=3)
    USERID=models.CharField(max_length=100)
    PHONE = models.CharField('手機',max_length=10, blank=False, null=True)
    NAME = models.CharField('姓名',max_length=10, blank=False, null=True)
    PASSWORD = models.CharField('密碼',max_length=20, blank=False, null=True)
    NICKNAME = models.CharField('暱稱',max_length=20, blank=False, null=True)
    POINT = models.CharField('點數',max_length=30, blank=True, null=True)
    #Email = models.EmailField('Email',max_length=30, blank=False, null=False)
    IDCARD = models.CharField('身分證',max_length=10, blank=False, null=True)
    ACCESSCODE = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.USERID

#問題回報--------------------/
class qa(models.Model):
    
    MEMID = models.CharField('會員ID',primary_key=True,max_length=1000,null=False)
    DISC = models.TextField('問題描述',max_length=255, blank=False, default='')
    IMAGE=models.ImageField('上傳圖片',max_length=1000, blank=True, default='')
    RDATE = models.DateTimeField('送出日期',default = timezone.now)

    def __str__(self):
        return self.MEMID

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

class Report(models.Model):
    # 其他字段
    description = models.TextField()
    image = models.ImageField(upload_to='reports/')
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.description

#碳權存摺、兌換卷--------------------/

class REWARD(models.Model):
    R_ID = models.CharField('商品ID',max_length=50)
    R_NAME = models.CharField('商品名稱',max_length=50,null=False)
    R_IMG = models.ImageField('商品img',upload_to='static/images')
    R_CONTENT= models.CharField('商品內容',max_length=50, null=False, default='')
    COSTPOINT= models.CharField('商品點數',max_length=50, null=False, default='')
    ALERT= models.CharField('兌換警告',max_length=50, null=False, default='')
    def __str__(self):
        return self.R_ID

#class userbuy(models.Model):
#    DATE=models.DateTimeField('日期',default=timezone.now)
#    ORDERID=models.CharField('訂單編號',max_length=5)
#    USERNAME = models.CharField('使用者名稱',max_length=20,blank=True)
#    PNAME = models.CharField('商品名稱',max_length=50)
#    EX= models.CharField('支出',max_length=50)
#    LEFT= models.CharField('剩餘點數',max_length=50)
#    def __str__(self):
#        return self.ORDERID
class buy(models.Model):
    bmem = models.CharField('使用者名稱',max_length=50)
    bname = models.CharField('商品名稱',max_length=50, blank=False, null=True)
    num= models.IntegerField('數量')
    ex= models.IntegerField('支出')
    left= models.IntegerField('剩餘點數') 
    bid = models.UUIDField('訂單編號',default=uuid.uuid4)
    bdate = models.DateTimeField('兌換日期',default = timezone.now)

    def __str__(self):
        return self.bmem

class ORDER(models.Model):
    ORDID = models.CharField('訂單編號',max_length=50,null=False)
    MEMID = models.CharField('使用者編號',max_length=50, null=False, default='')
    APPID = models.CharField('APP編號',max_length=50, null=False, default='')
    C_AMOUNT= models.CharField('花費碳稅',max_length=50, null=False, default='')
    GPOINT = models.IntegerField('獲得點數')
    AMOUNT = models.CharField('消費總金額',max_length=50, null=False, default='')
    CDATE = models.DateTimeField('成立時間',default = timezone.now)

    def __str__(self):
        return self.ORDID



#api------------------
import uuid
def UUIDrand():
    return str(uuid.uuid4())

class LOGIN(models.Model):
    FKcheck=models.CharField(max_length=36,default=UUIDrand)
    Rstate=models.CharField(max_length=42)
    Raccesscode=models.CharField(max_length=43)

class USER(models.Model):
    USERID=models.CharField(max_length=100)
    ACCESSCODE=models.CharField(max_length=100)
