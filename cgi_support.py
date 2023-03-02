import cgi


class Subscriber:
    def __init__(self, name, email):
        """Initialize a new subscriber object with the given name and email."""
        self.name = name
        self.email = email

    def add_to_mailing_list(self):
        """Add the subscriber to the mailing list."""
        # TODO: Implement this method to actually add the subscriber to the mailing list.
        pass


def main():
    """Handle the form submission and display the subscribe page."""
    # Parse the form data.
    form = cgi.FieldStorage()
    name = form.getvalue("name")
    email = form.getvalue("email")

    if name and email:
        # If the form was submitted, create a new Subscriber object and add it to the mailing list.
        subscriber = Subscriber(name, email)
        subscriber.add_to_mailing_list()
        message = f"Thank you, {name}! Your email ({email}) has been added to our mailing list."
    else:
        # If the form has not been submitted, display the subscribe form.
        message = "Please fill out both name and email fields."

    # Set the response headers.
    print("Content-Type: text/html\n")

    # Write the HTML response.
    print(f"""
        <html>
            <head>
                <title>Subscribe to our mailing list</title>
            </head>
            <body>
                <p>{message}</p>
                <form method="post">
                    <label>Name: <input type="text" name="name"></label><br>
                    <label>Email: <input type="email" name="email"></label><br>
                    <input type="submit" value="Subscribe">
                </form>
            </body>
        </html>
    """)


if __name__ == "__main__":
    main()
