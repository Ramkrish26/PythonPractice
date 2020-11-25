import os

class ReadAndWrite():

    def read_entire_file(self, filename):
        """
        To read the entire file
        :param filename: Name of the file to be opened
        :return: The entire file as string
        """
        obj = open(os.path.realpath(filename), 'r')
        return str(obj.read())

    def read_first_line(self, filename):
        """
        To read the first line of the file
        :param filename: Name of the file to be opened
        :return: The first line of file as string
        """
        obj = open(os.path.realpath(filename), 'r')
        return str(obj.readline())

    def read_character_range(self, filename, no_of_characters=10):
        """
        To read the specific range of characters from the file
        :param filename: Name of the file to be opened
        :param no_of_characters: Specify the number of characters to be read. It defaults to first 10 characters
        :return: The first line of file as string
        """
        obj = open(os.path.realpath(filename), 'r')
        return str(obj.read(no_of_characters))

    def write_data(self, filename, data):
        """
        To read the entire file
        :param filename: Name of the file to be opened
        :param data: Some data that should be written in the file
        :return: The entire file as string
        """
        obj = open(os.path.realpath(filename), 'w')
        obj.write(data)


# Object creation of the class ReadAndWrite
readAndWrite = ReadAndWrite()

# This is to read the entire file
print("Entire File :\n" + readAndWrite.read_entire_file("Sample.txt"))

# This is to read the first line of the file
print("\nFirst line of file :\n" + readAndWrite.read_first_line("Sample.txt"))

# This is to read the first 50 characters of the file
print("\nSome characters of the file :\n" + readAndWrite.read_character_range("Sample.txt", 21))

# This is to write some data to the file
readAndWrite.write_data("Sample.txt", "This is return from python")
print("\nData from after write :\n" + readAndWrite.read_entire_file("Sample.txt"))
