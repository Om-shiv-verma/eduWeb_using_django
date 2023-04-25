from django.http import HttpResponse,HttpResponseRedirect
# HttpResponse to show text message on the browser
from django.shortcuts import render, redirect
from .forms import usersForm

from service.models import Contact_img
from news.models import News
from contactenquiry.models import contactEnquiry
#Contact_img is name model
#News is name model
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives

def homePage(request):

    # subject='Testing mail'
    # form_email='patelomshiv65@gmail.com'
    # msg='<p>Welcome to <b>Om Shiv Patel</b></p>'
    # to='patelomshiv999@gmail.com'
    # msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    # msg.content_subtype='html'
    # msg.send()


# it is not working because of gmail less secure system is not allow
#     send_mail(
#     'Subject here',
#     'Here is the message.',
#     'patelomshiv65@gmail.com',
#     ['patelomshiv999@gmail.com'],
#     fail_silently=False,
#  )




    newsData=News.objects.all()
    data={
        'title':'Home Page',
        'bdata':'Welcome to Om Shiv Patel this is home page',
        'clist':['Cloude','AI','machine learning'],
        'numbers':[10,20,30,40,50,60],
        'newsData':newsData,

        'student_details':[
        {'name':'OmShiv','phone':7392949998},
        {'name':'testing','phone':7392949999},
        ]
    }
    return render(request,"index.html",data)

def newsDetails(request,slug):
    newsDetails = News.objects.get(news_slug=slug)
    data={
        'newsDetails':newsDetails
    }

    return render(request,"newsdetails.html",data)

def contact(request):
    # contactData = Contact_img.objects.all().order_by('-id')[2:6]
    contactData = Contact_img.objects.all()
    paginator = Paginator(contactData,3)

    page_number = request.GET.get('page')
    contactDatafinal = paginator.get_page(page_number)
    totalpage = contactDatafinal.paginator.num_pages
    # if request.method == "GET":
    #     st=request.GET.get('servicename')
    #     if st!=None:
    #         contactData = Contact_img.objects.filter(vision__icontains=st)
    # for a in contactData:
    #     print(a.imgpath)
    data3={
        'contactData':contactDatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request,"contact.html",data3)

def aboutus(request):
    if request.method == "GET":
        output=request.GET.get('output')
    return render(request,"aboutus.html",{'output':output})

def course(request):
    return render(request,"course.html")


def courseDetails(request,courseid):
    return HttpResponse(courseid)

def registration(request):
    finalans=0
    fn = usersForm()
    data1={'form':fn}
    try:
        if request.method == "POST":
        # fname = request.GET['fname']
        # lname = request.GET['lname']
        # fathname = request.GET['fathname']
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            fathname = request.POST.get('fathname')
            finalans= fname+lname+fathname

            data1={
                'form':fn,
                'output':finalans
            }
            url="/aboutus/?output={}".format(finalans)

            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass   
    return render(request,"registration.html",data1)


def submitform(request):
    try:
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            fathname = request.POST.get('fathname')
            email = request.POST.get('email')
            finalans= fname+lname+fathname+email
       
            return HttpResponse(finalans)
    except:
        pass


def calculator(request): 
    c=''
    try:
        if request.method == "POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr == '+':
                c=n1+n2
            elif opr == '-':
                c=n1-n2
            elif opr == '*':
                c=n1*n2
            else:
                c=n1/n2  
        print(c)          
    except:
        c="Invalid Operation"
    return render(request,"calculator.html",{'c':c})


def evenodd(request):
    c=''
    try:
        if request.method == "POST":
            if request.POST.get('num1') == "":
                return render(request,"evenodd.html",{'error':True})
            n=eval(request.POST.get('num1'))
            if n%2==0:
               c="Even Number"
            else:
                c="Odd Number"           
    except:
        c="Invalid Operation"
    return render(request,"evenodd.html",{'c':c})

def marksheet(request):
    data={}
    c=''
    try:
        if request.method == "POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            n3=eval(request.POST.get('num3'))
            n4=eval(request.POST.get('num4'))
            n5=eval(request.POST.get('num5'))
            sum=n1+n2+n3+n4+n5
            p=sum*100/500
            if p>=60:
                d="1st"
            elif p>=48:
                d="2nd"
            elif p>=35:
                d="3rd"
            else:
                d="fail"

            data={
                'total':sum,
                'per':p,
                'division':d
            }
            return render(request,"marksheet.html",data) 
        return render(request,"marksheet.html") 
    except:
        d="Invalid Operation"
   
def saveEnquiry(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        fathername = request.POST.get('fathname')
        email = request.POST.get('email')
        phone = request.POST.get('ph')

        en=contactEnquiry(fname=fname,lname=lname,fathername=fathername,email=email,phone=phone)
        en.save()
    return render(request,"contact.html")
