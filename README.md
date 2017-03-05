# Triton-s-PARK
* Demo video: https://www.youtube.com/watch?v=KXEeFLMeUOM
* APK file (for Android): https://github.com/adityak74/Triton-s-PARK/blob/master/Triton-s-PARK.apk
* Github repository: https://github.com/adityak74/Triton-s-PARK

## 1. Inspiration

In 2012, the US has half of the world's passenger cars (about 300 million units). The need for parking space will grow as the US population grows (projected to be 460 million people in 2050)[ref 1]. It is obvious that people and their cars grow much faster than the expansion of parking spaces in cities. More than just convenience, lack of efficient parking can slow the economy down.

**Triton's Park is a one-of-a-kind parking system aiming at:**
+ Autonomous precision tracking/billing
+ Flexible and scalable system
+ Dynamic business models allowing advertising
+ Social networking enabled

## 2. Autonomous precision tracking/billing

[![Autonomous precision tracking.png](https://s28.postimg.org/nxh3ysh19/Autonomous_precision_tracking.png)](https://postimg.org/image/im27e2uyh/)

1. A cheap ultrasonic or light sensor (HC-SR04 for $2) detects the movements of cars going in and out of a parking slot. Signals got sent out whenever there is a change (car coming in).
2. A controller board was hooked up to multiple (10 to 15) sensors receives the signals and establishes communication channel(s) with PubNub service. One communication channel for each sensor identifiable by sensor ID.
3. Pubnub, upon receipt of updates from the controller board will issue updates to the server correspondingly
4. Server receives updates and perform calculations including but not limitted to slot status verification, start/stop time counter for the slot, calculate the amount of money to be charged, etc. (more details in the business model section) Finally, server publish the update of all fields to PubNub via the channels for mobile app users.
5. PubNub receives update, and forward to the mobile clients accordingly.
6. Mobile client (Cordova powered) receives update, parse and display data accordingly. 

**WHY PUBNUB ?**
+ Pubnub is affordable and HIPAA compliant!
+ Light-weight and supports unlimited channels created dynamically
+ Automatically manages dropped connections, firewalls, connection switching, etc to ensure reliable real-time communication

**WHY A PARKING MANAGEMENT SERVER ?**
+ To scale better as school develops
+ To integrate better with existing and future technologies
+ To support more models

(* It's not that complicated, let us explain further. *)

## 3. Flexible and scalable system

This is how fast Iot will grow
[![IHS.jpg](https://s24.postimg.org/vbl12tcs5/IHS.jpg)](https://postimg.org/image/o8d5n77ch/)
_Ref 2._

This is how fast the machine learning driven market will grow
[![Screen-Shot-2017-02-28-at-1.27.30-PM-1200x868.png](https://s10.postimg.org/4668jjpjt/Screen_Shot_2017_02_28_at_1_27_30_PM_1200x868.png)](https://postimg.org/image/4668jjpjp/)
_Ref 3._

How fast a parking lot will change 5 years from now?

It is undeniable that changes come at a faster speed than before. Flexibility and scale-ability are not optional anymore. Thanks to PubNub, the system has a **clear modular design**. For example, We decided to go with cheap sensors (HC-SR04). As time goes by and sensors get more powerful yet cheaper, we can add or replace sensors (or even controller boards) without modifying or stopping the server or the mobile client.

Python was used to code the server. It is not just a fast language but also a language of choice for statistic and machine learning. Server is then placed on a python cloud and is super scalable.  By lifting a major processing power from the actual end-point and move it to the parking management servers, we allow faster updates to keep up with future changes. 


## 4. Dynamic business models allowing advertising
+ **Location based pricing**<br/>
Our system allows fine categorization of parking sections with different per-hour or per-day rates that can be easily updated by system administrators. Users while checking the mobile client app for empty parking spots will also be able to see zones with corresponding rates and pick the ones that fit their needs. This can be part of a really good marketing/business model that we will discus more in the "Location based advertising/promotion" section
[![Untitled Diagram.png](https://s18.postimg.org/41edm2e7d/Untitled_Diagram.png)](https://postimg.org/image/twy459g11/)

+ **Event based pricing**<br/>
Together with location-based pricing, our system also allows rate customization per event (especially for visitors). Event pricing can be integrated with official school calendars to automate the kick-in and roll-back of prices.

+ **Ultra event parking bid**<br/><br/>
[![ParkBid.png](https://s2.postimg.org/b57soqb49/Park_Bid.png)](https://postimg.org/image/rg7wl1nlx/)

+ **Location based advertising/promotion**
Links to deals/coupons can be placed on empty slots on user's mobile client. It is an effective way to promote brand because psychologically, users were actively looking for empty spots on the map - brand image will be associated with the positive feeling of "I found a spot". It will even more effective if the parking spot is near the business.

Organizations/individuals will also be able to have their banner or message displayed on empty parking spots in the mobile app for a small fee.

During important events, business can sponsor certain spots through our systems and their loyal members will receive discounts when parking in those spots.

This concept can be used for UMSL and other heavy traffic areas.

## 5. Social networking enabled
+ **Location based lottery/gaming** <br/>
With the "Pokemon Go" phenomenon, location-based gaming is the trend (even more true when combined with augmented reality). Quick trivia, lottery, online challenges can be integrated with our system and be activated whenever users park their car in certain spots. 

+ **Location based message communication** <br/>
Prior parking slot user can leave an anonymous for message for later parking user of the same slot. This promotes communication and networking between users within an organization. Some messages can be served as safety warnings, stress reliever, morale booster.

## 6. Security and Authentication
+ **Authenticate users and visitors**<br/>
Upon installation of the app, users will have to register for an account using their organizational ID, phone number, car license plate number. Visitors will have to put in their credit card information. Upon arrival at a parking slot, user will confirm by entering their license plate number

Payments will be processed by industry api like stripe.com

Lisence plate number with no associated credit card or organizational ID will be notified and towed.

+ **Administrator's real-time dashboard **<br/>
A real-time dashboard will be available for parking system's administrator(s). Strange license plates, obstructions, and other policy violations will be displayed visually so the admins can call the owner of the car or corresponding policy enforcers.

## 7. What's next for Triton's Park
We believe our solution is secure, scalable and affordable. The architecture is highly modular. The price for each main module is cheap. For example, the ultra sonic we use only costs $2 per sensor. One controller board ($80 to $100) can support 10 to 20 sensors.

We would like to have the opportunity to implement this idea around campus and scale up to Downtown St. Louis.


## References
[1] http://www.parking.org/2016/01/19/tpp-2013-12-urban-parking-as-economic-solution/#sthash.iybWgYD7.dpuf

[2] https://www.forbes.com/sites/louiscolumbus/2016/11/27/roundup-of-internet-of-things-forecasts-and-market-estimates-2016/#16735a02292d

[3] http://techemergence.com/valuing-the-artificial-intelligence-market-2016-and-beyond/
