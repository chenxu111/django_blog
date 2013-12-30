from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
# from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user 	 = auth.authenticate(username = username, password = password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',
							{'fullname':request.user.username})

def logout(request):
	print 'logout'
	auth.logout(request)
	return render_to_response('logout.html')

def invalid_login(request):
	print 'login invalid'
	return render_to_response('invalid.html')

def register_user(request):
	print 'register_user'
	return render_to_response('loggedin.html')

def register_user(request):
	print 'register_user'
	if request.method == 'POST':
		# form = UserCreationForm(request.POST)
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			print 'form is_valid'
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))
	# args['form'] = UserCreationForm()
	args['form']  = MyRegistrationForm()
	return render_to_response('register.html',args)

def register_success(request):
	return render_to_response('register_success.html')



