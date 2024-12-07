# student_test.py
import io
import sys
from student import Student  # Import Student from student.py
from chatty_student import ChattyStudent  # Import ChattyStudent from chatty_student.py

class TestStudent:
    def test_says_hello(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.hello()
        assert captured_out.getvalue().strip() == "Hey there! I'm so excited to learn stuff."

    def test_raises_hand(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.raise_hand()
        assert captured_out.getvalue().strip() == "Pick me!"
    
class TestChattyStudent:
    def test_says_hello(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.hello()
        output = captured_out.getvalue().strip()
        assert "Hey there! I'm so excited to learn stuff." in output
        assert "How are you doing today? I'm okay, but I'm kind of tired." in output
    
    def test_raises_hand(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.raise_hand()
        output = captured_out.getvalue().strip()
        assert output.count("Pick me!") == 10
