#Day 02 - Student: Erica CalaΓ§a

# π¨ Don't change the code below π
age = input("What is your current age?")
# π¨ Don't change the code above π

#Write your code below this line π
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.

years_remaining = 90 - int(age)
months_remaining = years_remaining*12
weeks_remaining = years_remaining*52
days_remaining = years_remaining*365

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
