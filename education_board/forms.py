from company.models import Team, TeamAdmin
from .models import Board, Slide
from django import forms


class CreateBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'description', 'team']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CreateBoardForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['team'].queryset = Team.objects.filter(team_of_admin__user=user)
            self.user = user  # Store user for later use in save method

    def save(self, commit=True):
        board = super(CreateBoardForm, self).save(commit=False)
        if not self.instance.pk:  # Checking if it's a new instance
            team_admin = TeamAdmin.objects.filter(user=self.user, team=self.cleaned_data['team']).first()
            if team_admin:
                board.created_by = team_admin
            else:
                raise forms.ValidationError("You are not an admin for the selected team.")
        if commit:
            board.save()
            self.save_m2m()
        return board


class CreateSlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['title', 'description']  # Update this if you decide to include 'image' in the future

    def __init__(self, *args, **kwargs):
        self.board_id = kwargs.pop('board_id', None)  # Extract the board_id from kwargs
        super(CreateSlideForm, self).__init__(*args, **kwargs)
        if not self.board_id:
            raise forms.ValidationError("Board ID must be provided to create a slide.")

    def save(self, commit=True):
        slide = super(CreateSlideForm, self).save(commit=False)
        slide.board_id = self.board_id  # Set the board ID for the slide

        if commit:
            slide.save()
        return slide
