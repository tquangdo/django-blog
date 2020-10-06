# ~~~ Lúc đã có Comment (giống C1) ~~~
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms_dotq_cmt import CommentForm
from .forms_dotq_post import PostForm  #nhập vô 1 file "forms_dotq_cmt.py" OK!
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# ~~~ C1 ~~~
# def onList(req):
#     data = {'postOnList': Post.objects.all().order_by('-date')}
#     return render(req, 'pages/blog_dotq.html', data)


# ~~~ C1 ~~~
# def onPost(req, arg_id):
#     try:
#         postOnPost = Post.objects.get(id=arg_id)
#     except Post.DoesNotExist:
#         # xử lí 404!!!
#         raise Http404('Bài viết KO tồn tại!!!')
#     return render(req, 'pages/post_dotq.html', {'postOnPost': postOnPost})
def onPost(req, arg_pk):
    postOnPost = get_object_or_404(
        Post, pk=arg_pk)  #(Post, pk=arg_pk, field n=val n...)
    formVar = CommentForm()
    if req.method == 'POST':
        # post= & author= chính là post & author of "forms_dotq_cmt.py>class CommentForm>__init__()"
        formVar = CommentForm(req.POST, post=postOnPost, author=req.user)
        if formVar.is_valid():
            formVar.save()
            return HttpResponseRedirect(
                req.path
            )  #vì nếu không redirect thì khi user nhấn F5 thì lại POST lại
        else:
            return HttpResponse('Lỗi validate!!!')
    return render(req, 'pages/post_dotq.html', {
        'postOnPost': postOnPost,
        'formOnPost': formVar
    })


def onVote(req, arg_pk):
    post_var = get_object_or_404(Post, pk=arg_pk)
    try:
        data_var = req.POST[
            'choiceName']  #tương đương req.POST.get('choiceName')
        choice_var = post_var.choice_set.get(pk=data_var)
    except:
        return HttpResponse('KO có choice nào!!!')
    choice_var.vote = choice_var.vote + 1  #khác với ++choice_var.vote!!!
    choice_var.save()
    return render(req, 'pages/vote_result.html', {'postOnVote': post_var})


class AddPost(LoginRequiredMixin, View):
    login_url = '../../login'

    def get(self, req):
        return render(req, 'pages/them_post.html', {'postAddPost': PostForm()})

    def post(self, req):
        post_form = PostForm(req.POST)
        if not post_form.is_valid():
            return HttpResponse('Nhập thông tin post bị invalid!!!')
        print(req.user.get_all_permissions())
        if req.user.has_perm(
                'blog_dotq.add_post'
        ):  #"add" là fix name, "post" là models.py>Post viết thường
            post_form.save()
        else:
            return HttpResponse('User "%s" KO có quyền tạo post!!!' %
                                (req.user.username))
        return HttpResponse('Lưu form OK')