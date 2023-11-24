from django import forms
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def save(self, commit=True):
        # Call the save method of the parent class
        instance = super().save(commit=False)

        # Call the custom image_size_save method to handle image resizing
        instance.image_size_save()

        # Save the instance to the database
        if commit:
            instance.save()
            self.save_m2m()

        return instance


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("text", "rating")
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect())
