from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

def get_context(context):

	#Check Empty Image
    carasoul =  frappe.get_list("Carousel", fields=["title", "image", "caption","active"],filters={"image": ("!=", "")},order_by='active DESC')
    carousel_items=[]
    active = ''
    #to solve problem when more than one slide is active
    activeRegisted=0
    for counter, r in enumerate(carasoul):
        if activeRegisted==0:
            if r.active == 1:
                active = 'active'
                activeRegisted=1
        array = {'num': counter, 'title': r.title, 'image_src': r.image, 'caption': r.caption, 'active': active}
        active=''
        carousel_items.append(array)


    # carousel_items = [
	# {'num':0, 'title': 'Chicago','image_src':'/assets/band/images/chicago.jpg','caption':'Thank you, Chicago - A night we won\'t forget.', 'active':'active'},
	# {'num':1, 'title': 'Los Angeles','image_src':'/assets/band/images/la.jpg','caption':'Even though the traffic was a mess, we had the best time playing at Venice Beach!'},
	# {'num':2, 'title': 'New York','image_src':'/assets/band/images/ny.jpg','caption':'The atmosphere in New York is lorem ipsum.' }
    # ]
    

    band_members = [
	{'id': 1 , 'name':'Chris Sanford', 'profile_image' : '/assets/band/images/bandmember.jpg', 'role':'Guitarist and Lead Vocalist', 'hobby' :'Loves long walks on the beach', 'join_year':'1988'},
	{'id': 2 , 'name':'Jovani Tate', 'profile_image' : '/assets/band/images/bandmember.jpg', 'role':'Drummer', 'hobby' :'Loves drummin', 'join_year':'1988'},
	{'id': 3 , 'name':'April Mata', 'profile_image' : '/assets/band/images/bandmember.jpg', 'role':'Bass player', 'hobby' :'Loves math', 'join_year':'1988'}
    ]

	
    return {'carousel_items': carousel_items, 'band_members' : band_members}
