from django.db import models
import users.exceptions as CustomExceptions
from django.utils.translation import gettext_lazy as _
import users.config as config
from users.utils import external_api


class Profile(models.Model):
    github_url = models.URLField(blank=True, default="")
    bio = models.TextField(blank=True)
    front_end_score = models.IntegerField(null=False, default=20)
    back_end_score = models.IntegerField(null=False, default=20)
    database_score = models.IntegerField(null=False, default=20)
    devops_score = models.IntegerField(null=False, default=20)
    mobile_score = models.IntegerField(null=False, default=20)
    cv = models.FileField(null=True, upload_to="cv")
    academic_qualification = models.CharField(blank=True, max_length=30)
    academic_qualification_file = models.FileField(
        null=True, upload_to="academic")
    projects = models.CharField(_("projects"), blank=True, max_length=200)
    user = models.ForeignKey(
        'auth.User', related_name='profile', on_delete=models.CASCADE)
    news_pref = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return "%s's profile" % (self.user)

    def total_score(self):
        return self.mobile_score+self.devops_score+self.database_score+self.front_end_score+self.back_end_score

    def save(self, *args, **kwargs):
        """
        Fails if score does not have a total of 100 and if news source is not available.
        """
        if self.total_score() != 100:
            raise CustomExceptions.ScoreNot100

        if self.news_pref not in config.NEWS_SITES:
            raise CustomExceptions.NewsSourceNotAvailable

        super(Profile, self).save(*args, **kwargs)


class LanguageWithScore(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='languages')

    def save(self, *args, **kwargs):

        added_language = self.name[0].capitalize()+self.name[1:]
        data = external_api.get_programming_language(added_language)
        
        if len(data['results'])==0:
            raise CustomExceptions.CannotCreateSameLanguage

        for i in data["results"]:
            if i["ProgrammingLanguage"] != added_language:
                raise CustomExceptions.LanguageNotFound([i["ProgrammingLanguage"] for i in data['results']])
            else:
                print(True)


        super(LanguageWithScore, self).save(*args, **kwargs)


    def __str__(self):
        return "%s: %d" % (self.name, self.score)

    class Meta:
        ordering = ['score']


class Hackathon(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=30)
    members = models.ManyToManyField(Profile, related_name="hackathons", blank=True)
    website = models.URLField(null=True)
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title
