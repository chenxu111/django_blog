#encoding:utf8
# from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from forms import ArticleForm
from forms import CommentForm

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator,InvalidPage,EmptyPage

def hello(request):
	name = 'mike'
	html = "<html><body>hi %s this seems to have worked</body></html>" %name
	return HttpResponse(html)

def hello_template(request):
	name = 'mike'
	t = get_template('hello.html')
	html = t.render(Context({'name':name}))
	return HttpResponse(html)

def hello_from_simple(request):
	name = 'sean for hello from simple'
	return render_to_response('hello.html', {'name':name})

from article.models import Article
from article.models import Comment

# def articles(request):
# 	return render_to_response('articles.html',{'articles':Article.objects.all()})

#演示session使用
def articles(request):
	language = 'en-gb'
	session_language = 'en-gb'
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	
	print language
	if 'lang' in request.session:
		session_language = request.session['lang']
	print "session language %s"%session_language

	articles = Article.objects.all().order_by("pub_date")
	paginator = Paginator(articles,3)

	try:
		page = int(request.GET.get("page",1))
	except ValueError:
		page = 1

	try:
		display_articles = paginator.page(page)
	except (InvalidPage,EmptyPage):
		display_articles = paginator.page(paginator.num_pages)
		
	return render_to_response('articles.html',{'articles':display_articles,'language':language,'session_language':session_language})


def article(request,article_id=1):
	myArticle = Article.objects.get(id=article_id)
	comments = Comment.objects.filter(article=myArticle)
	return render_to_response('article.html',{'article':myArticle, 'comments':comments})

def language(request,language='en-gb'):
	response = HttpResponse('setting language to %s' %language)
	response.set_cookie('lang',language)
	request.session['lang'] = language
	return response

def create(request):
	print 'create'
	if request.POST:
		# form = ArticleForm(request.POST)
		form = ArticleForm(request.POST,request.FILES)
		print 'post'
		if form.is_valid():
			form.save()
			print 'is_valid'
			return HttpResponseRedirect('/articles/all')
		else:
			print 'invalid'
	else:
		form = ArticleForm()
		print 'else'

	args = {}
	args.update(csrf(request))
	args['form'] = form
	print 'create_article'
	return render_to_response('create_article.html',args)

def like_article(request,article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		if a:
			count = a.likes
			count+=1
			a.likes = count
			a.save()
		else:
			print 'artile is not valid'

		return HttpResponseRedirect('/articles/get/%s'%article_id)

def unlike_article(request,article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		if a:
			count = a.unlikes
			count +=1
			a.unlikes = count
			a.save()
		else:
			print 'article is not valid'

		return HttpResponseRedirect('/articles/get/%s'%article_id)




