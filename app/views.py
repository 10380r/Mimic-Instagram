from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Message, Friend, Like
from .forms import FriendsForm, PostForm

from django.db.models import Q
from django.contrib.auth.decorators import login_required
import sys, os, pickle
from .imagenet import imagenet
#import recommend_user

# indexのビュー関数
@login_required(login_url='/admin/login/')
def index(request):
    # POST時
    # メッセージの取得
    messages = Message.objects.all()

    params = {
            'login_user' : request.user,
            'contents'   : messages,
            }
    return  render(request, 'app/index.html', params)


@login_required(login_url='/admin/login/')
def post(request):
    # POST時
    if request.method == 'POST':
        # 送信内容取得

        msg             = Message()
        msg.owner       = request.user
        msg.photo       = request.FILES['photo']
        imagenet_results = imagenet(msg.photo)
        msg.img_subject = imagenet_results[0][1]
        msg.img_acc     = imagenet_results[0][2]
        msg.content     = request.POST['content']
        msg.save()

        result_dic = {obj:pred for ctg,obj,pred in imagenet_results}

        try:
            with open('pickles/%s.pkl' %(str(msg.owner).replace('@','')), 'rb') as f:
                user_results = pickle.load(f)
                for obj,pred in result_dic.items():
                    if obj in user_results.keys():
                        user_results[obj] += pred
                    else:
                        user_results[obj] = pred

            with open('pickles/%s.pkl' %(str(msg.owner).replace('@','')), 'wb') as f:
                pickle.dump(user_results, f)

        # 初投稿の場合
        except FileNotFoundError:
            with open('pickles/%s.pkl' %(str(msg.owner).replace('@','')), 'wb') as f:
                pickle.dump(result_dic, f)

        return redirect(to='/app')
    # GET時
    else:
        form = PostForm()
        
    params = {
            'login_user' : request.user,
            'form'       : form,
            }
    return render(request, 'app/post.html', params)


@login_required(login_url='/admin/login/')
def like(request, like_id):
    # いいねするメッセージを取得
    like_msg = Message.objects.get(id=like_id)
    is_like  = Like.objects.filter(owner=request.user) \
            .filter(message=like_msg).count()
    # いいね済みかどうか
    if is_like > 0:
        messages.success(request, 'you were already liked.')
        return redirect(to='/app')

    # いいねカウント
    like_msg.like_count += 1
    like_msg.save()
    # いいねを作成
    like = Like()
    like.owner = request.user
    like.message = like_msg
    like.save()

    messages.success(request, 'Liked!')
    return redirect(to='/app')


@login_required(login_url='/admin/login/')
def recommend(request):

    #recomend_user = recomend_user(request.user)
    params = {
            'login_user'     : request.user,
           # 'reccomend_user' : recommend_user,
            }

    return  render(request, 'app/recommend.html', params)
