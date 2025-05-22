# Area restriction in accounting.
- version: 18

## How to use
- add the file under the custom module with new directory of area 
- add the path of custom module in the conf file
- and then you can run

- Download the module and place under the custom addon
- go the app and search the area: you will see the app module, Activate it 
![Screenshot from 2025-01-21 15-12-03](https://github.com/user-attachments/assets/0b44e81a-d5cd-49ac-afc9-63ddc9d246df)

- Go to the accounting of configuration and in the child menu (at the bottom) contain the Area menu ; click it to add define area
![Screenshot from 2025-01-21 15-13-14](https://github.com/user-attachments/assets/aa155211-5dde-4487-95c1-0fdb1981843d)

- click the new button to define the area
![Screenshot from 2025-01-21 15-15-14](https://github.com/user-attachments/assets/6d6b6372-fa6c-4ac1-a55e-eddf58c10d95)

- then you can view the list of the created area: like this
![Screenshot from 2025-01-21 15-16-14](https://github.com/user-attachments/assets/0e09d79a-4c7e-4ce0-a49e-9a0623bbda84)

- and then go to setting to define user of area and the group of the acccounting module access 
- Setting>user>mitchel Admin>fill the Multi Location of allowed Areas, in the current area will show the first added area name (that is system automatically define base on you input of allowed area)
- (In this some of the invoice are created by mitchel admin , so i defned for that user of area)
![Screenshot from 2025-01-21 15-18-34](https://github.com/user-attachments/assets/63263820-ba4c-4103-bebd-7991f35fe536)

- And then i wll change for another user of Marc Demo 
![Screenshot from 2025-01-21 15-21-56](https://github.com/user-attachments/assets/61c5a61d-ced4-489a-aa91-db3d82a28cb7)

- Now i need to add for new user who is to define for the restrict of to show the data of invoice and bill only .that user can create but confirm the invoice but can't delete
- firstly define the name , email ,allowed area, and accounting to Area-Based Access group and then give the user of password and save all
![Screenshot from 2025-01-21 15-22-51](https://github.com/user-attachments/assets/95a637ca-aa9c-4e57-adc1-8167a8167d11)

- admin can view all of the invoice 
![Screenshot from 2025-01-21 15-30-00](https://github.com/user-attachments/assets/212ad1a0-a954-48f3-951b-8dcb84f179af)

- But the defined group can see the same area of invoice and some of the early invoice are not defined the area. like this
![Screenshot from 2025-01-21 15-30-00](https://github.com/user-attachments/assets/9e9a5bef-c166-4bc4-acb3-091b8de0466b)

here you can do create invoice ,confirm invoice but can't do deletion if the user is defined for the Area-Based Access group and Bill also.<br/>
Thank you. Good luck guys! :tada:
