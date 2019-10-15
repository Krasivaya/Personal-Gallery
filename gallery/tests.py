from django.test import TestCase
from .models import Category, Image, Location
# Create your tests here.

class CategoryTestCase(TestCase):
    
    def setUp(self):
        self.category = Category(category = 'Person')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
        
    def test_save_categories(self):
        self.category.save_category()
        all_categories = Category.objects.all()
        self.assertTrue(len(all_categories) > 0)
        
    def test_search_category(self):
        self.category.save_category()
        images = Category.objects.filter(category__icontains='person')
        self.assertTrue(self.category, images)
        
        

class LocationTestCase(TestCase):
    
    def setUp(self):
        self.location = Location(location = 'Kigali')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
        
    def test_save_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)
        
    def test_get_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)
        
        
class ImageTestCase(TestCase):
    
    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Location(location = 'Kigali')
        self.new_location.save()
        
        self.category = Category(category = 'Person')
        self.category.save()
        
        # Creating a new Image and saving it
        self.image= Image(image_name = 'Image01', description ='In_glasses', image_file ='images/image01.jpg', location = self.new_location, category = self.category)
        self.image.save_image()


    def test_save_images(self):
        self.image.save_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) > 0)