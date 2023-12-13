# Instructions

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.



The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

### BMI Formula
![Run](../../assets/bmi_equation.png)

NOTE: You should convert the bmi to a whole number using the method `math.floor()`. See examples below. 
- `miles = 6.76`
- `whole_miles = math.floor(miles)`
- In this case, `whole_miles` will be `6`

### Example Input 1
1.75
80

### Expected Output 1
26

---
### Example Input 2
1.58
57
### Expected Output 1
22