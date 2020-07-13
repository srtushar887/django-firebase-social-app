from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User



#firebase admin sdk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth, firestore




# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request,'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

def dashboard(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'dashboard/index.html')
    else:
        return render(request,'account/login.html')



cred = credentials.Certificate("social-a44c3-firebase-adminsdk-va99i-a207695022.json")
db =firebase_admin.initialize_app(cred)

def filrebaseusers(request):
    if request.user.is_authenticated:

    
        auth.list_users()
        # while page:
            # for user in page.users:
            #     print('User: ' + user.uid)
            # # Get next batch of users.
            # page = page.get_next_page()
        


        # for user in auth.list_users().iterate_all():
        #     print('User: ' + user.uid)


        context = {
            'users' : auth.list_users().iterate_all()
        }

        return render(request, 'dashboard/firebase.html',context)
    else:
        return render(request,'account/login.html')




def userdelete(request,uid):
    if request.user.is_authenticated:
        auth.delete_user(uid)
        return redirect('filrebaseusers')





db = firestore.client()
def filrebaseusersposts(request,uid):
    if request.user.is_authenticated:

        docs = db.collection(u'post').stream()
        
        

        docss = db.collection(u"post").where(u"userid",u"==", uid).get()

        for doc in docss:
            print(f'{doc.id} => {doc.to_dict()}')
        



        context = {
            'posts' : doc
        }
        

        return render(request, 'dashboard/firbaseUserPosts.html',context)
    else:
        return render(request,'account/login.html')
