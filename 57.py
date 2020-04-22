'''Відомість на зарплату представлена як дві таблиці.
Одна містить прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище працівника,
 зарплата якого найменше відхиляється від середньої зарплати всіх працівників за поточний місяць.
 Знайдіть прізвища двох працівників з найбільшою заробітною платою.
 Видаліть з відомості на зарплату відомості про працівника, зарплата якого мінімальна.'''
from random import randint

employee = [i+1 for i in range(20)]
salary = [randint(1700, 12000) for i in range(20)]
print('Працівники:',employee)
print('Заробітні плати:',salary)

salarySum = 0
for i in range(len(salary)):
    salarySum += salary[i]

averageSalary = salarySum / len(salary)
print('Середня заробітня плата:',averageSalary)

averageSalaryWorkerIndex = None
minimalSalaryDifference = max(salary)
for i in range(len(salary)):
    if abs(salary[i] - averageSalary) < minimalSalaryDifference:
        minimalSalaryDifference = abs(salary[i] - averageSalary)
        averageSalaryWorkerIndex = i

highestPaidWorkerIndex = salary.index(max(salary))
temporarySalaryList = salary.copy()
temporarySalaryList.pop(highestPaidWorkerIndex)
secondHighestPaidWorkerIndex = salary.index(max(temporarySalaryList))
lowestSalaryWorkerIndex = salary.index(min(salary))
salary.pop(lowestSalaryWorkerIndex)

print("Заробітна плата, що найменше відхиляється від середньої зарплати всіх працівників:", employee[averageSalaryWorkerIndex])
print("1 найбільша заробітна плата:", employee[highestPaidWorkerIndex])
print("2 найбільша заробітна плата:", employee[secondHighestPaidWorkerIndex])
print("Найнижча заробітна плата:", employee[lowestSalaryWorkerIndex])
