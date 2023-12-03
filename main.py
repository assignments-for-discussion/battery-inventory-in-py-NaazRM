
def count_batteries_by_health(present_capacities):
  # Initialize counts for healthy, exchange, and failed batteries
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }


    # Rated capacity
    rated_capacity = 120

    # Classify based on SoH
    for capacity in present_capacities:
        soh = (capacity / rated_capacity) * 100

        if soh > 80:
            counts["healthy"] += 1
        elif 62 <= soh <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  # Test 1: Standard test
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  # Test Case 2: Boundary condition - minimum SoH
  present_capacities = [0]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 1)

  # Test Case 3: Boundary condition - maximum SoH
  present_capacities = [120]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 1)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
