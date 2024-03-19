class Input:
    def __init__(self, filename):
        self.filename = filename

    def input_console(self):
        """
        Prompts the user to input text from the console.

        Returns:
            str: The text inputted by the user.
        """
        text = input("Input text: ")
        return text

    def read_file(self):
        """
        Reads text from the .txt file.

        Returns:
            str or None: The text read from the CSV file if successful, None if the file is not found.
        """
        with open(self.filename, 'r') as file:
            text = file.read()
        return text

    def read_file_pandas(self):
        """
        Reads text from the specified CSV file using pandas library.

        Returns:
            str or None: The text read from the CSV file if successful, None if the file is not found.
        """
        import pandas as pd
        data = pd.read_csv(self.filename)
        return data.to_string()
