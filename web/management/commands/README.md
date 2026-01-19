# Demo Data Generation Command

This directory contains Django management commands for the web application.

## generate_demo_data

A management command that generates demo/test data for all models in the application using factory_boy factories.

### Usage

**Generate demo data (keeps existing data):**
```bash
python manage.py generate_demo_data
```

**Generate demo data (clears existing data first):**
```bash
python manage.py generate_demo_data --clear
```

### What Data is Generated

The command creates the following demo data:

- **3 Home Banners** - Homepage banner content
- **5 Service Categories** - Different service categories
- **10 Services** - Services distributed across categories
- **30 Service Planning Steps** - 3 planning steps per service
- **20 Service Process Steps** - 2 process steps per service
- **40 Service Page Images** - 4 images per service page
- **50 Service FAQs** - 5 FAQs per service
- **12 Works** - Portfolio/work items with associated services and categories
- **36 Works Related Images** - 3 related images per work item
- **8 Testimonials** - Client testimonials
- **10 Blogs** - Blog posts
- **6 Journey Entries** - Company journey/milestone entries
- **15 Contact Submissions** - Contact form submissions
- **12 Clients** - Client logos/information

### Requirements

The following packages must be installed (already included in requirements.txt):
- factory_boy
- Faker
- Pillow (for image generation)

### Notes

- The `--clear` flag will delete all existing data before generating new data
- Generated images are placeholder images created programmatically
- All text content is generated using Faker library with realistic dummy data
- Foreign key relationships are properly maintained across all models
