# Float Moodle
**200050018-200050040-200050075-200050151**

Float Moodle is a website which provides services to its users. Some of it's important features include: 
## Signup
- When a user visits the home page and want to create an account in Float Moodle they must use this signup option. It redirects us to the Signup portal.
- In this SignUp portal we can choose a username of our interest within 150 characters and we have to create a password for this username following certain protocols like having atleast 8 characters, not entirely numeric etc.
   
## Login
- Once an account is created we can use those credentials to login into our account and there we can see the dashboard.

## Dashboard
- After we login in to the website we can see our dashboard and it contains the user profile.
- We have the options of editing our profile and we also have an option of changing our current password.

  
## Courses
- We can create a course or join a course either as a student or a TA.
- After we create a course then 2 codes will be generated randomly, one for TA's and other for students.
- We can use these codes to join the course as a student or a TA.
- Everyone can view the list of students registered in the course while only the instructor has the authority of removing a student.
- TA's don't have the authority of adding or removing students from the courses, but this can be altered by the instructor.
- And each course created has an indicator indicating the percentage of course activities that are finished.
- For students it indicates the percentage of assignments that are finished and for instructors it indicates the percentage of assignments that are graded by them.
- There is also a **To do** list present on the sides which reminds us of our incomplete activities in our courses.
<img src="https://drive.google.com/uc?export=view&id=1PKrd84konD6gRUNAb-QG3k9-rHVHo7__" width="600">



## Assignment
- If we are an instructor then we can create an assignment and can upload it in the website.
- While uploading the assignment we have to give assignment name, attach a copy of the assignment,also we can give a url link for that assignment and we can add some description if needed along with maximum marks and the deadline for submission.
- Now when a student in the course opens the course he can see the assignments that are uploaded and when he opens the assignment he can see the name of the assignment, document of the assignment and also a url of the assignment and below it we can see the submission status and also an option for choosing a file to submit.
- Once submitted it shows the students an option of re-submit if we have made any changes to our original file afterwards.
- Now the instructor can see the number of submissions made and also can view and download those submissions and can give the grades and feedback to the assignment.
<img src="https://drive.google.com/uc?export=view&id=1eDwtVykfBxyDsq7EVPe1yXEVTWUzJGTl" width="600">

- In the assignments section the list of assignments whose deadline is finished and those whose isn't are distinguished from each other by using different colors.
- Instructor can upload the grades and feedbacks of the students as a bulk using a csv file.
- Instructor can also view the statistics of marks scored by students in a particular assignment.
<img src="https://drive.google.com/uc?export=view&id=1Bkv7cAxFJb_ONTNK0zA5PyAl5bldfCbC" width="600">

- Instructors can assign weightages to each assignment of the course in float moodle.
<img src="https://drive.google.com/uc?export=view&id=1hyfQ12tV3kgN6Qc5fr76Hnwv-Q_mrwsq" width="600"> 

- Students can view their course totals and the Instructor can view the statistics of marks in the course.
<img src="https://drive.google.com/uc?export=view&id=1tHFV32pxW603xEbdcw9-GRQd5h26O--Z" width="500"> <img src="https://drive.google.com/uc?export=view&id=1Kv7lXIQPIIp2Ytc6lPCEQ05A8skAqAPU" width="500">
- TA's can view the submissions of students, can download them, can grade them ,upload the marks and give feedback of the assignments.
- TA's don't have the authority of creating a new assignment by default, but this can be changed by the instructor if required.  



## Other Features 
- Instructor can also give an order of authority among the TA's of a course.
- Instructor can view the progress of all the students throughout a particular course along with their statistics.
<img src="https://drive.google.com/uc?export=view&id=1fcp9S2d8_ROi0PRM8S-YDA-fkPPD9uSM" width="600"> 

- Histogram of the course total of every student upto a particular assignment is also available for the instructor of the course.
<img src="https://drive.google.com/uc?export=view&id=1eKgTLHqNV2yPqR4LCR4u9HhDFP3nC0OQ" width="600"> 

- Various graphs for comparison of assignments by different methods are also available for the instructor.
<img src="https://drive.google.com/uc?export=view&id=1xb4jBt7M_kseOWAGddVPKEdmLK47R5Hx" width="500"> <img src="https://drive.google.com/uc?export=view&id=19sZbD6B1R5msTcidNSSfnIpricHv1U_Z" width="500">

- Various graphs for progress of the course in different means are also available for the instructor of the course.
<img src="https://drive.google.com/uc?export=view&id=1ZFSQVRduVJRKSY9zy5E6dpm2W_oVTYf9" width="500"> <img src="https://drive.google.com/uc?export=view&id=12VCL34D-0GSKOCX62j9UsujCiXmFmera" width="500">
<img src="https://drive.google.com/uc?export=view&id=1GjNeBJKiyJKD9i9jh5jsvdg-6pJhxW4d" width="600">

- Navigation bar
  - This contains the options of visting dashboard or courses list or chat or logout from our account.
- Chat
  - Student teacher interaction for doubts is often quite productive and thus there is a public duscussion forum where students and instructor can discuss the doubts publicly.
  - TA's cannot create public discussion forums by default but this can be changed by the instructor.
  - This feature also enables the students to make private conversations with fellow students in that particular course.
  <img src="https://drive.google.com/uc?export=view&id=1_-9Gl4rAsRQ9LsILgsPeKI94ziNQKgUZ" width="600">


  - However this may lead to plagiarism during a test and hence can be temporarily disabled by the instructor.
  - There are also system run servers(cli bot) in every course which contains the information about deadlines,grades etc. and there are specific commands for which it answers. The commands and the response by the server are as follows:
    - if our msg is any of hi/hii/hiii/hello/hey then the reply is Hello 👋 followed by username.
    - if our msg is my-name then it responds with our name and similar is the case for my-email,my-first-name,my-last-name,my-profile
    - if our msg is who-r-u then the response is I am CLI-BOT 🤖, U can ask me queries and I will try my best to answer them.
    - if our msg is users-list then it gives out the list of users in the course other than itself.
    - Other Various Commands are:
    - It tells our profile details when we query ```my-name, my-email, my-profile``` etc..
    - It returns the list various types of courses on asking ```list-stud-courses, list-courses``` etc
    - Also many commands work even with Capital letters in between.
    - ```ls -a -all``` tells all assignments in all courses
    - ```ls -ad -<Course>``` tells The TO-DO list assignments in that course
    - ```ls -ag -<Course>``` tells the grades of all assignmnets in that course
    - We can also send messages to other users via the bot, using ```send-msg-<name>-<message>```