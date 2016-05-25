import sys
from ge.core.genetic_executor import GeneticExecutor


def test_problem(problem, target_value):
    print(problem, end=' ')
    sys.stdout.flush()
    TIMES_TO_FAIL = 5
    
    ge_config = {}
    
    # Randomized algorithm, so it needs to fail TIMES_TO_FAIL times to be considered failure
    for _ in range(TIMES_TO_FAIL):
        ge = GeneticExecutor(**ge_config)    
        solution = ge.get_solution()
        print(solution.get_fitness_value(), end=' ')
        sys.stdout.flush()
        try:
            assert solution.get_fitness_value() >= -target_value
        except AssertionError:
            # Don't do anything. Will fail outside of the loop after TIMES_TO_FAIL times
            pass
        except Exception:
            break
        else:
            print('OK')
            return True
    print('FAIL')
    return False
    

def test_dummy():
    ge = GeneticExecutor()
    sol = ge.get_solution()


def test_all():
    result = True
    result &= test_problem('dummy', 0)
    
    
if __name__ == '__main__':
    test_all()