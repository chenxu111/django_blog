from django import forms
from models import Article
from models import Comment

class ArticleForm(forms.ModelForm):

	class Meta():
		model = Article
		fields = ('title','body','pub_date','thumbnail')

class CommentForm(forms.ModelForm):
	class Meta():
		model = Comment
		fields = ('first_name','second_name','body')

# def add_comment(request,pk):
# 	"""add a new comment."""
# 	p = request.POST

# 	if p.has_key("body") and p["body"]:
# 		author = "anonymous"
# 		if p["author"]:
# 			author = p["author"]

# 		comment = Comment(article = Article.objects.get(pk=pk))
# 		cf = CommentForm(p,instance =comment)
# 		cf.fields["author"].required = False

# 		comment = cf.save(commit = False)
# 		comment.author = author
# 		comment.save()
