# St. George Resort

For my project four milestone project I have created a hotel website with booking system, using Django with a Postgres database, deployed on Heroku.

[View live project](https://st-george-resort.herokuapp.com/)

![Responsive image](/assets/images/responsive.png)

# Table of contents
1. [User Experience](#user-experience(ux))
    - [Strategy](##strategy)
    - [User Stories](##userstories)
    - [Scope](##scope)
    - [Structure](##structure)
        - [Database](###database)


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

### Wireframes




