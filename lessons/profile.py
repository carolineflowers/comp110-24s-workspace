"""Practice writing a class."""

class Profile:
    
    username: str
    private: bool

    def __init__(self, username_input: str):    # don't have to list return type bc automatically returns self
        """Create a new profile object."""
        self.username = username_input
        self.private = True


    def tweet(self, msg: str) -> None:    # make sure def is indented to be inside of Class
        """If profile is public, print msg."""
        if self.private is False:    # could also use self.private as stand-alone bool or if not self.private is True...
            print(msg)