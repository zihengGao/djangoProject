from django.shortcuts import render, redirect
from webapp import models
from webapp.models import User


# def users(request):
#     student_queryset = models.User.objects.all()
#     return render(request, "user.html", {"student_queryset": student_queryset})




# 查询所有数据

def user(request):
    # 查询所有数据
    user_list = models.Users.objects.all()#查询方法：all(),filter(),exclude(),get()
    return render(request, 'user.html', {'user_list': user_list})
#添加数据
def add(request):
    # 判断请求方式，如果post，说明前端需要提交数据
    if request.method == 'POST':
        # 获取传过来的get()函数中的参数（html文件input（）标签的name属性）
        dep_name=request.POST.get('dep_name')
        dep_script=request.POST.get('dep_script')
    # strip()过滤
        if dep_name.strip()=='':
            return render(request,'test_orm_old/add_dep_old.html',{'error_info':'名称不能为空'})
        # 用create（）函数新建一条函数，会自动保存，不需要调用save（）函数
        try:
            # 添加数据有两种方式：1.使用模型管理器的create（）方法添加数据，2.使用模型实列save（）方法保存
            p=User.objects.create(dep_name=dep_name,dep_script=dep_script)
            return redirect('/test_orm_old/list_dep_old/')
        except Exception as e:
            return render(request,'test_orm_old/add_dep_old.html',{'error_info':'输入部门名称重复或信息错误！'})
        finally:
            pass
    return render(request,'test_orm_old/add_dep_old.html/')
#删除数据
def dele(request,dep_id):
    dep_object=User.objects.get(id=dep_id)
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old/')
#修改数据
def edit(request,dep_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        dep_object=User.objects.get(id=id)
        dep_object.dep_name=dep_name
        dep_object.dep_script=dep_script
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object=User.objects.get(id=dep_id)
        return render(request,'test_orm_old/edit_dep_old.html',{'User':dep_object})

