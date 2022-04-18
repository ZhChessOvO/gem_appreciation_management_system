from django.shortcuts import render
from django.contrib import messages
from gem import dataValidity
import csv
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import random
import tempfile


# Create your views here.
from django.http import HttpResponse, FileResponse

from django.shortcuts import render

from gem.models import *


def index(request):
    v1 = Yangpin.objects.all()
    a1 = len(v1)  # 总数
    a2 = 0  # 处理数
    for v in v1:
        if v.situation == "通过审核" or v.situation == "证书作废":
            a2 = a2 + 1
    a3 = a1 - a2  # wei处理数量
    # a = [a1, a2, a3]
    return render(request, 'index.html', {'a1': a1, 'a2': a2, 'a3': a3})


def page1(request):
    v1 = Shouyang.objects.all()
    return render(request, 'page1.html', {'v1': v1})


def page2(request):
    # if request.method=='POST':
    #     for n1 in Yangpin.no:
    #         if request.POST[n1]:
    #             Yangpin.objects.filter(no=request.POST[n1]).update(situation="通过审核")
    #
    #     messages.success(request, "已通过！")
    #
    #     v1 = Yangpin.objects.all()
    #     return render(request, 'page2.html', {'v1': v1})
    # else:
    v1 = Yangpin.objects.all()
    return render(request, 'page2.html', {'v1': v1})


def page3(request):
    v1 = Yangpin.objects.all()
    return render(request, 'page3.html', {'v1': v1})


def page4(request):
    v1 = Yangpin.objects.all()
    return render(request, 'page4.html', {'v1': v1})


def page5(request):
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="datas.csv"'
        writer = csv.writer(response)
        writer.writerow(['任务序号', '检测批号', '检测员', '编号', '证书种类', '任务状态', '样品名称'])
        datas = Yangpin.objects.all().values_list('no', 'testNo', 'jcy', 'no', 'certificate', 'situation', 'name')
        for data in datas:
            writer.writerow(data)
        return response
    else:
        v1 = Yangpin.objects.all()
        return render(request, 'page5.html', {'v1': v1})


def page6(request):
    v1 = vip.objects.all()
    return render(request, 'page6.html', {'v1': v1})


def page7(request):
    return render(request, 'page7.html')


def page8(request):
    return render(request, 'page8.html')


def page1add(request):
    if request.method == 'POST':
        x1 = Shouyang(testNo=request.POST['a1'], tel=request.POST['a2'], testSituation=request.POST['a3'],
                      testCompany=request.POST['a4'], testNum=request.POST['a5'], kuangNo=request.POST['a6'],
                      time=request.POST['a7'], money=request.POST['a8'], paid=request.POST['a9'])
        if dataValidity.isValid(x1):
            x1.save()
        messages.success(request, "添加成功！")
        # con=sqlite3.connect("db.sqlite3")
        # con.execute("insert into Shouyang(testNo) values(%s)" %(request.POST['a1']))
        return render(request, 'page1add.html')
    else:
        return render(request, 'page1add.html')


def page2add(request):
    if request.method == 'POST':
        # test = request.POST['a1']
        # if len(Shouyang.objects.filter(testNo=test)) == 0:  # 不存在收养单
        #     messages.error(request, "检测批号不存在！请检查是否正确")
        #     return render(request, "page2add.html")

        x1 = Yangpin(testNo=request.POST['a1'], situation=request.POST['a2'], no=request.POST['a3'],
                     result=request.POST['a4'], appear=request.POST['a5'], weight=request.POST['a6'],
                     midu=request.POST['a7'], zheshe=request.POST['a8'], name=request.POST['a9'])
        if dataValidity.isValid(x1):
            x1.save()

        try:
            photo = request.FILES.get('photo')
            photoname = "gem/static/img/" + request.POST['a3'] + "." + photo.name.split('.')[-1]
            with open(photoname, 'wb+') as f:
                f.write(photo.read())
            # messages.success(request, "图片上传成功！")
        except Exception as e:
            print(e)

        messages.success(request, "添加成功！")
        # con=sqlite3.connect("db.sqlite3")
        # con.execute("insert into Shouyang(testNo) values(%s)" %(request.POST['a1']))
        return render(request, 'page2add.html')
    else:
        # win32print.GetDefaultPrinter():
        messages.error(request, "没有检测到电子秤，改为手动输入！")
        return render(request, 'page2add.html')


