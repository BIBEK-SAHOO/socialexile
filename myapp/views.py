from django.shortcuts import render
from .forms import DownVoteForm
from .models import DownVote
from .serializers import DownVoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, Http404
import json

# Create your views here.

def downvote(request):
    form = DownVoteForm(request.POST or None)
    if form.is_valid():
        url = request.POST.get('url')
        userId = url.split('/')[-1]
        postId = url.split('/')[-2]
        all_data = DownVote.objects.all()
        flag = 0
        for data in all_data:
            if data.user_profile == userId:
                if data.post_id == postId:
                    flag = 0
                    break
                else:
                    flag = 1
            else:
                flag = 1
        if flag == 1:
            new_data = DownVote(post_id=postId, user_profile=userId)
            new_data.save()
        form = DownVoteForm()
    context = {
        'form': form
    }
    return render(request, "myapp/form_input.html", context)


def downvote_ext(request):
    url = request.POST.get('url')
    userId = url.split('/')[-1]
    postId = url.split('/')[-2]
    all_data = DownVote.objects.all()
    flag = 0
    for data in all_data:
        if data.user_profile == userId:
            if data.post_id == postId:
                flag = 0
                break
            else:
                flag = 1
        else:
            flag = 1
    if flag == 1:
        new_data = DownVote(post_id=postId, user_profile=userId)
        new_data.save()
    vote_list = []
    all_data = DownVote.objects.all()
    for data in all_data:
        if data.post_id == postId:
            vote_list.append(data)
    return HttpResponse(
        json.dumps({'total_downvote': len(vote_list), 'msg': 'Update Success.'}),
        content_type="application/json"
    )

def d(request, pid, uid):
    all_data = DownVote.objects.filter(post_id=pid, user_profile=uid)
    if len(all_data) >0: 
        vote= DownVote.objects.get(post_id=pid, user_profile=uid)
        vote.delete()
    else: 
        new_data = DownVote(post_id=postId, user_profile=userId)
        new_data.save()
        
    all_data = DownVote.objects.filter(post_id=pid)
    
    
    return HttpResponse(
        json.dumps({'total_downvote': len(all_data), 'msg': 'Update Success.'}),
        content_type="application/json"
    )

# REST APIs

# FOR DOWN VOTE
class DownVoteAPI(APIView):
    """
    Submit your Social URL with USER_ID and POST_ID
    URL LIKE : example.com/postID/userID
    """
    def post(self, request, format=None):
        success = False                             # Initially Success is set to False
        message = ""                                # Initially message is empty
        if 'url' in request.data.keys():            # Check If URL is passed from POST request or not
            url = request.data['url']               # get URL from Post Request
            if len(url.split('/')) == 3:            # Check Url have userId and PostId
                userId = url.split('/')[-1]         # Extract UserID from URL
                postId = url.split('/')[-2]         # Extract PostID from URL
                # Code is same as downvote function from below line to Line - 114
                all_data = DownVote.objects.all()
                flag = 0
                for data in all_data:
                    if data.user_profile == userId:
                        if data.post_id == postId:
                            flag = 0
                            break
                        else:
                            flag = 1
                    else:
                        flag = 1
                if flag == 1:
                    new_data = DownVote(post_id=postId, user_profile=userId)
                    new_data.save()
                success = True # Set Success is true if User Down vote submitted successfully
                message="Downvote submitted successfully!"
            else:
                message = "Please Provide URL with userId and postId as requested!"
        else:
            message = "Please Provide URL with postId and userId as requested!"
        return Response({"success": success, "message": message}, status=status.HTTP_201_CREATED) # Success response to User
        

# FOR DOWN VOTE EXT
class DownVoteExtAPI(APIView):
    """
    Submit your Social URL with USER_ID and POST_ID
    URL LIKE : example.com/postID/userID
    """
    def post(self, request, format=None):
        hit_by_current_user = False               # Initially hit_by_current_user is set to False
        vote_list = []                            # Initially vote_list is set as empty array
        message = ""                              # Initially message is empty
        if 'url' in request.data.keys():          # Check If URL is passed from POST request or not
            url = request.data['url']             # get URL from Post Request
            if len(url.split('/')) == 3:          # Check Url have userId and PostId
                userId = url.split('/')[-1]       # Extract UserID from URL
                postId = url.split('/')[-2]       # Extract PostID from URL
                # Code is same as downvote_ext function from below line to Line - 159
                all_data = DownVote.objects.all()
                flag = 0
                for data in all_data:
                    if data.user_profile == userId:
                        # Set hit_by_current_user is True if current user found in DB for dislike that post
                        hit_by_current_user = True
                        if data.post_id == postId:
                            flag = 0
                            break
                        else:
                            flag = 1
                    else:
                        flag = 1
                if flag == 1:
                    new_data = DownVote(post_id=postId, user_profile=userId)
                    new_data.save()
                all_data = DownVote.objects.all()
                for data in all_data:
                    if data.post_id == postId:
                        vote_list.append(data)
                message="successfully get records!"
            else:
                message = "Please Provide URL with postId and userId as requested!"
        else:
            message = "Please Provide URL with postId and userId as requested!"
        total_downvote = len(vote_list) # Count the Number of total downvote
        return Response({"total_downvote": total_downvote, "hit_by_current_user": hit_by_current_user, "message": message}, status=status.HTTP_201_CREATED)