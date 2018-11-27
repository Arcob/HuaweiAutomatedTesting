class SubTestCase:

    total_mutate_time = 0
    effective_mutate_time = 0
    sufficiency = 1.0

    def __init__(self, info, result, value, test_case=None):
        self.info = info
        self.result = result
        self.value = value
        self.father = test_case

    def update_sufficiency(self):
        self.sufficiency = (self.effective_mutate_time+1)/(self.total_mutate_time+1)
