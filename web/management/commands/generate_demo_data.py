from django.core.management.base import BaseCommand
from web.tests.factories import (
    HomeBannerFactory,
    ServiceCategoryFactory,
    ServiceFactory,
    ServicePlaningStepFactory,
    ServiceProcessStepFactory,
    ServicePageImageFactory,
    ServiceFAQFactory,
    WorksFactory,
    WorksRelatedImagesFactory,
    TestimonialFactory,
    BlogFactory,
    JourneyFactory,
    ContactFactory,
    ClientFactory,
)


class Command(BaseCommand):
    help = 'Generate demo data for all models using factories'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before generating new data',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            from web.models import (
                HomeBanner, ServiceCategory, Service, ServicePlaningStep,
                ServiceProcessStep, ServicePageImage, ServiceFAQ, Works,
                WorksRelatedImages, Testimonial, Blog, Journey, Contact, Client
            )
            
            # Delete in reverse order to avoid foreign key constraints
            WorksRelatedImages.objects.all().delete()
            Works.objects.all().delete()
            ServiceFAQ.objects.all().delete()
            ServicePageImage.objects.all().delete()
            ServiceProcessStep.objects.all().delete()
            ServicePlaningStep.objects.all().delete()
            Service.objects.all().delete()
            ServiceCategory.objects.all().delete()
            HomeBanner.objects.all().delete()
            Testimonial.objects.all().delete()
            Blog.objects.all().delete()
            Journey.objects.all().delete()
            Contact.objects.all().delete()
            Client.objects.all().delete()
            
            self.stdout.write(self.style.SUCCESS('✓ Existing data cleared'))

        self.stdout.write(self.style.WARNING('Generating demo data...'))

        # Generate HomeBanner data
        self.stdout.write('Creating Home Banners...')
        for i in range(3):
            HomeBannerFactory()
        self.stdout.write(self.style.SUCCESS('✓ Created 3 Home Banners'))

        # Generate ServiceCategory data
        self.stdout.write('Creating Service Categories...')
        categories = []
        for i in range(5):
            categories.append(ServiceCategoryFactory())
        self.stdout.write(self.style.SUCCESS('✓ Created 5 Service Categories'))

        # Generate Service data with related models
        self.stdout.write('Creating Services with related data...')
        services = []
        for category in categories:
            # Create 2-3 services per category
            for i in range(2):
                service = ServiceFactory(category=category)
                services.append(service)
                
                # Create planning steps for each service
                for j in range(3):
                    ServicePlaningStepFactory(service=service)
                
                # Create process steps for each service
                for j in range(2):
                    ServiceProcessStepFactory(service=service)
                
                # Create page images for each service
                for j in range(4):
                    ServicePageImageFactory(service=service)
                
                # Create FAQs for each service
                for j in range(5):
                    ServiceFAQFactory(service=service)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(services)} Services with related data'))

        # Generate Works data
        self.stdout.write('Creating Works...')
        works_list = []
        for i in range(12):
            # Distribute works across categories and services
            category = categories[i % len(categories)]
            service = services[i % len(services)]
            work = WorksFactory(category=category, service=service)
            works_list.append(work)
            
            # Add related images for each work
            for j in range(3):
                WorksRelatedImagesFactory(service=work)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(works_list)} Works with related images'))

        # Generate Testimonials
        self.stdout.write('Creating Testimonials...')
        for i in range(8):
            TestimonialFactory()
        self.stdout.write(self.style.SUCCESS('✓ Created 8 Testimonials'))

        # Generate Blogs
        self.stdout.write('Creating Blogs...')
        for i in range(10):
            BlogFactory()
        self.stdout.write(self.style.SUCCESS('✓ Created 10 Blogs'))

        # Generate Journey entries
        self.stdout.write('Creating Journey entries...')
        for i in range(6):
            JourneyFactory()
        self.stdout.write(self.style.SUCCESS('✓ Created 6 Journey entries'))

        # Generate Contact submissions
        self.stdout.write('Creating Contact submissions...')
        for i in range(15):
            ContactFactory()
        self.stdout.write(self.style.SUCCESS('✓ Created 15 Contact submissions'))

        # Generate Clients
        self.stdout.write('Creating Clients...')
        for i in range(12):
            ClientFactory()
        self.stdout.write(self.style.SUCCESS('✓ Created 12 Clients'))

        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('✓ Demo data generation completed successfully!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        
        # Print summary
        self.stdout.write('\nSummary:')
        self.stdout.write(f'  • Home Banners: 3')
        self.stdout.write(f'  • Service Categories: 5')
        self.stdout.write(f'  • Services: {len(services)}')
        self.stdout.write(f'  • Service Planning Steps: {len(services) * 3}')
        self.stdout.write(f'  • Service Process Steps: {len(services) * 2}')
        self.stdout.write(f'  • Service Page Images: {len(services) * 4}')
        self.stdout.write(f'  • Service FAQs: {len(services) * 5}')
        self.stdout.write(f'  • Works: {len(works_list)}')
        self.stdout.write(f'  • Works Related Images: {len(works_list) * 3}')
        self.stdout.write(f'  • Testimonials: 8')
        self.stdout.write(f'  • Blogs: 10')
        self.stdout.write(f'  • Journey entries: 6')
        self.stdout.write(f'  • Contact submissions: 15')
        self.stdout.write(f'  • Clients: 12')
