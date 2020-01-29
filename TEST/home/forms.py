from django import forms

class ContactForm(forms.Form):
    job_size = forms.ChoiceField(choices =[('0-$400','0-$400'), ('$400-$1000','$400-$1000'), ('$1000 - $3000','$1000 - $3000'), ('$3,000-$5,000','$3,000-$5,000'), ('$5,000-$10,000','$5,000-$10,000'), ('$10,000 - $25,000','$10,000 - $25,000'), ('$25,000 - $50,000','$25,000 - $50,000'), ('$25,000 - $50,000','$25,000 - $50,000'),], label = 'Job Size')
    company_size = forms.ChoiceField(choices =[('0-$400','0-$400'), ('400-$1000','$400-$1000'), ('$1000 - $3000','$1000 - $3000'), ('$3,000-$5,000','$3,000-$5,000'), ('$5,000-$10,000','$5,000-$10,000'), ('$10,000 - $25,000','$10,000 - $25,000'), ('$25,000 - $50,000','$25,000 - $50,000'), ('$25,000 - $50,000','$25,000 - $50,000'),], label = 'Company Size')
    priority = forms.ChoiceField(choices =[('1.1','1.1'), ('1','1'), ('2','2'), ('3','3'),], label = 'Priority')
    ctc = forms.CharField(label = 'Average CTC of the Production team working on this Project')
    hrs = forms.CharField(label = 'Estimated # of hrs for this Project')
    turnaround_time = forms.ChoiceField(choices = [('Very Quick','Very Quick'), ('Quick','Quick'), ('Average','Average'),], label = 'Turnaround Time')
    req_spec = forms.ChoiceField(choices = [('Hardly any definition','Hardly any definition'), ('Roughly Defined','Roughly Defined'), ('Clearly Defined','Clearly Defined'), ('Clearly defined with Disclaimer','Clearly defined with Disclaimer'), ('Manmonth','Manmonth'),], label = 'Requirement Specification')
    credit_days = forms.ChoiceField(choices = [('Advance Payment','Advance Payment'), ('21 days Credit','21 days Credit'), ('30 days Credit','30 days Credit'), ('45 days Credit','45 days Credit'), ('60 days Credit','60 days Credit'),], label = 'Credit Days')
    manpower_util = forms.ChoiceField(choices = [('110%','110%'), ('90%','90%'), ('80%','80%'), ('70%','70%'), ('60%','60%'),], label = 'Manpower Utilization')