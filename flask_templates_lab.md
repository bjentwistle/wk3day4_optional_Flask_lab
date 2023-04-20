# Flask Templates Lab

Your task is to model a Flask app which will list upcoming events and allow users to add events to the list.

## MVP

Add the functionality to add a new event to our event list. 

* Create an event in the event planner.

### Extensions

* Update the Date property to be of the Python type `datetime.date` (Tip: you'll need to import `datetime`)
* Add a 'recurring' boolean property to the `Event` class.
* Give the user visual feedback on what events are recurring
* Use an HTML date picker instead of a text input for the new event date.
* Style the app using CSS

## Advanced Extensions

* Delete the items from the list (either use index or event name to do this)
    * Because we can't use the `DELETE` HTTP method you will need to create a `POST` route to `/events/delete/<index>` in order to avoid conflicts!
* Anything else you can think of


#### Guidance

To style a Flask app you will need to put your CSS files inside a folder called `static` inside the `app` package.

Then add the following line inside the <HEAD> tag of your `base.html`

```html
    <link rel="stylesheet" href="{{ url_for('static', filename='your_file_name.css') }}">
```

When deleting the event use a form and the event name to identify which one is to be deleted.

An HTML checkbox input value will only be included in the form dictionary if the box is checked. It will by default return the string 'On'
