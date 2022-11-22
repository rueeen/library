from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.
# The Country class is a model that has an id and a name. The id is a UUIDField, the name is a
# CharField
class Country(models.Model):
    # Creating a column in the database called id, which is a UUIDField.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID pais")
    # Creating a column in the database called name, which is a varchar(50)
    name = models.CharField(max_length=50, verbose_name="Nombre pais")

    def __str__(self) -> str:
        """
        This function returns the name of the object
        :return: The name of the object
        """
        return self.name

# The Author class has a name and a country. The name is a CharField, the country is a ForeignKey
class Author(models.Model):
    # Creating a column in the database called name, which is a varchar(200) and it is the primary
    # key.
    name = models.CharField(primary_key=True, max_length=200, verbose_name="Nombre autor")
    # Creating a column in the database called country, which is a foreign key to the Country table.
    country = models.ForeignKey(Country, verbose_name="Pais autor", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        """
        The __str__() function is a special function in Python classes. It is used to control how
        variables are displayed when using functions such as print()
        :return: The name of the object
        """
        return self.name

# The Category class is a model that has an id, a name, and a string representation
class Category(models.Model):
    # Creating a column in the database called id, which is a UUIDField.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Categoría")
    # Creating a column in the database called name, which is a varchar(50)
    name = models.CharField(max_length=50, verbose_name="Nombre Categoría")

    def __str__(self) -> str:
        """
        This function returns the name of the object
        :return: The name of the object
        """
        return self.name

# The Book class has a one-to-many relationship with the Author class, and a many-to-many relationship
# with the Category class
class Book(models.Model):
    # Creating a column in the database called isbn, which is a varchar(10) and it is the primary key.
    isbn = models.CharField(primary_key=True, max_length=10, verbose_name="Isbn")
    # Creating a column in the database called title, which is a varchar(50)
    title = models.CharField(max_length=50, verbose_name="Título")
    # Creating a column in the database called year, which is a date.
    year = models.DateField(verbose_name="Año publicacion")
    # Creating a column in the database called description, which is a text field.
    description = RichTextField(verbose_name="Descripción")
    # Creating a many-to-many relationship between the Book and Category classes.
    category = models.ManyToManyField(Category, verbose_name="Categorias")
    # Creating a column in the database called author, which is a foreign key to the Author table.
    author = models.ForeignKey(Author, verbose_name="Autor", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        """
        The __str__ function is a special function that is called when you print an object
        :return: The title of the question
        """
        return self.title


