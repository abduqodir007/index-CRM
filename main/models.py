from django.db import models
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify

class Users(models.Model):
    GENDER_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Boshqa', 'Boshqa'),
    ]

    REGION_CHOICES = [
        ('Toshkent', 'Toshkent'),
        ('Andijon', 'Andijon'),
        ('Samarqand', 'Samarqand'),
        ('Buxoro', 'Buxoro'),

    ]

    CITY_CHOICES = [
        ('Toshkent shahar', 'Toshkent shahar'),
        ('Andijon shahar', 'Andijon shahar'),
        ('Samarqand shahar', 'Samarqand shahar'),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    birth_date = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    city_or_district = models.CharField(max_length=50, choices=CITY_CHOICES)
    profile_image = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to='profiles/')
        
    def __str__(self):
        return f"{self.name}"
    

class ProductCategory(models.Model):
    title = models.CharField(_("title"), max_length=256)

    class Meta:
        db_table = "project_category"
        verbose_name = _("project category")
        verbose_name_plural = _("project categories")

    def __str__(self):
        return f"{self.title}"
    
class ProductTag(models.Model):
    title = models.CharField(_("title"), max_length=256)

    class Meta:
        db_table = "product_tag"
        verbose_name = _("product tag")
        verbose_name_plural = _("product tags")

    def __str__(self):
        return f"{self.title}"
    

class Product(models.Model):
    title = models.CharField(_("title"), max_length=256)
    slug = models.SlugField(_("slug"), unique=True, blank=True, null=True)
    description = models.TextField(_("description"))
    categories = models.ManyToManyField(ProductCategory, verbose_name=_("categories"), related_name="products")
    tags = models.ManyToManyField(ProductTag, related_name="products", verbose_name=_("tags"))
    main_image = ResizedImageField(_("1-Rasm"), size=[545, 621], quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    main_image1 = ResizedImageField(_("2-Rasm"), size=[545, 621], quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    main_image2 = ResizedImageField(_("3-Rasm"), size=[545, 621], quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    main_image3 = ResizedImageField(_("4-Rasm"), size=[545, 621], quality=95, crop=["middle", "center"], upload_to="products/%Y/%m")
    is_top = models.BooleanField(_("project is top"), default=False)
    published_date = models.DateField(_("published date"), auto_now_add=True)
    price = models.DecimalField(_("Narhi"), max_digits=10, decimal_places=2)
    brand = models.CharField(_("brand"), max_length=256)
    product_code = models.CharField(_("Product code"), max_length=256)
    product_count = models.IntegerField(_("product count"), default=0)

    def save(self, *args, **kwargs):
        if not self.slug or self.title != Product.objects.get(id=self.id).title:  
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return f"{self.title}"
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_count = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order for {self.product.title} - {self.sale_count} units on {self.sale_date}"
    
    class Meta:
        db_table = "order"
        verbose_name = _("order")
        verbose_name_plural = _("orders")