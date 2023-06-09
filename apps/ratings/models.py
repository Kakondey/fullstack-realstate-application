from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampUUIDModel
from apps.profiles.models import Profile
from core.settings.base import AUTH_USER_MODEL


class Rating(TimeStampUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_(
        "User providing the rating"), on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(Profile, verbose_name=_("Agent being rated"),
                              related_name="agent_review", on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(verbose_name=_("Rating"), choices=Range.choices,
                                 help_text="add your ratings please.", default=0)
    comments = models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
