from typing import List
from django.db.models import query
from django.http import response, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post
from .models import Person
from .forms import createNewRegister, signIn

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
import re

# Create your views here.

# class StartingPageView(ListView):

#     template_name = "news/index.html"
#     model = Post
#     ordering = ["date"]
#     context_object_name = "posts"

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         data = queryset[:2]
#         return data

def StartingPageView(response):
    data = [
        {
            "image_name": {"url": "https://i.imgur.com/YZ5aejt.jpeg"},
            "title": "إقامة شراكة عالمية من أجل إتاحة 120 مليون اختبار من اختبارات كوفيد-19 السريعة ‏والميسورة التكلفة والعالية الجودة للبلدان ذات الدخل المنخفض والمتوسط",
            "excerpt": "أُعلن اليوم في إطار مبادرة تسريع إتاحة أدوات مكافحة كوفيد-19 (مسرّع الإتاحة) عن إبرام مجموعة من الاتفاقات من أجل إتاحة اختبارات كوفيد-19 السريعة والميسورة التكلفة والعالية الجودة للبلدان ذات الدخل المنخفض والمتوسط. ومن بين المنظمات المشاركة في هذه الاتفاقات الهامة المركز الأفريقي لمكافحة الأمراض والوقاية منها، ومؤسسة بيل وميليندا غيتس، ومبادرة كلينتون لتوفير الصحة (CHAI)، ومؤسسة وسائل التشخيص الجديدة المبتكرة (FIND)، والصندوق العالمي، والمرفق الدولي لشراء الأدوية (Unitaid)، ومنظمة الصحة العالمية."
        },
        {   "image_name": {"url": "https://i.imgur.com/1GDA3fE.jpg"},
            "title": "إدارة الوباء المعلوماتي بشأن كوفيد-19: تعزيز السلوكيات الصحية وتخفيف الآثار الضارة للمعلومات الخاطئة والمضللة",
            "excerpt": "بيان مشترك لمنظمة الصحة العالمية والأمم المتحدة واليونيسيف وبرنامج الأمم المتحدة الإنمائي واليونسكو وبرنامج الأمم المتحدة المشترك المعني بفيروس نقص المناعة البشرية/الإيدز والاتحاد الدولي للاتصالات ومبادرة جس النبض العالمي للأمم المتحدة والاتحاد الدولي لجمعيات الصليب الأحمر والهلال الأحمر"
        }
    ]
    return render(response, "news/index.html", {"posts": data, "loggedIn": response.user.is_authenticated })

class AllNewsView(ListView):
    template_name = "news/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class AllImages(ListView):
    template_name = "news/all-images.html"
    model = Post
    ordering = ["date"]
    context_object_name = "all_images"

# class RegisterForm(ListView):
#     template_name = "news/register-form.html"
#     model = Person
#     ordering = []

class SingleNewView(DetailView):
    template_name = "news/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context


def Login(response):
    if response.method == "POST":
        form = signIn(response.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # print(username, password)
            if username == "admin" and password == "admin":
                print("Logged In")
                user = authenticate(response, username=username, password=password)
                # print(user.is_authenticated, request.user.is_authenticated)
                if user is not None:
                    login(response, user)
                    return redirect("/")
            else:
                print("Not Logged In")
                return render(response, "news/login.html", {"form": form, "message": True})
    else:
        form = signIn()
        return render(response, "news/login.html", {"form": form, "message": False})

def Logout(response):
    logout(response)
    return redirect("/login")



def registerCase(response):
    if response.method == "POST":
        form = createNewRegister(response.POST)
        print(form)
        # print(form)
        if form.is_valid():
            personName = form.cleaned_data["personName"]
            age = form.cleaned_data["age"]
            typeVaccine = form.cleaned_data["typeVaccine"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            sickBefore = form.cleaned_data["sickBefore"]
            notes = form.cleaned_data["notes"]

            # print("N:", personName);
            t = Person(personName=personName, age=age, typeVaccine=typeVaccine, phone=phone, email=email, sickBefore=sickBefore, notes=notes)
            t.save()
            print("Saved Successfully")

        # return HttpResponseRedirect("index.html")
        return render(response, "news/index.html", {"form": form})
    else:
        form = createNewRegister()
        return render(response, "news/register-form.html", {"form": form})

@login_required(login_url="login")
def Data(response):
    # form = Person()
    all_entries = Person.objects.all();
    
    pattern = re.compile("(?:^|\s)'([^']*?)'(?:$|\s)")
    # sickBefore = pattern.match(all_entries.sickBefore)
    # typeVaccine = pattern.match(all_entries.typeVaccine)
    # print(sickBefore)
    # print(typeVaccine)
    # for entry in all_entries:
    #     print(entry.sickBefore)
    return render(response, "news/applicant.html", {"all_entries": all_entries})