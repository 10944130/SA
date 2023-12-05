from django.contrib import admin
from myapp.models import REWARD
# Register your models here.(0)
#admin.site.register(student)
#登入註冊--------------------
from myapp.models import MEM
class MEMAdmin(admin.ModelAdmin):
    list_display=('USERID','id','PHONE','NAME','PASSWORD','NICKNAME','POINT','IDCARD','ACCESSCODE')
    list_filter=('id',)
    search_fields=('PHONE','NAME','PASSWORD',)
    ordering=('id',)

admin.site.register(MEM, MEMAdmin)
#admin.site.(MEM, MEMAdmin)

#問題回報-----------------------
from myapp.models import Issue
admin.site.register(Issue)

from myapp.models import qa
admin.site.register(qa)

from myapp.models import Report
admin.site.register(Report)


# Register your models here.(1)
#碳權存摺、兌換卷--------------------

class REWARDAdmin(admin.ModelAdmin):
    list_display=('R_ID','R_NAME','R_IMG','COSTPOINT','R_CONTENT','ALERT',)
    list_filter=('R_ID',)
    ordering=('R_ID',)

admin.site.register(REWARD, REWARDAdmin)



from myapp.models import buy
class buyAdmin(admin.ModelAdmin):
    list_display=('bmem','bname','num','bid','bdate','ex','left')
    list_filter=('bid',)
    ordering=('bid',)

admin.site.register(buy, buyAdmin)

from myapp.models import ORDER
class ORDERAdmin(admin.ModelAdmin):
    list_display=('id','ORDID','MEMID','APPID','C_AMOUNT','GPOINT','AMOUNT',)
    ordering=('ORDID','MEMID',)

admin.site.register(ORDER, ORDERAdmin)

#api-----------------------------------

from myapp.models import LOGIN
class LOGINAdmin(admin.ModelAdmin):
    list_display=('FKcheck','Rstate','Raccesscode',)
    ordering=('FKcheck',)

admin.site.register(LOGIN, LOGINAdmin)

from myapp.models import USER
admin.site.register(USER)
#-----------------------------------------------