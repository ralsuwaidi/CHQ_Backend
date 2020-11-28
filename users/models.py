from django.db import models


class Profile(models.Model):
    github_url = models.URLField(blank=True, default="")
    bio = models.TextField(blank=True)
    user = models.ForeignKey(
        'auth.User', related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return "%s's profile" % (self.user.user)


class CriteriaWithScore(models.Model):
    FRONTEND = 'FE'
    BACKEND = 'BE'
    DATABASE = 'DA'
    DEVOPS = 'DO'
    MOBILE = 'MO'
    CRITERIA_CHOICES = [
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
        (DATABASE, 'Database'),
        (DEVOPS, 'Devops'),
        (MOBILE, 'Mobile'),
    ]
    criteria_name = models.CharField(
        max_length=2,
        choices=CRITERIA_CHOICES,
    )
    score = models.IntegerField(null=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.criteria_name


class LanguageWithScore(models.Model):
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    criteria = models.ForeignKey(
        CriteriaWithScore, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %d" % (self.name, self.score)

    class Meta:
        ordering = ['score']
