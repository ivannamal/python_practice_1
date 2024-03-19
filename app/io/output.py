from app.io.input import Input


class Output:
    def __init__(self, output_file):
        self.output_filename = output_file

    def output_text_to_console(self):
        """
        Outputs text from a .txt file to the console.

        This method creates an instance of the Input class with the specified file, then reads text from the file
        using the read_text_from_file method and prints it to the console.

        Returns:
            None
        """
        input_instance = Input(self.output_filename)
        print("Your text: ", input_instance.input_console())

    def write_to_file(self):
        """
        Writes into a file from another file.

        Returns:
            None
        """
        input_instance = Input(self.output_filename)
        with open("text.txt", 'w') as file:
            file.write(input_instance.read_file())
            print("Added text from .txt!")
        # file.close()
        return None

    def output_pandas(self):
        """
        Outputs text from a CSV file using pandas.

        Returns:
            None
        """
        input_instance = Input(self.output_filename)
        with open("text.csv", 'w') as file:
            file.write(input_instance.read_file_pandas())
            print("Added text from .csv!")
