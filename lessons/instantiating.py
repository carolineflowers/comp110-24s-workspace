"""Practice writing in class: try on own!"""

# DEFINITION
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

# INSTANTIATION (outside of class)
user1: Profile = Profile("110_rulz")   # construct it by calling the constructor (in this class) -- this calls __init__()
user1.private = False    # makes it private
user1.tweet("OOP is cool!")  #tweets the message here


