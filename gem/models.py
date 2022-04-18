from django.db import models


class ORIGINAL_CHECK(models.Model):
    Uid = models.CharField(max_length=10)
    Tel = models.CharField(max_length=11)
    Atti = models.CharField(max_length=4)
    Order = models.CharField(max_length=6)
    SendId = models.IntegerField()


class ORIGINAL_SENDER(models.Model):
    Scomp = models.CharField(max_length=70)
    Sper = models.CharField(max_length=20)
    Stel = models.CharField(max_length=11)
    Spost = models.CharField(max_length=6)
    SendId = models.IntegerField()


class ORIGINAL_INNERINFO(models.Model):
    Total = models.IntegerField()
    finishTime = models.DateField()
    Pick = models.CharField(max_length=20)
    Cost = models.FloatField()
    pickTime = models.DateField()
    IsPay = models.BooleanField()
    Uid = models.CharField(max_length=10)


class CHECK_PATH(models.Model):
    PicUrl = models.CharField(max_length=120)
    ChechMan = models.CharField(max_length=20)
    TaskAttri = models.CharField(max_length=6)
    Code = models.CharField(max_length=4)
    StoneId = models.CharField(max_length=10)
    Result = models.CharField(max_length=10)
    Appearance = models.IntegerField()
    Massive = models.FloatField()
    Density = models.FloatField()
    Refraction = models.FloatField()
    LightFigure = models.IntegerField()
    Detail = models.CharField(max_length=150)
    ORD = models.CharField(max_length=50)
    Uid = models.CharField(max_length=10)


class TASK_MANAGE(models.Model):
    StoneId = models.CharField(max_length=10)
    Demand = models.CharField(max_length=200, default="无")
    Condition = models.CharField(max_length=200, default="无")
    Dived = models.CharField(max_length=20)
    Book = models.CharField(max_length=20)  # 证书种类


class MEMBER_INFO(models.Model):
    MemberName = models.CharField(max_length=10)
    MemberTel = models.CharField(max_length=11)
    MemberType = models.CharField(max_length=10)
    Represent = models.CharField(max_length=50)
    BookId = models.CharField(max_length=20)  # 执照号
    PostId = models.CharField(max_length=6)
    MenberComp = models.CharField(max_length=150)
    MemCompAddr = models.CharField(max_length=150)


# Create your models here.

class Shouyang(models.Model):
    testNo = models.CharField(max_length=20, default='未填写')
    tel = models.CharField(max_length=20, default='未填写')
    testSituation = models.CharField(max_length=20, default='未填写')
    testCompany = models.CharField(max_length=20, default='未填写')
    testNum = models.CharField(max_length=20, default='未填写')
    kuangNo = models.CharField(max_length=20, default='未填写')
    time = models.CharField(max_length=20, default='未填写')
    money = models.CharField(max_length=10, default='未填写')
    paid = models.CharField(max_length=4, default='未填写')


class Yangpin(models.Model):
    testNo = models.CharField(max_length=20, default='未填写')
    situation = models.CharField(max_length=20, default='未填写')
    no = models.CharField(max_length=10, default='未填写')
    result = models.CharField(max_length=20, default='未填写')
    appear = models.CharField(max_length=20, default='未填写')
    weight = models.CharField(max_length=20, default='未填写')
    midu = models.CharField(max_length=20, default='未填写')
    zheshe = models.CharField(max_length=20, default='未填写')
    jcy = models.CharField(max_length=20, default='未分配')
    certificate = models.CharField(max_length=20, default='未生成证书')
    name = models.CharField(max_length=20, default='--')


class totalCalculate(models.Model):
    a1 = models.IntegerField(default=0)
    a2 = models.IntegerField(default=0)
    a3 = models.IntegerField(default=0)
    a4 = models.IntegerField(default=0)
    a5 = models.IntegerField(default=0)
    a6 = models.IntegerField(default=0)
    a7 = models.IntegerField(default=0)


class vip(models.Model):
    name = models.CharField(max_length=20, default='未填写')
    tel = models.CharField(max_length=20, default='未填写')
    type = models.CharField(max_length=10, default='未填写')
    people = models.CharField(max_length=20, default='未填写')
    number = models.CharField(max_length=20, default='未填写')
    mail = models.CharField(max_length=20, default='未填写')
    company = models.CharField(max_length=20, default='未填写')
    address = models.CharField(max_length=20, default='未填写')


class a基本设置(models.Model):
    单页表格长度上限 = models.CharField(max_length=20, default='未填写')
    站点编号 = models.CharField(max_length=20, default='未填写')
    当前编号 = models.CharField(max_length=20, default='未填写')
    默认检测批号 = models.CharField(max_length=20, default='未填写')
    电子秤默认串口 = models.CharField(max_length=20, default='未填写')
    电子秤显示精度 = models.CharField(max_length=20, default='未填写')
    电子秤默认波特率 = models.CharField(max_length=20, default='未填写')
    默认分页长度 = models.CharField(max_length=20, default='未填写')
    默认证书存储路径 = models.CharField(max_length=20, default='未填写')
    默认报表存储路径 = models.CharField(max_length=20, default='未填写')
