class SubTestCase:
    info = ""
    result = True
    value = 0

    total_mutate_time = 0
    effective_mutate_time = 0
    sufficiency = 1.0

    def __init__(self, test_case):
        self.father = test_case

    def update_sufficiency(self):
        self.sufficiency = (self.effective_mutate_time+1)/(self.total_mutate_time+1)
