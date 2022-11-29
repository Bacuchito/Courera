def student_grade(name, grade):
	return '{} received {}% of the exam'.format(name, grade) 

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

###################################################

def prices_with_tax(prices):
    tax = prices * 1.09
    return 'The amount with tax is ${:.2f}'.format(tax)

print(prices_with_tax(12))
