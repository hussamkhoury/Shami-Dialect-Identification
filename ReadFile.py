repeated_character = ['ب', 'ت', 'ل', 'ه', 'ر', 'م', 'ن', 'د', 'ف', 'ي', 'ه', 'خ', 'ص', 'ط']
Valid_character = ['ب','ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ',
                    'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي', 'أ', 'إ', 'آ', 'ى', 'ؤ,', 'ئ ', 'ا', ' ']

class Preprocessor:
    # initialize the path arg with the file name/path
    def __init__(self, path):
        self.path = path

    # Open the file in state=('r'->read, 'a'->append) mode --- the default mode will be reading
    # use the path argument for opening file other than the original unprocessed text file
    def open_file(self, path=" ", state='r'):
        print("Opening the file.......")
        if path != ' ':
            file_object = open(path,state,encoding='utf-8')
        else:
            file_object = open(self.path,state,encoding='utf-8')
        print("File opened successfuly...... ")
        return file_object

    # read a file object
    def read_file(self, file_object):
        data = file_object.read()
        return data

    # close the file
    def close_file(self, file_object):
        file_object.close()
        print("file closed successfuly.......")

    # Actual processing for the text -- target is the path/name for the file where we want to write the processed data
    def process_text(self, target):

        # open the text file from we want to read our data
        file_object_1 = self.open_file(' ','r')
        file_object_2 = self.open_file(target, 'w')

        # read the data from the opened text file (the file object)
        data = self.read_file(file_object_1)

        # split the data into tokens (by the space between the words)
        list_ = data.split('\n')
        # print(list_[0:1])

        # validating every token in the file
        # using checker(Boolean) to mark the begging of the word
        checker = True
        # use temp_char to discover the repeated character
        temp_char = ' '
        for phrase in list_:
            for token in phrase:
                for char in token:
                    if (char != ' ّ' or char != ' ٌ' or char != ' َ') and (char in Valid_character):
                        if (temp_char == char)  and (char in  repeated_character):
                            continue
                        elif checker and char == 'أ':
                            file_object_2.write('ا')
                            temp_char = char
                            checker = False
                        else:
                            file_object_2.write(char)
                            temp_char = char
                    #cheker = char
                #file_object_2.write(' ')
                checker = True
            #file_object_2.write('syrian')
            file_object_2.write('\n')

        # closing the files after we finish the preprocessing
        self.close_file(file_object_1)
        self.close_file(file_object_2)
