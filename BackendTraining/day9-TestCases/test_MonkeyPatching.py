from Alexa.CMDS import myName

def monkey_patch():
    return "Reporting from child sir!!"
myName.monkeyTest  = monkey_patch

def test_monkeyTest():
    assert myName.monkeyTest() ==  "Reporting from child sir!!"