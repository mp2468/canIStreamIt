# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    # def get(self, request, **kwargs):
    #     return render(request, 'index.html', context=None)
    template_name = "index.html"
    # def post(request, self):
    #     if request.method == "POST":
    #         print("yoyooyoyoo")
    #         print(request)
    #         screenname = request.POST.get("handle", None)  # handle is the name of the input in the question.
    #         # Here you can do anything with your screenname, like passing it to the function.
    #         return render(request, 'index.html', context=None)

        # Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"
    def page(request, second):
        if request.method == "POST":
            print("yoyooyoyoo")
            print(request)
            screenname = request.POST.get("handle", None)  # handle is the name of the input in the question.
            # Here you can do anything with your screenname, like passing it to the function.
            return render(request, 'about.html', context=None)

# class ShowAddView(TemplateView):
#     def post(request, second):
#         if request.method == "POST":
#             print("yoyooyoyoo")
#             print(request)
#             screenname = request.POST.get("handle", None)  # handle is the name of the input in the question.
#             # Here you can do anything with your screenname, like passing it to the function.
#             return render(request, 'index.html', context=None)