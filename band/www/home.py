from __future__ import unicode_literals
import frappe

def get_context(context):
    carousel_items = [{'title': 'Chicago','image_src':'/assets/band/images/chicago.jpg','caption':'Thank you, Chicago - A night we won\'t forget.', 'active':'active'}, {'title': 'Los Angeles','image_src':'/assets/band/images/la.jpg','caption':'Even though the traffic was a mess, we had the best time playing at Venice Beach!'}, {'title': 'New York','image_src':'/assets/band/images/ny.jpg','caption':'The atmosphere in New York is lorem ipsum.' }]
    
    return {'carousel_items': carousel_items}
