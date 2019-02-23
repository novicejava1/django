from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

#CHART_CHOICES = [
#        ('tablechart', 'tablechart'),
#        ('barchart', 'barchart'),
#        ('piechart', 'piechart'),
#        ('linechart', 'linechart'),
#]

class ChartForm(forms.Form):

    CHART_CHOICES = (
        ("tablechart", "reports/tablechart.jpg"),
        ("barchart", "reports/barchart.jpg"),
        ("piechart", "reports/piechart.jpg"),
        ("linechart", "reports/linechart.jpg")
)

#    chartName = forms.CharField(label="Select the Type of Chart to Generate",widget=forms.RadioSelect(choices=CHART_CHOICES))
#    chartName = forms.ChoiceField(widget=forms.RadioSelect, choices=CHART_CHOICES)
    chartName = forms.ChoiceField(widget=forms.RadioSelect, choices=CHART_CHOICES)

