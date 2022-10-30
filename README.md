# St. George Resort

For my project four milestone project I have created a hotel website with booking system, using Django with a Postgres database, deployed on Heroku.

[View live project](https://st-george-resort.herokuapp.com/)

![Responsive image](/assets/images/responsive.png)

# Table of contents
1. [User Experience](#user-experience(ux))
    - [Strategy](#strategy)
    - [User Stories](#userstories)
    - [Scope](#scope)
    - [Structure](#structure)
        - [Database](#database)
        - [Skeleton](#skeleton)
        - [Surface](#surface)
    - [Features](#features)
        - [Homepage](#homepage)


# User Experience(UX)

## Strategy

The target audience for St. George Resort are:

    - People looking holiday at a beach resort
    - Couple and families
    - People looking to visit Hawaii

The target user will be looking for:

    - A website that is easy to navigate and find the realtive information they are looking for
    - Images of the resort and different rooms available
    - Ingormation on other activites and excursions the resort offers
    - The ability to send a booking request to stay at the resort
    - A way to contact the resort directly with any questions they may have

As many people view website on smaller  screen devices I have allowed for this by creating a resposive website using boostrap and css.

## User Stories

My user stories can also be found [here](https://github.com/users/EJDiamond/projects/5)

1. As a user I can easily navigate the site to find desired content to decide if I want to stay at the hotel.
2. As a user I can find useful information about the hotel on the home page so I can spend less time browsing the site.
3. As a user I can use a navigation bar to move around the site with ease.
4. As a user I can see the name of the page in the browser window so that I know which page I am viewing.
5. As a user I can contact the hotel via a form so that I can ask additional questions.
6. As a user I am notified that my contact form has been sent.
7. As a user I can see activities and excursions the hotel has to offer.
8. As a user I can request to book a room so that I can stay at the hotel.
9. As an admin user I can log in so that I can view bookings and contact forms on the backend.
10. As an admin user I can edit and/or delete bookings so that I can assist any customers who need help modifying their booking.
11. As an admin user I can change customer booking status from requested to confirmed.
12. As a user I can register an account so that I can view/manage my booking requests.
13. As a registered user I can login to my account so that I can manage my bookings.
14. As a registered user I can see clearly if I'm logged in, so that I can either log in or out.
15. As a registered user, I can log out of my account so that I am signed out securely.
16. As a registered user I can edit my booking request so that I can make any changes needed.
17. As a registered user I can delete my booking request so that I can cancel my stay if needed.

## Scope

The following features will be implemented to achieve the user stories:

    - The landing page will summarise what the resort has to offer showing room types, activities and excursions offered as well as the contact details for the resort and links to request to book a room.
    - The navbar will have links to all pages and be scrollable and resposive so always accessible to the user.
    - The accomodation page will show all rooms abvailable and their features, with links to the booking page.
    - The booking page will allow users to send a booking request to the resort.
    - The my bookings page will allow the user to view there booking requests to see if they have been confirmed and allow them to edit/delete them.
    - The contact page will allow the user to send a message to the resort.
    - Register and login/out features using Django allauth.

## Structure

### Database

I have used two models to store the information for the hotel app, Booking and Contact:

![Models](/assets/images/models.png)

### Skeleton

St. George resort wireframes can also be viewed [here](https://github.com/EJDiamond/St-George-Resort/blob/main/assets/images/hotel-wireframes.png).

![Wireframes](/assets/images/hotel-wireframes.png)

Produced website differs slightly from wireframes as bootstrap features such as cards and carousels allowed me to enhance the website further.

### Surface

I chose to use a simple colour scheme of green and white as I felt the overall look of the website was clean and more appealing to the eye.

![Green](/assets/images/colour.png)

I chose the two fonts Playfair Display and Source Sans Pro:

- Playfair Display was used for all heading in a heavy font weight depending on whether it was a H1, H2 etc.
- Source Sans Pro was used across the body of the site as well as for some sub headings as I felt it complimented the H1 headings effectively.


## Features


#### - __Navigation Bar__

The navigation bar has links to all the pages the users are able to access, the page title allows the user to know which page they are viewing. As the page is scrolled the nav bar turns green so that white text can still be visible to the user.

![NavBar](/assets/images/navbar.png)
![Green NavBar](/assets/images/green-nav.png)


#### - __Navigation Bar Mobile__

On a smaller screen device the navigation bar condenses to toggle form and and the background of the drop down menu is set to green so again the text can be viewed on the white background of the pages.

![Mobile NavBar](/assets/images/mobile-landing.png) ![Mobile NavBar](/assets/images/mobile-nav-green.png)


#### - __Room View Carousel__

The rooms choices are displayed on an automatic carousel which allows the user to view all the rooms and has link to view the details of the room on the accomodation page and to book the room on the bookings page.

![Room Carousel](/assets/images/room-carousel.png)


#### - __Activities__

The activities and excursions the resort has to offer are displayed on the landing page in a grid format which is resposive and displays in column form when viewed on smaller devices.

![Activites](/assets/images/activities.png)


#### - __Accomodation__

This page displays the rooms and their features. Each room type is presented with a carousel with a number of images of each room, displayed next to the name and the features of the room type. There is a link to the booking page on each room. These cards are responsive and therefore shrink to fit smaller screen sizes.

![Footer](/assets/images/room-info.png)


#### - __Booking__

The booking page presents the four room types in small cards above the booking form the remind the user of the room types. Below is the booking form used to send a booking request to the resort using the booking model.

![Booking Form](/assets/images/booking-form.png)


#### - __Contact Us__

This page allows the user to send the resort a message with a simple user friendly form using the contact model.

![Contact Form](/assets/images/contact-form.png)


#### - __My Bookings__

The my bookings page shows the user the bookings they have request and their details. From here the user can see if the request has been approved as well as select to edit and delete their booking.

![My Bookings](/assets/images/my-bookings.png)


#### - __Edit Bookings__

From the my bookings edit booking link the user is sent to the booking form with all the booking details already in, from here they can change an aspect of the booking they require.]

![Edit Bookings](/assets/images/edit-booking.png)





