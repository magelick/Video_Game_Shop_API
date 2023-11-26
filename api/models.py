from django.db import models


class Platform(models.Model):
    """
    Модель представления Платформ: Xbox, PlayStation5, PC.....
    """
    # Название платформы
    title = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        verbose_name="название платформы"
    )
    # Слаг платформы
    slug = models.SlugField(
        unique=True,
        blank=False,
        null=False,
        verbose_name="слаг платформы"
    )
    # Информация о платформе
    information = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="информация о платформе"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "платформа"
        verbose_name_plural = "платформы"
        ordering = ("title",)


class Game(models.Model):
    """
    Модель представления Игр: Dead Space, Hogwarts Legacy, Resident Evil 4, Marvel’s Spider-Man 2.........
    """
    # Название игры
    title = models.CharField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        verbose_name="название игры"
    )
    # Слаг игры
    slug = models.SlugField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        verbose_name="слаг игры"
    )
    # Цена игры
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="цена игры"
    )
    # Обратная связь с моделью Платформ (многие ко многим)
    platform = models.ManyToManyField(
        to="Platform",
        related_name="games",
        verbose_name="платформы игры"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "игра"
        verbose_name_plural = "игры"
        ordering = ("title",)


class Device(models.Model):
    """
    Модель представления Девайсов: джостики, мышки, клавиатуры, VR.......
    """
    # Название девайса
    title = models.CharField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        verbose_name="название девайса"
    )
    # Слаг девайса
    slug = models.SlugField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        verbose_name="слаг девайса"
    )
    # Информация о девайсе
    information = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="информация о девайсе"
    )
    # Цена девайса
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="цена девайса"
    )
    # Обратная связь с моделью Платформ
    platform = models.ForeignKey(
        to="Platform",
        on_delete=models.CASCADE,
        db_index=True,
        blank=False,
        null=False,
        related_name="devices",
        verbose_name="платформа девайса"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "девайс"
        verbose_name_plural = "девайсы"
        ordering = ("title",)


class Souvenir(models.Model):
    """
    Модель представления Сувениров: фигурки, комиксы, подписки.........
    """
    # Название сувенира
    title = models.CharField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        verbose_name="название сувенира"
    )
    # Слаг сувенира
    slug = models.SlugField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        verbose_name="слаг сувенира"
    )
    # Игформация о сувенире
    information = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name="информация о сувенире"
    )
    # Цена сувенира
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="цена сувенира"
    )
    # Обратная связь с моделью Игр
    game = models.ForeignKey(
        to="Game",
        on_delete=models.CASCADE,
        db_index=True,
        blank=False,
        null=False,
        related_name="souvenirs",
        verbose_name="игра сувенира"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "сувенир"
        verbose_name_plural = "сувениры"
        ordering = ("title",)