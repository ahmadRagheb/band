from __future__ import unicode_literals
import frappe

def get_context(context):
    title = 'Bootstrap Theme The Band'

    carousel_items = [
        {'num':0, 'title': 'Chicago','image_src':'/assets/band/images/chicago.jpg','caption':'Thank you, Chicago - A night we won\'t forget.', 'active':'active'},
        {'num':1, 'title': 'Los Angeles','image_src':'/assets/band/images/la.jpg','caption':'Even though the traffic was a mess, we had the best time playing at Venice Beach!'},
        {'num':2, 'title': 'New York','image_src':'/assets/band/images/ny.jpg','caption':'The atmosphere in New York is lorem ipsum.' }
    ]

    band_members = [
        {'id': 1 , 'name':'Chris Sanford', 'profile_image' : '/assets/band/images/bandmember.jpg', 'role':'Guitarist and Lead Vocalist', 'hobby' :'Loves long walks on the beach', 'join_year':'1988'},
        {'id': 2 , 'name':'Jovani Tate', 'profile_image' : '/assets/band/images/bandmember.jpg', 'role':'Drummer', 'hobby' :'Loves drummin', 'join_year':'1988'},
        {'id': 3 , 'name':'April Mata', 'profile_image' : '/assets/band/images/bandmember.jpg', 'role':'Bass player', 'hobby' :'Loves math', 'join_year':'1988'}
    ]

    not_sold_tours = [
        {'id':1, 'city_name' : 'Paris', 'city_image':'/assets/band/images/paris.jpg', 'date':'Friday 27 November 2015', 'tickets_price':20},
        {'id':2, 'city_name' : 'New York', 'city_image':'/assets/band/images/newyork.jpg', 'date':'Saturday 28 November 2015', 'tickets_price':20},
        {'id':3, 'city_name' : 'San Francisco', 'city_image':'/assets/band/images/sanfran.jpg', 'date':'Sunday 29 November 2015', 'tickets_price':20}
    ]
    return {'carousel_items': carousel_items, 'band_members' : band_members, 'not_sold_tours':not_sold_tours}
