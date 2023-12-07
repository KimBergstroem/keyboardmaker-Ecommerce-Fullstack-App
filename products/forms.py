from django import forms
from .models import Product, Category, Review, ProductImage
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    images = forms.ModelMultipleChoiceField(
        queryset=ProductImage.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        has_bought = self.initial.get('has_bought', False)
        
        if has_bought:
            self.fields['text'].widget.attrs['placeholder'] = 'Your review...'
            self.fields['text'].widget.attrs['rows'] = 3
        else:
            self.fields['text'].widget.attrs['placeholder'] = ''
            self.fields['text'].widget.attrs['rows'] = 3

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            field.label = False  # This removes the label from the form field

    def clean(self):
        cleaned_data = super().clean()
        has_bought = cleaned_data.get('has_bought', False)  # Default to False if not present
        text = cleaned_data.get('text', '')
        rating = cleaned_data.get('rating', '')

        if has_bought and not text:
            self.add_error('text', 'This field is required.')
        if has_bought and not rating:
            self.add_error('rating', 'This field is required.')

        return cleaned_data
