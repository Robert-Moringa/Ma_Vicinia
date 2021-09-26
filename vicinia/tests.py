from django.test import TestCase
from .models import Business, Profile, NeighbourHood
from django.contrib.auth.models import User

class ProfileTest(TestCase):
    def setUp(self):
        self.robert= User.objects.create(username="Robert")
        self.test_profile= Profile.objects.create(user=self.robert,
                                                email='rober@gmail.com',
                                                pub_date='12',                                   
                                                why_here ='No retreat no surrender',
                                                profile_pic ='picture.jpg',
                                                )
        self.test_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))

    #Testing Save method
    def test_save_method(self):
        self.test_profile.save()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    # Tear down
    def tearDown(self):
        Profile.objects.all().delete()

    # delete methodTesting 
    def test_delete_profile(self):
        self.test_profile.delete()
        self.assertEqual(len(Profile.objects.all()), 0)


class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.robert= User.objects.create(username="Robert")
        self.test_neighbourhood= NeighbourHood.objects.create(admin=self.robert,
                                                name='Kibagabaga',
                                                county='Kericho',
                                                population=100, 
                                                description='Kericho',                                  
                                                
                                                area_pic_one ='picture.jpg',
                                                area_pic_two ='picture.jpg',
                                                )
        self.test_neighbourhood.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_neighbourhood, NeighbourHood))

    #Testing Save method
    def test_save_neigborhood_method(self):
        self.test_neighbourhood.save()
        nbd = NeighbourHood.objects.all()
        self.assertTrue(len(nbd)>0)

    # Tear down
    def tearDown(self):
        NeighbourHood.objects.all().delete()

    # delete methodTesting 
    def test_delete_neigborhood(self):
        self.test_neighbourhood.delete()
        self.assertEqual(len(NeighbourHood.objects.all()), 0)

    def test_find_neigborhood(self):
        self.test_neighbourhood.save()
        nbd=NeighbourHood.find_neigborhood(NeighbourHood, 1)
        self.assertTrue(len(nbd)==0)

    
    def test_update_occupants(self):
        self.test_neighbourhood.save()
        nbd=NeighbourHood.find_neigborhood(NeighbourHood, 1)
        self.assertTrue(len(nbd)==0)

class BusinessTest(TestCase):
    def setUp(self):
        self.robert= User.objects.create(username="Robert")
        self.test_profile= Business.objects.create(user=self.robert,
                                                email='rober@gmail.com',
                                                name='robert',
                                                pub_date='12',                                   
                                                description='No retreat no surrender',
                                                business_pic_one ='picture.jpg',
                                                business_pic_two ='picture.jpg',
                                                products='robert',
                                                Phone_no=12,
                                               
                                                )
        self.test_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Business))

    #Testing Save method
    def test_create_business(self):
        self.test_profile.save()
        profile = Business.objects.all()
        self.assertTrue(len(profile)>0)

    # Tear down
    def tearDown(self):
        Profile.objects.all().delete()

    # delete methodTesting 
    def test_delete_business(self):
        self.test_profile.delete()
        self.assertEqual(len(Business.objects.all()), 0)