def page2edit(request):
    if request.method == 'POST':
        x0 = Yangpin.objects.filter(no=request.POST['a1'])

        if len(x0) == 0:
            messages.error(request, "编号不存在！请检查是否正确")
            return render(request, "page2edit.html")

        x = x0[0]
        if x.jcy == "未分配":
            messages.error(request, "当前任务没有安排检测员！无法通过审核")
            return render(request, "page2edit.html")
        if not x.situation == "审核中":
            messages.error(request, "当前任务已经审核过！无需重新审核")
            return render(request, "page2edit.html")

        Yangpin.objects.filter(no=request.POST['a1']).update(situation="通过审核")
        Yangpin.objects.filter(no=request.POST['a1']).update(certificate="自动生成证书")
        messages.success(request, "已通过！")
        # con=sqlite3.connect("db.sqlite3")
        # con.execute("insert into Shouyang(testNo) values(%s)" %(request.POST['a1']))
        return render(request, 'page2edit.html')
    else:
        return render(request, 'page2edit.html')


# def jumpTest(request):
#     return render(request,'jumpTest.html')

# def tables(request):
#     return render(request, 'tables.html')


def page3edit(request):
    if request.method == 'POST':
        x0 = Yangpin.objects.filter(no=request.POST['a1'])
        if len(x0) == 0:
            messages.error(request, "任务编号不存在！请检查是否正确")
            return render(request, "page3edit.html")

        Yangpin.objects.filter(no=request.POST['a1']).update(jcy=request.POST['a2'])
        # Yangpin.objects.filter(no=request.POST['a1']).update(certificate="获得证书")
        messages.success(request, "已分配！")
        # con=sqlite3.connect("db.sqlite3")
        # con.execute("insert into Shouyang(testNo) values(%s)" %(request.POST['a1']))
        return render(request, 'page3edit.html')
    else:
        return render(request, 'page3edit.html')


def page4print(request):
    if request.method == 'POST':

        v = Yangpin.objects.filter(no=request.POST['a1'])

        if len(v) == 0:
            messages.error(request, "证书编号不存在！请检查是否正确")
            return render(request, "page4print.html")

        x = v[0]

        if x.situation == "证书作废" or x.situation == "审核中":
            messages.error(request, "当前编号没有证书！请检查其是否已经作废！")
            return render(request, 'page4print.html')

        jieguo = x.result
        waiguan = x.appear
        zhiliang = x.weight
        fangda = x.zheshe
        guijinshu = x.name
        qita = ""
        jiandingzhe = x.jcy
        shenhezhe = x.jcy
        bianhao = x.no
        yanzhengma = str(random.randint(0, 99999999)).zfill(8)

        img = cv2.imread("gem/static/img/background.jpg")
        fontpath = "gem/static/SimHei.ttf"
        font = ImageFont.truetype(fontpath, 12)
        pil = Image.fromarray(img)
        draw = ImageDraw.Draw(pil)
        draw.text((90, 65), jieguo, font=font, fill=(0, 0, 0))
        draw.text((90, 98), waiguan, font=font, fill=(0, 0, 0))
        draw.text((90, 130), zhiliang, font=font, fill=(0, 0, 0))
        draw.text((95, 160), fangda, font=font, fill=(0, 0, 0))
        draw.text((100, 193), guijinshu, font=font, fill=(0, 0, 0))
        draw.text((80, 224), qita, font=font, fill=(0, 0, 0))
        draw.text((80, 287), jiandingzhe, font=font, fill=(0, 0, 0))
        draw.text((80, 320), shenhezhe, font=font, fill=(0, 0, 0))
        draw.text((380, 65), bianhao, font=font, fill=(0, 0, 0))
        draw.text((380, 98), yanzhengma, font=font, fill=(0, 0, 0))
        # try:
        #     draw.bitmap((380, 130), "gem/static/img/" + request.POST['a1'] + ".jpg")
        # except:
        #     pass

        img = np.array(pil)

        cv2.imshow("certificate-preview", img)
        cv2.waitKey()

        cv2.imwrite("gem/static/img/certi" + request.POST['a1'] + ".jpg", img)

        # try:
        #     response = FileResponse(img)
        #     response['Content-Type'] = 'image/jpg'
        #     response['Content-Disposition'] = 'attachment;filename="certificate.jpg"'
        #     win32api.ShellExecute(
        #         0,
        #         "printto",
        #         img,
        #         '"%s"' % win32print.GetDefaultPrinter(),
        #         ".",
        #         0
        #     )
        # except:
        #     messages.error(request, "系统默认打印机为空")

        # return response
        return render(request, 'page4print.html')
    else:
        return render(request, 'page4print.html')


