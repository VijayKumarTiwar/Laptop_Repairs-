from core.models import FAQ, Testimonial

# FAQs
faqs = [
    ("How quickly can I get service?", "Our professionals typically arrive within 30 minutes of booking, depending on your location and time of day."),
    ("Are the professionals background verified?", "Yes, every professional Engineer goes through rigorous background verification and police clearance before joining our team."),
    ("What if I'm not satisfied with the service?", "We offer a 100% satisfaction guarantee. If you're not happy, we'll send someone else or provide a full refund."),
    ("Do I need to provide Laptop Hardware?", "No, our professionals come fully equipped with all necessary Laptop materials and equipment.")
]

FAQ.objects.all().delete()
for i, (q, a) in enumerate(faqs):
    FAQ.objects.create(question=q, answer=a, order=i+1)

# Testimonials
testimonials = [
    ("Priya Sharma", "Delhi", "Absolutely love Tiwari! The engineer arrived within 8 minutes and did an amazing job. My laptop is rebooting fast!"),
    ("Rajesh Kumar", "Mumbai", "Professional, punctual, and thorough. The verification process gives me peace of mind. Highly recommended!"),
    ("Anita Desai", "Bangalore", "Game changer for working professionals. Book at late night if system crashing, no worries for morning meeting!"),
    ("Suresh Iyer", "Chennai", "Exceptional service. Highly recommend the experts for hardware upgrades."),
    ("Neha Gupta", "Pune", "The 30-minute guarantee is real! Saved my presentation when my screen died."),
    ("Amit Patel", "Ahmedabad", "Transparent pricing, no hidden fees. Purely Bhartiya and purely awesome.")
]

Testimonial.objects.all().delete()
for i, (name, loc, content) in enumerate(testimonials):
    Testimonial.objects.create(name=name, location=loc, content=content, order=i+1)

print("FAQs and Testimonials populated successfully.")
