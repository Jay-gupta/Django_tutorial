from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from home.forms import ContactForm

# Create your views here.
def contact(request):
    template = 'home/base.html'

    job_profit_dict = {'0-$400':30 ,'$400-$1000':29 ,'$1000 - $3000':28 ,'$3,000-$5,000':27 ,'$5,000-$10,000':26 ,'$10,000 - $25,000':25 ,'$25,000 - $50,000':24 ,'$25,000 - $50,000':23 }
    job_prodbill_dict = {'0-$400':80 ,'$400-$1000':82 ,'$1000 - $3000':84 ,'$3,000-$5,000':86 ,'$5,000-$10,000':88 ,'$10,000 - $25,000':90 ,'$25,000 - $50,000':92 ,'$25,000 - $50,000':95 }
    job_ie_dict = {'0-$400':110 ,'$400-$1000':100 ,'$1000 - $3000':80 ,'$3,000-$5,000':60 ,'$5,000-$10,000':40 ,'$10,000 - $25,000':30 ,'$25,000 - $50,000':20 ,'$25,000 - $50,000':10 }
    priority_dict = {'1.1':15 , '1':10 , '2':5 , '3':0 }
    turnaround_dict = {'Very Quick':10 , 'Quick':5 , 'Average':0 }
    rs_dict = {'Hardly any definition':100 , 'Roughly Defined':40 , 'Clearly Defined':20 , 'Clearly defined with Disclaimer':10 , 'Mammoth':0 }
    credit_dict = {'Advance Payment':0.0 , '21 days Credit':1.0 , '30 days Credit':2.0 , '45 days Credit':2.5 , '60 days Credit':3.0 }
    mu_dict = {'110%':-10 , '90%':0 , '80%':10 , '70%':20 , '60%':25 }

    tot_prod_hrs = 171
    usd_rate = 72
    prod_cost = 38000  #monthly cost
    

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            job_size = form.cleaned_data['job_size']
            company_size = form.cleaned_data['company_size']
            priority = form.cleaned_data['priority']
            ctc = float(form.cleaned_data['ctc'])
            hrs = float(form.cleaned_data['hrs'])
            turnaround_time = form.cleaned_data['turnaround_time']
            req_spec = form.cleaned_data['req_spec']
            credit_days = form.cleaned_data['credit_days']
            manpower_util = form.cleaned_data['manpower_util']
        
            profit_val = job_profit_dict[job_size]
            prodbill_val = job_prodbill_dict[job_size]
            indexp_val = job_ie_dict[job_size]
            priority_val = priority_dict[priority]
            avgctc_val = ctc
            esthrs_val = hrs
            ttime_val = turnaround_dict[turnaround_time]
            rs_val = rs_dict[req_spec]
            credit_val = credit_dict[credit_days]
            mu_val = mu_dict[manpower_util]

            gross_cost = (prod_cost/usd_rate)/tot_prod_hrs
            net_cost = (gross_cost+((indexp_val/100)*7000))/tot_prod_hrs
            net_cost_af_ttime = net_cost*(1+(ttime_val/100))
            net_cost_af_prodbill = net_cost_af_ttime/(prodbill_val/100)
            net_cost_af_profit = net_cost_af_prodbill/(1-(profit_val/100))
            net_cost_af_credit = net_cost_af_profit/(1-(credit_val/100))
            
            total_discount = priority_val + mu_val
            
            net_price = round(net_cost_af_credit*(1-(total_discount/100)), 2)
            net_price_per_month = round(net_price*tot_prod_hrs, 2)

        return render(request, template, {'form':form, 'text1':net_price, 'text2':net_price_per_month})

    else:
        form = ContactForm()
        return render(request, template, {'form':form})