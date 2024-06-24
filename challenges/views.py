from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
months={
   "junary":"this is first month",
   "februry":"this is second month",
   "march":"This is the third month",
   "may":"this is the fourth month ",
   "april":"this is the fifth month",
   "june":"this is the sixth month",
   "july":"this is the seventh month",
   "augest":"this is augest",
    "september":"this is ninth month",
    "november":" this is november",
    "october":None
}
def index(request):
   monthlist=list(months)
   return render(request,"challenges/index.html",{
      "monthlist":monthlist
   })
def monthlychallang(request,month):
   if month > len(months):
      raise Http404()
   all_months=list(months.keys())
   forward_month=all_months[month-1]
   fullmonth=reverse("all-month",args=[forward_month])
   return HttpResponseRedirect(fullmonth)

def monthly_challanges(request,month):
 try:
     show=months[month]   
     return render(request,"challenges/challenge.html",
                   {"challange":show ,
                    "Month_challengs":month})               
 except: 
      
     raise Http404()
 
  