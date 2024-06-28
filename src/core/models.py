from django.db import models
from users.models import User


class Company(models.Model):
    name = models.CharField('название', max_length=255, unique=True)
    members = models.ManyToManyField(
        User,
        verbose_name='участники',
        related_name='companies',
        through='CompanyMember',
    )

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'

    def __str__(self) -> str:
        return self.name


class CompanyMember(models.Model):
    company = models.ForeignKey(
        Company,
        verbose_name='компания',
        related_name='companies_members',
        on_delete=models.CASCADE,
    )
    member = models.ForeignKey(
        User,
        verbose_name='сотрудник',
        related_name='companies_members',
        on_delete=models.CASCADE,
    )
    date_joined = models.DateField('дата устройства')

    class Meta:
        verbose_name = 'сотрудник компании'
        verbose_name_plural = 'сотрудники компаний'

    def __str__(self) -> str:
        return f'{self.company}, {self.member.fullname}'

    @property
    def announcement_amount(self) -> int:
        return Announcement.objects.filter(author=self.member, company=self.company).count()


class Announcement(models.Model):
    title = models.TextField('заголовок')
    author = models.ForeignKey(User, verbose_name='автор', related_name='announcements', on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company,
        verbose_name='компания',
        related_name='announcements',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    views_amount = models.PositiveIntegerField('количество просмотров', default=0)
    position = models.PositiveSmallIntegerField('позиция в списке', unique=True, db_index=True)

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ('position',)

    def __str__(self) -> str:
        return self.title
