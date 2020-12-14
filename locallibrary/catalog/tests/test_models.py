from django.test import TestCase

from catalog.models import Author, Book, BookInstance, Genre, Language

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')
   
    def test_first_name_label(self):      
       author = Author.objects.get(id=1)
       field_label = author._meta.get_field('first_name').verbose_name
       self.assertEquals(field_label, 'first name')
    
    def test_date_of_death_label(self):      
       author = Author.objects.get(id=1)
       field_label = author._meta.get_field('date_of_death').verbose_name
       self.assertEquals(field_label, 'Died')
    
    def test_first_max_length(self):      
       author = Author.objects.get(id=1)
       max_length = author._meta.get_field('first_name').max_length
       self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))
    
    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/authors/1')
    
    def test_last_name_label(self):      
       author = Author.objects.get(id=1)
       field_label = author._meta.get_field('last_name').verbose_name
       self.assertEquals(field_label, 'last name')
    
    def test_date_of_birth_label(self):      
       author = Author.objects.get(id=1)
       field_label = author._meta.get_field('date_of_birth').verbose_name
       self.assertEquals(field_label, 'date of birth')
    
    def test_last_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        genre = Genre.objects.create(name='Psyhology')
    
    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def test_name_max_lenght(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)
    
    def test_object_name_is_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = '%s' % (genre.name)
        self.assertEquals(expected_object_name, str(genre))

class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        language = Language.objects.create(lang='Ukraine')
    
    def test_lang_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('lang').verbose_name
        self.assertEquals(field_label, 'lang')
    
    def test_name_max_lenght(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('lang').max_length
        self.assertEquals(max_length, 200)
    
    def test_object_name_is_lang(self):
        language = Language.objects.get(id=1)
        expected_object_name = '%s' % (language.lang)
        self.assertEquals(expected_object_name, str(language))


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = AuthorModelTest.setUpTestData()
        language = LanguageModelTest.setUpTestData()
        genre = GenreModelTest.setUpTestData()
        book = Book.objects.create(title='Pandas', author=author, summary='Some text', 
                                    isbn='2343234543234', language=language)
        #  ManyToMany fields add to test object(first save object)
        book.save()
        book.genre.add(genre)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = Book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_title_max_lenght(self):
        book = Book.objects.get(id=1)
        max_length = Book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)
    
    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = '%s' % (book.title)
        self.assertEquals(expected_object_name, str(book))
    
    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = Book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')
    
    def test_summary_max_lenght(self):
        book = Book.objects.get(id=1)
        max_length = Book._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)
    
    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = Book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')
     

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = Book._meta.get_field('isbn').max_length
        self.assertEquals(max_length, 13)
       
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')
    