def page4delete(request):
    if request.method == 'POST':
        x0 = Yangpin.objects.filter(no=request.POST['a1'])

        if len(x0) == 0:
            messages.error(request, "编号不存在！请检查是否正确")
            return render(request, "page4delete.html")

        x = x0[0]
        if x.certificate == "未生成证书":
            messages.error(request, "当前还没有证书！无法作废")
            return render(request, "page4delete.html")

        if x.situation == "证书作废":
            messages.error(request, "当前证书已作废！无需重新作废！")
            return render(request, "page4delete.html")

        Yangpin.objects.filter(no=request.POST['a1']).update(situation="证书作废")
        # Yangpin.objects.filter(no=request.POST['a1']).update(certificate="获得证书")
        messages.success(request, "已作废！可以前往管理员后台撤销")
        # con=sqlite3.connect("db.sqlite3")
        # con.execute("insert into Shouyang(testNo) values(%s)" %(request.POST['a1']))
        return render(request, 'page4delete.html')
    else:
        return render(request, 'page4delete.html')


def page6add(request):
    if request.method == 'POST':
        x1 = vip(name=request.POST['a1'], tel=request.POST['a2'], type=request.POST['a3'],
                 people=request.POST['a4'], number=request.POST['a5'], mail=request.POST['a6'],
                 company=request.POST['a7'], address=request.POST['a8'])
        if dataValidity.isValid(x1):
            x1.save()
        messages.success(request, "添加成功！")
        return render(request, 'page6add.html')
    else:
        return render(request, 'page6add.html')


def page6edit(request):
    if request.method == 'POST':

        x0 = vip.objects.filter(name=request.POST['a1'])
        if len(x0) == 0:
            messages.error(request, "会员名不存在！请检查是否正确")
            return render(request, "page6edit.html")

        vip.objects.filter(name=request.POST['a1']).update(tel=request.POST['a2'], type=request.POST['a3'],
                                                           people=request.POST['a4'], number=request.POST['a5'],
                                                           mail=request.POST['a6'],
                                                           company=request.POST['a7'], address=request.POST['a8'])
        messages.success(request, "已修改！")
        # con=sqlite3.connect("db.sqlite3")
        # con.execute("insert into Shouyang(testNo) values(%s)" %(request.POST['a1']))
        return render(request, 'page6edit.html')
    else:
        return render(request, 'page6edit.html')
    # return render(request, 'page6delete.html')


def page6delete(request):
    if request.method == 'POST':

        x0 = vip.objects.filter(name=request.POST['a1'])
        if len(x0) == 0:
            messages.error(request, "会员名不存在！请检查是否正确")
            return render(request, "page6delete.html")

        vip.objects.filter(name=request.POST['a1']).delete()
        messages.success(request, "已删除！可以在管理员后台根据日志进行撤销！")
        # con=sqlite3.connect("db.sqlite3")
        # con.execute("insert into Shouyang(testNo) values(%s)" %(request.POST['a1']))
        return render(request, 'page6delete.html')
    else:
        return render(request, 'page6delete.html')
    # return render(request, 'page6delete.html')
