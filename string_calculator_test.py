class TestCalculatorEvaluateExpression(unittest.TestCase):
  def test_evaluate_expression_simple(self):
        self.assertEqual(self.calc.evaluate_expression("2 + 3"), 5)
        self.assertEqual(self.calc.evaluate_expression("4 * 5"), 20)
        self.assertEqual(self.calc.evaluate_expression("6 / 2"), 3.0)
        self.assertEqual(self.calc.evaluate_expression("2 ^ 3"), 8)

  def test_evaluate_expression_complex(self):
    pass

  def test_evaluate_expression_with_complex_numbers(self):
    pass
  
  def test_evaluate_expression_with_nested_complex_operations(self):     
   pass
  
  def test_evaluate_expression_invalid(self):
    pass
  
  
  
if __name__ == '__main__':
    unittest.main()



        
