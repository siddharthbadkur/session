from django.shortcuts  import render

# Create your views here.
def set(request):
    my_list1={'id':1,'name':'siddharth','city':'pipariya'}
    my_list2={'id':2,'name':'arun','city':'gadarwara'}
    my_list=[my_list1,my_list2]
    request.session['data']=my_list
    return render(request,'set.html')
def get(request):
    data1=request.session.get('data','guest')
    return render(request,'get.html',{"name":data1})
def delete(request):
    if 'data' in request.session:
        del request.session ['data']
        # request.session.flush()
    return render(request,'delete.html')