class Toast:
    def __init__(self, name: str):
        """Class to test the functionality of the code.

        Parameters
        ----------
        name : str
            The name of the test.
        """
        self.name: str = name
        self.value: float = 0
    def run(self):

        print(f"Running test: {self.name}")

    def change_name(self, new_name: str):
        """Change the name of the test.

        Parameters
        ----------
        new_name : str
            The new name of the test.
        """
        self.name = new_name
        print(f"Test name changed to: {self.name}")

    def add_to_value(self, amount: float):
        """Add a value to the test.

        Parameters
        ----------
        amount : float
            The amount to add to the test value.
        """
        self.value += amount
        print(f"Value changed to: {self.value}")
        
    

