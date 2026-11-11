time-Slot

Exercise: 4

Create a Time Slot Timetable Using Django Templates

Objective

Create a Django application to display a daily timetable with different time slots in an HTML table.

Step-by-Step Instructions

Create a new Django project named TimeTableProject.

Create a Django app named timetable.

Register the timetable app in the INSTALLED_APPS section of the project settings.

Create a model named TimeSlot with the following fields:

Day

Start Time

End Time

Subject Name

Faculty Name

Perform the necessary database migrations.

Register the TimeSlot model in the Django Admin panel.

Insert at least 10 timetable records for different days and time slots using the Admin panel.

Create a view function to retrieve all timetable records from the database using Django ORM.

Configure the application URLs and connect them to the main project URLs.

Create the required template folder structure inside the app.

Create an HTML template named timetable.html.

Design an HTML table with the following columns:

Day

Time Slot

Subject

Faculty Name

Use Django template tags (for loop and variable expressions) to display the timetable records dynamically in the HTML table.

Add a suitable heading such as Class Timetable.

Run the Django development server and display the timetable in the browser.

Expected Output

A webpage displaying the class timetable in a properly formatted HTML table with day-wise time slots, subject names and faculty details.

Additional Tasks

Add a new field named Classroom to the TimeSlot model.
Update the HTML table to display the classroom details.
Display a message if no timetable records are available.
