# Defining Users (Personas)

There are two primary types of users in MyStamps.

## 1. Customers

Customers go to multiple different shops to get coffee regularly (3-4 times a week). Each shop has their own loyalty card, and customers have to bring all different cards everyday. This isn't practical.

MyStamps solve this issue by providing a platform that collects all of a customer's loyalty cards.

### What do customers want to do?
- Add shops to their collection
- Collect loyalty stamps on each shop
- Redeem loyalty when they have reached the minimum stamps

### User flow
- [Main landing page]: User sees text and logo MyStamps. Two buttons: Sign Up / Log In
    - [Sign Up Page]: Name, Email, Password
        (bonus) Sign Up Button, Sign In with Google
    - [Log In Page]: Email, Password
        (bonus) Sign In with Google
- [Home user page after signed in]:
  - Text \"My Collections\": list of shop pages
  - Add Shop button
  - Logout button -> logs user out back to the [Main landing page]
- [Add Shop Page]: Search Bar, list of shops with Add button on each list, Done button -> go back to landing page/my collections
- [Shop page]: Text \"Stamps\", Number of stamps, Add Stamp/Redeem button - this changes depending on how many stamps, Back/Return button




## 2. Shops (Local Businesses)

Shops want a loyalty program that attracts customers to keep coming back. However, printing the loyalty cards can be costly. It would also be nice to be able to track how the loyalty program can bring back customers.

MyStamps helps businesses reduce this friction for customers.

### What do shops want to do?
- Set up how many stamps before a customer can redeem
- Validate customers stamps
- Validate customers redeems
- Bonus features:
    - Keep track of the customers' stamps
    - Get analytics/dashboard

### User flow
-  [Main landing page]: User sees text and logo MyStamps. Two buttons: Sign Up / Log In
    - [Sign Up Page]: Business Name, Email, Password
        (bonus) Sign Up Button, Sign In with Google
    - [Log In Page]: Email, Password
        (bonus) Sign In with Google
- [Home user page after signed in]:
  - Text \"My Loyalty Programs\": list of loyalty programs
  - Create New Loyalty Program button
  - Logout button -> logs user out back to the [Main landing page]
  - (bonus feature) Statistics Page
- [Create New Loyalty Program Page]: Program Name, Number of Stamps to Redeem, Create button -> back to landing page
- [Loyalty Program Page]: Validate Stamp button -> generate QR code
- [QR Code Page]: randomly generated QR code token valid for 30-60 sec, DONE button -> back to Loyalty Program Page
- [Stamp Validation Page]: \"Stamp validated!\" or \"Could not validate stamp:(\", OK button -> back to Loyalty Program Page