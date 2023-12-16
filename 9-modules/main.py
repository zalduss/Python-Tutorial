
import conversion

def main():
    # Convert Celsius to Fahrenheit
    celsius = 25
    fahrenheit = conversion.celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

    # Convert Fahrenheit to Celsius
    fahrenheit = 77
    celsius = conversion.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")

if __name__ == "__main__":
    main()

