def calculate_pi(precision=5):
    """
    Calculate pi to a specified number of decimal digits using the Machin formula.
    The Machin formula converges much faster than the Leibniz formula.
    
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        precision: Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Approximation of pi
    """
    # We need extra iterations for accuracy
    # Using more terms than needed to ensure accuracy at the desired precision
    iterations = 10 ** (precision + 2)
    
    def arctan(x, num_terms):
        """Calculate arctan using Taylor series expansion"""
        result = 0
        x_squared = x * x
        x_power = x
        
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
            
            # Early termination if change is negligible
            if abs(x_power / (2 * n + 3)) < 10 ** -(precision + 3):
                break
        
        return result
    
    # Using Machin's formula for faster convergence
    pi_approx = 4 * (4 * arctan(1/5, 1000) - arctan(1/239, 1000))
    
    return round(pi_approx, precision)


def main():
    pi_value = calculate_pi(5)
    print(f"Pi to 5 decimal places: {pi_value}")
    print(f"Actual value of pi:      3.14159...")


if __name__ == "__main__":
    main()
