from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Country, ProductReview


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        countries = Country.objects.all()
        country_friendly_names = [(c.id, c.get_friendly_name()) for c in countries]

        self.fields['category'].choices = category_friendly_names
        self.fields['country'].choices = country_friendly_names
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'user_name', 'review']

