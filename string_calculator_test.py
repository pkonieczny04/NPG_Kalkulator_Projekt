class TestCalculatorEvaluateExpression(unittest.TestCase):
  def test_evaluate_expression_simple(self):
    self.assertEqual(self.calc.evaluate_expression("2 + 3"), 5)
    self.assertEqual(self.calc.evaluate_expression("4 * 5"), 20)
    self.assertEqual(self.calc.evaluate_expression("6 / 2"), 3.0)
    self.assertEqual(self.calc.evaluate_expression("2 ^ 3"), 8)

  def test_evaluate_expression_complex(self):
    self.assertEqual(self.calc.evaluate_expression("2 + 3 * 4"), 14)
    self.assertEqual(self.calc.evaluate_expression("(2 + 3) * 4"), 20)
    self.assertEqual(self.calc.evaluate_expression("4 * (3 + 2)"), 20)
    self.assertEqual(self.calc.evaluate_expression("2 + (3 * 4) ^ 2"), 146)

  def test_evaluate_expression_with_complex_numbers(self):
    result = self.calc.evaluate_expression("(5 + 6i) / (1 + 2i)")
    self.assertAlmostEqual(result.real, 4.4, places=1)
    self.assertAlmostEqual(result.im, -0.8, places=1)
    self.assertEqual(self.calc.evaluate_expression("(1 + 2i) + (3 + 4i)").real, 4)
    self.assertEqual(self.calc.evaluate_expression("(1 + 2i) + (3 + 4i)").im, 6)
        
    self.assertEqual(self.calc.evaluate_expression("(5 + 6i) - (1 + 2i)").real, 4)
    self.assertEqual(self.calc.evaluate_expression("(5 + 6i) - (1 + 2i)").im, 4)

    self.assertEqual(self.calc.evaluate_expression("(1 + 2i) * (3 + 4i)").real, -5)
    self.assertEqual(self.calc.evaluate_expression("(1 + 2i) * (3 + 4i)").im, 10)
  
  def test_evaluate_expression_with_nested_complex_operations(self):
    result = self.calc.evaluate_expression("((1 + 1i) + (2 + 2i)) * (3 + 3i)")
    self.assertAlmostEqual(result.real, 0, places=1)
    self.assertAlmostEqual(result.im, 12, places=1)

    result = self.calc.evaluate_expression("((2 + 3i) - (1 + 1i)) * (4 + 4i)")
    self.assertAlmostEqual(result.real, -4, places=1)
    self.assertAlmostEqual(result.im, 24, places=1)
   
  def test_evaluate_expression_invalid(self):
     with self.assertRaises(ValueError):	
     	self.calc.evaluate_expression("2 / 0")
     with self.assertRaises(ValueError):
	self.calc.evaluate_expression("sqrt(-1)")
  
  
if __name__ == '__main__':
    unittest.main()



        
