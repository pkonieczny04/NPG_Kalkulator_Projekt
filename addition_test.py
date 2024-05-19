def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(self.calc.add(-1, 5), 4) # -1 + 5 = 4
    
