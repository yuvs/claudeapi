import math
from main import calculate_pi


def test_calculate_pi():
    """Test the calculate_pi function"""
    
    # Test 1: Calculate pi to 5 decimal places
    print("Test 1: Calculate pi to 5 decimal places")
    calculated_pi = calculate_pi(5)
    actual_pi = round(math.pi, 5)
    print(f"  Calculated: {calculated_pi}")
    print(f"  Actual:     {actual_pi}")
    print(f"  Match: {calculated_pi == actual_pi}")
    assert calculated_pi == actual_pi, f"Expected {actual_pi}, got {calculated_pi}"
    print("  ✓ PASSED\n")
    
    # Test 2: Calculate pi to 3 decimal places
    print("Test 2: Calculate pi to 3 decimal places")
    calculated_pi_3 = calculate_pi(3)
    actual_pi_3 = round(math.pi, 3)
    print(f"  Calculated: {calculated_pi_3}")
    print(f"  Actual:     {actual_pi_3}")
    print(f"  Match: {calculated_pi_3 == actual_pi_3}")
    assert calculated_pi_3 == actual_pi_3, f"Expected {actual_pi_3}, got {calculated_pi_3}"
    print("  ✓ PASSED\n")
    
    # Test 3: Calculate pi to 2 decimal places
    print("Test 3: Calculate pi to 2 decimal places")
    calculated_pi_2 = calculate_pi(2)
    actual_pi_2 = round(math.pi, 2)
    print(f"  Calculated: {calculated_pi_2}")
    print(f"  Actual:     {actual_pi_2}")
    print(f"  Match: {calculated_pi_2 == actual_pi_2}")
    assert calculated_pi_2 == actual_pi_2, f"Expected {actual_pi_2}, got {calculated_pi_2}"
    print("  ✓ PASSED\n")
    
    # Test 4: Verify the value is close to pi
    print("Test 4: Verify calculated value is within acceptable range")
    calculated_pi_full = calculate_pi(5)
    difference = abs(calculated_pi_full - math.pi)
    print(f"  Calculated: {calculated_pi_full}")
    print(f"  Math.pi:    {math.pi}")
    print(f"  Difference: {difference}")
    print(f"  Within tolerance: {difference < 0.00001}")
    assert difference < 0.00001, f"Difference too large: {difference}"
    print("  ✓ PASSED\n")
    
    # Test 5: Check that it returns a numeric value
    print("Test 5: Check return type")
    result = calculate_pi(5)
    print(f"  Type: {type(result)}")
    print(f"  Is numeric: {isinstance(result, (int, float))}")
    assert isinstance(result, (int, float)), f"Expected numeric type, got {type(result)}"
    print("  ✓ PASSED\n")
    
    print("=" * 50)
    print("ALL TESTS PASSED! ✓")
    print("=" * 50)


if __name__ == "__main__":
    test_calculate_pi()
