from django.db import models
from users.exceptions import ScoreNot100

class Profile(models.Model):
    github_url = models.URLField(blank=True, default="")
    bio = models.TextField(blank=True)
    front_end_score = models.IntegerField(null=False, default=20)
    back_end_score = models.IntegerField(null=False, default=20)
    database_score = models.IntegerField(null=False, default=20)
    devops_score = models.IntegerField(null=False, default=20)
    mobile_score = models.IntegerField(null=False, default=20)
    user = models.ForeignKey(
        'auth.User', related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return "%s's profile" % (self.user)

    def total_score(self):
        return self.mobile_score+self.devops_score+self.database_score+self.front_end_score+self.back_end_score

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        if self.total_score()!=100:
            print(self.total_score())
            raise ScoreNot100
        super(Profile, self).save(*args, **kwargs)



class LanguageWithScore(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name='profile')

    def __str__(self):
        return "%s %d" % (self.name, self.score)

    class Meta:
        ordering = ['score']
