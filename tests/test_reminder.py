from lib.reminder import *

def test_reminds_user_to_do_a_task():
    reminder = Reminder('Sam')
    reminder.remind_me_to("Brush Yogi")
    result = reminder.remind()
    assert result == "Sam, Brush Yogi!"