from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data['title']
        qs = Article.objects.all().filter(title__icontains = title)
        if qs.exists():
            self.add_error("title", f"{title} is already exists!!")
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        return title


    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower() == "the office":
            self.add_error('title',"office is not allowed")
        if "office" in content.lower():
            self.add_error('content',"office is not allowed in content")
        return cleaned_data