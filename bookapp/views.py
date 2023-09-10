from django.shortcuts import render
from bookapp.models import*
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth import logout
import datetime

def index(request):
	return render(request,'user/index.html')

def service(request):
	return render(request,'user/service.html')

def about(request):
	return render(request,'user/about.html')

def contact(request):
	return render(request,'user/contact.html')

def registerr(request):
	if request.method=='POST':
		n=request.POST['Username']
		ph=request.POST['Phone']
		e=request.POST['Email']
		ps=request.POST['Password']
		if register.objects.filter(email=e):
			return render(request,'reg.html',{'msg':'email already exist'})
		else:
			q=register(name=n,phone=ph,email=e,password=ps,usertype='user')
			q.save()
	return render(request,'reg.html')

def login(request):
	if request.method=='POST':
		w=request.POST['email']
		e=request.POST['Password']
		q=register.objects.filter(email=w,password=e,status='approve')
		if q:
			for b in q:
				request.session['zz']=b.id
				ut=b.usertype
				if ut=='user':
					user_id=b.id
					return HttpResponseRedirect('/user_det/')
				else:
					return HttpResponseRedirect('/admin_det/')
		else:
			return render(request,'loggin.html',{'msg':'invalid email or password'})
	return render(request,'loggin.html')


def logoutt(request):
	if request.session.has_key('zz'):
		del request.session['zz']
	logout(request)
	return render(request,'loggin.html')


#########################################################################################admin


def admin_detail(request):
	return render(request,'admin/home.html')


def new_reg(request):
	if request.session.get('zz'):
		q=register.objects.filter(usertype='user',status='pending')
		return render(request,'admin/appremove.html',{'msg':q})
	return render(request,'loggin.html')


def Approve(request):
	y=request.GET['i_d']
	w=register.objects.filter(id=y).update(status='approve')
	return HttpResponseRedirect('/newregist/')



def Remove(request):
	t=request.GET['i_d']
	l=register.objects.filter(id=t).delete()
	return HttpResponseRedirect('/newregist/')


def Members(request):
	k=register.objects.filter(usertype='user',status='approve')
	return render(request,'admin/members.html',{'msg':k})


def add_book(request):
	if request.method=='POST':
		q=request.POST['name']
		w=request.POST['Author']
		e=request.POST['date']
		r=request.POST['edition']
		t=request.POST['pages']
		a=request.POST['copyy']
		s=request.POST['bookk']
		f=request.FILES['fil']
		l=add(book=q,author=w,date=e,edition=r,pages=t,copies=a,description=s,image=f)
		l.save()
	return render(request,'admin/addnew.html')


def updatepage(request):
	y=add.objects.all()
	return render(request,'admin/update.html',{'msg':y})

def remoove(request):
	q=request.GET['i_d']
	f=add.objects.filter(id=q).delete()
	return HttpResponseRedirect('/update_page/')

def updatelink(request):
	e=request.GET['i_d']
	d=add.objects.filter(id=e)
	return render(request,'admin/newform.html',{'msg':d})

def newform(request):
	if request.method=='POST':
		q=request.POST['name']
		w=request.POST['Author']
		e=request.POST['date']
		r=request.POST['edition']
		t=request.POST['pages']
		a=request.POST['copyy']
		s=request.POST['bookk']
		o=request.POST['idd']
		T=add.objects.filter(id=o).update(book=q,author=w,date=e,edition=r,pages=t,copies=a,description=s)
	return HttpResponseRedirect('/update_page/')


def img(request):
	q=request.GET['i_d']
	b=add.objects.filter(id=q)
	return render(request,'admin/update_img.html',{'msg':b})

def image_update(request):
	if request.method=='POST':
		i=request.FILES['fil'] 
		o=request.POST['img_id']
		r=add.objects.get(id=o)
		r.image=i
		r.save()
	return HttpResponseRedirect('/update_page/')




def details(request):
	r=add.objects.all()
	return render(request,'admin/details.html',{'msg':r})


def issu(request):
	w=requst.objects.filter(status='request pending')
	print(w)
	return render(request,'admin/issue.html',{'ms':w})

def app(request):
	q=request.GET['i']
	print(q)

	e=requst.objects.filter(id=q)
	for p in e:
		b_id=p.aa.id
		o=add.objects.filter(id=b_id)
		print(o)

	for x in o:
		w=x.copies
		u=int(w)-1
		d=add.objects.filter(id=b_id).update(copies='u')
		w=requst.objects.filter(id=q).update(status='Approve')
		return HttpResponseRedirect('/is/')
	


def ree(request):
	x=request.GET['i_d']
	k=requst.objects.filter(id=x).delete()
	return HttpResponseRedirect('/is/')







######################################################################################user
def user_detail(request):
	return render(request,'user/u_home.html')

def bookss(request):
	t=add.objects.all()
	return render(request,'user/books.html',{'msgg':t})

def bookrvw(request):
	t=request.GET['i_d']
	w=add.objects.filter(id=t)
	return render(request,'user/digital lb.html',{'msg':w})


def backpage(request):
	q=add.objects.all()
	return render(request,'user/books.html',{'msg':q})

def requ(request):
	f=request.session['zz']
	print(f)
	o=register.objects.get(id=f)
	bu=request.GET['t']
	j=add.objects.get(id=bu)
	a=(datetime.datetime.now())

	if requst.objects.filter(rr=o,aa=j,status='request pending'):
		n={'am':'tty'}
		return JsonResponse(n)
	elif requst.objects.filter(rr=o,aa=j,status='Approve'):
		n={'ab':'abc'}
		return JsonResponse(n)


	elif add.objects.filter(id=bu):
		h=add.objects.filter(id=bu)
		for x in h:
			uu=x.copies
			if int(uu)==0:
				n={'ac':'def'}
				return JsonResponse(n)

		k=requst(rr=o,aa=j,status='request pending',z=a)
		n={'aa':'vv'}
		k.save()
		return JsonResponse(n)


def trackk(request):
	q=requst.objects.all()
	return render(request,'user/track.html',{'mm':q})

def tremove(request):
	t=request.GET['i_d']
	e=requst.objects.filter(id=t).delete()
	return HttpResponseRedirect('/tracke/')